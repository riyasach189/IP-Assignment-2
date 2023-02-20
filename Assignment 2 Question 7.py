#COMPLETED
#TESTED

"""
Write a program to create your own address book, in which each entry has: 
Name, address, phone number, and email address. In the program, the address book 
should be a dictionary -  the key of the dictionary has to be the name of the person, 
while the value has to be another dictionary with address, phone, and email as its keys.
Initially, you can assume that people in your directory have unique names. 
Then modify the program to handle multiple persons with same name.
(One way to handle this is to keep name as the key, but the value may be a list of 
dictionaries - one for each person)

Your program should provide the following operations: 
(i) insert a new entry, (ii) delete an entry (iii) find all matching entries 
given a partial name, (iv) find the entry with a phone number or email, and (v) exit. 
When the program exits, it writes the current dictionary in a file (addrbook.txt) 
and when it is started again next time, it reads the existing address book.

Suggestion: To create an address book with some entries, write a small script which 
will call the add function to add a few entries to create a dictionary.

Bonus. Write a program to merge address book of your friend with yours. 
For this, you can store the address book as a json or as a list of dictionary items - 
if both you and your friend agree to the structure, merging will be easier.
"""
import json

address_book = {}

with open("address_book.txt","r") as file:
    input_str = file.read()

address_book = json.loads(input_str)

while(True):
    try:
        user_input = int(input("1: insert a new entry; 2: delete an entry; 3: find all matching entries given a partial name; 4: find the entry with a phone number or email; 5: exit - "))
    except:
        print("Enter a valid number.")
        continue

    if user_input==1:
        name = input("Name: ")
        address = input("Address: ")
        phone_num = input("Phone number: ")
        email = input("Email Address: ")
        entry = [address, phone_num, email]
        
        if name in address_book:

            if any(isinstance(i, list) for i in address_book[name]):
                address_book[name] += [entry]
            else:
                address_book[name] = [address_book[name]] + [entry]

        else:
            address_book[name] = address_book.get(name, []) + entry


    elif user_input==2:
        try:
            name = input("Enter the name whose entry you want to delete: ")
            address_book.pop(name)
        except:
            print("Key does not exist.")

    elif user_input==3:
        s = input("Enter partial name: ")
        find = []
        for i in address_book:
            if s in i:
                find.append({i: address_book[i]})

        print(find)

    elif user_input==4:
        s = input("Enter address, phone number or email: ")
        find = []

        for i in address_book:
            for j in address_book[i]:

                if isinstance(j, str):
                    if s==j:
                        find.append(f"{i}: {address_book[i]}")

                elif isinstance(j, list):
                    for k in j:
                         if s==k:
                            find.append(f"{i}: {address_book[i]}")

        print(find)

    elif user_input==5:
        break

    else:
        print("Invalid Input")

with open("address_book.txt","w") as file:
    entry = str(f"{address_book}")
    output = ""
    for i in entry:
        if i=="'":
            output+='"'
        else:
            output+=i

    file.write(output)