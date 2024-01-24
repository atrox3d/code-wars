from pathlib import Path
import logging

from helpers import display, load_csv_battlefield, load_ascii_battlefield, convert_battlefield
import helpers

logging.basicConfig(level='WARN', format='%(levelname)s:%(funcName)-10.10s:%(message)s')
log = logging.getLogger(__name__)

def get_coords(battlefield, current, FREE, SHIP):
    ROWS = len(battlefield) 
    COLS = len(battlefield[0])
    LEFT = UP = -1
    RIGHT = DOWN = 1
    DIRECTIONS = ((0, RIGHT), (DOWN, 0), (0, LEFT), (UP, 0))
    
    new_coords = [(y+dy, x+dx) for dy, dx in DIRECTIONS for y, x in (current,)]
    legal_coords = [(y, x) for y, x in new_coords if 0 <= y < ROWS and 0 <= x < COLS]
    coords = [(y, x) for y, x in legal_coords if battlefield[y][x] in [FREE, SHIP]]

    for item in [battlefield[y][x] for y, x in coords]:
        assert item in [FREE, SHIP], f'get_coords: {item = }'
        assert item <= SHIP, f'get_coords: {item = }'
    return coords

def scan_ship(battlefield, path, y, x, FREE=0, SHIP=1, SCANNED=3):
    battlefield[y][x] = SCANNED
    ship = [(y, x)]

    log.debug(f'ENTER: {ship = }')
    log.debug(f'ENTER: {path = }')

    coords = get_coords(battlefield, (y, x), FREE, SHIP)
    for coord in [(y, x) for y, x in coords if (y, x) not in path and battlefield[y][x] == SHIP]:

        log.debug(f'for loop: {coord =} {ship = }') # DELETE

        y, x = coord
        battlefield[y][x] = SCANNED
        path = path + (coord, )

        log.debug(f'RECURSE {coord = }') # DELETE
        log.debug(f'RECURSE {path = }') # DELETE

        block = scan_ship(battlefield, path, y, x)
        assert not any(block in ship for block in block), 'duplicate ship'
        ship.extend(block)

    log.debug(f'EXIT: {ship = }')
    return ship

def explore(battlefield, path, ships=None, START='A', END='B', FREE=0, SHIP=1, VISITED=2, SCANNED=3, sleep=0.2):
    helpers.MAX_RECURSION_LEVEL += 1 # DELETE
    helpers.RECURSION_LEVEL += 1 # DELETE
    
    current = path[-1]
    ships = ships if ships is not None else []
    
    display(battlefield, path, ships, sleep=sleep) # DELETE

    coords = get_coords(battlefield, current, FREE, SHIP)
    for coord in [yx for yx in coords if yx not in path]:
        y, x = coord
        item = battlefield[y][x]
        if battlefield[y][x] == SHIP:
    
            log.debug(f'ship found {coord = }') # DELETE
    
            newpath = path + (coord,)
            ship = scan_ship(battlefield, newpath, y, x)
            ships.append(ship)
    
            log.debug(f'{ship = }') # DELETE
    
        elif battlefield[y][x] == FREE:
            newpath = path + (coord,)
            explore(battlefield, newpath, ships, START, END, FREE, SHIP)
            battlefield[y][x] = VISITED
        
        display(battlefield, path, ships) # DELETE
    helpers.RECURSION_LEVEL -= 1 # DELETE
    return ships

def check_ship(battlefield, ship):
    shipp = sorted(ship)
    print(f'{shipp = }')
    print(list(zip(*shipp)))
    y, x = list(zip(*shipp))
    print(y, x) 

    if len(shipp) > 1:
        straights = [len(set(x)) == 1 for x in zip(*shipp)]
        print(f'{straights = }')
        straight = straights.count(True) == 1
        print(f'{straight = }')
        if not straight:
            raise ValueError('! straight')

    for by, bx in shipp:
        for y, x in [(y, x) for y in (-1, 1) for x in (-1, 1)]:
            if battlefield[by+y][bx+x]:
                raise ValueError('diagonal')
    print()

def analyze(battlefield):
    bf = [row[:] for row in battlefield]
    ships = explore(battlefield, ((0, 0),), None, sleep=0.0)
    print(f'{ships = }')
    count = {}
    for ship in sorted(ships, key=len):
        count[len(ship)] = count.get(len(ship), 0) + 1
    print(f'{count = }')
    correct = {1: 4, 2: 3, 3: 3}
    print(f'{count == correct = }')

    for row in bf:
        print(row)

    for ship in ships:
        check_ship(bf, ship)

def main():
    battlefield = load_ascii_battlefield(Path(__file__).parent / 'battlefield.ascii.txt')
    battlefield = convert_battlefield(battlefield)
    analyze(battlefield)
    print('exit NOT FOUND!')

if __name__ == '__main__':
    import sys
    sys.exit(main())