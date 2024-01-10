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

def row_sum_odd_numbers(n):
    print(f'{n = }')
    
    to_skip = sum(x for x in range(n))
    odd_numbers = (x * 2 + 1 for x in range(n + to_skip))
    g = odd_numbers

    skipping = []
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
    row_sum_odd_numbers(t)
