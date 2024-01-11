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
    import string
    print(f'{message = }')

    def get_first_char_ord(char):
        return ord('a') if char.islower() else ord('A')
    
    def get_alpha_len(char):
        return len(string.ascii_lowercase) if char.islower() else len(string.ascii_uppercase)
    
    def rot13_chr(char, ord_a, alpha_len):

        if char.isalpha():
            ord_char = ord(char)
            ord_r13 = (ord_char - ord_a(char) + 13) % alpha_len(char) + ord_a(char)
            chr_ord13 = chr(ord_r13)
            return chr_ord13
        else:
            return char

    return ''.join(rot13_chr(char, get_first_char_ord, get_alpha_len) for char in message)

def tests():
    assert rot13('test') == 'grfg' 
    assert rot13('test123!') == 'grfg123!'
    assert rot13('Test') == 'Grfg'

tests()