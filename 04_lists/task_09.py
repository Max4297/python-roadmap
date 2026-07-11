"""
Given the list:

numbers = [10, 15, 8, 21, 14, 7]

Count the number of even and odd numbers.
"""

numbers = [10, 15, 8, 21, 14, 7]

even_counter = 0
odd_counter = 0

for number in numbers:
    if number % 2 == 0:
        even_counter += 1
    else:
        odd_counter +=1

print(f"Even: {even_counter}")
print(f"Odd: {odd_counter}")