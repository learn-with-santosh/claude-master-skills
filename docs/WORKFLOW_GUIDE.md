# Workflow Guide 🌊

Workflows are structured sequences that guide Claude through complex tasks. Unlike individual skills, workflows focus on the **process** and the **hand-off** between different phases of development.

## How to Use Workflows

1. **Choose your path**: Decide if you're building something new ([Startup MVP](../workflows/startup-mvp.md)) or fixing something ([Debugging](../workflows/debugging.md)).
2. **Follow the Phases**: Each workflow is broken into logical phases (Planning → Coding → Testing).
3. **Use the Triggers**: Copy the suggested "Trigger" phrases to prompt Claude for the specific phase you're in.
4. **Maintain Context**: Keep your `CLAUDE.md` updated as you move through phases to ensure Claude doesn't "forget" previous decisions.

---

## Example: The Startup MVP Loop

### Step 1: Planning
Trigger: *"Claude, I want to build a SaaS for tracking greenhouse gas emissions. Let's start Phase 1: Planning & Architecture."*
Result: Claude generates a technical spec and a database schema.

### Step 2: Implementation
Trigger: *"Great, now let's move to Phase 2: Core Implementation. Build the user dashboard and the emissions input form."*
Result: Claude writes the frontend and backend logic.

### Step 3: Polish
Trigger: *"It works! Now apply Phase 3: The Aesthetic Pass. Use the Aesthetic UI Engine skill to make it look premium."*
Result: Claude applies modern styling and animations.

---

## Maximizing Success

- **Be Granular**: Don't ask Claude to "do the whole workflow" in one prompt. Go phase by phase.
- **Feedback Loop**: After each phase, review the code using the `code-reviewer` skill.
- **Git Integration**: Use the `auto-commit` hook after each successful phase to save your progress.

By following these structured workflows, you turn Claude from a simple chatbot into a reliable engineering partner.
