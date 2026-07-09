"""
Ask the user to enter a number.

Determine if it is:

positive

negative

or zero
"""

number = int (input ('Please enter number:'))

if ( number > 0) :
    print('positive')
elif ( number < 0 ):
    print('negative')
else:
    print('Number is 0')