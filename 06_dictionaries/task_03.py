"""
Use the dictionary

student = {
    "name": "John",
    "age": 20
}

Add a new key

"city"

with the value

London

After that, print the dictionary.
"""

student = {
    "name": "John",
    "age": 20
}

student['city'] = "London"

print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"City: {student['city']}")