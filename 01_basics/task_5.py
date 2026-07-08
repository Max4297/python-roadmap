"""
Ask the user to enter a number.

Output:

even

or

odd
"""

number = int(input("Enter number:"))

if(number % 2 == 1):
     print("Odd")
else :
    print("Even")