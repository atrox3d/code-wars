'''
ROT13 is a simple letter substitution cipher that replaces a letter 
with the letter 13 letters after it in the alphabet. 
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered 
with Rot13. If there are numbers or special characters 
included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted, 
like in the original Rot13 "implementation".

Please note that using encode is considered cheating.'''

def rot13(message):
    print(f'{message = }')

    def rot13_chr(char):
        asc = ord(char)
        orda = ord('a')
        offset = asc - orda
        print(f'{char   = }')
        print(f'{asc    = }')
        print(f'{orda   = }')
        print(f'{offset = }')

        r13 = asc + 13
        r13_offset = r13 - orda
        print(f'{r13      = }')
        print(f'{chr(r13) = }')

        print(f'{r13_offset      = }')
        print(f'{chr(r13_offset) = }')
        
        print(f'{r13_offset % 26      = }')
        print(f'{chr(r13_offset % 26) = }')
        
        print(f'{ord("g")              = }')
        print(f'{ord("g") - ord(char)  = }')

        x = (ord(char) - orda + 13) % 26 + orda
        print(f'{x, chr(x) = }')


    # for char in message:
        # rot13_chr(char)
    
    rot13_chr(message[0])
print(rot13('test'))