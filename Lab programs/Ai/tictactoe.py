# 2 Player Tic Tac Toe
board = [" "] * 9
def show():
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])
for turn in range(9):
    show()
    # Take input from players
    pos = int(input("Enter position (1-9): ")) - 1
    player = "X" if turn % 2 == 0 else "O"
    # Check if position is empty
    if board[pos] == " ":
        board[pos] = player
    else:
        print("Position already taken!")
        continue
    # Check winning combinations
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    if any(board[a] == board[b] == board[c] == player for a,b,c in wins):
        show()
        print(player, "wins!")
        break
else:
    show()
    print("It's a draw!")
'''
17. What is wins in the program?
It is a list of tuples containing all 8 possible winning combinations.

18. How many winning combinations are possible?

There are 8:
3 horizontal
3 vertical
2 diagonal

19. What is a tuple in Python?
A tuple is an ordered collection of elements that cannot be changed after creation.

20. What is the use of any()?
It returns True if at least one condition in an iterable is True.

21. Explain this statement:
python
board[a] == board[b] == board[c] == player
It checks whether all three positions contain the current player's symbol.

22. What happens when a player wins?
The board is displayed, the winner is printed, and break stops the loop.

23. What is the use of else after the for loop?
It executes when the loop finishes normally without encountering a break.

24. When does a draw occur?
When all 9 positions are filled and neither player wins.

Important Python concepts used
Concept-Purpose
List-Stores the board
Function-Displays the board
For loop-Controls turns
If-else-Selects the player
Tuple-Stores winning positions
Slicing-Displays board rows
any()-Checks winning condition
break-Stops the game
continue-Skips an invalid occupied position

Most important tricky viva questions
25. Why do we use 9 in range(9)?
Because the board has 9 positions.

26. Can we use a while loop instead of a for loop?
Yes, both can be used.

27. What happens if both players do not win after 9 moves?
The game ends in a draw.

28. Why does Player X start first?
Because turn starts from 0, and 0 is an even number.

29. What is the difference between break and continue?
break terminates the loop.
continue skips the current iteration.

30. What is the limitation of this program?
It does not validate non-numeric input or out-of-range positions before accessing the board.

    
'''
