# Systematic Debugging Workflow 🔍

Stop guessing. This workflow provides a structured path for Claude to find and fix bugs without breaking existing features.

## Workflow Phases

### Phase 1: Context Gathering
**Objective**: Understand exactly what is happening vs. what is expected.
- **Task**: Provide Claude with error logs, screenshots, and the relevant code files.
- **Trigger**: "Claude, I'm seeing this error: [Error]. Here are the logs and the file where I think it's happening."

### Phase 2: Root Cause Analysis (RCA)
**Objective**: Identify *why* the bug is happening.
- **Task**: Claude analyzes the logic and state flow.
- **Trigger**: "Analyze the code and tell me the potential root causes. Is it a race condition, a type mismatch, or a logic error?"

### Phase 3: The Minimal Reproduction
**Objective**: Prove you found the bug.
- **Task**: Create a simple script or test case that fails because of this bug.
- **Trigger**: "Can you write a minimal reproduction case or a test that proves this bug exists?"

### Phase 4: The Fix
**Objective**: Implement the solution.
- **Task**: Refactor the code to eliminate the root cause.
- **Trigger**: "Apply the fix we discussed. Ensure it doesn't violate any patterns in our CLAUDE.md."

### Phase 5: Verification
**Objective**: Confirm the fix and prevent regression.
- **Task**: Run the reproduction test again (it should pass) and check related features.
- **Trigger**: "Run the reproduction test to confirm the fix. Also, check if this change affects [Related Feature]."

---

## Pro-Tips for Debugging with Claude
- **Be Detailed**: The more logs and context you provide, the faster Claude finds the bug.
- **Use the Code Reviewer Skill**: After the fix, ask Claude to use the `code-reviewer` skill to ensure the new code is high quality.
- **Check Environment**: Sometimes bugs are in `.env` or dependencies, not the code.
