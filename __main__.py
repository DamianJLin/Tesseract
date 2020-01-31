from src import *
import board_src

board = board_src.Board(size=5, dim=4)

# Game uses these assertions.
assert board.size == 5
assert board.dim == 4

players = [1, 2]

board.plot()
turn = 0
while True:
    player_this_turn = players[turn % 2]

    take_turn(player_this_turn, game_board=board)
    board.plot()
    if check_win(game_board=board, player=player_this_turn):
        print('Player {} wins by connecting 4!'.format(player_this_turn))
        exit(0)

    turn += 1
