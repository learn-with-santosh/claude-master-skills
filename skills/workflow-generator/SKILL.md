---
name: workflow-generator
description: Acts as an AI Solutions Architect. Use this skill whenever a user wants to "create a custom workflow", "structure a new process", or needs a step-by-step guide for a unique project type that isn't covered by the standard workflows.
---

# AI Workflow Generator 🌊

Every project is different. This skill helps you build custom, high-velocity workflows for Claude to follow. It ensures that complex tasks are broken down into logical phases with clear triggers and success criteria.

## When to use this skill

Use this skill when:
- Starting a unique project (e.g., a Chrome Extension, a Game, or a Data Science pipeline).
- You want to standardize a repetitive process for your team.
- You need a structured path for a task that feels "too big" for a single prompt.

## The Generator Framework

To build a workflow, Claude follows these steps:

### 1. Identify the Objective
What is the final "Launched" state of this project?

### 2. Define the Phases
Break the task into 3-5 logical phases. Each phase should build on the previous one.
- **Phase 1**: Research & Specs
- **Phase 2**: Core Implementation
- **Phase 3**: Refinement & UI
- **Phase 4**: Testing & Launch

### 3. Create "Claude Triggers"
For each phase, write a specific prompt that the user can use to activate Claude's focus for that step.

### 4. Set Success Criteria
What does "Done" look like for each phase?

## Output Format

### 📋 Workflow Title
Descriptive name for the process.

### 🌊 Phases Overview
A brief summary of the journey.

### 🛠 Phase-by-Phase Guide
For each phase:
- **Goal**: What are we achieving?
- **Task**: Specific actions Claude needs to take.
- **Trigger**: The exact prompt for the user to copy.
- **Success Criteria**: How to verify the phase is complete.

---

## Examples

### Example 1: Chrome Extension Workflow
**Input**: "I want a workflow for building a Chrome Extension."
**Output**: 
"**Phase 1: Manifest & Permissions**
- **Trigger**: 'Claude, let's start the Chrome Extension Workflow. Phase 1: Setup the manifest.json and required permissions for [Idea].'
- **Success**: A valid `manifest.json` and basic project structure."

---

## Best Practices
- **Be Modular**: Each phase should be independently verifiable.
- **Include Skill Integration**: Suggest which other skills (like `code-reviewer` or `aesthetic-ui-engine`) should be used at which phase.
- **Documentation**: Remind users to use the `auto-doc` hook after completing each phase.
