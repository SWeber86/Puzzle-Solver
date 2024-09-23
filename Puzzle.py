import tkinter as tk
from tkinter import messagebox
import time


def is_valid(grid, row, col, num):
    """Checks if placing a number at a given position is valid."""
    # Check the row
    if num in grid[row]:
        return False
    # Check the column
    if num in [grid[i][col] for i in range(9)]:
        return False
    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    return True


def solve_sudoku(grid):
    """Solves the Sudoku puzzle using a brute-force method and visualizes the process."""
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers 1 to 9
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        update_grid_display(entries, grid, row, col, num)
                        root.update()  # Force the window to update and show the number being tried
                        time.sleep(0.05)  # Pause to visually show the number being tried

                        if solve_sudoku(grid):
                            return True

                        # If no solution is found, backtrack
                        grid[row][col] = 0
                        update_grid_display(entries, grid, row, col, 0)
                        root.update()  # Force the window to update and show backtracking
                        time.sleep(0.05)  # Pause to visually show backtracking

                return False  # Trigger backtracking if no valid number found
    return True


def get_grid_from_entries(entries):
    """Extracts the Sudoku grid from the entry fields."""
    grid = []
    for row in range(9):
        grid_row = []
        for col in range(9):
            val = entries[row][col].get()
            if val.isdigit() and 1 <= int(val) <= 9:
                grid_row.append(int(val))
            else:
                grid_row.append(0)
        grid.append(grid_row)
    return grid


def update_grid_display(entries, grid, row, col, num):
    """Updates the displayed grid based on the current state of the solver, showing the current number being tried."""
    entries[row][col].delete(0, tk.END)
    if num != 0:
        entries[row][col].insert(0, str(num))


def solve():
    """Handles the solve button click and initiates the solving process."""
    grid = get_grid_from_entries(entries)
    if solve_sudoku(grid):
        messagebox.showinfo("Sudoku Solver", "Puzzle solved successfully!")
    else:
        messagebox.showerror("Sudoku Solver", "No solution exists for the given Sudoku puzzle.")


def clear_grid():
    """Clears the Sudoku grid to allow a new puzzle to be entered."""
    for row in range(9):
        for col in range(9):
            entries[row][col].delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("Sudoku Solver - Brute Force Visualization")

# Create a 9x9 grid of entry fields
entries = [[None for _ in range(9)] for _ in range(9)]
for row in range(9):
    for col in range(9):
        entry = tk.Entry(root, width=2, font=('Arial', 18), justify='center')
        entry.grid(row=row, column=col, padx=5, pady=5)
        entries[row][col] = entry

# Add a solve button
solve_button = tk.Button(root, text="Solve", command=solve)
solve_button.grid(row=9, column=0, columnspan=4)

# Add a clear button
clear_button = tk.Button(root, text="Clear", command=clear_grid)
clear_button.grid(row=9, column=5, columnspan=4)

# Run the application
root.mainloop()