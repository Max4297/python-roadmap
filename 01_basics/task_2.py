"""
Ask the user to enter two numbers.

Output:
Sum
Difference
Product
Quotient
"""

first_number = int(input ("Please enter first number:"))
second_number = int(input ("Please enter second number:"))

print(f"Sum: {first_number + second_number}")
print(f"Difference: {first_number - second_number}")
print(f"Product: {first_number * second_number}")

if(second_number == 0):
    print("Quotient: error (division by zero)")    
else:
    print(f"Quotient: {first_number / second_number}")