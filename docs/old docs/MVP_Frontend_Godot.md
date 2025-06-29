# MVP Frontend Godot

## Objective
The primary focus is to develop a native mobile version of the game, ensuring touch controls are fluid and intuitive. The web version will be derived from the mobile implementation, maintaining compatibility and responsiveness.

## Key Features

### Mobile Version
- **Touch Controls**:
  - Intuitive gestures for movement, combat, and interaction.
  - On-screen buttons for specific actions (e.g., attack, use ability).
- **Responsive UI**:
  - Optimized for various screen sizes.
  - Clear and accessible menus and interfaces.
- **Performance**:
  - Ensure smooth gameplay on mid-range Android devices.

### Web Version
- **Compatibility**:
  - Derived from the mobile version.
  - Adjustments for mouse and keyboard inputs.
- **Responsive Design**:
  - Adapt UI elements for larger screens.
  - Maintain functionality across browsers.

## Planned Scenes

### Main Menu
- **Features**:
  - Character selection.
  - Options menu (graphics, sound, controls).
  - Start game button.

### Dungeon Exploration
- **Features**:
  - Top-down view using `TileMap`.
  - Procedural generation of connected rooms.
  - Tile-by-tile player movement.
  - Detection of room events (combat, chest, healing).

### Tactical Combat
- **Features**:
  - Turn-based combat system.
  - Grid-based movement and actions.
  - UI for abilities, items, and stats.

## Integration
- **Backend Communication**:
  - Use `HTTPRequest` to interact with FastAPI.
  - Save/load character progress and dungeon exploration.
- **Local Storage**:
  - Fallback for offline mode.

## Testing
- **Mobile**:
  - Validate touch controls and responsiveness.
  - Ensure compatibility with Android devices.
- **Web**:
  - Test browser functionality and performance.
  - Verify UI adaptability for different screen sizes.
