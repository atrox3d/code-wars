maze = []
maze.append([1, 0, 0, 0, 0, 1, 1, 0, 0, 0])
maze.append([1, 0, 1, 0, 0, 0, 0, 0, 1, 0])
maze.append([1, 0, 1, 0, 1, 1, 1, 0, 1, 0])
maze.append([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
maze.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 0])
maze.append([0, 0, 0, 0, 1, 1, 1, 0, 0, 0])
maze.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 0])
maze.append([0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
maze.append([0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
maze.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

print(f'{maze[0] = }')

def print_maze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        print(f'{x, pos = }')

print_maze(maze)