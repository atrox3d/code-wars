from pathlib import Path

import helpers.files as files
import helpers.matrix as matrix

def main(solution):
    DATA_PATH = Path(__file__).parent / 'data'

    JSON = True
    if JSON:
        for file in files.get_files(DATA_PATH, '*.json'):
            tests = files.load_file(file)
            for test in tests:
                name = test['name']
                battlefield = test['data']
                expected = test['expected']
                matrix.display(battlefield)
                result = solution(battlefield)
                print(f'{name} -> {result = } -> {expected = }')
    else:
        for file in files.get_files(DATA_PATH, '*.ascii', '*.csv'):
            battlefield = files.load_file(file)
            battlefield = matrix.convert_battlefield(battlefield)
            result = solution(battlefield)
            print(f'{file.name} -> {result}')

if __name__ == '__main__':
    import sys
    sys.exit(main())