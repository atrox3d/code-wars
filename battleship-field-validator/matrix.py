def load_matrix(filename='matrix.txt', split=' '):
    from pathlib import Path
    
    filepath = Path(__file__).parent / filename
    with open(filepath) as file:
        matrix = [line.rstrip().split(split) for line in file]
    return matrix

def convert_matrix_to_type(matrix, convert_type):
    return [list(map(convert_type, row)) for row in matrix]

def replace_matrix_items(matrix, charmap):
    return [[charmap.get(c, c) for c in row] for row in matrix]

def format_matrix_join(matrix, join):
    return [join.join(map(str, row)) for row in matrix]

def format_matrix_border(matrix, join=' '):
    width = len(matrix[0])
    top = bottom = ['+' + '-' * (2*width-1) + '+']
    rows = [f'|{join.join(map(str, row))}|' for row in matrix]
    return top + rows + bottom

def format_matrix_grid(matrix, join='|'):
    width = len(matrix[0])
    top = bottom = middle = '+' + '-+' * width
    rows = [top]
    for row in matrix:
        rows.append(f'{join}{join.join(map(str, row))}{join}')
        rows.append(middle)
    return rows

def print_matrix(matrix: list[list]):
    for row in matrix:    
        print(row)

def bfs(maze, path=""):
    for x, pos in enumerate(maze[0]):
        print(f'{x, pos = }')
        if pos == 'O':
            start = x
            break
    else:
        raise ValueError('coulf not find "O" in the first row')

maze = load_matrix()
maze = convert_matrix_to_type(maze, convert_type=int)
maze = replace_matrix_items(maze, {1: '#', 0: ' '})
# maze = format_maze_join(maze, ' ')
maze = format_matrix_grid(maze)

print_matrix(maze)
# print_maze(maze)