"""
Using nested loops, output

*****
****
***
**
*
"""
    
for row in range(5):
    for column in range(5, row,-1):
        print('*', end="")
    print()