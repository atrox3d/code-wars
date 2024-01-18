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

def solve_maze(maze, exit_char='E', obstacle_char='#'):
    from collections import deque
    R, C = len(maze), len(maze[0])

    start = find_maze_start(maze)
    queue = deque()
    queue.append((*start, 0))   # 0 = distance
    print(queue)

    left, right, up, down = (0, -1), (0, 1), (-1, 0), (1, 0)
    directions = (right, left, down, up)
    visited = [[False] * C for _ in range(R)]

    while len(queue) != 0:
        coord = queue.pop() # value from the right
        print(f'{coord, queue = }')
        row, col, dist = coord
        visited[row][col] = True

        if maze[row][col] == exit_char:
            return dist
        
        for dir_row, dir_col in directions:
            new_row, new_col = row + dir_row, col + dir_col
            if (
                new_row < 0 or new_row >= R 
                or new_col < 0 or new_col >= C
                or maze[new_row][new_col] == obstacle_char
                or visited[new_row][new_col]
            ):
                continue
            queue.appendleft((new_row, new_col, dist+1))
            print(queue)

def main():
    matrix = mx.load(filename='maze.txt', split=None)
    bordered_matrix = mx.format_border(matrix, ' ')
    mx.print_matrix(bordered_matrix)

    solve_maze(matrix)

if __name__ == '__main__':
    main()
