"""
Use the same dictionary.

Change the age to

21

After that, output the dictionary.
"""

student = {
    "name": "John",
    "age": 20,
    "grade": 95
}

student["age"] = 21

print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Grade: {student['grade']}")