

class Board:
    def __init__(self, width, height, grid_size, space):
        """
        Initialize the Board object.

        Parameters:
        - width (int): Width of the board window
        - height (int): Height of the board window
        """
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.space = space
        self.cell_size = (width - self.space) // (self.grid_size - 1)
        self.board = [
            ['' for _ in range(self.grid_size)]
            for _ in range(self.grid_size)
            ]
        self.stones = []

    def get_cell(self, i, j):
        """
        Get the value of the cell at position (i, j).
        """
        if 0 <= i < len(self.board) and 0 <= j < len(self.board[i]):
            return self.board[i][j]
        else:
            return None

    def set_cell(self, i, j, value):
        self.board[i][j] = value

    def display(self):
        """
        Draw the Gomoku board on the screen.
        """
        strokeWeight(4)

        # Draw vertical lines
        for i in range(self.grid_size):
            line(
                self.space + i * self.cell_size,
                self.space,
                self.space + i * self.cell_size,
                self.space + (self.grid_size - 1) * self.cell_size
            )
        # Draw horizontal lines
        for j in range(self.grid_size):
            line(
                self.space,
                self.space + j * self.cell_size,
                self.space + (self.grid_size - 1) * self.cell_size,
                self.space + j * self.cell_size
            )

        # Display stones on the board
        for stone in self.stones:
            # print(self.stones)
            stone.display(self.cell_size)
