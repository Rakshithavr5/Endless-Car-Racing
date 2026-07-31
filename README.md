# 🚗 Endless Car Racing Game

## 📌 Project Overview

Endless Car Racing is a modular racing game built using Python and Pygame. The player controls a car that moves left and right to avoid incoming enemy vehicles while traveling on an endless scrolling road.

This project is designed with clean architecture so it can be extended in future with AI facial-expression controls.

---

## Features

- Endless scrolling road
- Smooth 60 FPS gameplay
- Player car movement
- Random enemy car spawning
- Collision detection
- Score system
- Distance tracker
- High score
- Dynamic speed increase
- Start screen
- Pause menu
- Game Over screen
- Modular architecture

---

## Technologies Used

- Python 3
- Pygame

---

## Project Structure

```
Endless-Car-Racing/
│
├── assets/
│   ├── images/
│   ├── sounds/
│   └── fonts/
│
├── game/
│   ├── car.py
│   ├── collision.py
│   ├── game.py
│   ├── obstacle.py
│   ├── road.py
│   ├── score.py
│   └── ui.py
│
├── main.py
├── settings.py
├── requirements.txt
└── README.md
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

---

## Controls

- ← Move Left
- → Move Right
- P Pause
- R Restart (Game Over)
- ESC Exit

---

## Future Improvements

- AI facial-expression controls
- Real car sprites
- Sound effects
- Multiple levels
- Coins and power-ups
- Leaderboard