"""
The user enters a password.
As long as the password is not

python123

the program must ask them to enter it again.
When the correct password is entered:
Access granted
"""

correct_password = 'python123'

user_password = ""

while user_password != correct_password:
    user_password = input("Enter password:")

print("Access granted")