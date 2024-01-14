def exercise_runner(func):
    import logging
    logging.basicConfig(level='DEBUG')
    logger = logging.getLogger('excercise_runner')
    def param2str(*args, **kwargs) -> str:
        params = list(map(str, args)) + [f'{k}={v}' for k, v in kwargs.items()]
        params = ', '.join(params)
        return params     

    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        params = param2str(*args, **kwargs)
        logger.debug(f'running {func.__name__}({params})')
        result = func(*args, **kwargs)
        logger.debug(f'{result = }')
        return result
    return wrapper

'''
My friend John and I are members of the "Fat to Fit Club (FFC)". 
John is worried because each month a list with the weights of members is 
published and each month he is the last on the list which means he is 
the heaviest.

I am the one who establishes the list so I told him: 
"Don't worry any more, I will modify the order of the list". 
It was decided to attribute a "weight" to numbers. 
The weight of a number will be from now on the sum of its digits.

For example 99 will have "weight" 18, 100 will have "weight" 1 so 
in the list 100 will come before 99.

Given a string with the weights of FFC members in normal order 
can you give this string ordered by "weights" of these numbers?

Example:
"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: 

"100 180 90 56 65 74 68 86 99"
When two numbers have the same "weight", 
let us class them as if they were strings (alphabetical ordering) 
and not numbers:

180 is before 90 since, having the same "weight" (9), 
it comes before as a string.

All numbers in the list are positive numbers and the list can be empty.

Notes
it may happen that the input string have leading,
trailing whitespaces and more than a unique whitespace between two 
consecutive numbers
For C: The result is freed.
'''

def order_weight(strng: str):
    # your code
    str_weights = strng.split()
    print(str_weights)

    weighted = {sum(map(int, list(w))):w for w in str_weights}
    print(weighted)

    ordered = [weighted[k] for k in sorted(weighted)]

    return ' '.join(ordered)


def main():
    runner = exercise_runner(order_weight)
    tests = [
        ("103 123 4444 99 2000", "2000 103 123 4444 99"),
        ("2000 10003 1234000 44444444 9999 11 11 22 123", "11 11 2000 10003 22 123 1234000 44444444 9999"),
        ("", ""),
    ]
    for input, expected in tests:
        result = runner(input)
        try:
            assert result == expected, f'{result} != {expected}'
        except AssertionError as ae:
            print(repr(ae))
        finally:
            print()
if __name__ == '__main__':
    main()