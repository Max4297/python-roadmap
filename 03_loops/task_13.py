"""
The user enters a number.

For example:
5

Output:
1
22
333
4444
55555
"""

user_number = int(input("Enter number:"))

for row in range(1, user_number + 1):
    for _ in range(1, row + 1):
        print(row, end="")
    print()