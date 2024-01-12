'''
A format for expressing an ordered list of integers is to use
a comma separated list of either

- individual integers
- or a range of integers denoted by the starting integer separated 
  from the end integer in the range by a dash, '-'. 
  The range includes all integers in the interval including 
  both endpoints. 
  It is not considered a range unless it spans 
  at least 3 numbers. For example "12,13,15-17"

Complete the solution so that it takes a list of integers 
in increasing order and returns a correctly formatted string 
in the range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
'''
import try1
import try2

def solution(args):
    # your code here
    print(f'{args = }')
    data = sorted(args)
    print(f'{data = }')

    
    result = try2.solution(data)
    print(result)
    return result

def test():
    args = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
    expected = "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
    result = solution(args)
    # assert result == expected, f'{result} != {expected}'
    if expected != result:
        ae = AssertionError(f'{result} != {expected}')
        ae.values = ','.join(map(str, args))
        ae.expected = expected
        ae.result = result
        raise ae
try:
    test()
except AssertionError as ae:
    print(repr(ae))
    print(f'{ae.values   = }')
    print(f'{ae.expected = }')
    print(f'{ae.result   = }')
