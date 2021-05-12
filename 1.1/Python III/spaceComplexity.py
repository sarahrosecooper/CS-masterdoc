''' 
Using Big O notation, what is the correct classification of space complexity for the function below?
'''

def do_a_couple_things(n):
    my_list = []
    my_second_list = [0] * 26

    for _ in range(n):
        my_list.append("lambda")
        print(my_second_list[n % 25])

        return my_list