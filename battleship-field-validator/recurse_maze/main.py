import csv, os, time
from pathlib import Path

def load_csv_maze(filename: str):
    with open(filename) as file:
        reader = csv.reader(file)
        grid =  [[int(char) if char in '01' else char for char in line] for line in reader ]
        return grid

def display_maze(maze, path, wall=chr(9608), free=' '):
    m2 = maze[:]
    os.system('clear')

    for y, x in path:
        m2[y][x] = '.'
    m2[y][x] = 'M'

    print('\n'.join(
            [''.join(
                [ str(item).replace('1', wall).replace('0', free) 
                 for item in row]) 
                for row in m2])
            )
    
def move(maze, path):
    time.sleep(0.5)
    ROWS = len(maze)
    COLS = len(maze[0])
    LEFT = UP = -1
    RIGHT = DOWN = 1
    DIRECTIONS = ((0, RIGHT), (DOWN, 0), (0, LEFT), (UP, 0))

    cur = path[-1]
    # os.system('clear')
    display_maze(maze, path)
    print(f'{path = }')

    availables = [(y+dy, x+dx) for dy, dx in DIRECTIONS for y, x in (cur,)]
    possibles = [(y, x) for y, x in availables if 0 <= y < ROWS and 0 <= x < COLS]
    legals = [(y, x) for y, x in possibles if maze[y][x] in ('A', 'B', 0)]
    for item in legals:
        y, x = item
        if item in path: 
            continue
        elif maze[y][x] == 'B':
            path.append(item)
            display_maze(maze, path)
            input('solution found, press enter to finish')
            sys.exit()
        else:
            newpath = path + [item]
            move(maze, newpath)


def main():
    maze = load_csv_maze(Path(__file__).parent / 'maze.txt')
    # display_maze(maze, [])
    move(maze, [(1, 0)])


if __name__ == '__main__':
    import sys
    sys.exit(main())