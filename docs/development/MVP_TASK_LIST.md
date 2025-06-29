# MVP Task List: Dungeon Codex

This document outlines the development tasks required to build the Minimum Viable Product (MVP) for Dungeon Codex, based on the established design documents.

## Phase 1: Backend Setup (FastAPI)

### 1.1. Database Models

-   [ ] **Task 1.1.1:** Implement the `User` model in `backend/app/db/models/user.py`.
-   [ ] **Task 1.1.2:** Implement the `Profession` model in `backend/app/db/models/profession.py`.
-   [ ] **Task 1.1.3:** Implement the `Character` model in `backend/app/db/models/character.py`.
-   [ ] **Task 1.1.4:** Implement the `DungeonRun` model in `backend/app/db/models/dungeon_run.py`.
-   [ ] **Task 1.1.5:** Create an initial SQL migration script in `backend/sql_migrations/` to create all the tables.

### 1.2. API Schemas (Pydantic)

-   [ ] **Task 1.2.1:** Create Pydantic schemas for `User` (create, read) in `backend/app/schemas/user.py`.
-   [ ] **Task 1.2.2:** Create Pydantic schemas for `Profession` in `backend/app/schemas/profession.py`.
-   [ ] **Task 1.2.3:** Create Pydantic schemas for `Character` (create, read) in `backend/app/schemas/character.py`.
-   [ ] **Task 1.2.4:** Create Pydantic schemas for `DungeonRun` in `backend/app/schemas/dungeon_run.py`.

### 1.3. API Endpoints & Logic

-   [ ] **Task 1.3.1:** Implement authentication endpoints (`/auth/register`, `/auth/login`) in `backend/app/api/routes/auth.py`.
-   [ ] **Task 1.3.2:** Implement character management endpoints (`POST /characters`, `GET /characters`, `GET /characters/{id}`) in `backend/app/api/routes/characters.py`.
-   [ ] **Task 1.3.3:** Implement dungeon run endpoint (`POST /dungeon/end`) in `backend/app/api/routes/dungeon.py`.
-   [ ] **Task 1.3.4:** Implement the endpoint to get all professions (`GET /professions`) in `backend/app/api/routes/professions.py`.

### 1.4. Backend Testing

-   [ ] **Task 1.4.1:** Write unit tests for all API endpoints.
-   [ ] **Task 1.4.2:** Write integration tests to ensure the database logic is correct.

## Phase 2: Frontend Development (Godot)

### 2.1. Core Scenes & UI

-   [ ] **Task 2.1.1:** Create the Main Menu scene with buttons for "New Game", "Load Game", and "Quit".
-   [ ] **Task 2.1.2:** Create the Character Creation scene, allowing name input and class selection (pulling data from the `/professions` endpoint).
-   [ ] **Task 2.1.3:** Design and implement the basic UI for the dungeon view (health bar, etc.).
-   [ ] **Task 2.1.4:** Design and implement the UI for the combat view (player/enemy stats, turn indicator).

### 2.2. Gameplay Implementation

-   [ ] **Task 2.2.1:** Implement the procedural dungeon generator.
-   [ ] **Task 2.2.2:** Implement tile-based player movement in the dungeon.
-   [ ] **Task 2.2.3:** Implement the turn-based combat system.
-   [ ] **Task 2.2.4:** Implement the logic for the two initial classes (Alchemist and Warrior) and their unique abilities.

### 2.3. Backend Integration

-   [ ] **Task 2.3.1:** Create a global script (`API.gd`) in Godot to handle all `HTTPRequest` calls to the backend.
-   [ ] **Task 2.3.2:** Integrate the character creation scene to send data to the `POST /characters` endpoint.
-   [ ] **Task 2.3.3:** Integrate the end-of-run summary to send data to the `POST /dungeon/end` endpoint.

## Phase 3: Finalization & Deployment

-   [ ] **Task 3.1:** Thoroughly test the full gameplay loop.
-   [ ] **Task 3.2:** Build the Godot project for Android and test on a physical device.
-   [ ] **Task 3.3:** Build the Godot project for HTML5 and deploy to a web server (like GitHub Pages or itch.io).
-   [ ] **Task 3.4:** Write clear instructions in the `README.md` on how to play the game.
