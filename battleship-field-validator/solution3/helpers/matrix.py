import os, time, logging

MAX_RECURSION_LEVEL = RECURSION_LEVEL = 0
logger = logging.getLogger(__name__)

def csv_to_int(battlefield):
    return [[int(char) for char in row] for row in battlefield]

def ascii_to_int(battlefield, sea=' ', ship='#'):
    battlefield = [[char.replace(sea, '0').replace(ship, '1') for char in row] for row in battlefield]
    battlefield = csv_to_int(battlefield)
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
            battlefield, 
            path=None, 
            ships=None, 
            SCANNED='#', SHIP=chr(9608), FREE=' ', PATH='.', HEAD='M', 
            print_matrix=True, 
            print_path=False,
            clear_screen=False,
            sleep=0.2
            ):
    logger.debug(f'{sleep = }')
    time.sleep(sleep)
    if clear_screen:
        os.system('clear')
        logger.info(f'screen cleared')

    # print(f'{MAX_RECURSION_LEVEL = }')
    # print(f'{RECURSION_LEVEL = }')

    ships = ships if ships is not None else []
    path = path if path is not None else []
    
    bf = battlefield[:]
    if path:
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
