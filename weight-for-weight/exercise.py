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
    # get list of strings
    str_weights = strng.split()
    # create list of dicts {computed_weight:weight_string}
    weighted = [{sum(map(int, list(weight))):weight} for weight in str_weights]
    # temporary list of dicts sorted by computed_weight
    sort = sorted(weighted, key=lambda w:list(w.keys())[0])
    # create two separated sorted lists
    sorted_weighted = [list(d.keys())[0] for d in sort]
    sorted_weights = [list(d.values())[0] for d in sort]
    # create final list
    if len(set(sorted_weighted)) != len(sorted_weighted):
        # manage same weighted values
        i = 0
        result = []
        # group and flatten same weight values
        while i < len(sorted_weighted):
            current = sorted_weighted[i]
            if (count := sorted_weighted.count(current)) > 1:
                result.extend(sorted(sorted_weights[i:i+count]))
                i += count
            else:
                result.append(sorted_weights[i])
                i += 1
    else:
        result = sorted_weights
    return ' '.join(map(str, result))

def _order_weight(_str):

    # 1)
    sl = sorted(_str.split())
    print(f'{sl = }')

    # 3-4-5
    for x in sl:
        y = sum(int(c) for c in x)
        print(f'{y = }')
    
    # 3-4-5
    comp = [sum(int(c) for c in x) for x in sl]
    print(f'{comp = }')

    return ' '.join(
        sorted(                         # 2) sort sorted splitted
                                        # using calculated weight
        sorted(                         
                _str.split(' ')         # 1) sort splitted       
            ),
            key=lambda x: sum(          # 5) compute weight
                    int(c)              # 4) convert to int each char
                        for c in x      # 3) parse each char in string 
                    )
        )
    )

def main():
    runner = exercise_runner(_order_weight)
    tests = [
        # ("103 123 4444 99 2000", "2000 103 123 4444 99"),
        ("2000 10003 1234000 44444444 9999 11 11 22 123", 
         "11 11 2000 10003 22 123 1234000 44444444 9999"),
        # ("", ""),
    ]
    for input, expected in tests:
        try:
            raised = True
            result = runner(input)
            assert result == expected, f'{result} != {expected}'
            raised = False
        except AssertionError as ae:
            print(repr(ae))
        # except Exception as e:
            # print(repr(e))
        finally:
            print()
            if raised:
                pass

if __name__ == '__main__':
    main()