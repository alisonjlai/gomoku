from stone import Stone


class ComputerPlayer:
    def __init__(self, board, player_color, computer_color):
        """
        Initialize the ComputerPlayer object.

        Parameters:
        - board (Board): The game board
        - player_color (str): Color of the human player's stones
        - computer_color (str): Color of the computer player's stones
        """
        self.board = board
        self.player_color = player_color
        self.computer_color = computer_color

    def make_move(self):
        """
        Make a move by picking the best available option and placing a stone.
        """
        empty_cells = [
            (i, j)
            for i in range(len(self.board.board))
            for j in range(len(self.board.board[i]))
            if self.board.get_cell(i, j) == ""
        ]

        best_move = self.pick_next_move(empty_cells)
        self.place_stone(*best_move)

    def pick_next_move(self, empty_cells):
        """
        Pick the best move from the available empty cells.

        Parameters:
        - empty_cells (list): List of empty cell positions

        Returns:
        - tuple: Best move coordinates (i, j)
        """
        best_score = float('-inf')
        best_move = None

        for i, j in empty_cells:
            score = self.evaluate_move(i, j)
            if score > best_score:
                best_score = score
                best_move = (i, j)

        # print("Best move:", best_move, "with score:", best_score)
        return best_move

    def evaluate_move(self, i, j):
        """
        Heuristic evaluation function for a given move.
        """
        score = 0

        if self.check_winning_move(i, j, self.computer_color):
            return float('inf')

        if self.check_winning_move(i, j, self.player_color):
            return float('inf')

        # Evaluate the move based on patterns, threats, and defensive moves
        score += 10 * self.evaluate_pattern(i, j, self.player_color)
        score += 10 * self.evaluate_pattern(i, j, self.computer_color)
        score += 8 * self.evaluate_threats(i, j, self.player_color)
        score += 15 * self.evaluate_defense(i, j, self.computer_color)

        return score

    def evaluate_pattern(self, i, j, color):
        """
        Evaluate patterns (e.g., number of pieces in a row) for a given color.
        """
        pattern_score = 0

        pattern_score += self.check_pattern(i, j, color, 1, 0)  # Horizontal
        pattern_score += self.check_pattern(i, j, color, 0, 1)  # Vertical
        pattern_score += self.check_pattern(i, j, color, 1, 1)  # Diagonal /
        pattern_score += self.check_pattern(i, j, color, 1, -1)  # Diagonal \

        return pattern_score

    def check_pattern(self, i, j, color, x, y):
        """
        Check a specific pattern for a given color.
        """
        count = 0
        ni, nj = i, j
        if color == self.player_color:
            a = 3
        elif color == self.computer_color:
            a = 2
        for _ in range(a):
            if (
                0 <= ni < len(self.board.board) and
                0 <= nj < len(self.board.board[i])
            ):
                cell_value = self.board.get_cell(ni, nj)
                if cell_value == "":
                    count += 1
                    ni, nj = ni + x, nj + y
                    cell_value = self.board.get_cell(ni, nj)
                    if cell_value == color:
                        count += 1
                        ni, nj = ni + x, nj + y
                    else:
                        break
        return count

    def evaluate_threats(self, i, j, color):
        """
        Evaluate potential threats for a given color.
        """
        threat_score = 0

        # Check for potential winning moves
        if self.check_winning_move(i, j, color):
            threat_score += 20

        return threat_score

    def check_winning_move(self, i, j, color):
        """
        Check if placing a stone at (i, j) would result in a winning position
        """
        winning_patterns = [
            [(1, 0), (-1, 0)],  # Horizontal
            [(0, 1), (0, -1)],  # Vertical
            [(1, 1), (-1, -1)],  # Diagonal /
            [(1, -1), (-1, 1)]   # Diagonal \
        ]

        for directions in winning_patterns:
            count = 1  # Count the current stone

            for di, dj in directions:
                ni, nj = i + di, j + dj

                while (
                    0 <= ni < len(self.board.board) and
                    0 <= nj < len(self.board.board[i]) and
                    self.board.get_cell(ni, nj) == color
                ):
                    count += 1
                    ni, nj = ni + di, nj + dj

            if count >= 4:
                return True

        return False

    def evaluate_defense(self, i, j, color):
        """
        Evaluate defensive moves
        """
        defense_score = 0

        # Check for computer's potential winning moves
        if self.check_winning_move(i, j, self.computer_color):
            defense_score += 25

        return defense_score

    def place_stone(self, i, j):
        if (
            0 <= i < len(self.board.board) and
            0 <= j < len(self.board.board[i])
        ):
            self.board.set_cell(i, j, self.computer_color)
            self.board.stones.append(Stone(i, j, self.computer_color))
