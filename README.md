# Simple Car Simulation Game

A simple and interactive console game, written in Python, that simulates starting, stopping, and managing the state of a car through text commands.

This project is a practical example of a Finite State Machine (FSM): the behavior of the application depends on the current state (car running or stopped).

---

## 🎮 How to Play

1. Clone the repo and enter the directory:

```bash
git clone https://github.com/david11501/Simple-car-game.git
cd Simple-car-game
```

2. Run the script (Python 3):

```bash
python simple_car_game.py
```

3. Available commands in the game:

- `start`  — start the car
- `stop`   — stop the car
- `status` — display current state
- `help`   — show command list
- `quit`   — exit the game

4. Example session:

```
Simple Car Simulation. Type 'help' for commands.
> start
Car is starting...
> status
State: running
> stop
Car is stopping...
> quit
Game over — goodbye!
```

## Requirements

- Python 3 (no external dependencies)
