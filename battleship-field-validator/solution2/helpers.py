import csv, os, time

def load_csv_battlefield(filename: str):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        battlefield =  [[int(char.strip()) if char.strip() in '01' else char for char in line] for line in reader ]
        return battlefield

def display(battlefield, path, wall=chr(9608), free=' ', print_path=True, sleep=0.2):
    time.sleep(sleep)
    os.system('clear')

    bf = battlefield[:]
    for y, x in path:
        bf[y][x] = '.'
    bf[y][x] = 'M'

    print('+' + '-' * len(battlefield[0]) + '+')
    print('\n'.join(['|' + ''.join(
                [str(item).replace('1', wall).replace('0', free).replace('2', free)
                 for item in row]) + '|' for row in bf]))
    print('+' + '-' * len(battlefield[0]) + '+')
    if print_path:
        print(f'{path = }')
