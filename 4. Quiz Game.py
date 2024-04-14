

def quiz():
    questions = ["What is 2+2? \n", "What continent is Germany in? \n", "What month comes after April? \n", "What is the color of the Sky? \n"]
    correct_answers = ["4", "Europe", "May", "Blue"]
    g = 0
    for i in range(len(questions)):
        
        if correct_answers[i] == input(questions[i]):
            g += 1
            print("Correct!")
            
        else:
            print("Nope!")
    grade = (g/4)*100
    print("Your quiz grade is: ", str(grade)+ "%.")
    if grade == 100:
        print("You got all the questions right!")
    elif grade == 75:
        print("You got 3/4 right! Nice job!")
    else:
        print("You did not pass thq quiz. Try again!")
quiz()