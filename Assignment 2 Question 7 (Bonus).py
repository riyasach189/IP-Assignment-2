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

Your  program should provide the following operations: 
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

with open("address_book.txt","r") as file:
    input_str = file.read()

address_book1 = json.loads(input_str)

with open("address_book2.txt","r") as file:
    input_str = file.read()

address_book2 = json.loads(input_str)

address_book_merged = address_book1

for i in address_book2:
    if i in address_book_merged:
        if type(address_book_merged[i])=="list":
            address_book_merged[i] = address_book_merged.get(i, []) + [address_book2[i]]
        else:
            address_book_merged[i] = [address_book_merged[i]] + [address_book2[i]]

    else:
        address_book_merged[i] = address_book_merged.get(i, []) + address_book2[i]

with open("address_book_merged.txt","w") as file:
    file.write(f"{address_book_merged}")