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
    result = list(dict.fromkeys(flatten))
        
    # loop through unique chars
    done = False
    while not done:
        done = True
        for idx in range(len(result)):
            # for each char in unique
            char = result[idx]
            # scan triplets
            for triplet in triplets:
                # check only triplets containing char
                if char in triplet:
                    # get position of unique char in triplet
                    for triplet_ndx, triplet_char in enumerate(triplet):
                        control = triplet.index(char)
                        # skip current char
                        if triplet_char != char:
                            #
                            # controls wether the chars in the triplets
                            # are relatively before or after the current char
                            # if they are not positioned relatively in the list
                            # as in the triplet (a sort of guide) the move them
                            #
                            where = result.index(triplet_char)
                            if triplet_ndx < control:
                                if where > idx:
                                    result.remove(triplet_char)
                                    result.insert( idx, triplet_char )
                                    done = False
                            else:
                                if where < idx:
                                    result.remove(triplet_char)
                                    result.insert( idx +1, triplet_char )
                                    done = False
                    # end for triplet
            # end for idx
    return ''.join(result)

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
