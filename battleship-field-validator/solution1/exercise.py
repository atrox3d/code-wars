'''
Write a method that takes a field for well-known board game "Battleship" as 
an argument and returns true if it has a valid disposition of ships, 
false otherwise. Argument is guaranteed to be 10*10 two-dimension array. 
Elements in the array are numbers, 0 if the cell is free and 1 if occupied 
by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for 
two players. Each player has a 10x10 grid containing several "ships" 
and objective is to destroy enemy's forces by targetting individual cells 
on his field. The ship occupies one or more cells in the grid. 
Size and number of ships may differ from version to version. 
In this kata we will use Soviet/Russian version of the game.

Before the game begins, players set up the board and place the ships 
accordingly to the following rules:
There must be single battleship (size of 4 cells), 2 cruisers (size 3), 
3 destroyers (size 2) and 4 submarines (size 1). 
Any additional ships are not allowed, as well as missing ships.
Each ship must be a straight line, except for submarines, 
which are just single cell.

The ship cannot overlap or be in contact with any other ship, 
neither by edge nor by corner.

This is all you need to solve this kata. 
If you're interested in more information about the game, visit this link.
'''
import logging

from v3 import (
    check_overlapping_ships_and_normalize,
    count_ships,
    find_ships
)

logging.basicConfig(format=logging.BASIC_FORMAT, level='DEBUG')
logger = logging.getLogger(__name__)

def matrix_formatter(matrix):
    return '\n' + '\n'.join(map(str, [row for row in matrix]))


def print_ships(ships, prefix=''):
    for ship in ships:
        print(f'{prefix}{ship = }')
    print()

def validate_battlefield(field):
    hships, vships = find_ships(field)
    print_ships(hships, 'hship')
    print_ships(vships, 'vship')

    check_overlapping_ships_and_normalize(hships, vships)

    print_ships(hships, 'hship')
    print_ships(vships, 'vship')

    all_ships = hships + vships
    print_ships(all_ships, 'all')

    ship_count = count_ships(all_ships)
    print(f'{ship_count = }')
    # print(matrix_formatter(field))
    
    REQUIRED_SHIPS = {1: 4, 2: 3, 3: 2, 4: 1}
    if ship_count != REQUIRED_SHIPS:
        return False

    return True


def main():
    import sys
    sys.path.insert(0, '.')
    from runner import run
    
    battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                   [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                   [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    tests = [
        (battleField, True)
    ]
    for input, expected in tests:
        result = run(validate_battlefield, input, param_formatter=matrix_formatter)
        try:
            assert result == expected, f'{result} != {expected}'
        except AssertionError as ae:
            print(repr(ae))

if __name__ == '__main__':
    main()