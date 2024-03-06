
class GameManager:
    def __init__(self, board, space, player, computer_player):
        """
        Initialize the GameManager object.
        """
        self.board = board
        self.space = space
        self.player = player
        self.computer_player = computer_player
        self.is_player_turn = True
        self.game_over = False
        self.winner = None
        self.name_prompted = False

    def switch_turn(self):
        """
        Switch the turn between the human player and the computer player.
        """
        self.is_player_turn = not self.is_player_turn

    def make_move(self, x, y):
        if self.game_over:
            return

        i = (x - self.space) // self.board.cell_size
        if x > self.space + i * self.board.cell_size + self.board.cell_size//2:
            i += 1
        j = (y - self.space) // self.board.cell_size
        if y > self.space + j * self.board.cell_size + self.board.cell_size//2:
            j += 1
        # print("i: " + str(i))
        # print("j: " + str(j))

        if self.is_player_turn:
            if self.player.make_move(i, j):
                self.check_game_over()
                self.switch_turn()
        else:
            self.computer_player.make_move()
            self.check_game_over()
            self.switch_turn()

    def check_game_over(self):
        """
        Check if the game is over, either due to a filled board or a winner.
        """
        if self.is_board_filled():
            self.game_over = True

        elif self.check_winner('black'):
            self.game_over = True
            self.winner = 'black'

        elif self.check_winner('white'):
            self.game_over = True
            self.winner = 'white'

    def is_board_filled(self):
        for row in self.board.board:
            if '' in row:
                return False
        return True

    def check_winner(self, color):
        for stone in self.board.stones:
            if self.check_sequence(stone.x, stone.y, color):
                return True
        return False

    def check_sequence(self, i, j, color):
        # Right, Down, Diagonal Down-Right, Diagonal Down-Left
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for direction in directions:
            count = 0
            ni, nj = i, j  # Initialize ni and nj outside the loop
            for _ in range(5):  # Check exactly 5 consecutive stones in a row
                if (
                    0 <= ni < len(self.board.board) and
                    0 <= nj < len(self.board.board[i]) and
                    self.board.get_cell(ni, nj) == color
                ):
                    count += 1
                    # print(count)
                    # print(ni)
                    # print(nj)
                    # print(color)
                    ni = ni + direction[0]
                    nj = nj + direction[1]
                else:
                    break
            if count == 5:
                return True
        return False

    def prompt_for_name(self):
        """
        Prompt the user to enter their name after the game is over.
        Update and write scores to a file based on the winner's name.
        """
        if self.game_over and not self.name_prompted:
            self.name_prompted = True
            name = self.input('Enter your name:')

            if self.winner == 'black':
                winner_name = name
                # print('Hi ' + winner_name)
                scores = self.read_scores()
                self.update_scores(scores, winner_name)
                # Write the updated scores back to the file
                self.write_scores(scores)

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def read_scores(self):
        """
        Read scores from the file and return them as a dictionary
        """
        scores = {}
        try:
            with open('scores.txt', 'r') as file:
                for line in file:
                    winner, score = line.strip().split()
                    scores[winner] = int(score)
        except FileNotFoundError:
            scores = {}  # File doesn't exist yet, scores will be initialized

        return scores

    def update_scores(self, scores, winner):
        """
        Update scores based on the winner
        """
        if winner in scores:
            scores[winner] += 1
        else:
            scores[winner] = 1

    def write_scores(self, scores):
        """
        Write the scores back to the file, ranked from highest to lowest
        """
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        with open('scores.txt', 'w') as file:
            for name, score in sorted_scores:
                file.write(name + " " + str(score) + "\n")
