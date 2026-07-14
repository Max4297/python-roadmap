"""
Given the tuple:

numbers = (5, 10, 15, 20, 25)

Create a new tuple in which each number is increased by 5.
"""

numbers = (5, 10, 15, 20, 25)

new_numbers = []

for number in numbers:
    new_numbers.append(number + 5)

modified_numbers = tuple(new_numbers)

print(modified_numbers)