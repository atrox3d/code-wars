import sys
import os

try:
    from matrix import matrix
except:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from matrix import matrix

def get_newcoord(_map, y, x, direction):
    ROWS = len(_map)
    COLS = len(_map[0])
    newy, newx = tuple(map(lambda a, b: a+b, (y, x), direction))

    if 0 <= newy < ROWS and 0 <= newx < COLS:
        return newy, newx
    return None

def get_valid_coords(_map, y, x, visited):
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)

    for direction in LEFT, UP, RIGHT, DOWN:
        if (coord := get_newcoord(_map, y, x, direction)) is None:
            continue
        if coord in visited:
            continue
        yield coord
        

def check_ship(_map, coord):
    y, x = coord
    NW = (y-1, x-1)
    N = (y-1, x)
    NE = (y-1, x+1)
    W = (y, x-1)
    E = (y, x+1)
    SW = (y+1, x-1)
    S = (y+1, x)
    SE = (y+1, x+1)

    for diagonal in NW, NE, SW, SE:
        dy, dx = diagonal
        if _map[dy][dx] == '#':
            raise ValueError(f'diagonal adjacency: {diagonal} - {coord}')
    
    for (y1, x1), (y2, x2) in (N, W), (N, E), (S, W), (S, E):
        if _map[y1][x1] == '#' and _map[y2][x2] == '#':
            raise ValueError(f'cross adjacency: {diagonal} - {coord}')
    return True

def check_ships(_map):
    ROWS = len(_map)
    COLS = len(_map[0])
    visited = []
    
    for y, row in enumerate(_map):
        for x, col in enumerate(row):
            current = (y, x)
            if col == '#' and current in visited:
                    continue
            for coord in get_valid_coords(_map, y, x, visited):
                newy, newx = coord
                if _map[newy][newx] == '#':
                    check_ship(_map, coord)
                visited.append(coord)


def main():
    print(f'{os.getcwd() = }')
    map_file = os.path.join(os.path.dirname(__file__), 'map.txt')
    map = matrix.load(map_file, split=None)
    matrix.display(matrix.format_border(matrix.add_coordinates(map)))

    try:
        check_ships(map)
    except ValueError as ae:
        print(repr(ae))
        sys.exit()

if __name__ == '__main__':
    sys.exit(main())
