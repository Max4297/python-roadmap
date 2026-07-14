"""
Given the tuple

numbers = (5, 10, 15, 20, 25)

Print the sum of all elements without using sum().
"""

numbers = (5, 10, 15, 20, 25)

total_sum = 0

for number in numbers:
    total_sum +=number

print(f"Sum of all elements: {total_sum}")