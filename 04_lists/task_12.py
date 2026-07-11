"""
The user enters 10 numbers.

Store them in a list.

Then, output:

the sum of all the numbers;
the arithmetic mean.

You cannot use `sum()`.
"""

numbers = []
total_sum = 0

while len(numbers) < 10:
    numbers.append(int(input("Enter number:")))

for number in numbers:
    total_sum +=number

arithmetic_mean = total_sum / len(numbers)

print(f"Sum of all numbers: {total_sum}")
print(f"Arithmetic mean: {arithmetic_mean}")