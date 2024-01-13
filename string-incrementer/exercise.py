'''
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to 
the new string.

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
    exp = r'([a-z]+[0-9]*[a-z]+)([0-9+]*)'
    parts = re.match(exp, strng)
    str
    print(strng, parts, parts.groups())
    return parts

if __name__ == '__main__':
        assert increment_string("foobar001") == "foobar002"
        assert increment_string("fo99obar99") == "fo99obar100"
        assert increment_string("") == "1"
        assert increment_string("foo") == "foo1"
        assert increment_string("foobar1") == "foobar2"
        assert increment_string("foobar00") == "foobar01"
        assert increment_string("foobar99") == "foobar100"
        assert increment_string("foobar099") == "foobar100"