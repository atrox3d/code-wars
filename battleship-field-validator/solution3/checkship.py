import data

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

    

for ship in data.ships:
    check_ship(data.battlefield, ship)

