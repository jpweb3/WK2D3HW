#1) Build a Shopping Cart 

#You can use either lists or dictionaries. The program should have the following capabilities:

#1) Takes in input 
#2) Stores user input into a dictionary or list 
#3) The User can add or delete items 
##4) The User can see current shopping list 
#5) The program Loops until user 'quits' 
#6) Upon quiting the program, print out all items in the user's list #

def storeinfo():
    cart = {}

    def add():
        item = input("What would you like to add to your cart? ")
        quan = input("How many? ")
        cart[item] = quan
        print(f"{item} has been added  to your cart.")

    def show():
        print(cart)

    while True:
        menu = input("Welcome to my  shop!  Show/Add/Delete or Quit?  ")
        
        if menu.lower() == "quit":
            show()
            break

        elif menu.lower()  ==  "add":
            add()

storeinfo()


#2) Set Practice
#Remove all duplicates from the following list

nums_list = [1, 1, 1, 2, 2, 3, 5, 6, 4, 12, 11, 12, 12, 14, 16, 16, 16, 1, 1, 1, 2, 2]

my_set = set(nums_list)
print(my_set)

#3) Out put the intersection of the following the following sets.

set1 = {20, 24, 26, 27}
set2 = {26, 35, 63, 27}

set3  = set2.intersection(set1)
print(set3)

#4) Output the difference between the following sets

set3 = {100, 65, 89, 200}
set4 = {65, 103, 54, 200}

diff = set3  -  set4

print(diff)