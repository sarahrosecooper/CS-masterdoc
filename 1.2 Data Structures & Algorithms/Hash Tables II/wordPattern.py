"""
Given a pattern and a string a, find if a follows the same pattern.

Here, to "follow" means a full match, such that there is a one-to-one correspondence between a letter in pattern and a non-empty word in a.

Example 1:

Input:
pattern = "abba"
a = "lambda school school lambda"

Output: true
Example 2:

Input:
pattern = "abba"
a = "lambda school school coding"

Output:
false
Example 3:

Input:
pattern = "aaaa"
a = "lambda school school lambda"

Output: false
Example 4:

Input:
pattern = "abba"
a = "lambda lambda lambda lambda"

Output: false
Notes:

pattern contains only lower-case English letters.
a contains only lower-case English letters and spaces ' '.
a does not contain any leading or trailing spaces.
All the words in a are separated by a single space.
[execution time limit] 4 seconds (py3)

[input] string pattern

[input] string a

[output] boolean


"""
def csWordPattern(pattern, a)
    words = a.split(" ")

    if not len(words) == len(pattern):
        return False
    
    mapping = dict() 

    for char in range(len(words)):
        if pattern[char] not in mapping:
            if words[char] not in mapping.values():
                mapping[pattern[char]] = words[char]
            else:
                return False
        else:
            if not mapping[pattern[char]] == words[char]:
                return False
    return True