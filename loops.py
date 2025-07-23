#while loop

number = 1
while number <= 5:
    print(number)
    number += 1

num = 105
while num >= 100 :
    print(num)
    num -= 1

#Break statement
count = 20
while count <= 25 :
    if count == 23 :
        break
    print(count)
    count += 1

#Continue
x = 10
while x <= 20 :
        if x == 15 :
            x +=1
            continue
        print("number is", x)
        x += 1

#for loop
for y in range(5):
    print(y)

for mynumber in range(20,26):
    print(mynumber)

for z in range(30, 40, 2): #increment by 2 from 30-40, excluding 40
    print(z)

for p in range(70, 90, 3): #increment by 3 from 70-90 excluding 90
    print(p)

for q in range(80,59, -2): #printing from 80-60, decreasing by 2
    print(q)

for s in range(90, 39, -5): #printing from 90-40, decreasing by 5
    print(s)



