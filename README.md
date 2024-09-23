# Puzzle-Solver
Brute Force Sudoku 9x9 Puzzles in Python
# Sudoku Solver with Brute Force Visualization

This Python script is a graphical Sudoku solver built using `Tkinter`. It uses a brute-force method to solve Sudoku puzzles and visualizes the solving process in real-time on a 9x9 grid. The solver attempts to fill in numbers, backtracking when necessary, and displays the process directly in the grid interface.

## Features

- **Visual Solver**: Watch the solver attempt to fill in the grid step-by-step.
- **Brute Force**: The solver uses a brute-force approach, trying every possible number until it finds a valid solution.
- **User Input**: Enter your own Sudoku puzzle in the 9x9 grid, and the solver will attempt to solve it.
- **Clear Grid**: Start over by clearing the grid with a button click.
- **Real-Time Updates**: The GUI updates in real-time as the solver progresses, showing each number being tried and the backtracking steps.

## How It Works

- **Backtracking Algorithm**: The algorithm tries to place a valid number (1-9) in each empty cell. If a valid number can't be found, the solver backtracks to the previous cell and tries a different number.
- **Grid Input**: The user can input a Sudoku puzzle in the 9x9 grid. Empty cells should be left blank or set to `0`.

## Requirements

- Python 3.x
- `tkinter` (This is included with most standard Python installations)
