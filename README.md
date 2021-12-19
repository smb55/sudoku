# sudoku
Simple GUI program that solves and/or creates sudoku puzzles

Running sudoku_main.py provides a GUI program with two functions:
1) Solving a sudoku puzzle after the user enters the known numbers
2) Creating a new (somewhat) random sudoku puzzle of the desired difficulty.

sudoku.py is the file that includes the sudoku puzzle objects and their methods

sudoku_main.py imports sudoku.py and adds a GUI.

Solving methods:
This program does not implement most of the logic based methods for solving sudoku puzzles. 
The solving function simply identifies the empty squares with the least possibilities
and then uses trial and error with recursion to solve the puzzle one square at a time. Since the code 
performs well and solves even the hardest problems quickly, no further optimisations were required.

GUI - Object interations:
The GUI accepts the known values and places them into a list. 
When initialised, the SudokuPuzzle object uses accepts list of values as a paramenter. These values are
then saved as SudokuValue objects inside the SudokuPuzzle object.
Once solved, the SudokuValue object does not return the solution. The GUI program simply checks the value
of each SudokuValue object and copies the value to the GUI to display the solution.

Building methods:
In order to build a new puzzle 27 numbers are added to a static layout of predetermined positions.
These positions are set, but which numbers appear in each position is random.
From this starting position, the puzzle is solved. Then, an amount (determined by difficulty)
of random numbers are removed. After this another amount (determined by difficulty) of squares are
removed based on number of possibilities. The squares with the least number of possibilities are removed.

The building method is very rudimentary and likely to be a poor implementation. It's randomisation
is likely low, and the difficulty settings are probably a poor approximation. Plenty more work could 
be done in this area.
