"""
Given the list:

numbers = [5, 3, 8, 1, 9, 2]

Find:

the maximum number;
the minimum number;
the difference between them.

You cannot use max() or min().
"""
numbers = [5, 3, 8, 1, 9, 2]

maximum_number = numbers[0]
minimum_number = numbers[0]

for number in numbers:
    if maximum_number < number:
        maximum_number = number
    
    if minimum_number > number:
        minimum_number = number
    
print(f"Maximum number: {maximum_number}")
print(f"Minimum number: {minimum_number}")
print(f"Difference: {maximum_number - minimum_number}")