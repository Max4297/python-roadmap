"""Password check. 
The user enters a password. 
If the length is less than 8 characters, 
report that the password is too short; 
otherwise, report that the length is acceptable. 
For now, we are checking only the length.
"""

user_password = input("Enter user password:")

if len(user_password) < 8:
    print("Password is too short")
else:
    print("Password length is acceptable.")