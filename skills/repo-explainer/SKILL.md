---
name: repo-explainer
description: Helps Claude explain complex codebases, folder structures, and tech stacks. Use this skill whenever a user asks "what does this repo do?", "how is this project structured?", "where is the logic for X?", or needs an onboarding guide for a new repository.
---

# Repo Explainer 📂

This skill transforms a collection of files into a clear, understandable architectural map. It helps users (especially beginners or new contributors) navigate and understand a codebase quickly.

## When to use this skill

Use this skill when:
- A user is new to a repository and wants an overview.
- Explaining the relationship between different modules/folders.
- Identifying the tech stack and core dependencies.
- Documenting the high-level architecture.
- Helping a user find where a specific feature is implemented.

## Core Framework: The "Layered Deep-Dive"

When explaining a repo, follow this sequence:

### 1. The High-Level Pitch (The "What")
- **Purpose**: 1-2 sentences on what the project actually does.
- **Value Proposition**: Why does it exist?

### 2. The Tech Stack (The "How")
- **Frontend**: Frameworks, styling libraries.
- **Backend**: Runtime, language, database.
- **DevOps**: Deployment, CI/CD, scripts.

### 3. Folder Map (The "Where")
Provide a curated tree view with descriptions:
```txt
src/
├── components/  # Reusable UI elements
├── hooks/       # Custom React logic
├── services/    # API calls and data fetching
└── utils/       # Helper functions
```

### 4. Core Logic Flow (The "Why")
Describe the "happy path" or the main execution flow.
"When a user does X, the system triggers Y in `service/A.ts` and updates Z."

## Output Format

### 📦 Repository Overview
A brief summary of the project.

### 🛠️ Tech Stack
Bullet points of the main technologies used.

### 📁 Structure Walkthrough
A guided tour of the important directories.

### 🚀 Getting Started (Contextual)
Based on the `package.json` or equivalent, tell the user how to run the project.

---

## Examples

### Example 1: Explaining a Next.js App
**Input**: "What is this project?"
**Output**: 
"This is a **Next.js 14** application for managing tasks. It uses **Prisma** for database access and **TailwindCSS** for styling.
- `/app`: Contains the main routes and pages.
- `/components`: Shared UI like Buttons and Modals.
- `/lib`: Database client and shared utilities.
To start, run `npm install` and then `npm run dev`."

### Example 2: Deep Dive into Logic
**Input**: "Where is the auth logic?"
**Output**:
"The authentication logic is centralized in `/src/auth/`.
1. Middleware check: `middleware.ts` handles session validation.
2. Provider: `AuthProvider.tsx` wraps the app to provide user context.
3. API: `api/auth/[...nextauth].ts` handles the OAuth callbacks."

---

## Best Practices
- **Be Concise**: Don't list every single file; focus on the important ones.
- **Stay Updated**: Always check the root config files (`package.json`, `go.mod`, `pyproject.toml`) first.
- **Link Files**: If your environment supports it, provide clickable links to the files you mention.
