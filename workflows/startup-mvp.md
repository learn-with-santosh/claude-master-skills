# Startup MVP Workflow 🚀

This workflow is designed for speed. It guides Claude to build a functional Minimum Viable Product (MVP) in the shortest time possible while maintaining professional standards.

## Workflow Phases

### Phase 1: Planning & Architecture
**Objective**: Define the "What" and "How" before writing a single line of code.
- **Task**: Ask Claude to generate a `specs.md` and `schema.md`.
- **Trigger**: "Claude, I want to build [Idea]. Help me plan the architecture, tech stack, and database schema."

### Phase 2: Core Implementation
**Objective**: Build the "Happy Path" — the features that provide 80% of the value.
- **Task**: Implement the main database models and basic API routes/pages.
- **Trigger**: "Using the schema we defined, let's implement the core [Feature X]. Keep it simple and functional."

### Phase 3: The "Aesthetic" Pass
**Objective**: Make the MVP look professional and expensive.
- **Skill**: Use the `aesthetic-ui-engine` skill.
- **Trigger**: "Now make the UI look premium. Use the Aesthetic UI Engine skill to style the landing page and dashboard."

### Phase 4: Verification & Testing
**Objective**: Ensure the MVP actually works.
- **Task**: Run manual tests or generate unit tests.
- **Trigger**: "Review the implementation for any critical bugs. Generate basic tests for the main API routes."

### Phase 5: Launch & Deployment
**Objective**: Get the code live.
- **Task**: Setup environment variables and deployment scripts (Vercel, Railway, etc.).
- **Trigger**: "Help me prepare this for deployment to [Platform]. What env variables do I need?"

---

## Best Practices
- **Stay Lean**: If a feature isn't essential for the MVP, put it in a `ROADMAP.md`.
- **Use CLAUDE.md**: Ensure you have a project-specific memory file so Claude doesn't lose context between phases.
- **Iterate Fast**: Don't aim for perfection in Phase 2; aim for functionality.
