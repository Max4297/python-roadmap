"""
Create a function

multiplication_table(number)

that outputs the multiplication table for the given number.
"""

def multiplication_table(number):
    counter = 1
    while counter <= 10:
        print(f"{number} x {counter} = {number * counter}")
        counter += 1
    
multiplication_table(7)