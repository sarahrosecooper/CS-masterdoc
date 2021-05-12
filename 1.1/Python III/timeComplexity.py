def do_lots_of_things(items):
    last = len(items) -1
    print(items[last])

    middle = len(items) / 2
    i = 0
    while i < middle:
        print(items[i])
        i += 1

    for num in range(100):
        print(num)

''' 
Using Big O notation, what is the correct classifiction of time complexity for the function below?

Answer = O(n) ??
'''


