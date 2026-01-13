# PyGameEngine

**PyGameEngine** is a custom game engine built in **Python**, focusing on **modularity**, **reusability**, and clean architectural design.  
It provides a structured foundation for developing 2D games while keeping core engine logic separate from gameplay rules.

This repository also serves as a long-term reference for game engine design decisions and performance considerations in Python.

---

## Features

- **Modular Architecture** – Engine components are easy to extend and reuse  
- **Core Game Mechanics** – Physics, event handling, and motor functions  
- **Structured Gameplay Logic** – Clear separation between engine and game logic  
- **Efficient Entry Point** – Clean and scalable project initialization  
- **Built with PyGame** – Uses PyGame for rendering, input, and timing  

---

## Requirements

You will need a **custom domain**.  
SendGrid Inbound Parse **does not work with free email providers**.  

I personally bought one from **Namecheap for about $2/year**.

You also need a SendGrid account with:

- Inbound Parse enabled  
- Domain authentication completed  
- MX records pointing to SendGrid  

Additionally:

- Python 3.9+  
- Flask  

---

## Installation

Clone the repository and navigate into the project directory:

```sh
git clone https://github.com/Osman-Kahraman/PyGameEngine.git
cd PyGameEngine
pip install -r requirements.txt
```

---

## Project Structure

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

---

## Usage

After the installation of required libraries,
Run this project using this command:

```sh
python3 game_engine/ui/main.py
```

---

## License

MIT License
