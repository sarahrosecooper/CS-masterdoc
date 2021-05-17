'''

Given a string, write a function that removes all duplicate words from the input. The string that you return should only contain the first occurrence of each word in the string.

Examples:

`csRemoveDuplicateWords("alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta") -> "alpha bravo golf delta"
`csRemoveDuplicateWords("my dog is my dog is super smart") -> "my dog is super smart"
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] string
'''

def csCheckPalindrome(input_str):
    origList = input_str.split()
    newList = []
    newString = ""

    for x in origList:
        if x not in newList:
            newList.append(x)
            newString += " " + x

    return newString.strip()