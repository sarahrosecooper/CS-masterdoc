'''
Write a function that takes a string as input and returns that string in reverse order, with the opposite casing for each character within the string.
Examples:
csOppositeReverse("Hello World") ➞ "DLROw OLLEh"
csOppositeReverse("ReVeRsE") ➞ "eSrEvEr"
csOppositeReverse("Radar") ➞ "RADAr"
Notes:
The input string will only contain alpha characters.
[execution time limit] 4 seconds (py3)
[input] string txt
[output] string
'''

def csOppositeReverse(txt):
   txt = txt[::-1].swapcase()
   return txt