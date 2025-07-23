num = int(input("Enter a number: "))

if num > 1:

    for i in range(3, num):
        if num % i == 0:
            print(num," is not a prime number")
            break
    else:
        print(num,"is a prime number")

else:
    print("is not a prime number")