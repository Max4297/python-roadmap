"""
Using nested loops, output

1
12
123
1234
12345
"""

for row in range(1, 6):
    for column in range(1, row + 1):
        print(column, end="")
    print()