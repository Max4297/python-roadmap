"""
Given a dictionary

grades = {
"John": 90,
"Kate": 80,
"Alice": 95,
"Bob": 75
}

Calculate the average grade without sum().
"""

grades = {
"John": 90,
"Kate": 80,
"Alice": 95,
"Bob": 75
}

total_sum = 0

for grade in grades.values():
    total_sum += grade

print(f'Average grade: {total_sum/len(grades)}')