"""
Create a function that 
determines whether a number is even or not.
"""

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
print(is_even(10))