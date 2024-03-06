from game_manager import GameManager
from board import Board
from player import Player
from computer_player import ComputerPlayer
from stone import Stone


def test_constructor():
    board = Board(200, 200, 3, 50)
    me = Player(board, "black")
    you = ComputerPlayer(board, "black", "white")
    gm = GameManager(board, 20, me, you)
    assert gm.board == board
    assert gm.space == 20
    assert gm.player == me
    assert gm.computer_player == you
    assert gm.is_player_turn is True
    assert gm.game_over is False
    assert gm.winner is None
    assert gm.name_prompted is False


def test_switch_turn():
    board = Board(200, 200, 3, 50)
    me = Player(board, "black")
    you = ComputerPlayer(board, "black", "white")
    gm = GameManager(board, 20, me, you)
    gm.switch_turn()
    assert gm.is_player_turn is False


def test_make_move():
    board = Board(200, 200, 3, 50)
    me = Player(board, "black")
    you = ComputerPlayer(board, "black", "white")
    gm = GameManager(board, 20, me, you)

    # Test make_move for the player's turn
    gm.make_move(50, 50)  # Assume valid coordinates for testing
    assert gm.player.board.stones[-1].color == "black"
    assert gm.is_player_turn is False

    # Test make_move for the computer's turn
    gm.make_move(100, 100)  # Assume valid coordinates for testing
    assert gm.computer_player.board.stones[-1].color == "white"
    assert gm.is_player_turn is True


def test_check_game_over():
    board = Board(200, 200, 3, 50)
    me = Player(board, "black")
    you = ComputerPlayer(board, "black", "white")
    gm = GameManager(board, 20, me, you)

    # Test when the board is filled
    gm.board.board = [
        ['black', 'white', 'black'],
        ['white', 'black', 'white'],
        ['black', 'white', 'black']
        ]
    gm.check_game_over()
    assert gm.game_over is True
    assert gm.winner is None

    gm.board.stones = [
        Stone(0, 0, 'black'), Stone(0, 1, 'black'), Stone(0, 2, 'black'),
        Stone(0, 3, 'black'), Stone(0, 4, 'black')
        ]
    gm.check_game_over()
    assert gm.game_over is True


def test_is_board_filled():
    board = Board(200, 200, 3, 50)
    me = Player(board, "black")
    you = ComputerPlayer(board, "black", "white")
    gm = GameManager(board, 20, me, you)

    # Test when the board is not filled
    gm.board.board = [
        ['black', 'white', 'black'],
        ['white', '', 'white'],
        ['black', 'white', 'black']
        ]
    assert gm.is_board_filled() is False

    gm.board.board = [
        ['black', 'white', 'black'],
        ['white', 'black', 'white'],
        ['black', 'white', 'black']
        ]
    assert gm.is_board_filled() is True


def test_check_winner():
    board = Board(200, 200, 3, 50)
    me = Player(board, "black")
    you = ComputerPlayer(board, "black", "white")
    gm = GameManager(board, 20, me, you)

    gm.board.stones = [
        Stone(0, 0, 'black'),
        Stone(1, 1, 'white'),
        Stone(2, 2, 'black')
        ]
    assert gm.check_winner('black') is False


def test_check_sequence():
    board = Board(200, 200, 3, 50)
    me = Player(board, "black")
    you = ComputerPlayer(board, "black", "white")
    gm = GameManager(board, 20, me, you)

    # Test when there is no winning sequence
    gm.board.board = [
        ['black', 'white', 'black'],
        ['white', 'black', 'white'],
        ['black', 'white', 'black']
        ]
    assert gm.check_sequence(0, 0, 'black') is False
