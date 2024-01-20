def load(filename: str, split: str = ' ') -> list[list[str]]:
    from pathlib import Path
    import os
    
    # filepath = Path(__file__).parent / filename
    # print(f'{os.getcwd() = }')
    with open(filename) as file:
        if split:
            matrix = [line.rstrip('\n').split(split) for line in file]
        else:
            matrix = [list(line.rstrip('\n')) for line in file]
    return matrix

def convert_to_type(matrix: list[list[str]], convert_type) -> list[list]:
    return [list(map(convert_type, row)) for row in matrix]

def replace_items(matrix: list[list], charmap: dict) -> list[list]:
    return [[charmap.get(c, c) for c in row] for row in matrix]

def format_join(matrix: list[list], join: str, coords=True) -> list[str]:
    if coords:
        horizontal = join.join([str(x)[-1] for x in range(len(matrix[0]))])
        lines = [horizontal]
        for y, row in enumerate(matrix):
            lines.append( str(y)[-1] + join.join(map(str, [c for c in row])))
        return lines
    else:
        return [join.join(map(str, row)) for row in matrix]

def format_border(matrix: list[list], join: str = ' ') -> list[str]:
    top = bottom = f'+{"-".join("-" for _ in matrix[0])}+'
    rows = [f'|{join.join(map(str, row))}|' for row in matrix]
    return [top] + rows + [bottom]

def format_grid(matrix: list[list], join: str='|') -> list[str]:
    top = middle = f'+{"+".join("-" for _ in matrix[0])}+'
    rows = [top]
    for row in matrix:
        rows.append(f'{join}{join.join(map(str, row))}{join}')
        rows.append(middle)
    return rows

def display(matrix: list[list]):
    for row in matrix:    
        print(row)

def main():
    import os
    matrix = load(os.path.join(os.path.dirname(__file__), 'matrix.txt'))
    matrix = convert_to_type(matrix, convert_type=int)
    matrix = replace_items(matrix, {1: '#', 0: ' '})

    joined_matrix = format_join(matrix, ' ')
    bordered_matrix = format_border(matrix, ' ')
    grid_matrix = format_grid(matrix)

    display(bordered_matrix)

if __name__ == '__main__':
    main()
