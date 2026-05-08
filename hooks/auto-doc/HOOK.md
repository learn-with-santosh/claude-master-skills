---
name: auto-doc
description: Automatically updates project documentation (README, JSDoc, etc.) based on code changes. Use this skill whenever a feature is added or modified to ensure the documentation stays in sync with the codebase.
---

# Auto Documentation Hook 📝

Documentation is often the first thing to go stale. This skill ensures your README, API docs, and internal comments are always up to date with your latest code changes.

## When to use this skill

Use this skill when:
- You've added a new feature and need to document it in the README.
- You've changed an API signature and need to update JSDoc/TS comments.
- You've reorganized the project structure and need to update the folder map.

## How it works

1. **Scan**: Claude identifies files that have changed in the current session.
2. **Analyze**: Understands the new functionality or structural changes.
3. **Sync**: Suggests specific edits to `README.md`, `CLAUDE.md`, or relevant source files.

## Output Format

Claude will provide a diff or a block of content for the specific documentation file.

---

## Examples

### Example 1: Updating README Gallery
**Change**: Added a new "Billing" module.
**Output**: 
"I've detected the new Billing module. I'll update the 'Features' section in the README:
```md
- [x] Auth System
- [x] Task Management
- [x] Billing & Subscriptions (New)
```"

### Example 2: Updating Function Comments
**Change**: Added a `timeout` parameter to `fetchData()`.
**Output**:
"Updating JSDoc for `fetchData`:
```typescript
/**
 * @param {string} url - The target URL
 * @param {number} timeout - Request timeout in ms (added)
 */
```"

---

## Best Practices
- **Run after feature completion**: Use this as the final step of a feature branch.
- **Maintain Consistency**: Ensure the new documentation matches the tone and style of the existing docs.
- **Check CLAUDE.md**: Always update your "Project Memory" file to keep Claude aligned.
