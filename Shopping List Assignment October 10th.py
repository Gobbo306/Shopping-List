#-----------------------------
#Shopping List.py
#Dylan Friesen
#October 10th, 2019
#-----------------------------


#---------------Imports-----------------------

import time

#----------Shopping List/Dictionary---------

shopping_list = {}

#----------------Functions---------------------

def add_stuff():
    stop = False
    while stop == False:
        stuff = input("What do you want to add to to your shopping list?").lower()
        if stuff == "stop":
            stop = True
        elif stuff != "stop":
            value = input("How many or description?")
            print("adding", value, stuff)
            shopping_list[stuff] = value
        
def remove_stuff():
    stop = False
    while stop == False:
        stuff = input("What do you want to take off of your shopping list?").lower()
        if stuff == "stop":
            stop = True
        elif stuff != "stop":
            if stuff in shopping_list:
                print("removing", stuff)
                del shopping_list[stuff]
            else:
                print("You don't have that on your list")
                
           
def view_stuff():
    for (stuff, value) in shopping_list.items():
        print("you have", value, stuff, "on your shopping list")
            
def main():
    play = 1
    print("Shopping Time")
    while play == 1:
        print("")
        print("")
        choice = input("Would you like to Add, Remove, View, or Stop?").lower()
        if choice == "add":
            add_stuff()
        elif choice == "remove":
            remove_stuff()
        elif choice == "view":
            view_stuff()
        elif choice == "stop":
            play = 0
            print ("I don't feel so good")
        else:
            ("Sorry, I didn't understand that.")
        
#--------------------Code---------------------
            
main()
    
