# MVP General Design

## Completed Tasks

### A. General Design

- **Define character data structure**: The character data structure has been implemented, including attributes such as name, class, stats, and abilities.
- **Define base classes**: The base classes, Alchemist and Warrior, have been partially defined, with progress ongoing.
- **Define backend structure**: The backend structure has been outlined, including entities, API routes, and progress persistence mechanisms.

## Database Models

### User
- **Table Name**: `users`
- **Fields**:
  - `id`: Primary key, unique identifier for each user.
  - `username`: String, unique name for the user.
  - `email`: String, unique email address.
  - `password_hash`: String, hashed password for authentication.
  - `created_at`: Timestamp, date and time of user creation.
- **Description**: Stores user account information for authentication and identification.

### Character
- **Table Name**: `characters`
- **Fields**:
  - `id`: Primary key, unique identifier for each character.
  - `user_id`: Foreign key, links the character to a user.
  - `name`: String, name of the character.
  - `profession`: String, character profession (e.g., Alchemist, Warrior).
  - `stats`: JSON, stores character stats such as HP, damage, defense, and speed.
  - `abilities`: JSON, list of abilities the character possesses.
  - `created_at`: Timestamp, date and time of character creation.
- **Description**: Represents playable characters created by users.

### Progress
- **Table Name**: `progress`
- **Fields**:
  - `id`: Primary key, unique identifier for each progress entry.
  - `user_id`: Foreign key, links the progress to a user.
  - `character_id`: Foreign key, links the progress to a character.
  - `dungeon_level`: Integer, level of the dungeon explored.
  - `materials_collected`: JSON, list of materials gathered during exploration.
  - `completed_at`: Timestamp, date and time of dungeon completion.
- **Description**: Tracks user progress and exploration results.

### Profession
- **Table Name**: `professions`
- **Fields**:
  - `id`: Primary key, unique identifier for each profession.
  - `name`: String, name of the profession (e.g., Alchemist, Warrior).
  - `description`: String, brief description of the profession.
  - `base_stats`: JSON, default stats for the profession (e.g., HP, damage, defense, speed).
  - `abilities`: JSON, default abilities associated with the profession.
- **Description**: Stores available professions and their attributes, ensuring consistency and enabling easy updates or additions.

### Materials
- **Table Name**: `materials`
- **Fields**:
  - `id`: Primary key, unique identifier for each material.
  - `name`: String, name of the material (e.g., essence, powder).
  - `description`: String, brief description of the material.
  - `rarity`: String, rarity level of the material (e.g., common, rare).
- **Description**: Stores information about materials used for crafting and upgrading.

### Recipes
- **Table Name**: `recipes`
- **Fields**:
  - `id`: Primary key, unique identifier for each recipe.
  - `name`: String, name of the recipe.
  - `description`: String, brief description of the recipe.
  - `required_materials`: JSON, list of materials needed for the recipe.
  - `result`: JSON, details of the crafted item or card.
- **Description**: Tracks crafting recipes and their requirements.

### Dungeon Rooms
- **Table Name**: `dungeon_rooms`
- **Fields**:
  - `id`: Primary key, unique identifier for each room.
  - `dungeon_id`: Foreign key, links the room to a dungeon.
  - `type`: String, type of room (e.g., combat, chest, healing).
  - `content`: JSON, details of the room's content (e.g., enemies, rewards).
- **Description**: Represents individual rooms within a dungeon.

### Events
- **Table Name**: `events`
- **Fields**:
  - `id`: Primary key, unique identifier for each event.
  - `name`: String, name of the event.
  - `description`: String, brief description of the event.
  - `effect`: JSON, details of the event's impact (e.g., buffs, debuffs).
- **Description**: Stores narrative or gameplay events encountered during exploration.
