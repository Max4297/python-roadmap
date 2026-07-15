"""
The user enters a word.

For example:

banana

Get dictionary

{
'b': 1,
'a': 3,
'n': 2
}
"""

user_word = input("Enter word: ")

letters = {}

for letter in user_word:
    if letter not in letters:
        letters[letter] = 1
    else:
        letters[letter] = letters[letter] +1

print(letters)