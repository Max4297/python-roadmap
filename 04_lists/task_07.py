"""
The user enters 5 numbers.

Save them in a list.

Then display the list.
"""

user_numbers = list()

for _ in range(5):
    number = int(input("Enter number:"))
    user_numbers.append(number)

print(user_numbers)