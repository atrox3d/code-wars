from pathlib import Path
from helpers import display, load_csv_battlefield, MAX_RECURSION_LEVEL
import helpers

def get_coords(battlefield, current, FREE, SHIP):
    ROWS = len(battlefield) 
    COLS = len(battlefield[0])
    LEFT = UP = -1
    RIGHT = DOWN = 1
    DIRECTIONS = ((0, RIGHT), (DOWN, 0), (0, LEFT), (UP, 0))
    
    new_coords = [(y+dy, x+dx) for dy, dx in DIRECTIONS for y, x in (current,)]
    legal_coords = [(y, x) for y, x in new_coords if 0 <= y < ROWS and 0 <= x < COLS]
    coords = [(y, x) for y, x in legal_coords if battlefield[y][x] in [FREE, SHIP]]
    return coords

def scan_ship(battlefield, path, y, x, FREE=0, SHIP=1, SCANNED=3):
    battlefield[y][x] = SCANNED
    ship = [(y, x)]

    print(f'scan_ship start: {ship = }')

    coords = get_coords(battlefield, (y, x), FREE, SHIP)
    for coord in [(y, x) for y, x in coords if (y, x) not in path and battlefield[y][x] == SHIP]:
        ship.append(coord)
        print(f'scan_ship for: {ship = }')
        y, x = coord
        battlefield[y][x] = SCANNED

        temp = scan_ship(battlefield, path, y, x)
        print(f'scan_ship: {temp = }')
        assert temp not in ship, 'duplicate ship'
        ship.append(temp)

    print(f'scan_ship end: {ship = }')
    return ship
        

def explore(battlefield, path, ships=None, START='A', END='B', FREE=0, SHIP=1, VISITED=2, sleep=0.2):
    helpers.MAX_RECURSION_LEVEL += 1
    helpers.RECURSION_LEVEL += 1
    
    current = path[-1]
    ships = ships if ships is not None else []
    display(battlefield, path, ships, sleep=sleep)
    coords = get_coords(battlefield, current, FREE, SHIP)
    for coord in [yx for yx in coords if yx not in path]:
        y, x = coord
        if battlefield[y][x] == SHIP:
            newpath = path + (coord,)
            ship = scan_ship(battlefield, path, y, x)
            print(f'explore: {ship = }')
            input()
            display(battlefield, path, ships)
            print('ship found')
        else:
            newpath = path + (coord,)
            explore(battlefield, newpath, ships, START, END, FREE, SHIP)
            battlefield[y][x] = VISITED
            display(battlefield, path, ships)
    helpers.RECURSION_LEVEL -= 1
    assert len(set(path)) == len(path), "you have duplicate coordinates"

def main():
    battlefield = load_csv_battlefield(Path(__file__).parent / 'battlefield.txt')
    explore(battlefield, ((0, 0),), None, sleep=0.0)
    print('exit NOT FOUND!')

if __name__ == '__main__':
    import sys
    sys.exit(main())