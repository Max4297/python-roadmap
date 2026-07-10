"""
Create a list

numbers = [4, 9, 1, 7, 3]

Find the minimum element without using min().
"""

numbers = [4, 9, 1, 7, 3]

minimum = numbers[0]

for number in numbers:
    if number < minimum:
        minimum = number
print(minimum)