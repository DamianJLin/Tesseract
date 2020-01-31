import board_src
import shapes
import parse_args
import numpy as np


def take_turn(player_id, game_board: board_src.Board):
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
                if game_board.tile_at_position(parsed).value == 0:
                    game_board.tile_at_position(parsed).value = player_id
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
                'pass                       Take no action.',
                'quit                       Quit the game.']
            for string in help_strings:
                print(string)

        elif player_input[0] == 'quit':
            if input('Quit the game? [Y/N]: ').lower() == 'y':
                exit(0)
            else:
                continue

        elif player_input[0] == 'pass':
            break

        else:
            print('{} is not a command. Type \'help\' to see a list of commands.'.format(player_input[0]))
            continue


def check_win(game_board: board_src.Board, player):
    """
    Returns true if player has a winning position on game_board.
    """

    # Checks the win condition on a single base_tile.
    def check_win_at_tile(base_tile: board_src.Tile):

        def check_win_with_orientation(orientation):

            checks = [np.asarray(base_tile.pos) + vec for vec in orientation]

            if all(game_board.value_at_position(pos.tolist()) == player for pos in checks):
                return True
            else:
                return False

        if any(check_win_with_orientation(ori) for ori in shapes.get_orientations(shapes.adj_4)):
            return True
        else:
            return False

    if any(check_win_at_tile(tl) for tl in game_board.board):
        return True
    else:
        return False


def underline_print(message):
    print(message)
    print('=' * len(message))
