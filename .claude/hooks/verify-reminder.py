#!/usr/bin/env python3
"""
Verification Reminder Hook

Non-blocking reminder that fires on Write/Edit to files that require
post-edit verification before task completion.

Hook Event: PostToolUse (matcher: "Write|Edit")
"""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

# Colors for terminal output
CYAN = "\033[0;36m"
GREEN = "\033[0;32m"
NC = "\033[0m"

# File-level verification actions
VERIFY_EXTENSIONS = {
    ".tex": "compile with /compile-latex",
    ".qmd": "render and verify output (PDF/HTML as applicable)",
    ".R": "run to verify output",
    ".md": "run quality score if this is a referee report artifact",
}

# Files to skip by extension (unless explicitly whitelisted by path)
SKIP_EXTENSIONS = [
    ".txt", ".rst",
    ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg",
    ".lock", ".env", ".gitignore",
    ".svg", ".png", ".jpg", ".pdf",
    ".bib", ".cls", ".sty"
]

# Directory skips for non-report files
SKIP_DIRS = [
    "/docs/",
    "/templates/",
    "/.claude/",
    "/node_modules/",
    "/build/",
    "/dist/"
]


def get_session_dir() -> Path:
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", "")
    if not project_dir:
        return Path.home() / ".claude" / "sessions" / "default"

    import hashlib
    project_hash = hashlib.md5(project_dir.encode()).hexdigest()[:8]
    session_dir = Path.home() / ".claude" / "sessions" / project_hash
    session_dir.mkdir(parents=True, exist_ok=True)
    return session_dir


def is_referee_report_artifact(file_path: str) -> bool:
    normalized = file_path.replace("\\", "/")
    return "quality_reports/referee_reports/" in normalized


def should_skip(file_path: str) -> bool:
    path = Path(file_path)

    # Do not skip referee report markdown artifacts.
    if is_referee_report_artifact(file_path):
        return False

    if path.suffix.lower() in SKIP_EXTENSIONS:
        return True

    for skip_dir in SKIP_DIRS:
        if skip_dir in file_path:
            return True

    name = path.name.lower()
    if name.startswith("test_") or name.endswith("_test.py"):
        return True

    return False


def needs_verification(file_path: str) -> tuple[bool, str]:
    path = Path(file_path)
    suffix = path.suffix.lower()

    if suffix == ".md" and not is_referee_report_artifact(file_path):
        return False, ""

    if suffix in VERIFY_EXTENSIONS:
        return True, VERIFY_EXTENSIONS[suffix]

    return False, ""


def was_recently_reminded(file_path: str) -> bool:
    cache_file = get_session_dir() / "verify-reminder-cache.json"

    try:
        if cache_file.exists():
            cache = json.loads(cache_file.read_text())
        else:
            cache = {}
    except (json.JSONDecodeError, IOError):
        cache = {}

    last_reminder = cache.get(file_path, 0)
    now = time.time()

    cache[file_path] = now
    cache = {k: v for k, v in cache.items() if now - v < 300}

    try:
        cache_file.write_text(json.dumps(cache))
    except IOError:
        pass

    return (now - last_reminder) < 60


def format_reminder(file_path: str, action: str) -> str:
    filename = Path(file_path).name
    return f"""
{CYAN}Verification reminder:{NC} {filename}
   -> {GREEN}{action}{NC} before marking task complete
"""


def main() -> int:
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, IOError):
        return 0

    tool_input = hook_input.get("tool_input", {})
    file_path = tool_input.get("file_path", "")

    if not file_path:
        return 0

    if should_skip(file_path):
        return 0

    needs_verify, action = needs_verification(file_path)
    if not needs_verify:
        return 0

    if was_recently_reminded(file_path):
        return 0

    print(format_reminder(file_path, action))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
