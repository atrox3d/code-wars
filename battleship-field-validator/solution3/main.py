from pathlib import Path

import helpers.load as load
import helpers.matrix as matrix
import battleship

def main(solution):
    extensions = 'json, ascii, csv'
    for file_path in load.get_files(extensions=extensions):
        tests = load.battlefield(file_path)
        for test in tests:
            name = test['name']
            battlefield = test['data']
            expected = test['expected']

            matrix.display(battlefield)
            result = solution(battlefield)
            print(f'{name} -> {result = } -> {expected = }')
            
            print()
            print()


if __name__ == '__main__':
    import sys
    sys.exit(main(solution=battleship.validate_battlefield))