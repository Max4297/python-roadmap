"""
Create a function:

def average(numbers):

Return the arithmetic mean of the list.
"""

def average(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum/len(numbers)


numbers = [5, 18, 2, 9]

print(average(numbers))