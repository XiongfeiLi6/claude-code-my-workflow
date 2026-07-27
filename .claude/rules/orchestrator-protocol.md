# Orchestrator Protocol: Contractor Mode

After plan approval, execute autonomously unless ambiguity or decisions require user input.

## Main Loop

```
Plan approved
  -> IMPLEMENT
  -> VERIFY
  -> REVIEW
  -> FIX
  -> RE-VERIFY
  -> SCORE
```

If score >= threshold: deliver artifacts + summary.
If score < threshold: iterate fix/re-verify (max 5 rounds).

## Milestone Check-ins (Early Sessions)

Emit concise check-ins at stage boundaries:
1. plan -> implementation handoff
2. first draft generated
3. verification finished
4. final PDF + score ready

## Escalate to User Only For

- recommendation category ambiguity
- missing/unclear manuscript evidence affecting major conclusions
- conflicting instructions that change deliverable scope

## Guardrails

- no fabricated evidence or references
- preserve reviewer anonymity
- keep confidential editor comments separate from author comments
- no delivery before verification and quality gate pass
