#Arithmetic Operators

num1 = 45
num2 = 2
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2) #Modulus - Returns the remainder after division


#Comparison operators
print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 == num2) #Equal to
print(num1 != num2) #Not equal to

#Assignment Operators
x = 56
x -= 2
print(x)

number = 12 + (40/2) * 3 #Operator Precedence
print(number)
print(int(number))

#Logical Operators - and, or, not
log = 20
print(log < 30 and log > 50) #and returns a False if one condition is False
print(log < 30 or log > 50) #or returns True if one condition is True
print(not(log < 30 or log > 50)) #not reverses the results