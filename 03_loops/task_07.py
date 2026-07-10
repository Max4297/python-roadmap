"""
The user enters a number.

Display the multiplication table for that number.
"""

user_number = int(input("Enter number:"))

counter = 0
while counter <= 9:
    counter += 1
    print(f"{user_number} * {counter} = {counter*user_number}")