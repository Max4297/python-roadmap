
"""
Write a program that:

asks for the user's name;

asks for their age;

outputs:

Hello, Maxim!

You are 29 years old.

In a year, you will be 30.
"""

name = input('Enter your name: ');
age = input('Enter your age: ');
print(
'\nHello', name,'!',
'\nYou are', age,'.',
'\nIn a year, you will be', int(age)+1 ,'.');