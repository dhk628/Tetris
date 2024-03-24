# Tetris
I am trying to recreate the classic Tetris game using the <a href="https://pypi.org/project/pygame/">pygame</a> package in Python.
The goal of this project is to essentially re-familiarize myself with Python and Git.


### Progress

| Task                                              | Status      |
|---------------------------------------------------|-------------|
| [Creating the game grid](#creating-the-game-grid) | Done        |
| Creating the tetrominoes                          | Done        |
| Moving the tetrominoes with keyboard inputs       | Done        |
| Rotating the tetrominoes with keyboard inputs     | --          |
| Determining when the tetrominoes hit the bottom   | In progress |
| Determining collision rules                       | In progress |
| Dropping the tetrominoes automatically            | Done        |
| Clearing filled lines                             | --          |

## Creating the game grid
Tetris is played on a grid with 20 rows and 10 columns. I defined variables for box sizes
and gridline widths to draw the grid using pygame. I am also storing the grid as a 2D array,
where the (j,i)-th entry of the array corresponds to the element on the i-th row and j-th column.
Furthermore, the (j.i)-th entry will be 0 if the corresponding block is empty, and it will contain
the color of the block otherwise.