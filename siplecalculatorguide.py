first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
operator = input("Enter operation: (+, -, *, /): ")

if operator == "+":
    print(first + second)

elif operator == "-":
    print(first - second)

elif operator == "*":
    print(first * second)

elif operator == "/":
    print(first / second)

else:
    print("Invalid operator")


