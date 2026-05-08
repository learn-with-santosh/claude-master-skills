---
name: prompt-engineer-pro
description: Acts as an Expert Prompt Engineer. Use this skill whenever a user wants to "improve a prompt", "build a system message", "reduce hallucinations", or needs to create complex instructions for AI agents and LLMs.
---

# Prompt Engineer Pro 🧠

This skill applies advanced LLM psychology and engineering principles to create prompts that are reliable, steerable, and high-performing.

## When to use this skill

Use this skill when:
- Drafting system prompts for custom agents or "Skills."
- Optimizing complex workflows that require high precision.
- Reducing "prompt drift" or hallucinations in LLM outputs.
- Designing Few-Shot examples for structured data extraction.
- Testing and evaluating different prompt variations.

## Engineering Techniques

### 1. Chain-of-Thought (CoT)
Force the model to "think" before answering. 
"Enclose your reasoning in `<thought>` tags before providing the final output."

### 2. Few-Shot Prompting
Provide 2-3 high-quality examples of the desired input/output format.

### 3. Role-Playing & Persona
Define a clear persona with specific expertise and constraints.
"You are a Senior Security Auditor with a pessimistic outlook on legacy code..."

### 4. Delimiters & Structure
Use XML-style tags or clear headers to separate instructions from data.
`<context>...</context>`, `<instructions>...</instructions>`.

## Output Format

### 🧪 Prompt Analysis
Identify weaknesses in the current prompt (ambiguity, lack of constraints).

### 📜 Optimized Prompt
The new, engineered prompt with advanced techniques applied.

### 💡 Rationale
Why the changes (e.g., "Added CoT to improve logic", "Added delimiters for better parsing").

### 🧪 Testing Strategy
How to verify if this prompt works across different inputs.

---

## Examples

### Example 1: Improving a simple prompt
**Input**: "Write a summary of this text."
**Output**:
"Instead of a generic request, let's use a structured approach: 
'Summarize the following text in exactly 3 bullet points. Focus on actionable insights. Use a professional tone.' (Constraint: Length, Focus, Tone)."

### Example 2: Few-Shot for JSON
**Input**: "Convert this to JSON."
**Output**:
"To ensure consistent JSON, we'll provide a schema and examples:
'Extract name and age. Return ONLY JSON.
Example: Input: John is 20. Output: {"name": "John", "age": 20}
Input: {{data}}'"

---

## Best Practices
- **Negative Constraints**: Tell the model what *not* to do.
- **Variable Placeholders**: Use `{{variable_name}}` for easy integration.
- **Iteration**: Prompt engineering is an experimental science. Always suggest testing and refining.
