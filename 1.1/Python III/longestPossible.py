'''
Given two strings that include only lowercase alpha characters, str_1 and str_2, write a function that returns a new sorted string that contains any character (only once) that appeared in str_1 and str_2.

Examples:
Understand:

csLongestPossible("aabbbcccdef", "xxyyzzz") -> "abcdefxyz"
csLongestPossible("abc", "abc") -> "abc"
csLongestPossible("a", "aeeddf") -> "aedf"

Plan:
Initialize an empty string to store our outputs. 

[execution time limit] 4 seconds (py3)

[input] string str_1

[input] string str_2

[output] string

'''

def csLongestPossible(str_1, str_2):
    
    uniString1 = set(str_1)
    uniString2 = set(str_2)
    uniString1.update(uniString2)
    

    finalString = list(uniString1)
    finalString.sort()

    return "".join(finalString)

    


