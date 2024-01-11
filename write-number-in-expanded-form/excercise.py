'''
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
'''

def expanded_form(num):
    def string_version(num):
        '''
        decompose number as string
        '''
        strnum = str(num)
        reverse_powers_of_ten = [10**p for p in range(len(strnum))][::-1]
        digits = []
        for char, power in zip(strnum, reverse_powers_of_ten):
            if digit := int(char):
                digits.append(digit*power)
        result = ' + '.join(map(str, digits))
        return result
    
    def int_version(num):
        print(f'{num = }')
        digits = []
        power = 1
        while num:
            m = num % 10
            num = num // 10
            print(f'{m, num, power = }')
            if m:
                digits.append(m*power)
            power *= 10
        print(f'{digits = }')
        
        return ' + '.join(map(str, digits[::-1]))


    sv = string_version(num)
    iv = int_version(num)

    assert sv == iv, ValueError(f'{sv!r} != {iv!r}')

    return iv



for n in 12, 42, 70304:
    print(expanded_form(n))