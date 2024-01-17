# maze = []
# maze.append([1, 0, 0, 0, 0, 1, 1, 0, 0, 0])
# maze.append([1, 0, 1, 0, 0, 0, 0, 0, 1, 0])
# maze.append([1, 0, 1, 0, 1, 1, 1, 0, 1, 0])
# maze.append([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# maze.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 0])
# maze.append([0, 0, 0, 0, 1, 1, 1, 0, 0, 0])
# maze.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 0])
# maze.append([0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
# maze.append([0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
# maze.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

def load_maze(filename='maze.txt'):
    from pathlib import Path
    
    filepath = Path(__file__).parent / filename
    with open(filepath) as file:
        maze = [line.rstrip().split() for line in file]
    return maze

def convert_maze_to_type(maze, convert_type):
    return [list(map(convert_type, row)) for row in maze]

def replace_maze_items(maze, charmap):
    return [[charmap.get(c, c) for c in row] for row in maze]

def print_maze(maze: list[list]):
    for row in maze:    
        print(row)

def bfs(maze, path=""):
    for x, pos in enumerate(maze[0]):
        print(f'{x, pos = }')
        if pos == 'O':
            start = x
            break
    else:
        raise ValueError('coulf not find "O" in the first row')

maze = load_maze()
maze = convert_maze_to_type(maze, convert_type=int)
maze = replace_maze_items(maze, {1: 'X', 0: ' '})
print_maze(maze)
# print_maze(maze)