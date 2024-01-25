from pathlib import Path

import helpers

def get_coords(battlefield, current, FREE, SHIP):
    ROWS = len(battlefield) 
    COLS = len(battlefield[0])
    LEFT = UP = -1
    RIGHT = DOWN = 1
    DIRECTIONS = ((0, RIGHT), (DOWN, 0), (0, LEFT), (UP, 0))
    DIRECTIONS = [(y, x) for y in range(-1, 2) for x in range(-1, 2) 
          if y!=x and 0 in (y, x)]
    
    new_coords = [(y+dy, x+dx) for dy, dx in DIRECTIONS for y, x in (current,)]
    legal_coords = [(y, x) for y, x in new_coords if 0 <= y < ROWS and 0 <= x < COLS]
    coords = [(y, x) for y, x in legal_coords if battlefield[y][x] in [FREE, SHIP]]
    return coords

def scan_ship(battlefield, path, y, x, FREE=0, SHIP=1, SCANNED=3):
    battlefield[y][x] = SCANNED
    ship = [(y, x)]
    coords = get_coords(battlefield, (y, x), FREE, SHIP)
    for coord in [(y, x) for y, x in coords if (y, x) not in path and battlefield[y][x] == SHIP]:
        y, x = coord
        battlefield[y][x] = SCANNED
        path = path + (coord, )
        block = scan_ship(battlefield, path, y, x)
        ship.extend(block)
    return ship

def explore(battlefield, path, ships=None, FREE=0, SHIP=1, VISITED=2):
    current = path[-1]
    ships = ships if ships is not None else []
    coords = get_coords(battlefield, current, FREE, SHIP)
    for coord in [yx for yx in coords if yx not in path]:
        y, x = coord
        item = battlefield[y][x]
        if battlefield[y][x] == SHIP:
            newpath = path + (coord,)
            ship = scan_ship(battlefield, newpath, y, x)
            ships.append(ship)
        elif battlefield[y][x] == FREE:
            newpath = path + (coord,)
            explore(battlefield, newpath, ships, FREE, SHIP)
            battlefield[y][x] = VISITED
    return ships

def check_ship(battlefield, ship):
    for by, bx in ship:
        for y, x in [(y, x) for y in (-1, 1) for x in (-1, 1)]:
            if battlefield[by+y][bx+x]:
                raise ValueError('diagonal')

def analyze(battlefield):
    bf = [row[:] for row in battlefield]
    ships = explore(battlefield, ((0, 0),), None)

    count = {}
    correct = {1: 4, 2: 3, 3: 3}
    for ship in sorted(ships, key=len):
        count[len(ship)] = count.get(len(ship), 0) + 1
    if count != correct:
        return False

    try:
        for ship in ships:
            check_ship(bf, ship)
    except ValueError as ve:
        return False
    
    return True

def main():
    for file in helpers.get_files(__file__, '*.ascii', '*.csv'):
        battlefield = helpers.load_file(file)
        battlefield = helpers.convert_battlefield(battlefield)
        result = analyze(battlefield)
        print(f'{file.name} -> {result}')

if __name__ == '__main__':
    import sys
    sys.exit(main())