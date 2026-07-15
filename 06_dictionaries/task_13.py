"""
Given a dictionary

products = {
"apple": 30,
"banana": 25,
"orange": 40,
"pear": 35
}

Without using max(), find:

Most expensive:
orange
40
"""
products = {
"apple": 30,
"banana": 25,
"orange": 40,
"pear": 35
}

maximum = None
name = ''

for key, value in products.items():
    if maximum is None or value > maximum:
        maximum = value
        name = key


print(name)
print(maximum)
