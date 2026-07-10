"""
The user enters a number.

Determine whether it is a prime number.
"""

user_number = int(input("Enter number:"))


is_prime = True

if user_number <= 1:
    is_prime = False
elif user_number == 2:
    is_prime = True
elif user_number % 2 == 0:
    is_prime = False
else:
    i = 3
    while i * i <= user_number:
        if user_number % i == 0:
            is_prime = False  
            break             
        i += 2                

if is_prime:
    print(f"Number {user_number} — prime!")
else:
    print(f"Number {user_number} — composite!")