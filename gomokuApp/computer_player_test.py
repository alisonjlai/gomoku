from board import Board
from computer_player import ComputerPlayer


def test_constructor():
    board = Board(200, 200, 3, 50)
    computer_player = ComputerPlayer(board, "black", "white")
    assert computer_player.board == board
    assert computer_player.player_color == "black"
    assert computer_player.computer_color == "white"


def test_pick_next_move():
    board = Board(200, 200, 3, 50)
    computer_player = ComputerPlayer(board, "black", "white")
    empty_cells = [(0, 0), (0, 1), (1, 0)]
    move = computer_player.pick_next_move(empty_cells)
    assert move in empty_cells


def test_evaluate_move():
    board = Board(200, 200, 3, 50)
    computer_player = ComputerPlayer(board, "black", "white")
    i, j = 1, 1
    score = computer_player.evaluate_move(i, j)
    assert isinstance(score, (int, float))


def test_evaluate_pattern():
    board = Board(200, 200, 3, 50)
    computer_player = ComputerPlayer(board, "black", "white")
    i, j = 1, 1
    color = "black"
    pattern_score = computer_player.evaluate_pattern(i, j, color)
    assert isinstance(pattern_score, int)


def test_check_pattern():
    board = Board(200, 200, 3, 50)
    computer_player = ComputerPlayer(board, "black", "white")
    i, j = 1, 1
    color = "black"
    count = computer_player.check_pattern(i, j, color, 1, 0)
    assert isinstance(count, int)


def test_evaluate_threats():
    board = Board(200, 200, 3, 50)
    computer_player = ComputerPlayer(board, "black", "white")
    i, j = 1, 1
    color = "black"
    threat_score = computer_player.evaluate_threats(i, j, color)
    assert isinstance(threat_score, int)


def test_check_winning_move():
    board = Board(200, 200, 3, 50)
    computer_player = ComputerPlayer(board, "black", "white")
    i, j = 1, 1
    color = "black"
    winning_move = computer_player.check_winning_move(i, j, color)
    assert isinstance(winning_move, bool)


def test_evaluate_defense():
    board = Board(200, 200, 3, 50)
    computer_player = ComputerPlayer(board, "black", "white")
    i, j = 1, 1
    defense_score = computer_player.evaluate_defense(i, j, "white")
    assert isinstance(defense_score, int)


def test_place_stone():
    board = Board(200, 200, 3, 50)
    computer_player = ComputerPlayer(board, "black", "white")
    i, j = 1, 1
    computer_player.place_stone(i, j)
    assert board.get_cell(i, j) == "white"