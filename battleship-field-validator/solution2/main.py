import csv, os, time
from pathlib import Path

def load_csv_maze(filename: str):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        grid =  [[int(char) if char in '01' else char for char in line] for line in reader ]
        return grid

def display_maze(maze, path, wall=chr(9608), free=' ', print_path=True, sleep=0.2):
    m2 = maze[:]
    if sleep:
        time.sleep(sleep)
    os.system('clear')

    for y, x in path:
        m2[y][x] = '.'
    m2[y][x] = 'M'

    print('\n'.join([''.join(
                [ str(item).replace('1', wall).replace('0', free).replace('2', free)
                 for item in row]) for row in m2]))
    if print_path:
        print(f'{path = }')

    
def move(maze, path, START='A', END='B', FREE=0, WALL=1, VISITED=2, sleep=0.2):
    ROWS = len(maze)
    COLS = len(maze[0])
    LEFT = UP = -1
    RIGHT = DOWN = 1
    DIRECTIONS = ((0, RIGHT), (DOWN, 0), (0, LEFT), (UP, 0))

    current = path[-1]
    display_maze(maze, path, sleep=sleep)

    new_coords = [(y+dy, x+dx) for dy, dx in DIRECTIONS for y, x in (current,)]
    legal_coords = [(y, x) for y, x in new_coords if 0 <= y < ROWS and 0 <= x < COLS]
    coords = [(y, x) for y, x in legal_coords if maze[y][x] in (START, END, FREE)]
    for coord in [yx for yx in coords if yx not in path]:
        y, x = coord
        if maze[y][x] == 'B':
            newpath = path + (coord,)
            display_maze(maze, path)
            print('solution found')
            sys.exit()
        else:
            newpath = path + (coord,)
            move(maze, newpath, START, END, FREE, WALL)
            maze[y][x] = VISITED
            display_maze(maze, path)

def main():
    maze = load_csv_maze(Path(__file__).parent / 'maze.txt')
    move(maze, ((1, 0),), sleep=0)
    print('exit NOT FOUND!')

if __name__ == '__main__':
    import sys
    sys.exit(main())