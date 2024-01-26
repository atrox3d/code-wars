from pathlib import Path

import helpers.load as load
import helpers.matrix as matrix

def main(solution):

    for file_path in load.get_files(extensions='json, ascii, csv'):
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
