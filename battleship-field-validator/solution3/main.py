from pathlib import Path

import helpers

def main(solution):
    DATA_PATH = Path(__file__).parent / 'data'

    JSON = True
    if JSON:
        for file in helpers.get_files(DATA_PATH, '*.json'):
            tests = helpers.load_file(file)
            for test in tests:
                name = test['name']
                battlefield = test['data']
                expected = test['expected']
                helpers.display(battlefield)
                result = solution(battlefield)
                print(f'{name} -> {result = } -> {expected = }')
    else:
        for file in helpers.get_files(DATA_PATH, '*.ascii', '*.csv'):
            battlefield = helpers.load_file(file)
            battlefield = helpers.convert_battlefield(battlefield)
            result = solution(battlefield)
            print(f'{file.name} -> {result}')

if __name__ == '__main__':
    import sys
    sys.exit(main())