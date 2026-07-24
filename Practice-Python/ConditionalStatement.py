marks = int(input("Please , Enter your marks : "))

if(marks >= 90) :
    grade = "A"
elif(marks >= 80) :# indentation (proper spacing is important in Python) because there is no concept of curly braces as such exists{}
    grade = "B"
elif(marks >= 70) :
    grade = "C"
else:
    grade = "D"

print("grade of the student -> " , grade)

# nesting in if statement
age = 80

if(age >= 18):
    if(age >= 80):
        print("You are not able to drive a car!")
    else:
        print("Can Drive")
else:
    print("Too Young!")


num = int(input("Enter your Number : "))

rem = num % 2

# if(rem == 0):
#     print("EVEN Number")
# else:
#     print("ODD Number")
if(not rem):
    print("EVEN Number")
else:
    print("ODD Number")

a = int(input("Enter first Number : "))
b = int(input("Enter second Number : "))
c = int(input("Enter third Number : "))

if(a > b and a > c):
    print("a is the greatest")
elif (b > c):
   print("b is greatest")
else:
    print("c is greatest")