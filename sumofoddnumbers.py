'''
Calculate the sum of the numbers in the nth row of this triangle 
(starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8

               1               - 1: skip  0, print 1
            3     5            - 2: skip  1, print 2
         7     9    11         - 3: skip  3, print 3
     13    15    17    19      - 4: skip  6, print 4
  21    23    25    27    29   - 5: skip 10, print 5
...
'''

def odd_range_generator(n):
    for x in range(1, 2*n+1, 2):
        yield x

def odd_generator(_):
    n = 0
    while True:
        yield n * 2 + 1 
        n += 1

def row_sum_odd_numbers(n, generator):
    print(f'{n = }')
    g = generator(n)

    skipping = []
    to_skip = sum(x for x in range(n))
    for i in range(to_skip):
        skip_val = next(g)
        skipping.append(skip_val)
    print(f'{skipping = }')

    printing = []
    for i in range(n):
        print_val = next(g)
        printing.append(print_val)
    print(f'{printing = }')
    
for t in range(1, 6):
    row_sum_odd_numbers(t, odd_generator)
