'''
Given two strings a and b, determine if they are isomorphic.

Two strings are isomorphic if the characters in a can be replaced to get b.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: 
a = "odd"
b = "egg"

Output:
true
Example 2:

Input:
a = "foo"
b = "bar"

Output:
false
Example 3:

Input:
a = "abca"
b = "zbxz"

Output:
true
Example 4:

Input:
a = "abc"
b = ""

Output:
false
'''

def csIsomorphicStrings(a, b):
    d1 = {}
    d2 = {}

    for i, char in enumerate(a):
        d1[char] = d1.get(char, []) + [i]
    for i, char in enumerate(b):
        d2[char] = d2.get(char, []) + [i]
    
    return sorted(d1.values()) == sorted(d2.values())
