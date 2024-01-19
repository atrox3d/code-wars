def find_ships(field: list[list], direction: str):
    ships = []
    ship = False

    outer_range = range(len(field[0])) if direction == 'v' else range(len(field))
    inner_range = range(len(field)) if direction == 'v' else range(len(field[0]))

    for outer in outer_range:
        for inner in inner_range:
            if direction == 'v':
                value = field[inner][outer]
                coords = inner, outer
            else:
                value = field[outer][inner]
                coords = outer, inner
            if value and not ship:
                ship = True
                new_ship = [coords]
            elif value and ship:
                new_ship.append(coords)
            elif ship and not value:
                if len(new_ship) > 1:
                    ships.append(new_ship)
                    ship = []
                ship = False
    return ships

def check_overlapping_ships(hships: list[list], vships: [list[list]]):
    print(f'{hships = }')
    print(f'{vships = }')
    vflatten = [coord for i in vships for coord in i]
    print(f'{vflatten = }')
    for ship in hships:
        for coord in ship:
            if coord in vflatten:
                return False
    return True

