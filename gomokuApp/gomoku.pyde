from board import Board
from game_manager import GameManager
from player import Player
from computer_player import ComputerPlayer

WIDTH = 900
SPACE = 30
GRID_SIZE = 15

board = Board(WIDTH, WIDTH, GRID_SIZE, SPACE)
player = Player(board, 'black')
computer_player = ComputerPlayer(board, "black", "white")
game_manager = GameManager(board, SPACE, player, computer_player)

# Variable to store the time when the game over condition is met
game_over_time = 0

def setup():
    size(WIDTH + SPACE, WIDTH + SPACE)
    colorMode(RGB, 1)

def draw():
    global game_over_time
    
    background(0.85)
    board.display()

    if not game_manager.is_player_turn:
        game_manager.make_move(0, 0)  
    
    if game_manager.game_over:
        if game_over_time == 0:
            # Store the time when the game over condition is met
            game_over_time = millis()

        textSize(128)
        fill(0, 408, 612, 816)
        text("Game Over.", 150, 700)

        if game_manager.winner == "black":
            text("Black wins!", 160, 850)
            # Check if 1000 milliseconds (1 second) have passed
            if millis() - game_over_time > 1000:
                game_manager.prompt_for_name()
        elif game_manager.winner == "white":
            text("White wins!", 150, 850)
            if millis() - game_over_time > 1000:
                game_manager.prompt_for_name()
        elif game_manager.is_board_filled():
            text("It's a draw!", 130, 850)
            if millis() - game_over_time > 1000:
                game_manager.prompt_for_name()

        if game_manager.name_prompted:
            game_manager.prompt_for_name()

def mousePressed():
    game_manager.make_move(mouseX, mouseY)