import logging

logger = logging.getLogger(__name__)

def inside_battlefield(battlefield, r, c):
    ROWS = len(battlefield) 
    COLS = len(battlefield[0])
    return 0 <= r < ROWS and 0 <= c < COLS

def get_coords(battlefield: list[list[int]], r:int, c:int, FREE:int, SHIP:int) -> list[tuple]:
    LEFT = UP = -1
    RIGHT = DOWN = 1
    DIRECTIONS = ((0, RIGHT), (DOWN, 0), (0, LEFT), (UP, 0))
    new_coords = [(r+dr, c+dc) for dr, dc in DIRECTIONS]
    legal_coords = [(r, c) for r, c in new_coords if inside_battlefield(battlefield, r, c)]
    coords = [(r, c) for r, c in legal_coords if battlefield[r][c] in [FREE, SHIP]]
    return coords

def scan_ship(battlefield: list[list[int]], path:tuple[tuple], r:int, c:int, FREE:int=0, SHIP:int=1, SCANNED:int=3) -> list[int]:
    battlefield[r][c] = SCANNED
    ship = [(r, c)]
    for r, c in [(r, c) for r, c in get_coords(battlefield, r, c, FREE, SHIP) if (r, c) not in path and battlefield[r][c] == SHIP]:
        battlefield[r][c] = SCANNED
        path = path + (r, c)
        block = scan_ship(battlefield, path, r, c)
        ship.extend(block)
    return ship

def explore(battlefield: list[list[int]], path:tuple[tuple], ships:list[list[int]]=None, FREE:int=0, SHIP:int=1, VISITED:int=2) -> list[list[int]]:
    r, c = path[-1]
    ships = ships if ships is not None else []
    if battlefield[r][c] == SHIP:
        ships.append(scan_ship(battlefield, path, r, c))

    for r, c in [rc for rc in get_coords(battlefield, r, c, FREE, SHIP) if rc not in path]:
        newpath = path + ((r, c),)
        if battlefield[r][c] == SHIP:
            ships.append(scan_ship(battlefield, newpath, r, c))
        elif battlefield[r][c] == FREE:
            explore(battlefield, newpath, ships, FREE, SHIP)
            battlefield[r][c] = VISITED
    return ships

def check_ship(battlefield: list[list[int]], ship: list[int]) -> bool:
    for ship_r, ship_c in ship:
        for check_r, check_c in [(ship_r+r, ship_c+c) for r in (-1, 1) for c in (-1, 1)]:
            if inside_battlefield(battlefield, check_r, check_c):
                if battlefield[check_r][check_c]:
                    return False
            else:
                continue
    return True

def count_ships(ships: list[list[int]]) -> bool:
    count = {}
    COUNT = {1: 4, 2: 3, 3: 2, 4: 1}

    for ship in sorted(ships, key=len):
        count[len(ship)] = count.get(len(ship), 0) + 1
    if count != COUNT:
        return False
    return True


def validate_battlefield(battlefield: list[list[int]]) -> bool:
    bf = [row[:] for row in battlefield]
    START = 0, 0
    PATH = (START, )
    
    ships: list[list[int]] = None
    ships = explore(battlefield, PATH, ships)
    for ship in ships:
        checked_ship: bool = check_ship(bf, ship)
        if not checked_ship:
            return False

    check_count: bool =  count_ships(ships)
    if not check_count:
        return False
    return check_count
