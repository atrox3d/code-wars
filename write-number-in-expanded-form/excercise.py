'''
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
'''

def expanded_form(num):
    print(f'{num = }')
    def string_version(num):
        strnum = str(num)
        ps = list([10**p for p in range(len(strnum))])[::-1]
        digits = []
        for n, p in zip(strnum, ps):
            if n := int(n):
                digits.append(n*p)
        print(digits)
        result = ' + '.join(map(str, digits))
        print(result)
        return result
    
    return string_version(num)




for n in 12, 42, 70304:
    expanded_form(n)