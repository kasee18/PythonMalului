#standard library functions/also called inbuilt functions

y = max(89, 56, 34, 800, 18)
print("The maximum value is", y)

x = min(54, 56, 34, 800, 6)
print("The minimum value is", x)

#user-defined functions
def school():
    print("My coding school is eMobilis")

school() #calling a function so as to get a response

def sum():
    p = 20
    q = 30
    print(p + q)

sum()

#parameter/variable and argument/value assigned to a variable
def multiply(num1, num2):
    print(num1 * num2)

multiply(8,9)
multiply(3,9)
multiply(8,6)
multiply(4,9)

def add(num1, num2):
    print(num1 + num2)

add(8,9)
add(3,9)
add(8,6)
add(4,9)

def student(fullname, age, gender):
    print(fullname, age, gender)

student("Were", 40, "male")
student("John", 34, "male")
student("Parmphy", 27, "female")
student("Mercy", 23, "female")
student("everlyne", 41, "female")


def employee(fullname, position, salary, email):
    print(fullname, position, salary, email)

employee("Vincent Mutisya", "Chief Executive Officer", 2500000, "mutisyavincent99@gmail.com")
employee("Joseph Malului", "Managing Director", 1200000, "josephmalului@gmail.com")
employee("Michael Mang'eli", "project Manager", 550000, "michaelM@gmail.com")
employee("Joseh Nzuki", "Deputy Managing Director", 450000, "nzukiJ@gmail.com")
employee("Nicholus Mutinda", "Production Manager", 350000, "mutindaN@gmail.com")



