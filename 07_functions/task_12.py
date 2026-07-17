"""
Create a function:

def reverse_list(numbers):

It should return a new list in reverse order.

Do not use:

reverse()
reversed()
[::-1]

For example:
"""


def reverse_list(numbers):

    counter = len(numbers)
    new_list = []
    
    while counter != 0:
        new_list.append(numbers[counter-1])
        counter -=1

    return new_list


numbers = [5, 18, 2, 9]

print(reverse_list(numbers))