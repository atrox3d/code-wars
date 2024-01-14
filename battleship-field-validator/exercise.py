def exercise_runner(func):
    def param2str(*args, **kwargs) -> str:
        params = list(map(str, args)) + [f'{k}={v}' for k, v in kwargs.items()]
        params = ', '.join(params)
        return params     

    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        params = param2str(*args, **kwargs)
        print(f'running {func.__name__}({params})')
        result = func(*args, **kwargs)
        print(f'{result = }')
        return result
    return wrapper

'''
My friend John and I are members of the "Fat to Fit Club (FFC)". 
John is worried because each month a list with the weights of members is 
published and each month he is the last on the list which means he is 
the heaviest.

I am the one who establishes the list so I told him: 
"Don't worry any more, I will modify the order of the list". 
It was decided to attribute a "weight" to numbers. 
The weight of a number will be from now on the sum of its digits.

For example 99 will have "weight" 18, 100 will have "weight" 1 so 
in the list 100 will come before 99.

Given a string with the weights of FFC members in normal order 
can you give this string ordered by "weights" of these numbers?

Example:
"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: 

"100 180 90 56 65 74 68 86 99"
When two numbers have the same "weight", 
let us class them as if they were strings (alphabetical ordering) 
and not numbers:

180 is before 90 since, having the same "weight" (9), 
it comes before as a string.

All numbers in the list are positive numbers and the list can be empty.

Notes
it may happen that the input string have leading,
trailing whitespaces and more than a unique whitespace between two 
consecutive numbers
For C: The result is freed.
'''

def scan_ones(field) -> list[tuple]:
    """
    """
    ships = []
    for y in range(len(field)):
        for x in range(len(field[y])):
            current = field[y][x]
            print(f'{y, x, current = }', end='')
            if current:
                ships.append((y, x))
                print(' *')
            else:
                print()
    return ships

def print_ones(ones, field):
    """
    """
    ones = scan_ones(field)
    print(ones)
    for y, x in ones:
        print(f'{y, x, field[y][x] =}')

def find_h_ships(field: list[list]):
    ships = []
    ship = False
    for y in range(len(field)):
        for x in range(len(field[y])):
            value = field[y][x]
            coords = y, x
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

def find_v_ships(field: list[list]):
    ships = []
    ship = False
    for x in range(len(field[0])):
        for y in range(len(field)):
            value = field[y][x]
            coords = y, x
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
                
def validate_battlefield(field):
    # write your magic here
    hships = find_h_ships(field)
    print(hships)
    vships = find_v_ships(field)
    print(vships)
    return True

def main():
    runner = exercise_runner(validate_battlefield)
    battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                   [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                   [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    tests = [
        (battleField, True)
    ]
    for input, expected in tests:
        result = validate_battlefield(input)
        try:
            assert result == expected, f'{result} != {expected}'
        except AssertionError as ae:
            print(repr(ae))
if __name__ == '__main__':
    main()