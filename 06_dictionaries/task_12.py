"""
Create a dictionary

phone_book = {}

Menu:

1. Add contact
2. Find contact
3. Show all contacts
4. Delete contact
5. Update phone number
0. Exit


Contact:

Name
Phone

Example:

{
"John": "+380991112233",
"Kate": "+380931234567"
}
"""

phone_book = {}

while True:
    print("""
Menu
    
1. Add contact
2. Find contact
3. Show all contacts
4. Delete contact
5. Update phone number
0. Exit""")

    user_choice = input(f"Make choice: \n")
    
    match user_choice:
        case '0':
            print("Good bye")
            break
        case '1':
            name = input("Enter name: ")
            number = input("Enter number:")
            phone_book[name] = number
            print("Contact added.")
        case '2':
            name = input("Enter name: ")
            if name in phone_book:
                print(phone_book[name])
            else:
                print("Contact not found")
        case '3':
            if phone_book:
                for name, phone in phone_book.items():
                    print(f"{name}: {phone}")
            else:
                print('Phone book empty')
        case '4':
            name = input('Enter name for delete: ')
            if name in phone_book:
                del phone_book[name]
                print(f"Contact {name} was deleted.")
            else:
                print("Contact not found.")
        case '5':
            name = input('Enter name for update: ')
            number = input("Enter new number:")
            if name in phone_book:
                phone_book[name] = number
                print("Contact updated.")
            else:
                print("Contact not found.")
        case _:
            print("Invalid option.")