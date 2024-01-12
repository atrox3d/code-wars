'''
Write a function named first_non_repeating_letter that takes a string input,
and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', 
since the letter t only occurs once in the string, and occurs first in 
the string.

As an added challenge, upper- and lowercase letters are considered the 
same character, but the function should return the correct case for the
initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, 
it should return an empty string ("") or None -- see sample tests.
'''
def first_non_repeating_letter(s):
    print(f'{s = }')
    return s


if __name__ == '__main__':
    tests = dict(
                moonmen='r',
                aaa='',
                sTreSS='T'
    )
    for value, expected in tests.items():
        result = first_non_repeating_letter(value)
        try:
            assert result == expected, f'{result} != {expected}'
        except AssertionError as ae:
            print(repr(ae))