"""
Create a list

numbers = [4, 9, 1, 7, 3]

Find the maximum element without using max().
"""

numbers = [4, 9, 1, 7, 3]

maximum = numbers[0]
for number in numbers:
    if number > maximum:
        maximum = number
print(maximum)