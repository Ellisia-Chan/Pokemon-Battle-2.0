# Pokemon-Battle-2.0

[![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
![Generic badge](https://img.shields.io/badge/Development%3f-Complete-blue.svg)
![Developer](https://img.shields.io/badge/Developer-Ellisia-pink)

This Python project simulates a turn-based Pokemon battle game with features like:

- **Pokemon Selection:** Choose 3-4 Pokemon from a pool of 10.
- **Battle Preparation:** Use potions to increase your Pokemon's power and poison to decrease the opponent's power.
- **Battle Mechanics:** Each Pokemon has a base health and power. The Pokemon with higher power wins the battle.
- **Post-Battle Adjustments:**  Health and power adjustments are applied to the winner and loser based on battle outcomes.
- **Fatigue Effects:**  Both Pokemon's health decrease slightly after every battle due to fatigue.
- **Battle Stats Tracking:**  Track the number of wins, losses, and ties for each player.
- **User-Friendly Interface:**  Utilizes the `prettytable` library for clear, formatted display of Pokemon information and battle statistics.

## Navigation

* [Project Structure](#Project-Structure)
* [Key Files](#Key-Files)
* [Installation](#Installation)
* [Running the Game](#Running-the-Game)
* [Features](#Features)
* [Preview](#Preview) 



## Project Structure:

```
├── BattleStatsManager.py
├── DisplayManager.py
├── GameManager.py
├── PokemonArray.py
├── main.py
└── packages.py
```

## Key Files:

- **BattleStatsManager.py:**  Handles the tracking of battle statistics, including wins, losses, and ties.
- **DisplayManager.py:**  Manages the display of various game elements, including menus, Pokemon information, battle stats, and game messages.
- **GameManager.py:**  The core logic of the game, managing Pokemon selection, battle preparation, battle outcomes, and post-battle adjustments.
- **PokemonArray.py:**  Creates and manages the array of Pokemon with their initial attributes, including health, power, potions, and poison.
- **main.py:**  The entry point of the game, where the game loop and user interaction are managed.
- **packages.py:**  Checks and installs necessary Python packages (like `prettytable`) if they are not already installed.

## Installation:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Pokemon-Battle-2.0.git
   ```
2. **Install dependencies:**
   ```bash
   cd Pokemon-Battle-2.0
   python packages.py
   ```

## Running the Game:

1. **Navigate to the project directory:**
   ```bash
   cd Pokemon-Battle-2.0
   ```
2. **Run the main script:**
   ```bash
   python main.py
   ```

## Features:

- **Colorful Output:**  The game uses ANSI escape codes to make the output more visually appealing.
- **User-Friendly Input:**  Prompts guide the player through the selection process and battle actions.
- **Comprehensive Stats:**  Track wins, losses, and ties for each player, providing a clear overview of the game's outcome.
- **Dynamic Adjustments:**  Health and power adjustments after each battle create an engaging and strategic experience.

## Preview:
![image](https://github.com/user-attachments/assets/f2c2a139-9686-4e5b-a391-d2a5696e6646)<br>
![image](https://github.com/user-attachments/assets/ea60e063-3742-4b1c-890d-fa7ba063c7a9)
![image](https://github.com/user-attachments/assets/e3fb341a-aa54-4b17-a04d-2ae4ee2b050a)
![image](https://github.com/user-attachments/assets/0ac59fab-3e37-4c4e-885f-20ba3fde2bdf)
![image](https://github.com/user-attachments/assets/f98ab8f9-79b3-4aeb-bc7b-80902576bc0b)
