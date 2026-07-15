"""
Use the dictionary

student = {
    "name": "John",
    "age": 20,
    "grade": 95
}

Output

key -> value
"""

student = {
    "name": "John",
    "age": 20,
    "grade": 95
}

for key in student:
    print(f"{key} -> {student[key]}")