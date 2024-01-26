from pathlib import Path

import helpers.loader as loader
import helpers.matrix as matrix

def main(solution):

    JSON = True
    if JSON:
        for file in loader.get_files('*.json'):
            tests = loader.load_battlefield(file)
            for test in tests:
                name = test['name']
                battlefield = test['data']
                expected = test['expected']
                matrix.display(battlefield)
                result = solution(battlefield)
                print(f'{name} -> {result = } -> {expected = }')
    else:
        for file in loader.get_files('*.ascii', '*.csv'):
            battlefield = loader.load_battlefield(file)
            battlefield = matrix.convert_battlefield(battlefield)
            result = solution(battlefield)
            print(f'{file.name} -> {result}')
