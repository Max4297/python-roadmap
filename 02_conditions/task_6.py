""""
Mini-calculator. 
The user enters two numbers and an operation (+, -, *, /). 
The program performs the required operation. 
Make sure to handle division by zero.
"""

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
operation = input("Enter operation(+, -, *, /): ")
result = 0;

match operation:
    case "+":
        result = first_number + second_number

    case "-":
        result = first_number - second_number

    case "*":
        result = first_number * second_number

    case "/":
        if second_number == 0:
            result = "Division by zero is not allowed."
        else:
            result = first_number / second_number

    case _:
        result = "Unknown operation."		
                
print(result)