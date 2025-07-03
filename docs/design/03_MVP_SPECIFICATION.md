# MVP Specification

This document outlines the Minimum Viable Product (MVP) for the Dungeon Codex project.

## 1. Core Loop

The core gameplay loop consists of:
1.  Creating a character.
2.  Choosing a profession.
3.  Running a dungeon.
4.  Viewing results.

## 2. Key Features

-   User registration and login.
-   Character creation and management.
-   A selection of starting professions.
-   A single, repeatable dungeon experience.
-   Score tracking for dungeon runs.

## 3. API Endpoints (High-Level)

-   `POST /auth/register`: Create a new user.
-   `POST /auth/login`: Authenticate and get a token.
-   `GET /professions`: List available professions.
-   `POST /characters`: Create a new character.
-   `GET /characters`: List user's characters.
-   `POST /dungeon/end`: Record the result of a dungeon run.

## 4. Data Models

The core data models for the MVP are defined as follows, corresponding to the database tables.

### 4.1. Users

Stores user account information for authentication and linking to characters.

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `UUID` | Primary key, unique user identifier. |
| `email` | `VARCHAR` | Unique email for login. |
| `password_hash`| `VARCHAR` | Hashed user password. |
| `created_at` | `TIMESTAMPTZ` | Timestamp of user creation. |

### 4.2. Professions

Defines the available character classes in the game, seeded with initial data.

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `SERIAL` | Primary key, unique profession identifier. |
| `name` | `VARCHAR` | Unique name of the profession (e.g., "Warrior"). |
| `description` | `TEXT` | A brief description of the profession. |
| `base_stats` | `JSONB` | Base statistics (HP, mana, damage, etc.). |
| `base_inventory` | `JSONB` | Starting items for the profession. |

### 4.3. Characters

Represents a player's character, linked to a user and a profession.

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `SERIAL` | Primary key, unique character identifier. |
| `name` | `VARCHAR` | The character's name. |
| `level` | `INTEGER` | The character's current level. |
| `user_id` | `UUID` | Foreign key linking to the `users` table. |
| `profession_id` | `INTEGER` | Foreign key linking to the `professions` table. |

### 4.4. Dungeon Runs

Records the outcome of each dungeon attempt by a character.

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `SERIAL` | Primary key, unique run identifier. |
| `score` | `INTEGER` | Score achieved during the run. |
| `completed_at` | `TIMESTAMPTZ` | Timestamp when the run finished. |
| `is_successful`| `BOOLEAN` | Whether the character successfully cleared the dungeon. |
| `character_id` | `INTEGER` | Foreign key linking to the `characters` table. |