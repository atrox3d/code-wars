'''
There is a secret string which is unknown to you. 
Given a collection of random triplets from the string, recover the original 
string.

A triplet here is defined as a sequence of three letters such that each 
letter occurs somewhere before the next in the given string. 
"whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once 
in the secret string.

You can assume nothing about the triplets given to you other than that 
they are valid triplets and that they contain sufficient information to 
deduce the original string. 

In particular, this means that the secret string will never contain 
letters that do not occur in one of the triplets given to you.
'''
def recoverSecret(triplets: list[list]):
    '''
    triplets is a list of triplets from the secrent string. 
    Return the string.
    '''
    flatten = [i for l in triplets for i in l]
    print(f'{flatten = }')
    uniques = list(dict.fromkeys(flatten))
    print(f'{uniques = }')
    
    def to_str(l:list) -> str:
        return ''.join(l)
    
    # loop through unique chars
    done = False
    while not done:
        done = True
        print(f'while | uniques = {to_str(uniques)}')
        for idx in range(len(uniques)):
            # for each char in unique
            char = uniques[idx]
            print(f'    {char, idx = }')
            # scan triplets
            for triplet in triplets:
                print(f'        triplet = {to_str(triplet)}')
                # check only triplets containing char
                if char in triplet:
                    # get position of unique char in triplet
                    for triplet_ndx, triplet_char in enumerate(triplet):
                        control = triplet.index(char)
                        print(f'            {char, control = }')
                        if triplet_char != char:
                            where = uniques.index(triplet_char)
                            print(f'            {triplet_char, where = }')
                            if triplet_ndx < control:
                                if where > idx:
                                    print(f'            ***move*** {triplet_char}')
                                    uniques.remove(triplet_char)
                                    uniques.insert( idx, triplet_char )
                                    done = False
                                    break
                            else:
                                if where < idx:
                                    print(f'            ***move*** {triplet_char}')
                                    uniques.remove(triplet_char)
                                    uniques.insert( idx +1, triplet_char )
                                    done = False
                    # end for triplet
            # end for idx
            print(f'end for | uniques = {to_str(uniques)}')
            print()
            print()
    return to_str(uniques)

if __name__ == '__main__':
    secret = "whatisup"
    triplets = [
    ['t','u','p'],
    ['w','h','i'],
    ['t','s','u'],
    ['a','t','s'],
    ['h','a','p'],
    ['t','i','s'],
    ['w','h','s']
    ]
    
    result = recoverSecret(triplets)
    try:
        assert result == secret, f'{result} != {secret}'
    except AssertionError as ae:
        print(repr(ae))
