'''
You will be given a number and you will need to return it as a string in 
Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
'''

def expanded_form(num):
    '''
    contains various versions of the same algorithm
    tested against each other
    the purpose is learning more and more without deleting old code
    '''
    
    def string_version(num):
        '''
        decompose number as string
        '''
        strnum = str(num)
        reverse_powers_of_ten = [10**p for p in range(len(strnum))][::-1]
        expands = []
        for char, power in zip(strnum, reverse_powers_of_ten):
            if digit := int(char):
                expands.append(digit*power)
        result = ' + '.join(map(str, expands))
        return result
    
    def int_version(num):
        '''
        decompose number as integer
        '''
        expands = []
        power = 1
        while num:
            m = num % 10
            num = num // 10
            if m:
                expands.append(m*power)
            power *= 10
        return ' + '.join(map(str, expands[::-1]))
    
    def string_enumerate_version(num):
        '''
        decompose number as string
        compute powers of 10 via enumerate
        '''
        expands = []
        for p, n in enumerate(str(num)[::-1]):
            digit = 10**p * int(n)
            if digit:
                expands.append(digit)
        return ' + '.join(map(str, expands[::-1]))
    
    def int_enumerate_version(num):
        '''
        decompose number as integer
        compute powers of 10 via enumerate
        '''
        pow_num_rest = enumerate((num%10, num:=num//10) for n in range(len(str(num))))
        expands = []
        for power, (number, _) in list(pow_num_rest)[::-1]:
            digit = number * 10**power
            if digit:
                expands.append(digit)
        return ' + '.join(map(str, expands))

    def twoliner(num):
        '''
        same as above, less readable, just for fun
        '''
        pow_num_rest = enumerate((num%10, num:=num//10) for n in range(len(str(num))))
        digits = [str(number * 10**power) for power, (number, _) in pow_num_rest if number][::-1]
        return ' + '.join(digits)
    

    def autotest(num):
        '''
        test each version against the others
        '''
        sv = string_version(num)
        iv = int_version(num)
        sev = string_enumerate_version(num)
        iev = int_enumerate_version(num)
        tl = twoliner(num)
        assert sv == iv == sev == iev == tl, \
            ValueError(f'{sv!r} != {iv!r} != {sev!r} != {iev!r} != {tl!r}')
        
        # return whichever you like
        return tl

    return autotest(num)

if __name__ == '__main__':
    for n in 12, 42, 70304:
        print(expanded_form(n))