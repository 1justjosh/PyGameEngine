```
PyGameEngine/
├── game_engine/                # Core game engine package
│   ├── __pycache__/            # Python bytecode cache
│   │
│   ├── items/                  # Game entities & world objects
│   │   ├── __pycache__/
│   │   ├── character.py        # Player character logic
│   │   ├── enemy_1.py          # Enemy behavior & AI
│   │   ├── streetLight.py      # Environment / static objects
│   │   ├── template.py         # Base template for new game items
│   │   └── info.json           # Item metadata & configuration
│   │
│   ├── ui/                     # UI & gameplay flow layer
│   │   ├── __pycache__/
│   │   ├── images/             # UI-related assets
│   │   ├── designer.py         # UI layout & scene composition
│   │   ├── event.py            # Centralized event handling
│   │   ├── game.py             # Core gameplay state & loop control
│   │   ├── home.py             # Home / menu screen logic
│   │   ├── main.py             # Engine entry point
│   │   ├── tiles.py            # Tile rendering & map logic
│   │   └── tiles.json          # Tile definitions & level data
│   │
│   ├── gameMotors.py           # Engine motors (physics, update loop)
│   └── news.txt                # Engine notes / dev logs
│
├── images/                     # Global game assets
│
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
├── LICENSE                     # MIT License
└── .gitattributes
```

# Architectural Overview

This document describes the internal architecture of **PyGameEngine**, focusing on how responsibilities are separated across engine layers and how different components interact during runtime.

PyGameEngine is designed as a **modular, layered game engine**, prioritizing clarity, reusability, and performance in real-time applications.

---

## High-Level Architecture

The engine is organized into four main layers:

1. **Engine Core**
2. **Gameplay & Entities**
3. **UI & Game Flow**
4. **Data & Configuration**

Each layer has a clearly defined responsibility and communicates with others through well-defined boundaries.

---

## 1. Engine Core Layer

**Location:**  
```
game_engine/gameMotors.py
```

### Responsibilities
- Runs the main game loop
- Controls frame timing and tick rate
- Propagates update and render cycles
- Handles physics and movement updates

### Design Notes
- Independent from gameplay rules
- Does not contain UI or entity-specific logic
- Acts as the “motor” of the engine

---

## 2. Gameplay & Entity Layer

**Location:**  
```
game_engine/items/
```

### Responsibilities
- Defines all in-game objects (player, enemies, environment)
- Encapsulates object behavior and state
- Interacts with the engine via shared update methods

### Key Files
- `character.py` – Player logic
- `enemy_1.py` – Enemy AI and behavior
- `streetLight.py` – Static environment objects
- `template.py` – Base template for reusable entities
- `info.json` – Metadata and configuration

---

## 3. UI & Game Flow Layer

**Location:**  
```
game_engine/ui/
```

### Responsibilities
- Scene management (home, game, pause)
- Centralized event handling
- Tile-based rendering
- UI layout and composition

### Key Files
- `main.py` – Engine entry point
- `game.py` – Active gameplay state
- `home.py` – Menu / home screen
- `event.py` – Input and event abstraction
- `designer.py` – UI layout logic
- `tiles.py` – Tile rendering
- `tiles.json` – Map and tile data

---

## 4. Data & Configuration Layer

**Files:**
```
tiles.json
info.json
```

### Responsibilities
- Stores configuration and level data
- Enables data-driven behavior
- Reduces hardcoded logic

---

## Runtime Flow

1. `ui/main.py` initializes the engine  
2. Engine core starts the main loop  
3. Events are captured and processed  
4. Game entities update their state  
5. Physics and movement are applied  
6. Rendering is executed  
7. Loop continues until exit  

---

## Design Principles

- **Separation of Concerns**
- **Modularity**
- **Reusability**
- **Object-Oriented Architecture**
- **Performance Awareness**

---

## Summary

PyGameEngine’s architecture is intentionally simple but scalable.  
By isolating engine mechanics, gameplay logic, and UI flow, it provides a clean foundation for building and extending real-time Python games using PyGame.
