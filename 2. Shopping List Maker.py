grocery_list = []

while True:
    view = input("\n View the grocery list? \n Enter 'End' at any time to finish. \n >> ")
    if view == "Yes" or view == "yes" or view == "Sure" or view == "Please" or view == "View":
        if not grocery_list:
            print("The grocery list is empty.")
        else:
            print(grocery_list)
    elif view == "End" or view == "end" or view == "Finish" or view == "finish": #End could be made into its own function
            if not grocery_list:
                print("The grocery list is empty.")
                break
            else:
                print("Here is your grocery list: ", grocery_list)
                break
        
        
    a_r = input("\n Add or remove an item to the grocery list? \n >> ")
    if a_r == "End" or a_r == "end" or a_r == "Finish" or a_r == "finish": #End function here
        if not grocery_list:
            print("The grocery list is empty.")
            break
        else:
            print("Here is your grocery list: ", grocery_list)
            break

    z = input("\n Enter an item: \n >> ")
    if z == "End" or z == "end" or z == "Finish" or z == "finish": #End function here
        if not grocery_list:
            print("The grocery list is empty.")
            break
        else:
            print("Here is your grocery list: ", grocery_list)
            break

    def add():
        grocery_list.append(z)

    def remove():
        if not grocery_list:
            print("The grocery list is empty; you cannot remove anything.")
        elif z not in grocery_list:
            print(z,"is not in the grocery list.")
        else:
            grocery_list.remove(z)

   
    if a_r == "Add" or a_r == "add":
        add()
    
    elif a_r == "Remove" or a_r == "remove":
        remove()
    
    else:
        a_r = input("\n Command not recognized; try again. Add or remove an item to the grocery list? \n >> ")

    
   

