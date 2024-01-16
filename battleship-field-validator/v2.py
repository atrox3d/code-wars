import logging

logger = logging.getLogger(__name__)

def find_ships(field: list[list]):
    rows_range = range(len(field))
    cols_range = range(len(field[0]))
    h_ships = _find_ships(field, rows_range, cols_range, direction='h')
    
    rows_range = range(len(field[0]))
    cols_range = range(len(field))
    v_ships = _find_ships(field, rows_range, cols_range, direction='v')

    return h_ships, v_ships

def _find_ships(field: list[list],outer_range, inner_range, direction):
    ships = []
    for row in outer_range:
        is_ship = False
        ship = []
        for col in inner_range:
            current = field[row][col] if direction=='v' else field[col][row]
            if current and not is_ship:
                is_ship = True
                ship.append((row, col))
            elif current and is_ship:
                ship.append((row, col))
            elif not current and is_ship:
                ships.append(ship)
                is_ship = False
                ship = []
    return ships

def find_h_ships(field: list[list]):
    ships = []
    for y in range(len(field)):
        is_ship = False
        ship = []
        for x in range(len(field[y])):
            current = field[y][x]
            if current and not is_ship:
                is_ship = True
                ship.append((y, x))
            elif current and is_ship:
                ship.append((y, x))
            elif not current and is_ship:
                ships.append(ship)
                is_ship = False
                ship = []
    return ships

def find_v_ships(field: list[list]):
    ships = []
    for x in range(len(field[0])):
        is_ship = False
        ship = []
        for y in range(len(field)):
            current = field[y][x]
            if current and not is_ship:
                is_ship = True
                ship.append((y, x))
            elif current and is_ship:
                ship.append((y, x))
            elif not current and is_ship:
                ships.append(ship)
                is_ship = False
                ship = []
    return ships

def check_overlapping_ships_and_normalize(hships: list[list], vships: [list[list]]):
    done = False
    while not done:
        done = True
        for hship in hships:
            for hcoord in hship:
                for vship in vships:
                    if hcoord in vship:
                        if len(hship) >= 1 and len(vship) == 1:
                            logger.debug(f'removing {vship}: {hcoord =}')
                            vships.remove(vship)
                            done = False
                        elif len(hship) == 1 and len(vship) > 1:
                            logger.debug(f'removing {hship}: {hcoord =}')
                            hships.remove(hship)
                        elif len(hship) == 1 and len(vship) > 1:
                            done = False
                        elif len(hship) > 1 and len(vship) > 1:
                            return False
    return True

def count_ships(ships: list[list]) -> dict:
    count = {}
    for ship in ships:
        count[len(ship)] = count.get(len(ship), 0) + 1
    return count