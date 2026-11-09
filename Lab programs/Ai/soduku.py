grid = [
    [1, 0, 0, 4],
    [0, 4, 1, 0],
    [0, 1, 4, 0],
    [4, 0, 0, 1]
]
def solve():
    for r in range(4):
        for c in range(4):
            # Find an empty cell
            if grid[r][c] == 0:
                # Try numbers from 1 to 4
                for n in range(1, 5):
                    # Check row
                    if n in grid[r]:
                        continue
                    # Check column
                    if any(grid[i][c] == n for i in range(4)):
                        continue
                    # Find 2x2 box
                    br = (r // 2) * 2
                    bc = (c // 2) * 2
                    # Check box
                    found = False
                    for i in range(br, br + 2):
                        for j in range(bc, bc + 2):
                            if grid[i][j] == n:
                                found = True
                    if found:
                        continue
                    # Place the number
                    grid[r][c] = n
                    # Solve remaining cells
                    if solve():
                        return True
                    # Backtrack if incorrect
                    grid[r][c] = 0
                return False
    return True
solve()
# Display solved Sudoku
for row in grid:
    print(row)
'''
Basic questions
1. What is Sudoku?
Sudoku is a number puzzle in which numbers must be arranged without repetition in each row, column, and box.

2. What is the purpose of this program?
To solve a 4×4 Sudoku puzzle automatically using Python.

3. What is the size of this Sudoku?
It is a 4×4 Sudoku with 16 cells.

4. What numbers are used in 4×4 Sudoku?
Numbers from 1 to 4.

5. What does 0 represent in the grid?
Zero represents an empty cell that needs to be filled.

Questions based on the code
6. Why do we use a nested list?
To represent the Sudoku grid in rows and columns.

7. What is the use of def solve()?
It defines a function that solves the Sudoku puzzle.

8. What is the use of range(4)?
It repeats the loop four times, representing four rows or columns.

9. What does grid[r][c] represent?
It represents the value at row r and column c.

10. What is the use of if grid[r][c] == 0?
It checks whether the current cell is empty.

11. What does range(1, 5) mean?
It generates numbers from 1 to 4.

12. What is the use of if n in grid[r]?
It checks whether the number already exists in the current row.

13. What does continue do?
It skips the current iteration and moves to the next number.

14. What is the use of any()?
It returns True if at least one condition in the given iterable is True.

15. Explain this statement:
python
if any(grid[i][c] == n for i in range(4)):
It checks whether the number n already exists in the current column.

Important logic questions
16. What is backtracking?
Backtracking is an algorithmic technique that tries a possible solution and goes back if that solution does not work.

17. Why do we use backtracking in Sudoku?
Because we need to try different numbers until we find a valid solution.

18. What is the purpose of br = (r // 2) * 2?
It finds the starting row of the current 2×2 box.

19. What is the purpose of bc = (c // 2) * 2?
It finds the starting column of the current 2×2 box.

20. Why do we use // instead of /?
// performs floor division and returns an integer.

21. What is the use of found = False?
It initializes a Boolean variable to indicate whether a duplicate number is found in the box.

22. Why do we use found = True?
When the number already exists in the 2×2 box, it changes the value to True.

23. What is the purpose of return False?
It indicates that the current arrangement cannot lead to a valid solution.

24. What is the purpose of return True?
It indicates that all empty cells have been filled successfully.

25. Why do we write grid[r][c] = 0?
To undo an incorrect placement during backtracking.

Tricky viva questions
26. What is recursion?
Recursion is a process in which a function calls itself.

27. Is solve() a recursive function?
Yes. It calls itself using if solve():.

28. What is the difference between recursion and iteration?
Recursion uses function calls.
Iteration uses loops.

29. What is a Boolean data type?
It represents only two values: True and False.

30. What happens if no number is suitable for an empty cell?
The function returns False and backtracks to try another number.

31. Why are there two nested loops for checking the box?
To examine all four cells inside the 2×2 box.

32. What is the time complexity of this program?
In the worst case, backtracking can take exponential time. For a 4×4 Sudoku, the search space is relatively small.

33. What is the use of print(row)?
It displays each row of the solved Sudoku grid.

Important Python concepts used
Python concept - Purpose
Nested list - Stores Sudoku grid
Function - Defines solving logic
Nested loops - Checks rows, columns and boxes
if - Checks conditions
continue - Skips invalid numbers
any() - Checks column values
range() - Generates a sequence
Recursion - Calls the solve function again
Backtracking - Reverses incorrect choices
return - Returns True or False
// - Performs floor division
'''