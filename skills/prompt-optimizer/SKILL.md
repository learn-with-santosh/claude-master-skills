---
name: prompt-optimizer
description: Acts as a Prompt Refinement Engine. Use this skill whenever a user says "optimize this prompt", "make this prompt better", "I'm not getting good results from this prompt", or wants to upgrade a basic instruction into a professional-grade prompt.
---

# Prompt Optimizer 💎

Turn your basic instructions into high-performance prompts. This skill uses advanced engineering techniques (Chain-of-Thought, Delimiters, Few-Shot, and Persona) to ensure your AI interactions are consistent, accurate, and powerful.

## When to use this skill

Use this skill when:
- You have a simple prompt that is producing vague or incorrect results.
- You want to turn a task description into a reusable system prompt.
- You need to add constraints or structural requirements to an AI output.
- You want to "AI-ify" a business process.

## The Optimization Framework

To optimize a prompt, Claude applies these layers:

### 1. The Persona Layer
Define *who* Claude should be.
"Instead of 'Write a script', use 'You are a Senior Python Developer with 10 years of experience in automation...'"

### 2. The Objective Layer
Clarify exactly what the goal is.
"Define the 'Primary Mission' and the 'Success Criteria' for the task."

### 3. The Constraint Layer
Add the "Boundaries."
- Tone (Professional, Humorous, Academic)
- Length (Max 200 words, exactly 5 bullet points)
- Format (JSON, Markdown, CSV)

### 4. The Engineering Layer
Add advanced logic:
- **Chain-of-Thought**: Add `<thought>` blocks.
- **Delimiters**: Use tags like `<context>` or `<instructions>`.
- **Few-Shot**: Request specific examples to be added.

## Output Format

### 🛠 Analysis
What was wrong with the original prompt?

### ✨ The Optimized Prompt
The ready-to-use, engineered version.

### 💡 Why it's better
Explanation of the techniques applied.

---

## Examples

### Example: Transforming a simple request
**Original**: "Help me write a blog post about AI."
**Optimized**:
"**Persona**: You are a Tech Journalist and SEO Expert.
**Objective**: Write a 1,000-word deep-dive article about the impact of Claude Code on developer productivity.
**Instructions**:
1. Lead with a 'Pattern Interrupt' hook.
2. Use H2 headers for each major section.
3. Include a 'Key Takeaways' summary at the end.
**Constraints**: Avoid buzzwords. Use a conversational but professional tone."

---

## Best Practices
- **Iterate**: If the first optimization isn't perfect, tell Claude what's missing.
- **Use Prompt Pro**: For extremely complex prompts, use the `prompt-engineer-pro` skill first to define the strategy, then `prompt-optimizer` to draft it.
- **Test**: Always run the optimized prompt through its paces with different inputs.
