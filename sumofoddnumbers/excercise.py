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
    # get the count of value to skip
    to_skip = sum(x for x in range(n))
    # compute the upper range
    top = n + to_skip

    odd_val = 0
    total = 0
    for i in range(top):
        # compute odd value
        odd_val = i * 2 + 1
        # add to total only if part of the row
        if i >= to_skip:
            total += odd_val

    return total
