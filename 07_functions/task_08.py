"""
Create a function:

def list_sum(numbers):

It should return the sum of all elements in the list.

You cannot use sum().
"""

numbers = [10, 20, 30]

def list_sum(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum

print(list_sum(numbers))