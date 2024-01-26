from pathlib import Path

import helpers.loader as loader
import helpers.matrix as matrix

def main(solution):

    # for file in loader.get_files('*.json', '*.ascii', '*.csv'):
    for file in loader.get_files(extensions='json, ascii, csv'):
        tests = loader.load_battlefield(file)
        for test in tests:
            name = test['name']
            battlefield = test['data']
            expected = test['expected']
            matrix.display(battlefield)
            result = solution(battlefield)
            print(f'{name} -> {result = } -> {expected = }')
            print()
            print()
