'''
Given a string, return a new string with all the vowels removed.

Examples:
csRemoveTheVowels("Lambda School is awesome!") -> "Lmbd Schl s wsm!"
Notes:
For this challenge, "y" is not considered a vowel.
[execution time limit] 4 seconds (py3)
[input] string input_str
[output] string

'''

def csRemoveTheVowels(input_str):
   newstr = input_str
   vowels = ('a', 'e', 'i', 'o', 'u', 'I', 'O', 'U', 'A', 'E')
   for x in input_str:
       if x in vowels:
           newstr = newstr.replace(x,"")
 
   return newstr