from src import *


def take_turn(player_id):
    underline_print('Player {}\'s Turn'.format(player_id))

    while True:
        player_input = input().lower().split(' ')

        if player_input[0] == 'place':
            break

        elif player_input[0] == 'gravity':
            break

        elif player_input[0] == 'help':
            help_strings = [
                'place <x> <y> <z> <w>      Place a token at the coordinates (x, y, z, w).',
                'gravity <direction>        Change the gravity to the direction.',
                'help                       Show list of available commands.',
                'quit                       Quit the game.']
            for string in help_strings:
                print(string)

        elif player_input[0] == 'quit':
            if input('Quit the game? [Y/N]').lower() == 'y':
                exit(0)
            else:
                pass

        else:
            print('{} is not a command. Type \'help\' to see a list of commands.'.format(player_input[0]))


board = Board(size=5, dim=4)

players = [1, 2]
i = 0
while True:
    take_turn(players[i % 2])
    i += 1
