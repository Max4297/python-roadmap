"""
The user enters a sentence.

For example:

cat dog cat bird dog dog

Get

{
"cat": 2,
"dog": 3,
"bird": 1
}
"""

user_sentencу = input("Enter sentence: ")

words = user_sentencу.split()

word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

print(word_counts)