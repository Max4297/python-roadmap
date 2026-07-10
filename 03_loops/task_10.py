"""
Using nested loops, output

*
**
***
****
*****
"""
    
for row in range(5):
    for column in range(0, row + 1):
        print('*', end="")
    print()