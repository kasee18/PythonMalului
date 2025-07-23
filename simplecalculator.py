#define a function to add two numbers
def add(num1, num2):
    return (num1 + num2)

#define a function to subtract two numbers
def subtract(num1, num2):
    return (num1 - num2)

#define a function to multiply two numbers
def multiply(num1, num2):
    return (num1 * num2)

#define a function to divide two numbers
def divide(num1, num2):
    return (num1 / num2)

#User input to select operations (1 to 4)
sel = int(input("Select operation (1-4): "))

#Take num1 as an input and convert to integer(int)
num1 = int(input("Enter first number: "))

#Take the second number as an input from the user and convert it to an integer
num2 = int(input("Enter a second number:"))

#check which operation the user selected and perform the corresponding calculation
if sel == 1: #if user selects 1, perform addition
    print(num1, "+", num2, "=", add(num1, num2))

elif sel == 2: #if user selects 2, perform subtraction
    print(num1, "-", num2, "=", subtract(num1, num2))

elif sel == 3: #if user selects 3, perform multiplication
    print(num1, "*", num2, "+", multiply(num1, num2))

elif sel == 4: #if user selects 4, perform division
    print(num1, "/", num2, "=", divide(num1, num2))

else: #if user selects any other number outside 1-4, print an invalid input
    print("Invalid input")





