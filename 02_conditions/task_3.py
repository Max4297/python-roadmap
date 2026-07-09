"""
Discount calculator. 
The user enters the price of the item. 
If the amount is over 5,000 UAH, the discount is 10%; 
if over 10,000 UAH, it is 15%; otherwise, there is no discount.
Display the final price.
"""

start_price = float(input("Enter price of the item:"))

if start_price > 10000:
    discount = 0.15
    final_price = start_price * (1 - discount)
elif start_price > 5000:
    discount = 0.10
    final_price = start_price * (1 - discount)
else:
    final_price = start_price
4
print(f"Final price: {final_price:.2f} UAH")