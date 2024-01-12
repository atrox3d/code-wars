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

def fibonacci(n, branch: str):
    print(f'{branch:10}: {n = }')
    if n in [0, 1]:
        return n
    return fibonacci(n - 1, 'left') + fibonacci(n - 2, 'right')

def main():
    result = fibonacci(5, 'root')
    print(f'{result = }')

if __name__ == '__main__':
    main()