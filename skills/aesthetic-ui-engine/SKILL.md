---
name: aesthetic-ui-engine
description: Guides Claude to build stunning, premium, and modern web interfaces. Use this skill whenever the user asks for a UI design, a website, a component, or wants to make their web app look "premium," "professional," or "modern." This skill enforces high-end design principles like Glassmorphism, Dark Mode, sleek typography, and smooth animations.
---

# Aesthetic UI Engine 🚀

This skill transforms basic web components into premium, state-of-the-art user interfaces. It enforces design principles that make web applications feel expensive, modern, and alive.

## When to use this skill

Use this skill when:
- Designing a new web application from scratch.
- Refactoring an existing UI to look more "premium" or "professional."
- Building individual components (buttons, cards, navbars) that need to "wow" the user.
- Implementing dark mode or sophisticated color palettes.
- Adding animations and micro-interactions.

## Design Principles

### 1. The Glassmorphism Effect
Use background blur and subtle transparency to create depth.
```css
.glass {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
}
```

### 2. Modern Typography
Avoid default browser fonts. Use high-quality Google Fonts like **Inter**, **Outfit**, or **Poppins**.
- **Headings**: Semi-bold or Bold with tight letter-spacing.
- **Body**: Regular with generous line-height (1.6+).

### 3. Sophisticated Color Palettes
Avoid flat primary colors (pure red, blue, green). Use curated HSL colors:
- **Dark Mode**: Deep indigos (#0f172a), dark violets (#1e1b4b), or sleek blacks (#020617).
- **Accents**: Vibrant gradients (e.g., `linear-gradient(to right, #6366f1, #a855f7)`).

### 4. Micro-interactions
Everything should feel alive. Add hover effects and smooth transitions.
```css
.button {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.button:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px -5px rgba(99, 102, 241, 0.4);
}
```

## Output Format

Every UI design output must include:

### 1. Visual Specification
- **Color Palette**: List hex codes and their usage.
- **Typography**: Specify fonts and sizes.
- **Design Style**: Describe the "vibe" (e.g., "Minimalist Dark Mode with Neon Accents").

### 2. Implementation (Code)
- **HTML**: Clean, semantic structure.
- **CSS**: Modern, utility-first (if requested) or structured Vanilla CSS.
- **JS**: Only if needed for interactivity/animations.

### 3. Design Rational
Explain *why* these choices make the UI feel premium.

---

## Example Frameworks

### The "SaaS Hero" Section
1. **Hook**: Huge, bold heading with a gradient span.
2. **Sub-hook**: Muted text with 1.6 line height.
3. **Primary CTA**: Glowing button with a hover lift.
4. **Secondary CTA**: Ghost button with a subtle border.
5. **Background**: Radial gradient to create a "glow" behind the content.

### The "Feature Card" Grid
1. **Container**: Glassmorphism cards.
2. **Icon**: Styled with a soft background glow.
3. **Title**: High contrast.
4. **Description**: Low contrast (muted).
5. **Border**: Subtle top-border glow on hover.

---

## Safety & Accessibility
- Ensure high contrast for readability (WCAG compliance).
- Don't sacrifice usability for aesthetics.
- Keep animations subtle (don't cause motion sickness).

Use this skill by describing the component or page you want to build, and I will apply these premium design patterns to it.
