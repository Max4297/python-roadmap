"""
Here is a list:

numbers = [5, 10, 15, 20, 25]

Create a new list in which each number is increased by 5.
"""

numbers = [5, 10, 15, 20, 25]

increased_numbers =[]
addend = 5

for number in numbers:
    increased_numbers.append(number+addend)

print(increased_numbers)