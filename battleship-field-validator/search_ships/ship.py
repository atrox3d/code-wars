import coords

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
            for coord in coords.get_valid_coords(_map, y, x, visited):
                newy, newx = coord
                if _map[newy][newx] == '#':
                    check_ship(_map, coord)
                visited.append(coord)
