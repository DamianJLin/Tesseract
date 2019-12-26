import sys

board_size = 5


class Game:

    def __init__(self):

        # Initialise the empty 4D array
        self.board = []
        for i in range(board_size):
            self.board.append([])
            for j in range(board_size):
                self.board[i].append([])
                for k in range(board_size):
                    self.board[i][j].append([])
                    for l in range(board_size):
                        self.board[i][j][k].append(0)

        self.plot_game()

    def plot_game(self):
        """
        Prints a matrix of matrices to represent the 4D game board.

        Gaps in increasing {} are {} long:
        x   2 spaces
        y   1 line
        z   1 lines (+1 line from increasing gaps in y)
        w   5 spaces (+2 spaces from gaps in x)

        From one block to the next in increasing z, there are 20 spaces. (e.g. (0, 0, 0, 0) to (0, 0, 1, 0))
        From one block to the next in increasing w, there are 6 lines. (e.g. (0, 0, 0, 0) to (0, 0, 0, 1))
        """

        char_map = {0: '/', 1: '#', 2: '%'}

        # Reversed so that w increases upwards.
        for d in range(board_size).__reversed__():

            # Prints a 3D space as a bunch of cross-sections.
            # Reversed so that y increases upwards.
            for b in range(board_size).__reversed__():

                for c in range(board_size):

                    for a in range(board_size):

                        # Print the character, and the gaps in x.
                        print(char_map[self.board[a][b][c][d]] + '  ', end='')

                    # Print the gaps in z.
                    print('    ', end=' ')

                # Print the gaps in y.
                print('\n', end='')

            # Print the (z, w) coordinates at the bottom of each array.
            for c in range(board_size):
                # Sort out the spacing of these lines by making each (z, w) 20 chars long.
                print('({}, {}){}'.format(c, d, ' ' * (20 - len('({}, {})'.format(c, d)))), end='')

            # Print the gaps in w.
            print('\n\n', end='')


if __name__ == '__main__':
    game = Game()
