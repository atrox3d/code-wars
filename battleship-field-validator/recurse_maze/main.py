import csv, os
from pathlib import Path

def load_csv_maze(filename: str):
    with open(filename) as file:
        reader = csv.reader(file)
        return [line for line in reader]

def display_maze(maze, path):
    m = maze[:]
    os.system('clear')

    draw = ''
    for row in m:
        for item in row:
            item = str(item).replace('1', '#')
            item = str(item).replace('0', ' ')
            draw += item
        draw += '\n'
    
    print(draw)

def main():
    maze = load_csv_maze(Path(__file__).parent / 'maze.txt')
    display_maze(maze, None)


if __name__ == '__main__':
    import sys
    sys.exit(main())