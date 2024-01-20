import csv
from pathlib import Path

def load_csv_maze(filename: str):
    with open(filename) as file:
        reader = csv.reader(file)
        return [line for line in reader]

def main():
    maze = load_csv_maze(Path(__file__).parent / 'maze.txt')
    print(maze)


if __name__ == '__main__':
    import sys
    sys.exit(main())