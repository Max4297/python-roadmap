"""
The user enters numbers.

Input ends when the number 0 is entered.

Store all entered numbers (except 0) in a list.

After input is complete, print the list.
"""

numbers = []

while True:
    number = int(input("Enter number: "))

    if number == 0:
        break
    
    numbers.append(number)

print(numbers)