'''
Given a string of words, return the length of the shortest word(s).
Notes:
The input string will never be empty and you do not need to validate for different data types.
[execution time limit] 4 seconds (py3)
[input] string input_str
[output] integer
'''

def csShortestWord(input_str):
  
   if " " in input_str:
       text = input_str.split(" ")
   elif "\t" in input_str:
       text = input_str.split("\t")
   else:
       return len(input_str)
  
   shortestLength = 999999
 
   for w in text:
       if len(w) < shortestLength:
           shortestLength = len(w)
          
   return shortestLength