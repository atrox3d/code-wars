def fibonacci(n):
    print(f'{n = }')
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    result = fibonacci(10)
    print(f'{result = }')

if __name__ == '__main__':
    main()