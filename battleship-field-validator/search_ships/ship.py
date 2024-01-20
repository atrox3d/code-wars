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


def find_ships(maze):
    from collections import deque
    import sys, os
    try:
        from matrix import matrix as mx
    except:
        sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
        from matrix import matrix

    def print_status(maze, visited, coord, queue):
            mx.display(format_maze(maze, visited))
            print(f'{coord = }')
            print(f'{queue = }')
            input()

    def format_maze(maze, visited, visited_char='.', start_char='S'):
        R, C = len(maze), len(maze[0])
        top = bottom = f'+{"-".join("-" for _ in maze[0])}+'
        updated_maze = [
                [visited_char if visited[row][col] and maze[row][col] != start_char 
                else maze[row][col] for col in range(C)] 
            for row in range(R)
        ]
        rows = [f'|{" ".join(map(str, row))}|' for row in updated_maze]
        return [top] + rows + [bottom]

    def valid_direction(new_row, new_col, maze, visited, obstacle_char) -> bool:
        R, C = len(maze), len(maze[0])
        return (
                new_row >= 0 and new_row < R 
                and new_col >= 0 and new_col < C
                and maze[new_row][new_col] != obstacle_char
                and not visited[new_row][new_col]
        )

    R, C = len(maze), len(maze[0])
    LEFT, RIGHT, UP, DOWN = (0, -1), (0, 1), (-1, 0), (1, 0)
    DIRECTIONS = (RIGHT, LEFT, DOWN, UP)
   
    visited = [[False] * C for _ in range(R)]
    start = (0, 0)
    queue = deque()
    queue.append((*start, 0))   # 0 = distance

    ships = []
    ship = []
    while len(queue) != 0:
        coord = queue.pop() # value from the right
        row, col, dist = coord
        visited[row][col] = True
        print_status(maze, visited, coord, queue)
        
        if maze[row][col] == '#':
            ship.append(coord)
        
        for dir_row, dir_col in DIRECTIONS:
            new_row, new_col = row + dir_row, col + dir_col
            if not valid_direction(new_row, new_col, maze, visited, '#'):
                continue
            else:
                queue.appendleft((new_row, new_col, dist+1))
                print(f'{queue = }')
    raise Exception(f'could not find exit')
