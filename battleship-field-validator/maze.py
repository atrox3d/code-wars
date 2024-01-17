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

def read_maze(filename='maze.txt', convert_type=None):
    from pathlib import Path
    
    filepath = Path(__file__).parent / filename
    with open(filepath) as file:
        maze = [line.rstrip().split() for line in file]
        if convert_type:
            print(f'{type = }')
            maze = [list(map(convert_type, line)) for line in maze]
    return maze

def print_maze(maze: list[list], charmap=None, join=None):
    row : list
    for row in maze:
        if charmap:
            row = [charmap.get(c, c) for c in row]
        if join:
            row = join.join(map(str, row))
        print(row)

def _print_maze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        print(f'{x, pos = }')
        if pos == 'O':
            start = x
            break
    else:
        raise ValueError('coulf not find "O" in the first row')

maze = read_maze(convert_type=int)
print_maze(maze, join=' ', charmap={1: 'X', 0: ' '})
# print_maze(maze)