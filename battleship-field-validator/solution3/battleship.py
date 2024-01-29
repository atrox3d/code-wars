import logging

logger = logging.getLogger(__name__)

def get_coords(battlefield, y, x, FREE, SHIP):
    ROWS = len(battlefield) 
    COLS = len(battlefield[0])
    LEFT = UP = -1
    RIGHT = DOWN = 1
    DIRECTIONS = ((0, RIGHT), (DOWN, 0), (0, LEFT), (UP, 0))
    new_coords = [(cy+dy, cx+dx) for dy, dx in DIRECTIONS for cy, cx in ((y, x),)]
    legal_coords = [(y, x) for y, x in new_coords if 0 <= y < ROWS and 0 <= x < COLS]
    coords = [(y, x) for y, x in legal_coords if battlefield[y][x] in [FREE, SHIP]]
    return coords

def scan_ship(battlefield, path, y, x, FREE=0, SHIP=1, SCANNED=3):
    battlefield[y][x] = SCANNED
    ship = [(y, x)]
    logger.debug(f'{ship = }')
    for y, x in [(y, x) for y, x in get_coords(battlefield, y, x, FREE, SHIP) if (y, x) not in path and battlefield[y][x] == SHIP]:
        battlefield[y][x] = SCANNED
        path = path + (y, x)
        block = scan_ship(battlefield, path, y, x)
        ship.extend(block)
    return ship

def explore(battlefield, path, ships=None, FREE=0, SHIP=1, VISITED=2):
    y, x = path[-1]
    logger.debug(f'{y, x = }')
    ships = ships if ships is not None else []
    logger.debug(f'{ships = }')
    for y, x in [yx for yx in get_coords(battlefield, y, x, FREE, SHIP) if yx not in path]:
        logger.debug(f'for_loop: {y, x = }')
        newpath = path + ((y, x),)
        if battlefield[y][x] == SHIP:
            logger.debug(f'call: scan_ship')
            ships.append(scan_ship(battlefield, newpath, y, x))
        elif battlefield[y][x] == FREE:
            logger.debug(f'call: explore')
            explore(battlefield, newpath, ships, FREE, SHIP)
            battlefield[y][x] = VISITED
    return ships

def check_ship(battlefield, ship):
    ROWS = len(battlefield) 
    COLS = len(battlefield[0])
    for by, bx in ship:
        for y, x in [(y, x) for y in (-1, 1) for x in (-1, 1)]:
            if 0 <= by+y < ROWS and 0 <= bx+x < COLS:
                if battlefield[by+y][bx+x]:
                    return False
            else:
                continue
    return True

def count_ships(ships):
    count = {}
    COUNT = {1: 4, 2: 3, 3: 2, 4: 1}

    for ship in sorted(ships, key=len):
        count[len(ship)] = count.get(len(ship), 0) + 1
    if count != COUNT:
        logger.debug(f'{COUNT = }')
        logger.debug(f'{count = }')
        return False
    return True


def validate(battlefield):
    bf = [row[:] for row in battlefield]
    START = 0, 0
    PATH = (START, )
    ships = None
    logger.debug(f'start explore')
    ships = explore(battlefield, PATH, ships)
    logger.debug(f'end explore')
    logger.debug(f'{ships = }')

    for ship in ships:
        check = check_ship(bf, ship)
        print(f'{check = }')
        if not check:
            return False
        
    return count_ships(ships)
