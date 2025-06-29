# 3. MVP Specification

This document defines the precise scope of the Minimum Viable Product (MVP) for Dungeon Codex.

## 3.1. MVP Goal

To deliver a functional prototype that validates the core gameplay loop (exploration, combat, progression) on Android and Web platforms. The experience should be fun and demonstrate the game's potential.

## 3.2. Included Features

### Character

-   **Creation:** Players can create a character with a name.
-   **Classes:** Two playable classes:
    -   **Alchemist**
    -   **Warrior**
-   Each class will have 1 unique passive ability and 1 unique active ability.

### Dungeon & Exploration

-   **Procedural Generation:** Dungeons are procedurally generated as a grid of connected rooms.
-   **Top-Down View:** Exploration is from a top-down perspective.
-   **Tile-Based Movement:** The player moves one tile at a time.
-   **Room Events:** The following events are included:
    -   Combat with a random basic enemy.
    -   A treasure chest with a random reward.
    -   A healing altar (guaranteed to appear once per dungeon run).

### Combat

-   **Turn-Based:** Combat is turn-based on a grid.
-   **Player Actions:** Move, Attack, Use one active ability.
-   **Enemies:** 1-2 basic enemy types with simple AI (move and attack).

### Progression

-   **Persistence:** Character progress (stats, collected materials) is saved only at the end of a dungeon run.
-   **Summary Screen:** A screen at the end of the run shows a summary of materials gathered.

## 3.3. Technical Requirements

-   **Backend:** FastAPI with a PostgreSQL database.
-   **Frontend:** Godot 4.2+.
-   **Platforms:**
    -   Android (Native App)
    -   HTML5 (Web Browser)
-   **API:** A REST API for communication between the frontend and backend to manage character data and progress.

## 3.4. Exclusions for MVP

The following features are explicitly **out of scope** for the MVP:

-   Card crafting or any card-based mechanics.
-   Laboratory/Workshop area.
-   Hero companions.
-   Advanced combat mechanics (e.g., complex status effects, multiple abilities).
-   Blockchain integration.
-   Multiple dungeon types or biomes.
-   Story or narrative events.
-   Sound and music.
