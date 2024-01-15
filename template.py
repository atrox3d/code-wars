'''
description
'''

def your_function_here(*args, **kwargs):
    pass

def main():
    import sys
    sys.path.insert(0, '.')
    from runner import run
    
    tests = [
        ('input', True)
    ]
    for input, expected in tests:
        result = run(your_function_here, input)
        try:
            assert result == expected, f'{result} != {expected}'
        except AssertionError as ae:
            print(repr(ae))

if __name__ == '__main__':
    main()