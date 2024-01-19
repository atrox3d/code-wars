import sys
import os

try:
    from matrix import matrix
except:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from matrix import matrix

print(f'{os.getcwd() = }')
map_file = os.path.join(os.path.dirname(__file__), 'map.txt')
map = matrix.load(map_file, split=None)

matrix.display(matrix.format_border(map))
