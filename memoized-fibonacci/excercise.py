r'''
                     5
                ____/ \___    
              /            \
             4              3
          /     \          /   \
        3        2        2     1
      /   \     / \      / \
    2      1   1   0    1   0
 /    \
1       0

'''

def _fibonacci(n):
    if n in [0, 1]:
        return n
    return _fibonacci(n - 1) + _fibonacci(n - 2)

cache = {}
def fibonacci(n, branch: str):
    print(f'{branch:10}: {n = }')
    if n in [0, 1]:
        return n
    
    try:
        left = cache[n-1]
    except KeyError: 
        left = fibonacci(n - 1, 'left')
        cache[n-1] = left

    try:
        right = cache[n-2] 
    except KeyError: 
        right = fibonacci(n - 2, 'right')
        cache[n-2] = right
    
    return  left + right

def main():
    import time
    import functools

    def timed(func):
        functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            ret = func(*args, **kwargs)
            end_time = time.time() - start_time
            print(f'{end_time = }')
            return ret
        return wrapper

    @timed
    def runner(func, *args, **kwargs):
        print(f'running {func.__name__}...')
        ret = func(*args, **kwargs)
        print(f'end running {func.__name__}...')
        return ret

    root = 35
    
    result = runner(fibonacci, root, 'root')

    _result = runner(_fibonacci, root)
    
    print(f'{_result = }')
    print(f'{result = }')
    print(f'{cache = }')

    assert result == _result, f'{result} != {_result}'

if __name__ == '__main__':
    main()