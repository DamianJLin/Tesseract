from src import *
import board_src

board = board_src.Board(size=5, dim=4)

# Game uses these assertions.
assert board.size == 5
assert board.dim == 4

players = [1, 2]

board.plot()
i = 0
while True:
    take_turn(players[i % 2], game_board=board)
    board.plot()

    i += 1
