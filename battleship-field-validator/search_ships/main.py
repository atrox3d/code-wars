import sys
import os

try:
    from matrix import matrix
except:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from matrix import matrix
        
import ship

def main():
    print(f'{os.getcwd() = }')
    map_file = os.path.join(os.path.dirname(__file__), 'map.txt')
    map = matrix.load(map_file, split=None)
    matrix.display(matrix.format_border(matrix.add_coordinates(map)))

    try:
        ship.check_ships(map)
    except ValueError as ae:
        print(repr(ae))
        sys.exit()

if __name__ == '__main__':
    sys.exit(main())
