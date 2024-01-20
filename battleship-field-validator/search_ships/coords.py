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
