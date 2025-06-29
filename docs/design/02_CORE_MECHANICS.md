# 2. Core Mechanics

This document outlines the primary gameplay systems of Dungeon Codex.

## 2.1. The Gameplay Loop

The core gameplay loop is designed to be a continuous cycle of preparation, exploration, and progression.

1.  **Character Creation/Selection:** The player starts by creating a new character or selecting an existing one. They choose a name and a class (initially Alchemist or Warrior).
2.  **Dungeon Exploration:** The player enters a procedurally generated dungeon. The dungeon is a series of interconnected rooms on a grid.
3.  **Room Events:** Each room contains an event:
    -   **Combat:** A turn-based tactical battle against one or more enemies.
    -   **Treasure:** A chest with materials or, rarely, a piece of equipment.
    -   **Healing/Altar:** A one-time use opportunity to restore health or receive a temporary buff.
    -   **Narrative Event:** A short, choice-driven story moment that can result in rewards or challenges.
4.  **Dungeon Completion:** The run ends when the player either dies or defeats the final boss of the dungeon.
5.  **Progression:** Upon completing a run, the character's progress is saved. This includes collected materials, experience points, and any unlocked recipes.
6.  **Crafting & Upgrading:** Back in a safe area (the "Lab" or town), the player uses the collected materials to craft new items, upgrade existing gear, and unlock new abilities.

## 2.2. Procedural Dungeon Generation

-   Dungeons are generated as a grid of rooms.
-   The layout, room types, and enemy placements are randomized for each run to ensure high replayability.
-   The player moves from room to room, revealing the map as they explore.

## 2.3. Turn-Based Tactical Combat

-   Combat takes place on a grid within the dungeon rooms.
-   It is turn-based, with action order determined by a speed statistic.
-   On their turn, a player can:
    -   **Move:** Reposition on the grid.
    -   **Attack:** Use a standard attack.
    -   **Use an Ability:** Use a class-specific or item-granted ability. These have cooldowns or resource costs.
    -   **Use an Item:** Consume a potion or other usable item.
-   Enemies have simple AI patterns (e.g., move towards the player and attack).

## 2.4. Character Progression

-   **Stats:** Characters have core stats (HP, Damage, Defense, Speed) that can be increased by leveling up or through equipment.
-   **Classes:** The initial classes are the **Alchemist** and the **Warrior**.
    -   **Alchemist:** Focuses on potions, buffs, and debuffs. May have unique crafting recipes.
    -   **Warrior:** Focuses on direct damage and survivability. Gets bonuses with certain weapon types.
-   **Abilities:** Each class has a unique set of active and passive abilities.

## 2.5. Crafting System

-   **Materials:** Gathered from enemies, chests, and resource nodes in dungeons.
-   **Recipes:** Blueprints for crafting items. Recipes can be found in dungeons or unlocked through experimentation.
-   **Crafting:** The player combines materials according to recipes to create weapons, armor, potions, and other items.
