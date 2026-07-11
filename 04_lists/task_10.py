"""
Here is a list:

numbers = [5, -2, 10, -8, 7, -1]

Find the sum of only the positive numbers.
"""

numbers = [5, -2, 10, -8, 7, -1]
positive_sum = 0

for number in numbers:
    if number > 0:
        positive_sum +=number

print(f"Sum of positive numbers: {positive_sum}")