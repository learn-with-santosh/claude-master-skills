# CLAUDE.md — Next.js Master Template

This file serves as the "Project Memory" for Claude. It defines how to build, test, and maintain this specific Next.js codebase.

## 🛠 Build & Run Commands
- `npm run dev`: Start development server
- `npm run build`: Build production bundle
- `npm run start`: Run production server
- `npm run lint`: Run ESLint
- `npm run test`: Run Vitest/Jest
- `npm run type-check`: Run TypeScript validation

## 📐 Architecture & Patterns
- **Framework**: Next.js 14+ (App Router)
- **Styling**: TailwindCSS (Utility-first)
- **State Management**: React Context or Zustand
- **Data Fetching**: Server Components by default; Client Components only when needed for interactivity.
- **Form Handling**: React Hook Form + Zod for validation.
- **API**: Route Handlers in `app/api/`.

## 📜 Coding Standards
- **Naming**: 
  - Components: PascalCase (`UserButton.tsx`)
  - Hooks: camelCase starting with 'use' (`useLocalStorage.ts`)
  - Utilities: kebab-case (`date-formatter.ts`)
- **TypeScript**: 
  - Use `interface` for object shapes.
  - Avoid `any`. Use `unknown` or specific types.
  - Use `type` for unions/intersections.
- **Formatting**: 
  - Use 2-space indentation.
  - Semicolons are required.
  - Use arrow functions for components.

## 📁 Key Directories
- `/app`: Pages, layouts, and API routes.
- `/components`: Reusable UI components.
- `/hooks`: Custom React hooks.
- `/lib`: Third-party clients (Prisma, Stripe) and shared utilities.
- `/types`: Global TypeScript definitions.

## 🚀 Deployment
- Primary target: Vercel.
- Ensure environment variables are documented in `.env.example`.
