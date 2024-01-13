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
def explore_matrix(triplets):
    for y, triplet in enumerate(triplets):
        print(triplet, '*')
        search = triplets[:y] + triplets[y+1:]
        # for _ in search:
        #     print(_)
        # print()
        for x, char in enumerate(triplet):
            line: list
            for line in search:
                if char in line:
                    print(char, line, line.index(char))

def linked_list(triplets):
    from dataclasses import dataclass
    @dataclass
    class Node:
        value: str
        prev: 'Node' = None
        next: 'Node' = None
    
    root = None
    for y, triplet in enumerate(triplets):
        for x, char in enumerate(triplet):
            if not root:
                root = Node(char)
                node = root
            else:
                node = root
                while node.value != char and node.next:
                    node = node.next
                if node.value != char:
                    node.next = Node(char)
                    node.next.prev = root

    node = root
    values = []
    while node:
        values.append(node.value)
        node = node.next
    print(values)

def recoverSecret(triplets: list[list]):
    '''
    triplets is a list of triplets from the secrent string. 
    Return the string.
    '''
    import time
    import logging

    logging.basicConfig(level='DEBUG')
    logger = logging.getLogger('test')
    # explore_matrix(triplets)            
    # linked_list(triplets)
    # print(*triplets)
    flatten = [i for l in triplets for i in l]
    print(f'{flatten = }')
    # uniques = list(set(flatten))
    uniques = list(dict.fromkeys(flatten))
    print(f'{uniques = }')
    # done = False
    # exit()
    # while not done:
        # ready to quit loop
        # done = True
        # flatten = ['t', 'u', 'p', 'w', 'h', 'i', 't', 's', 'u', 'a', 't', 's', 'h', 'a', 'p', 't', 'i', 's', 'w', 'h', 's']
        # unique =  ['t', 'u', 'p', 'w', 'h', 'i', 's', 'a']
        # triplets = [
        # ['t','u','p'],
        # ['w','h','i'],
        # ['t','s','u'],
        # ['a','t','s'],
        # ['h','a','p'],
        # ['t','i','s'],
        # ['w','h','s']
        # ]
    
    def to_str(l:list) -> str:
        return ''.join(l)
    
    # loop through unique chars
    modified = False
    done = False
    while not done:
        done = True
        print(f'while | uniques = {to_str(uniques)}')
        time.sleep(2)
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
                                    modified = True
                                    done = False
                                    break
                            else:
                                if where < idx:
                                    print(f'            ***move*** {triplet_char}')
                                    uniques.remove(triplet_char)
                                    uniques.insert( idx +1, triplet_char )
                                    modified = True
                                    done = False
                    # end for triplet
            # end for idx
            print(f'end for | uniques = {to_str(uniques)}')
            print()
            print()
    return to_str(uniques)
                # exit()
                                
                        # try:
                        #     # try to get previous char in triplet
                        #     triplet_next_char = triplet[triplet_unique_idx + 1]
                        #     # check the relative position inside uniques
                        #     next_idx = uniques.index(triplet_next_char)
                        #     # prev char should be before current char
                        #     print(f'{            triplet_next_char, next_idx =}')
                        #     if next_idx < unique_idx:
                        #         # change place
                        #         print(f'         move {triplet_next_char}')
                        #         uniques.remove(triplet_next_char)
                        #         uniques.insert(
                        #             unique_idx -1,
                        #             triplet_next_char
                        #         )
                        #         modified = True
                        #         done = False
                        #         break
                        # except IndexError:
                        #     logger.exception('IndexError')
                        #     uniques.insert(
                        #         unique_idx,
                        #         triplet_next_char
                        #     )
                        #     modified = True
                        #     done = False
                        #     break                                    
    #             if modified:
    #                 break
    # print(f'END {uniques = }')


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
