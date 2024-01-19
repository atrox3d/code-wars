import matrix as mx

def _bfs(maze, path=""):
    for x, pos in enumerate(maze[0]):
        print(f'{x, pos = }')
        if pos == 'O':
            start = x
            break
    else:
        raise ValueError('coulf not find "O" in the first row')

def find_maze_start(maze, start_char='S'):
    R, C = len(maze), len(maze[0])

    start = (0, 0)
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'S':
                start = (r, c)
                break
        else: 
            continue    # no break detected, ignore parent break
        break           # parent break
    else:
        return None     # never found S, never break loop
    return start

class ExitNotFoundException(Exception):
    pass

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

def print_status(maze, visited, coord, queue):
        mx.display(format_maze(maze, visited))
        print(f'{coord = }')
        print(f'{queue = }')
        input()

def valid_direction(new_row, new_col, maze, visited, obstacle_char) -> bool:
    R, C = len(maze), len(maze[0])
    return (
            new_row >= 0 and new_row < R 
            and new_col >= 0 and new_col < C
            and maze[new_row][new_col] != obstacle_char
            and not visited[new_row][new_col]
    )

def solve_maze(maze, exit_char='E', obstacle_char='#'):
    from collections import deque
    
    R, C = len(maze), len(maze[0])
    LEFT, RIGHT, UP, DOWN = (0, -1), (0, 1), (-1, 0), (1, 0)
    DIRECTIONS = (RIGHT, LEFT, DOWN, UP)
   
    visited = [[False] * C for _ in range(R)]
    start = find_maze_start(maze)
    queue = deque()
    queue.append((*start, 0))   # 0 = distance

    while len(queue) != 0:
        coord = queue.pop() # value from the right
        row, col, dist = coord
        visited[row][col] = True
        print_status(maze, visited, coord, queue)
        
        if maze[row][col] == exit_char:
            return dist
        
        for dir_row, dir_col in DIRECTIONS:
            new_row, new_col = row + dir_row, col + dir_col
            if not valid_direction(new_row, new_col, maze, visited, obstacle_char):
                continue
            else:
                queue.appendleft((new_row, new_col, dist+1))
                print(f'{queue = }')
    raise ExitNotFoundException(f'could not find exit')

def main():
    matrix = mx.load(filename='maze.txt', split=None)
    bordered_matrix = mx.format_border(matrix, ' ')
    mx.display(bordered_matrix)

    print(solve_maze(matrix))

if __name__ == '__main__':
    main()
