import math
grades = []
def average():
    while True:
        print("\n Enter 'End' to finish and see the average at any time.")
        z = input(" Enter in the next grade: \n >> ")

        if z  == "End" or z == "end" or z == "Finish" or z == "finish": #End could be made into its own function
            if not grades:
                print("The grades list is empty.")
                break
            else:
                print("Here is your list of grades: ", grades)
                print("Here is the average: ", avg)
                break
        else:
            a = int(z)
            if a < 0:
                print("Student cannot receive less than a 0. Bad teacher.")  
                a = 0
                grades.append(a)
            else:
                grades.append(a)
            
        avg = (sum(grades)/(len(grades))) #if grades==False else print("Divide by zero error.")
        
        print("\n List of grades: ", grades)
        print("Current average grade: ", avg)      
average()