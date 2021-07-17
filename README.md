# TIC TAC TOE

Tic Tac Toe is dual player game played out on a 3X3 grid where players take alternate turns and place their symbol onto the grid in order to win.
In order to win, either of the below patterns have to be formed, else the game turns to be a draw.
- Any of the rows has the same symbol
- Any of the columns has the same symbol
- Any of the diagonals has the same symbol

```
+---+---+---+---+    +---+---+---+---+    +---+---+---+---+
|   | 0 | 1 | 2 |    |   | 0 | 1 | 2 |    |   | 0 | 1 | 2 |
+===+===+===+===+    +===+===+===+===+    +===+===+===+===+
| 0 | O | O | O |    | 0 | X | O | O |    | 0 | O | X | O |
+---+---+---+---+    +---+---+---+---+    +---+---+---+---+
| 1 | X | X |   |    | 1 |   | X |   |    | 1 |   | X |   |
+---+---+---+---+    +---+---+---+---+    +---+---+---+---+
| 2 | O | X | X |    | 2 | O | X | X |    | 2 | O | X | X |
+---+---+---+---+    +---+---+---+---+    +---+---+---+---+
```


Installation:

- Clone the repo and go to the source folder
- Download and install the necessary requirements 
    ```
    $ pip3 download -r requirements.txt
    $ pip3 install -r requirements.txt
    $ python3 src/game.py                       // to start the game
    ```

Rules for tic-tac-toe:

- Players take turns putting their marks in empty squares.
- The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
- When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

Following are few assumptions made while development:

- The board is of size (3X3).
- Player A starts the game.
- After making a move, player will not be allowed to undo the move.
- Player should be given the flexibility to choose his/her symbol.
- This is a dual player game 
- If the game comes to position where no player is winning and has no chances in that particular game, still the game has to be completed by filling all the boxes in order to "draw" the game.
- the player might enter a coordinate outside the grid, in that case a retry option is provided.
- Player might want to play another game, hence confirm once a game ends