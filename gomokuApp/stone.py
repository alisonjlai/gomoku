WIDTH = 900
SPACE = 30
GRID_SIZE = 15
FRAME_DELAY = 60


class Stone:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.cell_size = (WIDTH - SPACE) // (GRID_SIZE - 1)
        self.frames_elapsed = 0

    def __repr__(self):
        return str(self.x, self.y, self.color)

    def display(self, cell_size):
        """
        Display the stone on the game board.
        """
        if self.color == "black":
            fill(0)
            ellipse(
                SPACE + self.x * self.cell_size,
                SPACE + self.y * self.cell_size,
                self.cell_size - 8,
                self.cell_size - 8
            )
        elif self.color == "white":
            if self.frames_elapsed >= FRAME_DELAY:
                fill(1)
                ellipse(
                    SPACE + self.x * self.cell_size,
                    SPACE + self.y * self.cell_size,
                    self.cell_size - 8,
                    self.cell_size - 8
                )
            else:
                # If not, increment the frame counter
                self.frames_elapsed += 1
