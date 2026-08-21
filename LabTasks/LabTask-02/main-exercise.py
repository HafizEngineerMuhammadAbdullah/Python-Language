# Exercise 1:
# (I)Cabinets and Boxes are objects that are mostly in cubic shape. Make a program that takes
# inputs like height, width and depth from user and then calculate volume of the cube:
# volume = height ∗ width ∗ depth
# After calculating volume of cube, compare it with following ranges and print the relevant label:

cube_height = int(input("Please, Enter the height of box in cm3:..."))
cube_width = int(input("Please, Enter the width of box in cm3:..."))
cube_depth = int(input("Please, Enter the depth of box in cm3:..."))

volume = cube_height * cube_width * cube_depth

if volume >= 1 and volume <= 10:
    print(f"Cube is extra small!,it's volume is {volume}")
elif volume >= 11 and volume <= 25:
    print(f"Cube is Small!,it's volume is {volume}")
elif volume >= 26 and volume <= 75:
    print(f"Cube is Medium!,it's volume is {volume}")
elif volume >= 76 and volume <= 100:
    print(f"Cube is Large!,it's volume is {volume}")
elif volume >= 101 and volume <= 250:
    print(f"Cube is Extra Large!,it's volume is {volume}")
elif volume >= 251:
    print(f"Cube is Extra-Extra Large!,it's volume is {volume}")
else:
    print("Invalid height , width or depth.Please Try again!")


# Exercise II : In a company ,worker efficiency is determined on the basis of the time required for a worker
# to complete a particular job.If the  time taken by the worker is between 2-3 hours then the worker
# is said to be highly efficient. If the time required by the worker is between 3-4hours,then the worker
# is ordered to improve speed. If the time taken is between 4-5 hours ,the worker is given training to
# improve his speed ,and if the time taken by the worker is more than 5 hours ,then the worker  haas
# to leave the company, If the time taken by the worker is input through the keyboard,find the
# efficiency of the worker.

print("Welcome to Employee/Worker!")
job_exec_time = int(
    input("Kindly, Enter time you take to complete a particular job in hours!")
)

if job_exec_time >= 2 and job_exec_time <= 3:
    print("Highly Efficient Employee you are,Excellent job!")
elif job_exec_time >= 3 and job_exec_time <= 4:
    print("Improve your speed kindly!")
elif job_exec_time >= 4 and job_exec_time <= 5:
    print("Dear Employee,you are required to get a traning to improve your speed!")
elif job_exec_time > 5:
    print("Dear Employee,you are requested to leave the company!")
else:
    print("Go to Hell!")

# Exercise III : The program must prompt the user for a username and password. The program should compare
# the password given by the user to a known password. If the password matches, the program should
# display “Welcome!” If it doesn’t match, the program should display “I don’t know you.
# Note: the password should not be case sensitive and it’s value is abc$123 or ABC$123
user_name = input("Enter your name here... ")

user_password = input("Please,Enter your password here!").lower()

known_password = "abc$123"

if user_password == known_password:
    print(f"Welcome {user_name}!")
else:
    print("I don't know you!")

# Exercise 2:
# (i)What Would Python Print?
n = 3
while n >= 0:
    n -= 1
    print(n)

# The code block will continue to run until n becomes < 0, since 0 is not greater than or equal to 0.
# (ii): What Would Python Print?
# typing Ctrl-C will stop infinite loops
n = 4
# while n > 0:
    # n += 1
    # print(n)

# (ii)Try the scenario below:
# Make a program that lists the countries in the set
country_list = ["Canada", "USA", "Mexico", "Australia"]

for item in country_list:
    print(item)

# 1. Create a loop that counts from 0 to 100
i = 0
while i <= 100:
    print(i)
    i += 1
# 2. Make a multiplication table using a loop
n = int(input("Enter a number to print multiplication table:... "))
m = int(input("till where you want to print multiplication table:... "))

for i in range(1, m + 1):
    print(n, "x", i, "=", n * i)

# 3. Output the numbers 1 to 10 backwards using a loop
for i in range(10, 0, -1):
    print(i, end=" ")

print()
# 4. Create a loop that counts all even numbers to 10
count = 0
for i in range(1, 11):
    if i % 2 == 0:
        count += 1

print("Count of Even numbers : ", count)

# 5. Create a loop that sums the numbers from 100 to 200
sum = 0
for i in range(100,201):
    sum += i

print(sum)
