'''
Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum) of all integers in the range (except integers that contain the digit 5).
Examples:
csAnythingButFive(1, 5) -> 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)
csAnythingButFive(1, 9) -> 1, 2, 3, 4, 6, 7, 8, 9 -> 8
csAnythingButFive(4, 17) -> 4,6,7,8,9,10,11,12,13,14,16,17 -> 12
Notes:
The output can contain the digit 5.
The start number will always be less than the end number (both numbers can also be negative).
[execution time limit] 4 seconds (py3)
[input] integer start
[input] integer end
[output] integer
'''

def csAnythingButFive(start, end):
   initStart = start
   finalEnd = end
   counter = 0
   finalEnd = finalEnd + 1
   # finalEnd = 17, change it to 18
 
   numList = list(range(initStart, finalEnd))
 
   for d in numList:
       if "5" str(d):
           counter = counter + 1
  
   totalCount = len(numList)
 
   result = int(totalCount) - int(counter)
 
   return result