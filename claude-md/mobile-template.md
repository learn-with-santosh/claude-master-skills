# CLAUDE.md — Mobile (React Native) Template

This file serves as the "Project Memory" for Claude. It defines how to build, test, and maintain this specific Mobile application.

## 🛠 Build & Run Commands
- `npx expo start`: Start Expo development server
- `npm run ios`: Run on iOS Simulator
- `npm run android`: Run on Android Emulator
- `npm run lint`: Run ESLint
- `npm run test`: Run Jest tests
- `eas build`: Build for production (Expo Application Services)

## 📐 Architecture & Patterns
- **Framework**: React Native with Expo (SDK 50+)
- **Navigation**: Expo Router (File-based) or React Navigation.
- **Styling**: NativeWind (Tailwind for React Native) or StyleSheet.
- **State Management**: Zustand or TanStack Query.
- **Components**: Atomic design (Atoms, Molecules, Organisms).

## 📜 Coding Standards
- **Naming**: 
  - Components: PascalCase (`PrimaryButton.tsx`)
  - Hooks: camelCase starting with 'use' (`useBiometrics.ts`)
- **Performance**: 
  - Use `FlatList` for long lists.
  - Memoize heavy components with `React.memo`.
  - Avoid inline objects/arrays in props.
- **TypeScript**: 
  - Strict type checking.
  - Define navigation param types globally.

## 📁 Key Directories
- `app/`: Expo Router pages and layouts.
- `src/components`: UI components.
- `src/hooks`: Mobile-specific hooks (camera, location, sensors).
- `src/services`: API clients and local storage (MMKV/SQLite).
- `assets/`: Images, fonts, and icons.

## 🚀 Deployment
- Target: Apple App Store and Google Play Store.
- Use EAS for automated builds and submissions.
