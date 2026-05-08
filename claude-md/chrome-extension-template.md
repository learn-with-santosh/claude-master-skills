# CLAUDE.md — Chrome Extension Template

This file serves as the "Project Memory" for Claude. It defines how to build, test, and maintain this specific Chrome Extension.

## 🛠 Build & Run Commands
- `npm run dev`: Build with hot-reload (if using a bundler like Vite/Webpack)
- `npm run build`: Production build (Manifest V3)
- `npm run zip`: Package for Chrome Web Store
- **Installation**: Load unpacked from the `dist/` or root folder in `chrome://extensions`.

## 📐 Architecture & Patterns
- **Manifest Version**: V3 (Required)
- **Background Script**: Service Workers (No persistent background pages).
- **Content Scripts**: Isolated world logic for interacting with web pages.
- **Popup/Options**: Standard HTML/CSS/JS (React/Vue recommended for complex UIs).
- **Messaging**: Use `chrome.runtime.sendMessage` for one-time requests and `chrome.runtime.connect` for long-lived connections.

## 📜 Coding Standards
- **Asynchronous Code**: Use `async/await` instead of callbacks where possible.
- **Security**: 
  - Avoid `innerHTML`. Use `textContent` or sanitized templates.
  - Follow strict Content Security Policy (CSP).
- **Naming**: 
  - Scripts: kebab-case (`content-script.js`, `background-worker.js`).
  - Assets: snake_case (`icon_128.png`).

## 📁 Key Directories
- `src/background`: Service worker logic.
- `src/content`: Content scripts.
- `src/popup`: UI for the extension popup.
- `src/options`: UI for extension settings.
- `public`: Static assets and the `manifest.json`.

## 🚀 Deployment
- Target: Chrome Web Store / Microsoft Edge Add-ons.
- Always include a privacy policy if requesting sensitive permissions.
