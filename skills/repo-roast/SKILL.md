---
name: repo-roast
description: Provides a brutally honest, funny, and "roast-style" analysis of a repository. Use this skill whenever a user says "roast my repo", "be honest about my code", or "give me some tough love on this project." This is designed for viral sharing and social media.
---

# Repo Roast Tool 🔥

Is your code a masterpiece or a crime scene? This skill provides a "no-filter" analysis of your repository. It points out tech debt, questionable naming choices, and "I'll fix this later" comments that have been there for 2 years.

## When to use this skill

Use this skill when:
- A user wants a humorous critique of their project.
- You're looking for a fun way to identify obvious tech debt.
- Creating content for X (Twitter), LinkedIn, or Reddit to drive engagement.

## The Roast Framework

### 1. The "Tech Stack" Roast
Critique their choice of frameworks. 
"Oh, another Next.js app with Tailwind? How original. You're like the vanilla latte of developers."

### 2. The "Folder Structure" Chaos
Find the messy directories.
"Your `/utils` folder is where logic goes to die. It's basically a junk drawer for code you didn't know where to put."

### 3. The "Ghost Comments"
Find the TODOs and commented-out code.
"You have `// TODO: Fix this` from 2022. That's not a task; that's a historical artifact at this point."

### 4. The "Naming Crime"
Mock the variable names.
"Variable `temp1`, `data2`, and `thingy`? I've seen more descriptive names in a toddler's coloring book."

## Output Format

### 🏁 The Verdict
A brutal 1-sentence summary of the repo.

### 🔥 The Roasts
3-5 punchy, humorous critiques of specific files or patterns.

### 🩹 The "Tough Love" Advice
One actual, serious suggestion to fix the biggest mess.

---

## Examples

### Example 1: Roast of a messy Python script
**Output**: 
"**The Verdict**: This repo is held together by hope and spaghetti.
**The Roasts**:
- 'You have a 4,000 line `main.py`. The file isn't a script; it's a novel.'
- 'Global variables everywhere? It's 2026, not 1995.'
- 'Your error handling is just `try: ... except: pass`. That's not coding; that's hiding the evidence.'
**Tough Love**: Break that `main.py` into modules before it gains sentience and deletes itself."

---

## Safety Disclaimer
- **Keep it professional-adjacent**: Don't use actual insults or offensive language. Focus on the *code* and *dev tropes*.
- **Know the audience**: Only use this if the user explicitly asks for a roast.
- **Balance with Value**: The "Tough Love" section should provide actual engineering value.
