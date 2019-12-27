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

        self.plot_board()

    def plot_board(self):
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

    @staticmethod
    def get_point(player):

        def get_point_input():
            """
            Gets input from player and returns a point as a list of integers, or an error code.
            :return: -1 if incorrect number of inputs
                     -2 if inputs are not convertible to integers
                     -3 if integers are outside of correct range
                     otherwise list of inputs as integers
            """

            # Checks for the correct number of comma delimited inputs
            coords_unparsed = input('Player {}\'s Turn. Enter your coordinates:'.format(player)).split(',')
            if len(coords_unparsed) != 4:
                return -1

            # Checks that inputs are integers
            try:
                coords_unparsed = [int(i) for i in coords_unparsed]
            except ValueError:
                return -2

            # Checks that integers are in the correct range
            if not all(0 <= i < board_size for i in coords_unparsed):
                return -3

            return coords_unparsed

        # Initialise point_input
        point_input = None

        # Keep trying inputs until player inputs correctly
        while not isinstance(point_input, list):
            point_input = get_point_input()
            # Handling error codes.
            if point_input == -1:
                print('Incorrect number of comma-delimited inputs. Try again.')
            if point_input == -2:
                print('Comma-delimited inputs need to be integers. Try again.')
            if point_input == -3:
                print('Integers need to be in the range [0, {}]. Try again.'.format(board_size - 1))

        assert isinstance(point_input, list)

        return point_input


if __name__ == '__main__':
    game = Game()
