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
    top = bottom = f'+{"-".join("-" for _ in matrix[0])}+'
    rows = [f'|{join.join(map(str, row))}|' for row in matrix]
    return [top] + rows + [bottom]

def format_matrix_grid(matrix: list[list], join: str='|') -> list[str]:
    top = middle = f'+{"+".join("-" for _ in matrix[0])}+'
    rows = [top]
    for row in matrix:
        rows.append(f'{join}{join.join(map(str, row))}{join}')
        rows.append(middle)
    return rows

def print_matrix(matrix: list[list]):
    for row in matrix:    
        print(row)

def main():
    matrix = load_matrix()
    matrix = convert_matrix_to_type(matrix, convert_type=int)
    matrix = replace_matrix_items(matrix, {1: '#', 0: ' '})

    joined_matrix = format_matrix_join(matrix, ' ')
    bordered_matrix = format_matrix_border(matrix, ' ')
    grid_matrix = format_matrix_grid(matrix)

    print_matrix(bordered_matrix)

if __name__ == '__main__':
    main()
