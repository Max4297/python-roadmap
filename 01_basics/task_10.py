"""
Determining the time of day. 
The user enters an hour (from 0 to 23). 
The program outputs:

5–11 — morning;
12–17 — day;
18–22 — evening;
23–4 — night.
If a number outside this range is entered, report an error.
"""

user_hour = int(input("Enter an hour(from 0 to 23): "))

if user_hour < 0 or user_hour > 23:
    print("Error")
elif user_hour <= 4:
    print("Night")
elif user_hour <= 11:
    print("Morning")
elif user_hour <= 17:
    print("Day")
elif user_hour <= 22:
    print("Evening")
else:
    print("Night")