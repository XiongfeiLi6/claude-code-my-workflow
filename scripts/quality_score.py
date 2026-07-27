#!/usr/bin/env python3
"""
Quality Scoring System for Academic Workflow Artifacts.

Calculates objective quality scores (0-100) based on defined rubrics.
Enforces quality gates: 80 (deliverable), 90 (strong), 95 (excellence).

Usage:
    python scripts/quality_score.py quality_reports/referee_reports/report.qmd
    python scripts/quality_score.py quality_reports/referee_reports/report.md
    python scripts/quality_score.py Quarto/Lecture6_Topic.qmd
    python scripts/quality_score.py Slides/Lecture01_Topic.tex
    python scripts/quality_score.py scripts/R/Lecture06_simulations.R
"""

import sys
import argparse
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple
import re
import json

# ==============================================================================
# SCORING RUBRIC (from .claude/rules/quality-gates.md)
# ==============================================================================

QUARTO_RUBRIC = {
    'critical': {
        'compilation_failure': {'points': 100, 'auto_fail': True},
        'equation_overflow': {'points': 20},
        'broken_citation': {'points': 15},
        'typo_in_equation': {'points': 10},
        'missing_plotly_chart': {'points': 10},
    },
    'major': {
        'text_overflow': {'points': 5},
        'tikz_label_overlap': {'points': 5},
        'notation_inconsistency': {'points': 3},
        'missing_box_separation': {'points': 2},
        'color_contrast_low': {'points': 3},
    },
    'minor': {
        'font_size_reduction': {'points': 1},
        'missing_forward_ref': {'points': 1},
        'missing_framing_sentence': {'points': 1},
    }
}

R_SCRIPT_RUBRIC = {
    'critical': {
        'syntax_error': {'points': 100, 'auto_fail': True},
        'hardcoded_path': {'points': 20},
        'missing_library': {'points': 10},
    },
    'major': {
        'missing_set_seed': {'points': 10},
        'missing_figure': {'points': 5},
        'missing_rds': {'points': 5},
    },
    'minor': {
        'style_violation': {'points': 1},
        'missing_roxygen': {'points': 1},
    }
}

BEAMER_RUBRIC = {
    'critical': {
        'compilation_failure': {'points': 100, 'auto_fail': True},
        'undefined_citation': {'points': 15},
        'overfull_hbox': {'points': 10},
    },
    'major': {
        'text_overflow': {'points': 5},
        'notation_inconsistency': {'points': 3},
    },
    'minor': {
        'font_size_reduction': {'points': 1},
    }
}

REFEREE_REPORT_RUBRIC = {
    'critical': {
        'missing_recommendation': {'points': 25},
        'missing_editor_section': {'points': 20},
        'missing_author_section': {'points': 20},
        'unverifiable_or_placeholder_content': {'points': 30},
        'pdf_render_failure': {'points': 100, 'auto_fail': True},
    },
    'major': {
        'missing_evidence_anchor': {'points': 8},
        'recommendation_misaligned': {'points': 10},
        'missing_major_concerns_section': {'points': 5},
        'missing_minor_concerns_section': {'points': 5},
        'format_hierarchy_issue': {'points': 5},
    },
    'minor': {
        'writing_issue': {'points': 1},
        'terminology_drift': {'points': 2},
    }
}

THRESHOLDS = {
    'commit': 80,
    'pr': 90,
    'excellence': 95
}

# ==============================================================================
# ISSUE DETECTION (Lightweight checks - full agents run separately)
# ==============================================================================

