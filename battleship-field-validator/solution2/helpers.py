import csv, os, time

MAX_RECURSION_LEVEL = RECURSION_LEVEL = 0


def load_csv_battlefield(filename: str):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        battlefield =  [[int(char.strip()) if char.strip() in '01' else char for char in line] for line in reader ]
        return battlefield


def add_coordinates(matrix: list[list]) -> list[str]:
    top = bottom = [' '] + [str(i)[-1] for i in range(len(matrix[0]))] + [' ']
    out = [top]
    for i, row in enumerate(matrix):
        number = str(i)[-1]
        out.append([number] + row + [number])
    out.append(bottom)
    return out

def display(battlefield, path, ships, SCANNED='#', SHIP=chr(9608), FREE=' ', PATH='.', HEAD='M', print_matrix=True, print_path=True, sleep=0.2):
    time.sleep(sleep)
    os.system('clear')

    print(f'{MAX_RECURSION_LEVEL = }')
    print(f'{RECURSION_LEVEL = }')
    bf = battlefield[:]
    for y, x in path:
        bf[y][x] = PATH
    bf[y][x] = HEAD

    if print_matrix:
        for row in battlefield:
            print(''.join(map(str, row)))

    print('+' + '-' * len(battlefield[0]) + '+')
    print('\n'.join(['|' + ''.join(
                [str(item).replace('1', SHIP).replace('0', FREE).replace('2', FREE).replace('3', SCANNED)
                 for item in row]) + '|' for row in bf]))
    print('+' + '-' * len(battlefield[0]) + '+')
    for ship in ships:
        print(f'{ship = }')
    if print_path:
        print(f'{path = }')
