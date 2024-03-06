from stone import Stone


class Player:
    def __init__(self, board, color):
        """
        Initialize a Player object.
        """
        self.board = board
        self.color = color

    def make_move(self, i, j):
        """
        Make a move on the board.
        """
        if self.board.get_cell(i, j) == "":
            self.board.set_cell(i, j, self.color)
            self.board.stones.append(Stone(i, j, self.color))
            return True
        return False
