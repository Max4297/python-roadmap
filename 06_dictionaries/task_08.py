"""
Given the dictionary:

students = {
    "John": 85,
    "Alice": 92,
    "Bob": 78,
    "Kate": 95
}

The user enters a name.

If the student exists:

Grade: 92

If not:

Student not found.
"""

students = {
    "John": 85,
    "Alice": 92,
    "Bob": 78,
    "Kate": 95
}

user = input("Enter name: ")

if user in students:
    print(f"Grade: {students[user]}")
else:
    print("Student not found.")