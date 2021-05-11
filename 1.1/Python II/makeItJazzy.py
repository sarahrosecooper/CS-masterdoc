'''
Create a function that concatenates the number 7 to the end of every chord in a list. If a chord already ends with a 7, do not add another 7.
Examples:
csMakeItJazzy(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]
csMakeItJazzy(["G", "F7", "C"]) ➞ ["G7", "F7", "C7"]
csMakeItJazzy(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]
csMakeItJazzy(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]
csMakeItJazzy([]) ➞ []
Notes:
Return an empty list if the given list is empty.
You can expect all the tests to have valid chords.
[execution time limit] 4 seconds (py3)
[input] array.string chords
[output] array.string
'''

def csMakeItJazzy(chords):
   returnedChord = []
   for c in chords:
       if c.endswith("7"):
           returnedChord.append(c)
       else:
           c += str(7)
           returnedChord.append(c)
          
   return returnedChord