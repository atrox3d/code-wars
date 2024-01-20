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
        

def search_ship(_map):
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)
    ROWS = len(_map)
    COLS = len(_map[0])

    visited_matrix = [[False for c in range(COLS)] for r in range(ROWS)]
    visited = []
    
    for y, row in enumerate(_map):
        for x, col in enumerate(row):
            for coord in get_valid_directions(_map, y, x):
                newy, newx = coord
                if not is_visited(visited_matrix, visited, coord):
                    visited_matrix[newy][newx] = True
                    visited.append(coord)
                    
                    if _map[newy][newx] == '#':
                        print(f'found # @{coord}')
                        print('checking ship...')
                        

def main():
    print(f'{os.getcwd() = }')
    map_file = os.path.join(os.path.dirname(__file__), 'map.txt')
    map = matrix.load(map_file, split=None)
    matrix.display(matrix.format_border(map))

    search_ship(map)

if __name__ == '__main__':
    sys.exit(main())
