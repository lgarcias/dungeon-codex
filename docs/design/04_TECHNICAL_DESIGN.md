# 4. Technical Design

This document outlines the technical architecture, database models, and API endpoints for the Dungeon Codex MVP.

## 4.1. System Architecture

-   **Frontend:** A Godot Engine client responsible for rendering the game, handling user input, and communicating with the backend.
-   **Backend:** A FastAPI Python server that manages game logic, data persistence, and provides a RESTful API.
-   **Database:** A PostgreSQL database to store all persistent data.
-   **Communication:** The Godot client communicates with the FastAPI server via HTTP requests to the REST API.

## 4.2. Database Models (PostgreSQL)

These tables are based on the initial design and are subject to refinement.

### `users`

Stores player account information.

-   `id` (PK, UUID): Primary Key.
-   `username` (VARCHAR, UNIQUE): User's public name.
-   `email` (VARCHAR, UNIQUE): User's email for login.
-   `password_hash` (VARCHAR): Hashed password.
-   `created_at` (TIMESTAMPTZ): Timestamp of account creation.

### `professions`

Stores the definition of each playable class.

-   `id` (PK, SERIAL): Primary Key.
-   `name` (VARCHAR, UNIQUE): The name of the profession (e.g., "Alchemist", "Warrior").
-   `description` (TEXT): A brief description of the class.
-   `base_stats` (JSONB): Default stats for a new character of this class (e.g., `{"hp": 100, "damage": 10}`).

### `characters`

Represents a player's character.

-   `id` (PK, UUID): Primary Key.
-   `user_id` (FK, UUID): Foreign key to the `users` table.
-   `profession_id` (FK, INTEGER): Foreign key to the `professions` table.
-   `name` (VARCHAR): Character's name.
-   `stats` (JSONB): The character's current stats.
-   `inventory` (JSONB): A list of materials and items the character possesses.
-   `created_at` (TIMESTAMPTZ): Timestamp of character creation.

### `dungeon_runs`

Logs each dungeon exploration attempt.

-   `id` (PK, UUID): Primary Key.
-   `character_id` (FK, UUID): The character that participated in this run.
-   `dungeon_level` (INTEGER): The level or difficulty of the dungeon.
-   `materials_collected` (JSONB): Materials gathered during the run.
-   `completed_at` (TIMESTAMPTZ): Timestamp when the run finished.

## 4.3. API Endpoints (FastAPI)

These are the initial REST API endpoints required for the MVP.

### Authentication

-   `POST /auth/register`: Create a new user account.
-   `POST /auth/login`: Authenticate a user and return a JWT token.

### Characters

-   `POST /characters`: Create a new character for the logged-in user.
    -   Request Body: `{"name": "string", "profession_id": integer}`
-   `GET /characters`: Get a list of all characters for the logged-in user.
-   `GET /characters/{character_id}`: Get the details of a specific character.

### Game Loop

-   `POST /dungeon/start`: (Optional) Could be used to initialize a new dungeon run.
-   `POST /dungeon/end`: Save the results of a dungeon run.
    -   Request Body: `{"character_id": "uuid", "materials_collected": {...}}`

### Game Data

-   `GET /professions`: Get a list of all available professions to show on the character creation screen.
