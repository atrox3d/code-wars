import sys
import os

try:
    from matrix import matrix
except:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from matrix import matrix

def check_direction(_map, y, x, direction):
    ROWS = len(_map)
    COLS = len(_map[0])
    newy, newx = tuple(map(lambda a, b: a+b, (y, x), direction))

    if 0 <= newy < ROWS and 0 <= newx < COLS:
        return newy, newx
    return None

def is_visited(visited_matrix, visited, coord):
    newy, newx = coord
    if visited_matrix[newy][newx]:
        if not coord in visited:
            print(f'{visited_matrix[newy][newx] = }')
            print(f'{visited = }')
            raise ValueError(f'visited discrepancy {coord}')
        return True
    else:
        return False
    

def get_valid_directions(_map, y, x):
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)

    directions = []
    for direction in LEFT, UP, RIGHT, DOWN:
        if (coord := check_direction(_map, y, x, direction)) is None:
            continue
        directions.append(coord)
    return directions
        

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

def search_ship(_map):
    ROWS = len(_map)
    COLS = len(_map[0])

    visited_matrix = [[False for c in range(COLS)] for r in range(ROWS)]
    visited = []
    
    ships = []
    for y, row in enumerate(_map):
        for x, col in enumerate(row):
            if col == '#':
                print(f'found "#" @{y, x}: ', end='')
                if is_visited(visited_matrix, visited, (y, x)):
                    print('VISITED')
                    continue
                print('CHECKING')
                ship = [(y, x)]
                for coord in get_valid_directions(_map, y, x):
                    newy, newx = coord
                    if _map[newy][newx] == '#':
                        print(f'    found adjacent "#" @{coord}: ', end='')
                        if is_visited(visited_matrix, visited, coord):
                            print('VISITED')
                            continue
                        try:
                            check_ship(_map, coord)
                            print('OK')
                            ship.append(coord)
                        except ValueError as ve:
                            print('invalid')
                            sys.exit()
                    visited_matrix[newy][newx] = True
                    visited.append(coord)
                if ship:
                    ships.append(ship)
    return ships


def main():
    print(f'{os.getcwd() = }')
    map_file = os.path.join(os.path.dirname(__file__), 'map.txt')
    map = matrix.load(map_file, split=None)
    matrix.display(matrix.format_border(matrix.add_coordinates(map)))

    ships = search_ship(map)
    for ship in ships:
        print(ship)

if __name__ == '__main__':
    sys.exit(main())
