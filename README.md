# advance Tic Tac Toe

This project is a Tic Tac Toe game with a graphical user interface (GUI) built using PyQt6. The game allows for both single-player and two-player modes, offering an interactive and visually appealing experience.

## Features

- **Single-Player Mode:** Play against a computer opponent with basic AI.
- **Two-Player Mode:** Play against another human player on the same device.
- **Interactive GUI:** A well-designed interface with clear visuals and responsive controls.
- **Game Reset:** Easily reset the game to start over without closing the application.

## Project Structure

- **Main UI (main.py):**  
  This file contains the `UiMainWindow` class that sets up the main window, game board, player selection, and game control buttons. It handles user interactions, such as starting or resetting the game, and displays the current player's turn.

- **Game Logic (tic_tac_toe.py):**  
  This file contains the core game logic, including the `Board`, `Player`, `Computer`, and `Game` classes. It handles the game's internal state, checks for win conditions, and manages player moves (including the computer's moves).

## How to Run

1. **Install Dependencies:**
   Ensure you have Python installed, then install the required dependencies by running:
   ```bash
   pip install PyQt6
   ```

2. **Run the Game:**
   Execute the main Python file to start the game:
   ```bash
   python main.py
   ```

3. **Enjoy the Game:**
   Use the GUI to select the number of players, start the game, and take turns playing Tic Tac Toe.

## Requirements

- Python 3.x
- PyQt6
