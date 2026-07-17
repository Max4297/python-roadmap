"""
Create a function:

def list_max(numbers):

Return the maximum element of the list.

You cannot use max().
"""

def list_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

numbers = [5, 18, 2, 9]

print(list_max(numbers))