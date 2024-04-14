import math
x = float(input("Input the first number: "))
funct = input("Input: +, -, *, or % ")
y = float(input("Input the next number: "))

def add ():
    print(x+y)

def subtract ():
    print(x-y)

def multiply():
    print(x*y)

def divide():
    print(x/y) if y else print("Divide by 0 error.")
    
if funct == "+":
    add()

elif funct == "-":
    subtract()

elif funct == "*":
    multiply()

elif funct == "%" or "/":
    divide()