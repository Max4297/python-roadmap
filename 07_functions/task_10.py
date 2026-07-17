"""
Create a function:

def count_even(numbers):

Return the count of even numbers.
"""

def count_even(numbers):
    counter = 0
    for number in numbers:
        if number % 2 == 0: 
            counter +=1
    return counter

numbers = [5, 18, 2, 9]

print(count_even(numbers))