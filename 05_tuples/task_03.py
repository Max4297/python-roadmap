"""Given the tuple

numbers = (8, 3, 12, 1, 9)

Find the maximum element without using max().
"""

numbers = (8, 3, 12, 1, 9)

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number
print(f"Maximum: {maximum}")