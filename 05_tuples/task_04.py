"""
Given the tuple

numbers = (8, 3, 12, 1, 9)

Find the minimum element without using min().
"""

numbers = (8, 3, 12, 1, 9)

minimum = numbers[0]

for number in numbers:
    if number < minimum:
        minimum = number
print(f"Minimum: {minimum}")