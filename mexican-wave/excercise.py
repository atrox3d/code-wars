'''
Task
In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 
Rules
 1.  The input string will always be lower case but maybe empty.

 2.  If the character in the string is whitespace then pass over it 
 as if it was an empty seat
Example
wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
'''

def wave(people):
    waved = [
                people[0:i] + c.upper() + people[i+1:]
                for i, c in enumerate(people)
                if not c.isspace()
             ]
    return waved

print(wave('two words'))