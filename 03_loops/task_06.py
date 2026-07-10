"""
The user enters a number N.

Find the sum of all numbers from 1 to N.
"""

user_number = int(input("Enter number:"))
total_sum = 0

for number in range(1, user_number + 1):
    total_sum += number
    
print(total_sum)