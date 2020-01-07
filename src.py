import parse_args
from operator import add
import board_src


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


def check_win(game_board: board_src.Board, win_shape):
    """
    Returns a list of the player_id's with the most win_shapes achieved on the board.

    Does not check rotations or reflections of win_shape, only transformations.
    """

    # Checks the win condition on a single base_tile.
    def check_win_condition_at_tile(base_tile: board_src.Tile):

        # Builds a list of positions that need to be checked around base_tile.pos.
        tile_checks = [list(map(add, base_tile.pos, vec)) for vec in win_shape]

        # If all tiles in the shape have the same value as the base, and that value isn't a 0...
        if all(game_board.value_at_position(base_tile.pos) == game_board.value_at_position(tl) for tl in tile_checks)\
                and game_board.value_at_position(base_tile.pos) != 0:
            # Return the value of the base tile.
            return game_board.value_at_position(base_tile.pos)
        else:
            return None

    # Dictionary to store results
    results = {}

    # Check all tiles in board
    for tile in game_board.board:

        result = check_win_condition_at_tile(tile)

        if result is not None:
            # Increment the value at the result key in the dictionary, else create the key
            if result in results.keys():
                results[result] += 1
            else:
                results[result] = 1

    max_result = None
    try:
        max_result = max(results.values())
    except ValueError:
        pass

    most_results = [player for player in results.keys() if results.get(player) == max_result]

    if len(most_results) == 1:
        underline_print('Player {} wins by achieving a tesseract!'.format(most_results[0]))
        return True

    if len(most_results) > 1:
        print('Players {} all achieved the same number of tesseracts!'.format(tuple(most_results)))
        return False

    if len(most_results) < 1:
        return False


def underline_print(message):
    print(message)
    print('=' * len(message))
