'''
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, 
    the number should be incremented by 1.
If the string does not end with a number. 
the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be 
considered.
'''
def increment_string(strng):
    import re
    
    # exp = r'([a-z]+[0-9]*[a-z]+)([0-9+]*)'
    
    # exp = r'(.+(?!.*\d))([0-9+]*)'
    # exp = r'(.+)(?!.*\d)(\d*)'
    # exp = r'(.*)(?:\D|^)(\d+)'
    # exp = r'(\d+)\D*$'
    # exp = r'^(.*)(\d*)$'

    exp = r'(.*)(?<=\D)(\d+)'
    exp = r'(.*)(?<=\D)(\d*)'
    
    print(f'{strng = }')
    print(f'{exp   = }')
    match = re.match(exp, strng)
    if match:
        # print(f'{match.groups() = }')
        # print(f'{type(match.groups()) = }')
        # print(f'{len(match.groups()) = }')

        str_part, int_part = match.groups() 
    else:
        str_part, int_part = ("", "")

    print(f'{str_part = }')
    print(f'{int_part = }')

    len_int_part = len(int_part)
    int_part = int(int_part) if int_part else 0
    result = f'{str_part}{int_part + 1:0{len_int_part}}'
    print(f'------->{result = }')
    return result

if __name__ == '__main__':
    tests = [
        ("foobar001", "foobar002"),
        ("foobar1", "foobar2"),
        ("foobar00", "foobar01"),
        ("foobar99", "foobar100"),
        ("foobar099", "foobar100"),
        ("fo99obar99", "fo99obar100"),
        ("", "1"),
        ("30UiN959672340582688^][28{'F064)NLDC'59\v\"R::PL61800000000087637", 
            "30UiN959672340582688^][28{'F064)NLDC'59\v\"R::PL61800000000087638"),
        ("foo", "foo1"),
    ]
    for _input, expected in tests:
        try:
            print(f'running increment_string({_input})')
            res = increment_string(_input)
            assert res == expected, f'{res!r} != {expected!r}'
            print('[               OK                  ]')
        except AssertionError as ae:
            print(repr(ae))
            # exit()
        finally:
            print()