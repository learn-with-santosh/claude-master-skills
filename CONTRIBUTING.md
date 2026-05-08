# Contributing to Claude Master Skills 🚀

First off, thank you for considering contributing to Claude Master Skills! It's people like you that make this a powerful resource for the AI community.

## 🌟 How Can I Contribute?

### 1. Adding New Skills
If you have a specialized workflow or a set of prompts that make Claude significantly better at a specific task, we want it!
- Create a new directory in `.claude/skills/`.
- Name the folder descriptively (e.g., `react-performance-master`).
- Add a `SKILL.md` file inside that folder.
- Follow the standard skill structure (see below).

### 2. Improving Existing Skills
Found a bug in a prompt? Want to add a new framework to the Viral Tweet Generator? Submit a Pull Request!

### 3. Documentation
Help us make the README or the installation guides better.

---

## 🛠️ Skill Structure

Every skill should follow this format for consistency and maximum "Claude-triggering" efficiency:

1.  **YAML Frontmatter**:
    ```yaml
    ---
    name: your-skill-name
    description: A "pushy" description of when Claude should use this skill.
    ---
    ```
2.  **Skill Body**:
    - **Overview**: What the skill does.
    - **When to use**: Clear triggers and use cases.
    - **Input/Output formats**: What should the user provide and what will they get?
    - **Frameworks/Guidelines**: The actual "meat" of the instructions.
    - **Examples**: At least 2-3 realistic before/after examples.

---

## 📝 Pull Request Process

1. Fork the repository.
2. Create a new branch for your feature/skill.
3. Commit your changes with a descriptive message.
4. Push to your fork and submit a Pull Request.
5. We will review your skill for quality, clarity, and safety.

## ⚖️ Quality Standards

- **Value**: Does this skill actually make Claude better at something?
- **Clarity**: Are the instructions easy for an LLM to follow?
- **Aesthetics**: If the skill involves UI/Design, does it produce premium results?
- **Safety**: No malware, no harmful instructions, no deceptive prompts.

---

Let's build the ultimate toolkit for Claude together! 🚀
