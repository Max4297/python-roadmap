"""
Given the tuple

numbers = (10, 20, 30, 40, 50)

Count the number of elements without using len().
"""

numbers = (10, 20, 30, 40, 50)
counter = 0

for number in numbers:
    counter +=1

print(f"Number of elements: {counter}")