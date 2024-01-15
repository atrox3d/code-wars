'''
description
'''

def your_function_here(*args, **kwargs):
    pass

def main():
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '.')
    from runner import exercise_runner
    
    runner = exercise_runner(your_function_here)
    tests = [
        ('input', 'expected')
    ]
    for input, expected in tests:
        result = runner(input)
        try:
            assert result == expected, f'{result} != {expected}'
        except AssertionError as ae:
            print(repr(ae))
if __name__ == '__main__':
    main()