#COMPLETED
#TESTED

"""
The canteen in the Institute maintains has a table of prices of items, like:
Samosa: 15
Idli: 30
Maggie: 50
Dosa, 70
…

For the program you have to write, set the menu in your program by this statement 
(feel free to add more items).

menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), 
("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]

Write a program to take a user's order on a terminal and compute the bill. 
First show the menu by printing the menu.  
For ordering an item, the user inputs the item number and the quantity desired 
(e.g. an input can be: 3 1 followed by 1 5 ). 
The program should prompt the user to order more, 
till he/she hits return (without any numbers) - which is the end of the order. 
Print a bill for this order in the form (for the input example above):

Maggie, 1, Rs 50
Samosa, 5, Rs 75


TOTAL, 6 items, Rs 125

"""

menu = [("Samosa", 20), ("Idli", 100), ("Maggi", 25), ("Dosa", 70), ("Tea", 10), ("Coffee", 50), ("Sandwich", 60), ("Cold Drink", 30)]

print("Menu:")
print("")

for i in range(1,len(menu)+1):
    print(str(i)+") ",end='')
    for j in menu[i-1]:
        print(str(j)+" ",end='')
    print("")

order = []
items = []
prices = []

print("If you enter one value, there will be an Index Error.\nIf you enter more than two values, only the first two will be considered.")

while(True):
    item = list(map(int,input("Order (Item Quantity): ").split()))
    if item==[]:
        break

    elif item[0]<1 or item[0]>8:
        print("Invalid Input.")                        #program will return bill of items before invalid input
        continue

    else:
        items.append(item)

print("")        

for i in items:
    try:
        item = i[0]-1
        order.append(menu[item][0])
        prices.append(menu[item][1])

    except IndexError:
        pass

print("Bill: ")

total = 0
total_qt = 0

for i in range(len(order)):
    print(order[i] + ", " + str(items[i][1]) + ", Rs. " + str(prices[i]*items[i][1]))
    total += prices[i]*items[i][1]
    total_qt += items[i][1]

print("")
print("Total: " + str(total_qt) + " Items, Rs. " + str(total))