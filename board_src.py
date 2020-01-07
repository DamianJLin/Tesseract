class Board:
    """
    A board of tiles with equal side-length.
    :size: Number of tiles along one edge of the board.
    :dim: Number of dimensions the board extends to.
    """
    def __init__(self, size, dim):

        self.size = size
        self.dim = dim

        class Tile:
            """
            A point on the board.
            :idx: Index of the point on the board.
            :pos: Coordinates of tbe point on the board.
            :value: Value of the point.
            """
            def __init__(self, idx):
                self.idx = idx
                self.pos = [(idx // pow(size, i)) % size for i in range(dim)]
                self.value = 0
        self.board = [Tile(i) for i in range(self.size ** self.dim)]

    def tile_at_index(self, index):
        """
        Returns the tile at the given index.
        """
        assert self.board[index].idx == index
        return self.board[index]

    def tile_at_position(self, position):
        """
        Returns the tile at the coordinates given by position.

        Should be used only where position is known to be valid.
        """
        # Assert tile position is valid.
        assert all(0 <= position[i] < self.size for i in range(len(position)))

        index = sum(position[i] * (self.size ** i) for i in range(self.dim))
        return self.board[index]

    def value_at_position(self, position):
        """
        Returns the value of the tile at position, else None if position is not on Board.

        Can be used where position is not known to be valid.
        :return: None if tile doesn't exist, else the value at the tile.
        """
        if not all(0 <= position[i] < self.size for i in range(len(position))):
            return None
        else:
            return self.tile_at_position(position)

    def plot(self):
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

        # Printing text at the top:

        print('Printing board...\n\n', end='')

        # Reversed so that w increases upwards.
        for d in range(self.size).__reversed__():

            # Prints a 3D space as a bunch of cross-sections.
            # Reversed so that y increases upwards.
            for b in range(self.size).__reversed__():

                for c in range(self.size):

                    for a in range(self.size):

                        # Print the character, and the gaps in x.
                        print(char_map[self.tile_at_position([a, b, c, d]).value] + '  ', end='')

                    # Print the gaps in z.
                    print('    ', end=' ')

                # Print the gaps in y.
                print('\n', end='')

            # Print the (z, w) coordinates at the bottom of each array.
            for c in range(self.size):
                # Sort out the spacing of these lines by making each (z, w) 20 chars long.
                print('({}, {}){}'.format(c, d, ' ' * (20 - len('({}, {})'.format(c, d)))), end='')

            # Print the gaps in w.
            print('\n\n', end='')