def load_matrix(filename: str = 'matrix.txt', split: str = ' ') -> list[list[str]]:
    from pathlib import Path
    
    filepath = Path(__file__).parent / filename
    with open(filepath) as file:
        matrix = [line.rstrip().split(split) for line in file]
    return matrix

def convert_matrix_to_type(matrix: list[list[str]], convert_type) -> list[list]:
    return [list(map(convert_type, row)) for row in matrix]

def replace_matrix_items(matrix: list[list], charmap: dict) -> list[list]:
    return [[charmap.get(c, c) for c in row] for row in matrix]

def format_matrix_join(matrix: list[list], join: str) -> list[str]:
    return [join.join(map(str, row)) for row in matrix]

def format_matrix_border(matrix: list[list], join: str = ' ') -> list[str]:
    width = len(matrix[0])
    top = bottom = f'+{"-".join("-" for _ in matrix[0])}+'
    rows = [f'|{join.join(map(str, row))}|' for row in matrix]
    return [top] + rows + [bottom]

def format_matrix_grid(matrix: list[list], join: str='|', spacing: int=0) -> list[str]:
    width = len(matrix[0])
    top = middle = f'+{"+".join("-" for _ in matrix[0])}+'
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
# maze = format_matrix_join(maze, ' ')
# maze = format_matrix_border(maze, ' ')
maze = format_matrix_grid(maze)

print_matrix(maze)
# print_maze(maze)