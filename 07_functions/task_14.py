"""
Create a function:

def count_positive(numbers):

Return the number of positive elements.

"""

def count_positive(numbers):
    counter = 0
    for number in numbers:
        if number > 0:
            counter +=1
    return counter


numbers = [5, 18, -2, -10, -20]

print(count_positive(numbers))