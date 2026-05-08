---
name: auto-commit
description: Automatically generates high-quality, semantic commit messages. Use this skill whenever a user wants to "commit these changes", "stage and commit", or needs a descriptive message for their git history.
---

# Auto Commit Hook 🤖

This skill automates the most tedious part of the git workflow: writing meaningful commit messages. It analyzes your changes and generates messages following the [Conventional Commits](https://www.conventionalcommits.org/) standard.

## When to use this skill

Use this skill when:
- You've finished a feature or bug fix and are ready to commit.
- You have multiple staged changes and want a clear summary.
- You want to maintain a professional and readable git history.

## How it works

1. **Analyze**: Claude reads the `git diff --staged`.
2. **Categorize**: Determines if the change is a `feat`, `fix`, `docs`, `style`, `refactor`, `test`, or `chore`.
3. **Draft**: Generates a punchy subject line (< 50 chars) and a descriptive body.

## Output Format

Claude will output the commit command directly:
```bash
git commit -m "type(scope): subject" -m "Detailed description of changes."
```

---

## Examples

### Example 1: New Feature
**Changes**: Added a new login page and auth service.
**Output**:
`git commit -m "feat(auth): implement login page and auth service" -m "- Added login form with validation\n- Created AuthProvider for session management\n- Integrated with Firebase Auth"`

### Example 2: Bug Fix
**Changes**: Fixed a typo in a CSS class that was hiding a button.
**Output**:
`git commit -m "fix(ui): resolve visibility issue on submit button" -m "Fixed a typo in the .hidden class selector in global.css."`

---

## Best Practices
- **Stage First**: Always ensure your changes are staged (`git add .`) before triggering this skill.
- **Review**: Claude will provide the message; you should give a quick "LGTM" before it executes.
- **Scope**: Try to include the component or module name in the parenthesis (e.g., `feat(ui)`, `fix(api)`).
