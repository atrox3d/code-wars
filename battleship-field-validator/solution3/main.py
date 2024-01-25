import helpers

def main(solution):
    JSON = True
    if JSON:
        for file in helpers.get_files(__file__, '*.json'):
            tests = helpers.load_file(file)
            for test in tests:
                name = test['name']
                battlefield = test['data']
                expected = test['expected']
                helpers.display(battlefield)
                result = solution(battlefield)
                print(f'{name} -> {result = } -> {expected = }')
    else:
        for file in helpers.get_files(__file__, '*.ascii', '*.csv'):
            battlefield = helpers.load_file(file)
            battlefield = helpers.convert_battlefield(battlefield)
            result = solution(battlefield)
            print(f'{file.name} -> {result}')

if __name__ == '__main__':
    import sys
    sys.exit(main())