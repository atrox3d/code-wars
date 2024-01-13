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

def recoverSecret(triplets):
    '''
    triplets is a list of triplets from the secrent string. 
    Return the string.
    '''
    # explore_matrix(triplets)            
    # linked_list(triplets)
    # print(*triplets)
    flatten = [i for l in triplets for i in l]
    print(f'{flatten = }')
    # uniques = list(set(flatten))
    uniques = list(dict.fromkeys(flatten))
    print(f'{uniques = }')
    done = False
    # exit()
    while not done:
        # ready to quit loop
        done = True
        # unique =  ['t', 'u', 'p', 'w', 'h', 'i', 's', 'a']
        for unique_idx, char_unique in enumerate(uniques):
            # flatten = ['t', 'u', 'p', 'w', 'h', 'i', 't', 's', 'u', 'a', 't', 's', 'h', 'a', 'p', 't', 'i', 's', 'w', 'h', 's']
            for flatten_idx, char_flatten in enumerate(flatten):
                if char_flatten == char_unique:
                    try:
                        flatten_next_char = flatten[flatten_idx + 1]
                        unique_next_idx = uniques.index(flatten_next_char)
                        if  unique_next_idx < flatten_idx:
                            (uniques[unique_idx], uniques[unique_next_idx]) = (
                                uniques[unique_next_idx], uniques[unique_idx])
                            done = False
                    except IndexError:
                        done = True
        print(f'{char_unique = }, {char_flatten = }, {done = }')
    print(f'{uniques = }')


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
