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
from v1 import find_ships, check_overlapping_ships

def validate_battlefield(field):
    # write your magic here
    hships = find_ships(field, 'h')
    vships = find_ships(field, 'v')
    return check_overlapping_ships(hships, vships)
    
def matrix_formatter(matrix):
    ret = '\n'
    for row in matrix:
        ret += str(row) + '\n'
    return ret

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