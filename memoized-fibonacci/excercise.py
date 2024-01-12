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

    root = 50
    
    print(f'running cached fibonacci...')
    start_time = time.time()
    result = fibonacci(root, 'root')
    fibonacci_time = time.time() - start_time
    print(f'end running cached fibonacci...')

    print(f'running original _fibonacci...')
    start_time = time.time()
    _result = _fibonacci(root)
    _fibonacci_time = time.time() - start_time
    print(f'end running original _fibonacci...')
    
    print(f'{_result = }, {_fibonacci_time = }')
    print(f'{result = }, {fibonacci_time = }')
    print(f'{cache = }')

    assert result == _result, f'{result} != {_result}'

if __name__ == '__main__':
    main()