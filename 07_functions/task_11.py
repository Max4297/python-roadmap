"""
Create a function:

def contains(numbers, value):

It should return

True

if the number is in the list,

and

False

if it is not.

Do not use the `in` operator.
"""

def contains(numbers, value):
      counter = 0
      while counter < len(numbers):
        if numbers[counter] == value:
            return True
        else:
            counter += 1
      return False
    
numbers = [5, 18, 2, 9]

print(contains(numbers, 10))