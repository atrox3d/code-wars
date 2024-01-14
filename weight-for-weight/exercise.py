'''
exercise description
'''

def exercise_runner(func):
    def param2str(*args, **kwargs) -> str:
        params = list(map(str, args)) + [f'{k}={v}' for k, v in kwargs.items()]
        params = ', '.join(params)
        return params     

    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        params = param2str(*args, **kwargs)
        print(f'running {func.__name__}({params})')
        result = func(*args, **kwargs)
        print(f'{result = }')
        return result
    return wrapper

@exercise_runner
def your_function_here(arg, kwarg):
    return 'put function here'

def main():
    tests = [
        ('input', 'expected')
    ]
    for input, expected in tests:
        result = your_function_here(input, kwarg='kwarg')
        assert result == expected, f'{result} != {expected}'
if __name__ == '__main__':
    main()