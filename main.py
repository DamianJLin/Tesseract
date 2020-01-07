from src import *
import parse_args


def take_turn(player_id):

    underline_print('Player {}\'s Turn'.format(player_id))

    while True:
        player_input = input().lower().rstrip(' ').split(' ')

        if player_input[0] == 'place':

            parsed = parse_args.place_parse(player_input[1:])

            if parsed is None:
                continue
            else:
                # Check returned value is indeed a list of four ints.
                assert isinstance(parsed, list)
                assert len(parsed) == 4
                assert all(isinstance(parsed[j], int) for j in range(len(parsed)))

                # If returned value is a legal move, play it.
                if board.tile_at_position(parsed).value == 0:
                    board.tile_at_position(parsed).value = player_id
                    break
                else:
                    print('That position has already been played.')
                    continue

        elif player_input[0] == 'gravity':
            print('Feature is not yet implemented.')

        elif player_input[0] == 'help':
            help_strings = [
                'place <x> <y> <z> <w>      Place a token at the coordinates (x, y, z, w).',
                'gravity <direction>        Change the gravity to the direction.',
                'help                       Show list of available commands.',
                'quit                       Quit the game.']
            for string in help_strings:
                print(string)

        elif player_input[0] == 'quit':
            if input('Quit the game? [Y/N]: ').lower() == 'y':
                exit(0)
            else:
                continue

        else:
            print('{} is not a command. Type \'help\' to see a list of commands.'.format(player_input[0]))
            continue


board = Board(size=5, dim=4)

# Game uses these assertions.
assert board.size == 5
assert board.dim == 4

players = [1, 2]

board.plot()
i = 0
while True:
    take_turn(players[i % 2])
    board.plot()

    i += 1
