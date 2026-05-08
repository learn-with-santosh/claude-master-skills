# CLAUDE.md — Laravel Master Template

This file serves as the "Project Memory" for Claude. It defines how to build, test, and maintain this specific Laravel codebase.

## 🛠 Build & Run Commands
- `php artisan serve`: Start development server
- `php artisan migrate`: Run database migrations
- `php artisan test`: Run Pest/PHPUnit tests
- `php artisan tinker`: Open interactive shell
- `npm run dev`: Build frontend assets (Vite)
- `composer install`: Install PHP dependencies

## 📐 Architecture & Patterns
- **Framework**: Laravel 11+
- **Pattern**: Standard MVC, but prefer **Service Classes** for complex business logic.
- **Frontend**: Blade + Livewire (TALL stack) or Vue/React via Inertia.js.
- **Database**: Eloquent ORM. Use Factories and Seeders for all models.
- **API**: Standard Laravel API routes with Resource classes for transformation.

## 📜 Coding Standards
- **Naming**: 
  - Controllers: PascalCase ending in Controller (`UserController.php`)
  - Models: Singular PascalCase (`User.php`)
  - Migrations: snake_case (`create_users_table.php`)
  - Methods: camelCase (`getUserData`)
- **PHP**: 
  - Use strict types (`declare(strict_types=1);`).
  - Use constructor property promotion.
  - Type hint everything (params and return types).
- **Formatting**: 
  - PSR-12 standard.
  - 4-space indentation.

## 📁 Key Directories
- `app/Models`: Eloquent models.
- `app/Http/Controllers`: Logic for handling requests.
- `app/Services`: Custom business logic (if applicable).
- `database/migrations`: Database schema definitions.
- `resources/views`: Blade templates or Inertia pages.

## 🚀 Deployment
- Primary target: Laravel Forge / Vapor.
- Ensure `config:cache` and `route:cache` are run in production.
