from player import Player
from board import Board


def test_constructor():
    board = Board(200, 300, 3, 50)
    pl = Player(board, "white")
    assert pl.board == board
    assert pl.color == "white"

    board2 = Board(200, 300, 3, 50)
    pl = Player(board2, "black")
    assert pl.board == board2
    assert pl.color == "black"


def test_make_move():
    board = Board(200, 300, 3, 50)
    pl = Player(board, "black")
    i, j = 1, 2
    pl.board.get_cell = lambda x, y: ""
    result = pl.make_move(i, j)
    assert result is True
    assert pl.board.get_cell(i, j) == ""
