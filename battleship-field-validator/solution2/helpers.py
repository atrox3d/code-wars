import csv, os, time
from pathlib import Path

MAX_RECURSION_LEVEL = RECURSION_LEVEL = 0


def get_files(path, *wildcards):
    path = Path(path)
    path = path if path.is_dir() else path.parent
    return [file  for wildcard in [*wildcards] for file in Path(path).glob(wildcard)]

def load_file(file):
    loader = get_loader(file)
    return loader(file)

def get_loader(file):
    if Path(file).suffix == '.ascii':
        return load_ascii_battlefield
    elif Path(file).suffix == '.csv':
        return load_csv_battlefield
    elif Path(file).suffix == '.json':
        return load_json_battlefields
    else:
        raise NotImplementedError(f'unknown extension {Path(file).suffix}')

def load_json_battlefields(filename):
    import json
    with open(filename, 'r') as fp:
        tests = json.load(fp)
        return tests

def load_csv_battlefield(filename: str):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        battlefield =  [[char.strip() if char.strip() in '01' else char for char in line] for line in reader ]
        return battlefield

def load_ascii_battlefield(filename: str):
    with open(filename) as fp:
        battlefield = [[cell for cell in list(line.rstrip('\n'))] for line in fp]
    return battlefield

def battlefield_to_int(battlefield):
    return [[int(char) for char in row] for row in battlefield]

def convert_battlefield(battlefield, sea=' ', ship='#'):
    battlefield = [[char.replace(sea, '0').replace(ship, '1') for char in row] for row in battlefield]
    battlefield = battlefield_to_int(battlefield)
    return battlefield

def add_coordinates(matrix: list[list]) -> list[str]:
    top = bottom = ['  '] + [str(i)[-1] for i in range(len(matrix[0]))] + [' ']
    h_border = [' +'] + ['-' for _ in matrix[0]] + ['+']
    out = [top, h_border]
    for i, row in enumerate(matrix):
        number = str(i)[-1]
        out.append([number, '|'] + row + ['|', number])
    out.append(h_border)
    out.append(bottom)
    return out

def display(
            battlefield, path, ships, 
            SCANNED='#', SHIP=chr(9608), FREE=' ', PATH='.', HEAD='M', 
            print_matrix=True, 
            print_path=False, 
            sleep=0.2
            ):
    time.sleep(sleep)
    os.system('clear')

    print(f'{MAX_RECURSION_LEVEL = }')
    print(f'{RECURSION_LEVEL = }')

    ships = ships if ships is not None else []
    
    bf = battlefield[:]
    for y, x in path:
        bf[y][x] = PATH
    bf[y][x] = HEAD

    bf = [[str(item).replace('1', SHIP)
          .replace('0', FREE)
          .replace('2', FREE)
          .replace('3', SCANNED) for item in row] for row in bf]
    
    bf = add_coordinates(bf)
    matrix = add_coordinates(battlefield[:])
    for i, row in enumerate(bf):
        print(''.join(map(str, row)), ''.join(map(str, matrix[i])) if print_matrix else '')

    for ship in sorted(ships, key=len):
        print(f'{ship = }')

    if print_path:
        print(f'{path = }')
