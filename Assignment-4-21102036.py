#Q1 Grades
x=int(input("Enter marks:"))
if x<25:
    print("F")
elif (x>=25)and(x<45):
    print("E")
elif (x>=45)and(x<50):
    print("D")
elif (x>=50)and(x<60):
    print("C")
elif (x>=60)and(x<80):
    print("B")
elif (x>=80)and(x<100):
    print("A")
else:
    print("Not correct marks")

print("\n")

#Q2 Leap Year
x=int(input("Enter the year:"))
if ((x % 4==0 and x % 100 !=0)or x % 400 ==0):
    print(x,"is a leap year")
else:
    print(x,"is not a leap year")

print("\n")

# Q3 Multiplication Game
import random as r
score = 0
print("Going to generate random numbers")
for i in range(10):
    first = r.randint(1, 10)
    second = r.randint(1, 10)
    print(first, "*", second, "=", end="")
    product = first * second
    ask = eval(input(""))
    if (ask == product):
        score += 1
        print("Right!")
    else:
        print("Wrong")
        print(first, "*", second, "=", product)

print("Total Score:", score,"/10")
print("\n")

#Q4 Halloween Candy
x=200
for i in range(x):
    if i % 5==2:
        if i %6==3:
            if i % 7==2:
                print(i,"candies present in the bowl")
print("\n")