class IssueDetector:
    """Detect common issues for quality scoring."""

    @staticmethod
    def check_quarto_compilation(filepath: Path) -> Tuple[bool, str]:
        """Check if Quarto file compiles successfully."""
        try:
            result = subprocess.run(
                ['quarto', 'render', str(filepath), '--to', 'html'],
                capture_output=True,
                text=True,
                timeout=120,
                cwd=filepath.parent
            )
            if result.returncode != 0:
                return False, result.stderr
            return True, ""
        except subprocess.TimeoutExpired:
            return False, "Compilation timeout (>2min)"
        except FileNotFoundError:
            return False, "Quarto not installed"

    @staticmethod
    def check_equation_overflow(content: str) -> List[int]:
        """Detect displayed equations with single lines likely to overflow.

        Flags equations only when a SINGLE LINE within a math block exceeds
        120 characters. Multi-line equations properly broken across lines
        are not flagged even if the total block is long.

        Checks:
        - $$ ... $$ blocks (Quarto/LaTeX)
        - \\begin{equation} ... \\end{equation} blocks
        - \\begin{align} ... \\end{align} blocks
        - \\begin{gather} ... \\end{gather} blocks
        """
        overflows = []
        lines = content.split('\n')
        in_math = False
        math_start = 0
        math_delim = None  # Track which delimiter opened the block

        for i, line in enumerate(lines, 1):
            stripped = line.strip()

            # Check for $$ delimiter (toggle)
            if '$$' in stripped and math_delim != 'env':
                if not in_math:
                    in_math = True
                    math_start = i
                    math_delim = '$$'
                    # Handle single-line $$ ... $$ (both delimiters on same line)
                    if stripped.count('$$') >= 2:
                        inner = stripped.split('$$')[1]
                        if len(inner.strip()) > 120:
                            overflows.append(i)
                        in_math = False
                        math_delim = None
                    continue
                else:
                    in_math = False
                    math_delim = None
                    continue

            # Check for \begin{equation/align/gather/...}
            env_begin = re.match(
                r'\\begin\{(equation|align|gather|multline|eqnarray)\*?\}', stripped
            )
            if env_begin and not in_math:
                in_math = True
                math_start = i
                math_delim = 'env'
                continue

            # Check for \end{equation/align/gather/...}
            if re.match(r'\\end\{(equation|align|gather|multline|eqnarray)\*?\}', stripped):
                in_math = False
                math_delim = None
                continue

            # Inside a math block: check individual line length
            if in_math:
                # Strip LaTeX comments before measuring
                code_part = line.split('%')[0] if '%' in line else line
                if len(code_part.strip()) > 120:
                    overflows.append(i)

        return overflows

    @staticmethod
    def check_broken_citations(content: str, bib_file: Path) -> List[str]:
        """Check for LaTeX citation keys not in bibliography.

        Matches \\cite{}, \\citep{}, \\citet{}, \\citeauthor{}, \\citeyear{}, etc.
        """
        cite_pattern = r'\\cite[a-z]*\{([^}]+)\}'
        cited_keys = set()
        for match in re.finditer(cite_pattern, content):
            keys = match.group(1).split(',')
            cited_keys.update(k.strip() for k in keys)

        if not bib_file.exists():
            return list(cited_keys)

        bib_content = bib_file.read_text(encoding='utf-8')
        bib_keys = set(re.findall(r'@\w+\{([^,]+),', bib_content))

        broken = cited_keys - bib_keys
        return list(broken)

    @staticmethod
    def check_plotly_widgets(html_file: Path, expected: int = None) -> Tuple[int, bool]:
        """Check if plotly charts rendered in HTML."""
        if not html_file.exists():
            return 0, False

        html_content = html_file.read_text(encoding='utf-8')
        actual_count = html_content.count('htmlwidget')

        if expected is None:
            return actual_count, True

        return actual_count, (actual_count >= expected)

    @staticmethod
    def check_r_syntax(filepath: Path) -> Tuple[bool, str]:
        """Check R script for syntax errors."""
        try:
            result = subprocess.run(
                ['Rscript', '-e', f'parse("{filepath}")'],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode != 0:
                return False, result.stderr
            return True, ""
        except subprocess.TimeoutExpired:
            return False, "Syntax check timeout"
        except FileNotFoundError:
            return False, "Rscript not installed"

    @staticmethod
    def check_hardcoded_paths(content: str) -> List[int]:
        """Detect absolute paths in R scripts."""
        issues = []
        lines = content.split('\n')

        for i, line in enumerate(lines, 1):
            if re.search(r'["\'][/\\]|["\'][A-Za-z]:[/\\]', line):
                if not re.search(r'http:|https:|file://|/tmp/', line):
                    issues.append(i)

        return issues

    @staticmethod
    def check_latex_syntax(content: str) -> List[Dict]:
        """Check for common LaTeX syntax issues without compiling.

        Looks for:
        - Unmatched braces
        - Unclosed environments
        - Common typos in commands
        """
        issues = []
        lines = content.split('\n')

        # Track open environments
        env_stack = []
        for i, line in enumerate(lines, 1):
            # Skip comments
            stripped = line.split('%')[0] if '%' in line else line

            # Check for \begin{env}
            for match in re.finditer(r'\\begin\{(\w+)\}', stripped):
                env_stack.append((match.group(1), i))

            # Check for \end{env}
            for match in re.finditer(r'\\end\{(\w+)\}', stripped):
                env_name = match.group(1)
                if env_stack and env_stack[-1][0] == env_name:
                    env_stack.pop()
                elif env_stack:
                    issues.append({
                        'line': i,
                        'description': f'Mismatched environment: \\end{{{env_name}}} '
                                       f'but expected \\end{{{env_stack[-1][0]}}} '
                                       f'(opened at line {env_stack[-1][1]})',
                    })
                else:
                    issues.append({
                        'line': i,
                        'description': f'\\end{{{env_name}}} without matching \\begin',
                    })

        # Report unclosed environments
        for env_name, line_num in env_stack:
            issues.append({
                'line': line_num,
                'description': f'Unclosed environment: \\begin{{{env_name}}} never closed',
            })

        return issues

    @staticmethod
    def check_overfull_hbox_risk(content: str) -> List[int]:
        """Detect lines in LaTeX source likely to cause overfull hbox.

        Checks for very long lines inside text and math environments
        that are likely to overflow the slide width.
        """
        issues = []
        lines = content.split('\n')
        in_frame = False

        for i, line in enumerate(lines, 1):
            stripped = line.split('%')[0] if '%' in line else line

            # Track frame environments for context
            if r'\begin{frame}' in stripped:
                in_frame = True
            elif r'\end{frame}' in stripped:
                in_frame = False

            # Flag very long content lines inside frames
            # Strip leading whitespace and LaTeX commands for length check
            if in_frame and len(stripped.strip()) > 120:
                # Skip lines that are just comments or common long commands
                if stripped.strip().startswith('%'):
                    continue
                # Skip includegraphics, input, and similar path-based commands
                if re.match(r'\s*\\(includegraphics|input|bibliography|usepackage)', stripped):
                    continue
                issues.append(i)

        return issues

    @staticmethod
    def check_quarto_citations(content: str, bib_file: Path) -> List[str]:
        """Check Quarto-style citation keys against bibliography.

        Supports patterns: @key, [@key], [@key1; @key2]
        """
        cited_keys = set()

        # Pattern 1: [@key] or [@key1; @key2; ...]
        bracket_pattern = r'\[([^\]]*@[^\]]+)\]'
        for match in re.finditer(bracket_pattern, content):
            inner = match.group(1)
            # Extract individual @key references from within brackets
            for key_match in re.finditer(r'@([\w:.#$%&\-+?<>~/]+)', inner):
                cited_keys.add(key_match.group(1))

        # Pattern 2: standalone @key (not inside brackets, not email addresses)
        # Match @key that is preceded by start-of-line or whitespace or punctuation
        # but NOT preceded by characters that indicate an email address
        standalone_pattern = r'(?<![.\w])@([\w:.#$%&\-+?<>~/]+)'
        for match in re.finditer(standalone_pattern, content):
            key = match.group(1)
            # Skip if it looks like a Quarto directive or special syntax
            if key.startswith('{') or key in ('fig', 'tbl', 'sec', 'eq', 'lst'):
                continue
            cited_keys.add(key)

        if not cited_keys:
            return []

        if not bib_file.exists():
            return list(cited_keys)

        bib_content = bib_file.read_text(encoding='utf-8')
        bib_keys = set(re.findall(r'@\w+\{([^,]+),', bib_content))

        broken = cited_keys - bib_keys
        return list(broken)

    @staticmethod
    def has_markdown_heading(content: str, heading_text: str) -> bool:
        """Check whether a heading exists (case-insensitive)."""
        pattern = rf'^\s*#{{1,6}}\s+{re.escape(heading_text)}\s*$'
        return bool(re.search(pattern, content, flags=re.IGNORECASE | re.MULTILINE))

    @staticmethod
    def parse_recommendation(content: str) -> str:
        """Extract recommendation category if present."""
        match = re.search(
            r'\*{0,2}Category:\*{0,2}\s*(Reject|Major Revision|Minor Revision|Accept)',
            content,
            flags=re.IGNORECASE
        )
        if not match:
            return ""
        normalized = match.group(1).lower()
        if normalized == 'major revision':
            return 'Major Revision'
        if normalized == 'minor revision':
            return 'Minor Revision'
        if normalized == 'reject':
            return 'Reject'
        if normalized == 'accept':
            return 'Accept'
        return ""

    @staticmethod
    def extract_major_concern_blocks(content: str) -> List[str]:
        """Extract major concern sub-sections using MC headings."""
        matches = list(re.finditer(r'^\s*####\s+MC\d+\s*:', content, flags=re.MULTILINE))
        if not matches:
            return []
        blocks = []
        for idx, match in enumerate(matches):
            start = match.start()
            end = matches[idx + 1].start() if idx + 1 < len(matches) else len(content)
            blocks.append(content[start:end])
        return blocks

    @staticmethod
    def major_blocks_missing_anchor(content: str) -> List[int]:
        """Return 1-based indices of major concern blocks missing evidence anchors."""
        blocks = IssueDetector.extract_major_concern_blocks(content)
        missing = []
        for i, block in enumerate(blocks, 1):
            has_label = re.search(r'Evidence Anchor\s*:', block, flags=re.IGNORECASE)
            has_reference = re.search(
                r'(section|page|table|figure|equation|appendix)\s*[A-Za-z0-9.-]*',
                block,
                flags=re.IGNORECASE
            )
            if not has_label and not has_reference:
                missing.append(i)
        return missing

    @staticmethod
    def check_qmd_pdf_render(filepath: Path) -> Tuple[bool, str]:
        """Render QMD to PDF and validate output exists and is non-empty."""
        repo_root = Path(__file__).resolve().parent.parent
        render_script = repo_root / 'scripts' / 'render_referee_report.sh'

        if render_script.exists():
            try:
                result = subprocess.run(
                    [str(render_script), str(filepath)],
                    capture_output=True,
                    text=True,
                    timeout=240,
                    cwd=repo_root
                )
            except subprocess.TimeoutExpired:
                return False, "PDF render timeout (>4min)"
            if result.returncode != 0:
                return False, (result.stderr or result.stdout)[:400]

            output_pdf = filepath.with_suffix('.pdf')
            if output_pdf.exists() and output_pdf.stat().st_size > 0:
                return True, ""

            final_pdf = repo_root / 'output' / 'pdf' / f"{filepath.stem.replace('_report', '_referee_report')}.pdf"
            if final_pdf.exists() and final_pdf.stat().st_size > 0:
                return True, ""

            return False, "Render script completed but expected PDF was not found"

        # Fallback to direct Quarto render when script is unavailable.
        try:
            result = subprocess.run(
                ['quarto', 'render', filepath.name, '--to', 'pdf'],
                capture_output=True,
                text=True,
                timeout=180,
                cwd=filepath.parent
            )
        except subprocess.TimeoutExpired:
            return False, "PDF render timeout (>3min)"
        except FileNotFoundError:
            return False, "Quarto not installed"

        if result.returncode != 0:
            return False, (result.stderr or result.stdout)[:400]

        output_pdf = filepath.with_suffix('.pdf')
        if not output_pdf.exists() or output_pdf.stat().st_size == 0:
            return False, f"Rendered file missing or empty: {output_pdf}"
        return True, ""

    @staticmethod
    def detect_basic_writing_issues(content: str) -> int:
        """Count lightweight writing issues for minor deductions."""
        repeated_word_hits = re.findall(r'\b([A-Za-z]+)\s+\1\b', content, flags=re.IGNORECASE)
        double_space_hits = len(re.findall(r'[^ \n]  [^ \n]', content))
        return len(repeated_word_hits) + min(double_space_hits, 5)

# ==============================================================================
# QUALITY SCORER
# ==============================================================================

class QualityScorer:
    """Calculate quality scores for course materials."""

    def __init__(self, filepath: Path, verbose: bool = False):
        self.filepath = filepath
        self.verbose = verbose
        self.score = 100
        self.issues = {
            'critical': [],
            'major': [],
            'minor': []
        }
        self.auto_fail = False

    def score_quarto(self) -> Dict:
        """Score Quarto lecture slides."""
        content = self.filepath.read_text(encoding='utf-8')

        # Check compilation
        compiles, error = IssueDetector.check_quarto_compilation(self.filepath)
        if not compiles:
            self.auto_fail = True
            self.issues['critical'].append({
                'type': 'compilation_failure',
                'description': 'Quarto compilation failed',
                'details': error[:200],
                'points': 100
            })
            self.score = 0
            return self._generate_report()

        # Check equation overflow (heuristic)
        equation_overflows = IssueDetector.check_equation_overflow(content)
        for line in equation_overflows:
            self.issues['critical'].append({
                'type': 'equation_overflow',
                'description': f'Potential equation overflow at line {line}',
                'details': 'Single equation line >120 chars may overflow slide',
                'points': 20
            })
            self.score -= 20

        # Check broken citations (LaTeX-style \cite patterns)
        bib_file = self.filepath.parent.parent / 'Bibliography_base.bib'
        broken_citations = IssueDetector.check_broken_citations(content, bib_file)

        # Also check Quarto-style @key citations
        quarto_broken = IssueDetector.check_quarto_citations(content, bib_file)
        # Merge both sets, avoiding duplicates
        all_broken = set(broken_citations) | set(quarto_broken)
        for key in all_broken:
            self.issues['critical'].append({
                'type': 'broken_citation',
                'description': f'Citation key not in bibliography: {key}',
                'details': 'Add to Bibliography_base.bib or fix key',
                'points': 15
            })
            self.score -= 15

        # Check plotly widgets (if HTML exists)
        html_file = self.filepath.parent.parent / 'docs' / 'slides' / self.filepath.with_suffix('.html').name
        if html_file.exists():
            widget_count, _ = IssueDetector.check_plotly_widgets(html_file)
            expected_plotly = content.count('plotly::plot_ly')
            if expected_plotly > 0 and widget_count < expected_plotly:
                missing = expected_plotly - widget_count
                self.issues['critical'].append({
                    'type': 'missing_plotly_chart',
                    'description': f'{missing} plotly chart(s) failed to render',
                    'details': f'Expected {expected_plotly}, found {widget_count}',
                    'points': 10 * missing
                })
                self.score -= 10 * missing

        self.score = max(0, self.score)
        return self._generate_report()

    def score_r_script(self) -> Dict:
        """Score R script quality."""
        content = self.filepath.read_text(encoding='utf-8')

        # Check syntax
        is_valid, error = IssueDetector.check_r_syntax(self.filepath)
        if not is_valid:
            self.auto_fail = True
            self.issues['critical'].append({
                'type': 'syntax_error',
                'description': 'R syntax error',
                'details': error[:200],
                'points': 100
            })
            self.score = 0
            return self._generate_report()

        # Check hardcoded paths
        path_issues = IssueDetector.check_hardcoded_paths(content)
        for line in path_issues:
            self.issues['critical'].append({
                'type': 'hardcoded_path',
                'description': f'Hardcoded absolute path at line {line}',
                'details': 'Use relative paths or here::here()',
                'points': 20
            })
            self.score -= 20

        # Check for set.seed() if randomness detected
        has_random = any(fn in content for fn in ['rnorm', 'runif', 'sample', 'rbinom', 'rnbinom'])
        has_seed = 'set.seed' in content
        if has_random and not has_seed:
            self.issues['major'].append({
                'type': 'missing_set_seed',
                'description': 'Missing set.seed() for reproducibility',
                'details': 'Add set.seed(YYYYMMDD) after library() calls',
                'points': 10
            })
            self.score -= 10

        self.score = max(0, self.score)
        return self._generate_report()

    def score_beamer(self) -> Dict:
        """Score Beamer/LaTeX lecture slides."""
        content = self.filepath.read_text(encoding='utf-8')

        # Check for LaTeX syntax issues (without compiling)
        syntax_issues = IssueDetector.check_latex_syntax(content)
        if syntax_issues:
            # Mismatched environments are treated as compilation risk
            for issue in syntax_issues:
                self.issues['critical'].append({
                    'type': 'compilation_failure',
                    'description': f'LaTeX syntax issue at line {issue["line"]}',
                    'details': issue['description'],
                    'points': 100
                })
            self.auto_fail = True
            self.score = 0
            return self._generate_report()

        # Check for undefined/broken citations (\cite, \citep, \citet patterns)
        bib_file = self.filepath.parent.parent / 'Bibliography_base.bib'
        if not bib_file.exists():
            # Also check same directory
            bib_file = self.filepath.parent / 'Bibliography_base.bib'
        broken_citations = IssueDetector.check_broken_citations(content, bib_file)
        for key in broken_citations:
            self.issues['critical'].append({
                'type': 'undefined_citation',
                'description': f'Citation key not in bibliography: {key}',
                'details': 'Add to Bibliography_base.bib or fix key',
                'points': 15
            })
            self.score -= 15

        # Check for lines likely to cause overfull hbox
        overfull_lines = IssueDetector.check_overfull_hbox_risk(content)
        for line in overfull_lines:
            self.issues['critical'].append({
                'type': 'overfull_hbox',
                'description': f'Potential overfull hbox at line {line}',
                'details': 'Line >120 chars inside frame may overflow slide width',
                'points': 10
            })
            self.score -= 10

        # Check equation overflow (same heuristic as Quarto)
        equation_overflows = IssueDetector.check_equation_overflow(content)
        for line_num in equation_overflows:
            self.issues['critical'].append({
                'type': 'overfull_hbox',
                'description': f'Potential equation overflow at line {line_num}',
                'details': 'Single equation line >120 chars likely to overflow',
                'points': 10
            })
            self.score -= 10

        self.score = max(0, self.score)
        return self._generate_report()

    def score_referee_report(self, is_qmd: bool) -> Dict:
        """Score manuscript referee report artifacts (.md/.qmd)."""
        content = self.filepath.read_text(encoding='utf-8')

        recommendation = IssueDetector.parse_recommendation(content)
        if not recommendation:
            self.issues['critical'].append({
                'type': 'missing_recommendation',
                'description': 'Missing recommendation category',
                'details': 'Add Category: Reject / Major Revision / Minor Revision / Accept',
                'points': REFEREE_REPORT_RUBRIC['critical']['missing_recommendation']['points']
            })
            self.score -= REFEREE_REPORT_RUBRIC['critical']['missing_recommendation']['points']

        if not IssueDetector.has_markdown_heading(content, 'Confidential Comments to Editor'):
            self.issues['critical'].append({
                'type': 'missing_editor_section',
                'description': 'Missing \"Confidential Comments to Editor\" section',
                'details': 'Add explicit confidential section for editor-only comments',
                'points': REFEREE_REPORT_RUBRIC['critical']['missing_editor_section']['points']
            })
            self.score -= REFEREE_REPORT_RUBRIC['critical']['missing_editor_section']['points']

        if not IssueDetector.has_markdown_heading(content, 'Comments to Authors'):
            self.issues['critical'].append({
                'type': 'missing_author_section',
                'description': 'Missing \"Comments to Authors\" section',
                'details': 'Add explicit author-facing section',
                'points': REFEREE_REPORT_RUBRIC['critical']['missing_author_section']['points']
            })
            self.score -= REFEREE_REPORT_RUBRIC['critical']['missing_author_section']['points']

        # Placeholders indicate incomplete/unverifiable report content.
        if '{{' in content or '}}' in content:
            self.issues['critical'].append({
                'type': 'unverifiable_or_placeholder_content',
                'description': 'Template placeholders remain in report',
                'details': 'Replace all placeholder tokens with concrete text',
                'points': REFEREE_REPORT_RUBRIC['critical']['unverifiable_or_placeholder_content']['points']
            })
            self.score -= REFEREE_REPORT_RUBRIC['critical']['unverifiable_or_placeholder_content']['points']

        if not IssueDetector.has_markdown_heading(content, 'Major Concerns'):
            self.issues['major'].append({
                'type': 'missing_major_concerns_section',
                'description': 'Missing \"Major Concerns\" section',
                'details': 'Add major concern subsection with actionable items',
                'points': REFEREE_REPORT_RUBRIC['major']['missing_major_concerns_section']['points']
            })
            self.score -= REFEREE_REPORT_RUBRIC['major']['missing_major_concerns_section']['points']

        if not IssueDetector.has_markdown_heading(content, 'Minor Concerns'):
            self.issues['major'].append({
                'type': 'missing_minor_concerns_section',
                'description': 'Missing \"Minor Concerns\" section',
                'details': 'Add concise minor concern list',
                'points': REFEREE_REPORT_RUBRIC['major']['missing_minor_concerns_section']['points']
            })
            self.score -= REFEREE_REPORT_RUBRIC['major']['missing_minor_concerns_section']['points']

        missing_anchors = IssueDetector.major_blocks_missing_anchor(content)
        for idx in missing_anchors:
            self.issues['major'].append({
                'type': 'missing_evidence_anchor',
                'description': f'Major concern MC{idx} lacks evidence anchor',
                'details': 'Reference manuscript location (section/page/table/figure/equation)',
                'points': REFEREE_REPORT_RUBRIC['major']['missing_evidence_anchor']['points']
            })
            self.score -= REFEREE_REPORT_RUBRIC['major']['missing_evidence_anchor']['points']

        major_count = len(IssueDetector.extract_major_concern_blocks(content))
        if recommendation == 'Accept' and major_count > 0:
            self.issues['major'].append({
                'type': 'recommendation_misaligned',
                'description': 'Recommendation may be too positive for number of major concerns',
                'details': f'Found {major_count} major concern block(s) with Accept recommendation',
                'points': REFEREE_REPORT_RUBRIC['major']['recommendation_misaligned']['points']
            })
            self.score -= REFEREE_REPORT_RUBRIC['major']['recommendation_misaligned']['points']

        writing_issue_count = min(IssueDetector.detect_basic_writing_issues(content), 10)
        for _ in range(writing_issue_count):
            self.issues['minor'].append({
                'type': 'writing_issue',
                'description': 'Minor writing issue detected',
                'details': 'Review repeated words or spacing artifacts',
                'points': REFEREE_REPORT_RUBRIC['minor']['writing_issue']['points']
            })
            self.score -= REFEREE_REPORT_RUBRIC['minor']['writing_issue']['points']

        if is_qmd:
            rendered, error = IssueDetector.check_qmd_pdf_render(self.filepath)
            if not rendered:
                self.auto_fail = True
                self.issues['critical'].append({
                    'type': 'pdf_render_failure',
                    'description': 'QMD to PDF render failed',
                    'details': error,
                    'points': REFEREE_REPORT_RUBRIC['critical']['pdf_render_failure']['points']
                })
                self.score = 0
                return self._generate_report()

        self.score = max(0, self.score)
        return self._generate_report()

    def _generate_report(self) -> Dict:
        """Generate quality score report."""
        if self.auto_fail:
            status = 'FAIL'
            threshold = 'None (auto-fail)'
        elif self.score >= THRESHOLDS['excellence']:
            status = 'EXCELLENCE'
            threshold = 'excellence'
        elif self.score >= THRESHOLDS['pr']:
            status = 'PR_READY'
            threshold = 'pr'
        elif self.score >= THRESHOLDS['commit']:
            status = 'COMMIT_READY'
            threshold = 'commit'
        else:
            status = 'BLOCKED'
            threshold = 'None (below commit)'

        critical_count = len(self.issues['critical'])
        major_count = len(self.issues['major'])
        minor_count = len(self.issues['minor'])
        total_count = critical_count + major_count + minor_count

        return {
            'filepath': str(self.filepath),
            'score': self.score,
            'status': status,
            'threshold': threshold,
            'auto_fail': self.auto_fail,
            'issues': {
                'critical': self.issues['critical'],
                'major': self.issues['major'],
                'minor': self.issues['minor'],
                'counts': {
                    'critical': critical_count,
                    'major': major_count,
                    'minor': minor_count,
                    'total': total_count
                }
            },
            'thresholds': THRESHOLDS
        }

    def print_report(self, summary_only: bool = False) -> None:
        """Print formatted quality report."""
        report = self._generate_report()

        print(f"\n# Quality Score: {self.filepath.name}\n")

        status_emoji = {
            'EXCELLENCE': '[EXCELLENCE]',
            'PR_READY': '[PASS]',
            'COMMIT_READY': '[PASS]',
            'BLOCKED': '[BLOCKED]',
            'FAIL': '[FAIL]'
        }

        print(f"## Overall Score: {report['score']}/100 {status_emoji.get(report['status'], '')}")

        if report['status'] == 'BLOCKED':
            print(f"\n**Status:** BLOCKED - Cannot commit (score < {THRESHOLDS['commit']})")
        elif report['status'] == 'COMMIT_READY':
            print(f"\n**Status:** Ready for commit (score >= {THRESHOLDS['commit']})")
            gap_to_pr = THRESHOLDS['pr'] - report['score']
            print(f"**Next milestone:** PR threshold ({THRESHOLDS['pr']}+)")
            print(f"**Gap analysis:** Need +{gap_to_pr} points to reach PR quality")
        elif report['status'] == 'PR_READY':
            print(f"\n**Status:** Ready for PR (score >= {THRESHOLDS['pr']})")
            gap_to_excellence = THRESHOLDS['excellence'] - report['score']
            if gap_to_excellence > 0:
                print(f"**Next milestone:** Excellence ({THRESHOLDS['excellence']})")
                print(f"**Gap analysis:** +{gap_to_excellence} points to excellence")
        elif report['status'] == 'EXCELLENCE':
            print(f"\n**Status:** Excellence achieved! (score >= {THRESHOLDS['excellence']})")
        elif report['status'] == 'FAIL':
            print(f"\n**Status:** Auto-fail (compilation/syntax error)")

        if summary_only:
            print(f"\n**Total issues:** {report['issues']['counts']['total']} "
                  f"({report['issues']['counts']['critical']} critical, "
                  f"{report['issues']['counts']['major']} major, "
                  f"{report['issues']['counts']['minor']} minor)")
            return

        # Detailed issues
        print(f"\n## Critical Issues (MUST FIX): {report['issues']['counts']['critical']}")
        if report['issues']['counts']['critical'] == 0:
            print("No critical issues - safe to commit\n")
        else:
            for i, issue in enumerate(report['issues']['critical'], 1):
                print(f"{i}. **{issue['description']}** (-{issue['points']} points)")
                print(f"   - {issue['details']}\n")

        if report['issues']['counts']['major'] > 0:
            print(f"## Major Issues (SHOULD FIX): {report['issues']['counts']['major']}")
            for i, issue in enumerate(report['issues']['major'], 1):
                print(f"{i}. **{issue['description']}** (-{issue['points']} points)")
                print(f"   - {issue['details']}\n")

        if report['issues']['counts']['minor'] > 0 and self.verbose:
            print(f"## Minor Issues (NICE-TO-HAVE): {report['issues']['counts']['minor']}")
            for i, issue in enumerate(report['issues']['minor'], 1):
                print(f"{i}. {issue['description']} (-{issue['points']} points)\n")

        # Recommendations
        if report['status'] == 'BLOCKED':
            print("## Recommended Actions")
            print("1. Fix all critical issues above")
            print(f"2. Re-run quality score (target: >={THRESHOLDS['commit']})")
            print("3. Commit after reaching threshold\n")
        elif report['status'] == 'COMMIT_READY' and report['score'] < THRESHOLDS['pr']:
            print("## Recommended Actions to Reach PR Threshold")
            points_needed = THRESHOLDS['pr'] - report['score']
            print(f"Need +{points_needed} points to reach {THRESHOLDS['pr']}/100")
            if report['issues']['counts']['major'] > 0:
                print("Fix major issues listed above to improve score")
            print(f"\n**Estimated time:** 10-20 minutes\n")

# ==============================================================================
# CLI INTERFACE
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Calculate quality scores for workflow artifacts',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Score a referee report (markdown)
  python scripts/quality_score.py quality_reports/referee_reports/2026-03-05_report.md

  # Score a referee report (QMD, includes PDF render check)
  python scripts/quality_score.py quality_reports/referee_reports/2026-03-05_report.qmd

  # Score multiple files
  python scripts/quality_score.py quality_reports/referee_reports/*.qmd

  # Score a Beamer/LaTeX file
  python scripts/quality_score.py Slides/Lecture01_Topic.tex

  # Score an R script
  python scripts/quality_score.py scripts/R/Lecture06_simulations.R

Quality Thresholds:
  80/100 = Commit threshold (blocks if below)
  90/100 = PR threshold (warning if below)
  95/100 = Excellence (aspirational)

Exit Codes:
  0 = Score >= 80 (commit allowed)
  1 = Score < 80 (commit blocked)
  2 = Auto-fail (compilation/syntax error)
        """
    )

    parser.add_argument('filepaths', type=Path, nargs='+', help='Path(s) to file(s) to score')
    parser.add_argument('--summary', action='store_true', help='Show summary only')
    parser.add_argument('--verbose', action='store_true', help='Show all issues including minor')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    results = []
    exit_code = 0

    for filepath in args.filepaths:
        if not filepath.exists():
            print(f"Error: File not found: {filepath}")
            exit_code = 1
            continue

        try:
            scorer = QualityScorer(filepath, verbose=args.verbose)

            normalized = str(filepath).replace('\\', '/')
            is_referee_artifact = (
                'quality_reports/referee_reports/' in normalized
                or filepath.name.startswith('referee-report')
            )

            if filepath.suffix == '.qmd':
                if is_referee_artifact:
                    report = scorer.score_referee_report(is_qmd=True)
                else:
                    report = scorer.score_quarto()
            elif filepath.suffix == '.md':
                if is_referee_artifact:
                    report = scorer.score_referee_report(is_qmd=False)
                else:
                    print(f"Error: Unsupported markdown target (expected referee artifact): {filepath}")
                    exit_code = max(exit_code, 1)
                    continue
            elif filepath.suffix == '.R':
                report = scorer.score_r_script()
            elif filepath.suffix == '.tex':
                report = scorer.score_beamer()
            else:
                print(f"Error: Unsupported file type: {filepath.suffix}")
                continue

            results.append(report)

            if not args.json:
                scorer.print_report(summary_only=args.summary)

            if report['auto_fail']:
                exit_code = max(exit_code, 2)
            elif report['score'] < THRESHOLDS['commit']:
                exit_code = max(exit_code, 1)

        except Exception as e:
            print(f"Error scoring {filepath}: {e}")
            import traceback
            traceback.print_exc()
            exit_code = 1

    if args.json:
        print(json.dumps(results, indent=2))

    sys.exit(exit_code)

if __name__ == '__main__':
    main()
