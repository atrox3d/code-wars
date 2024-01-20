import csv, os
from pathlib import Path

def load_csv_maze(filename: str):
    with open(filename) as file:
        reader = csv.reader(file)
        return [line for line in reader]

def display_maze(maze, path, wall=chr(9608), free=' '):
    amazeing = maze[:]
    os.system('clear')
    print('\n'.join(
            [''.join(
                [ str(item).replace('1', wall).replace('0', free) 
                 for item in row]) 
                for row in amazeing])
            )

def main():
    maze = load_csv_maze(Path(__file__).parent / 'maze.txt')
    display_maze(maze, None)


if __name__ == '__main__':
    import sys
    sys.exit(main())