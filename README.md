# Tetris
I recreated the classic Tetris game using the <a href="https://pypi.org/project/pygame/">pygame</a> package in Python.
The goal of this project was to essentially re-familiarize myself with Python and Git.
The program requires main.py and shapes.py to run.


### Progress

| Task                                              | Status |
|---------------------------------------------------|--------|
| [Creating the game grid](#creating-the-game-grid) | Done   |
| Creating the tetrominoes                          | Done   |
| Moving the tetrominoes with keyboard inputs       | Done   |
| Rotating the tetrominoes with keyboard inputs     | Done   |
| Determining when the tetrominoes hit the bottom   | Done   |
| Determining collision rules                       | Done   |
| Dropping the tetrominoes automatically            | Done   |
| Clearing filled lines                             | Done   |
| Determining when game is over                     | Done   |
| Adding scores and levels                          | --     |
| Displaying next block                             | --     |

### Future fixes

- For determining when the game is over, the program creates a new tetromino at the center top position, and sees if it clashes with any pre-existing pieces. If there is a clash, the game ends. This does not look very satisfying when the pre-existing piece is at, for example, the second row: then the game ends without drawing anything in the first row. I would like to change this so that the program colors in whatever parts of the new tetromino can fit on the board.
- When a tetromino hits the bottom of the board, it immediately locks into place. I would like to add a delay before the tetromino is confirmed, so that players can move the tetromino sideways.
- Choosing the tetromino should be pseudo-random, to prevent too many of the same pieces appearing in a short amount of time.

## Creating the game grid
Tetris is played on a grid with 20 rows and 10 columns. I defined variables for box sizes
and gridline widths to draw the grid using pygame. I am also storing the grid as a 2D array,
where the (j,i)-th entry of the array corresponds to the element on the i-th row and j-th column.
Furthermore, the (j.i)-th entry will be 0 if the corresponding block is empty, and it will contain
the color of the block otherwise.