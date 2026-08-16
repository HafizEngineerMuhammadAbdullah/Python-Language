# Loops in Python
# Loops are used to perform repeating works(repeat instructions)
# While Loop:-
count = 1

while count <= 5:
    print(count)
    count += 1

count = 1
while count <= 5:
    print("Hello World!")
    count += 1

i = 1
while i <= 5:
    print(i)
    i += 1

i = 5
while i > 0:
    print(i)
    i -= 1
print("Loop Ended")



# 1.Print Numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1

# 2.Print Numbers from 100 to 1
i = 100
while i > 0:
    print(i)
    i -= 1 


# Print the multiplication table of a number n
n = int(input("Please,Enter a number : "))

i = 1
while i <= 100 :
    print(n , '*' , i , '=', n*i)
    i += 1

# print the elements of the follwing list using a loop:-
# list = [1,4,9,16,25,36,49,64,81,100]
list = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(list) :
    print(list[i])
    i += 1

# Search for a number x in this tuple using loop
tuple = (1,4,9,16,25,36,49,64,81,100)
x = 9
i = 0
while i < len(tuple) :
    if(x == tuple[i]) :
        print(x , "found at ", i)

    i += 1

# Break statement:-
# The break statement is used to terminate the loop when a certain condition is met.
i = 1
while i <= 10:
    if(i == 5):
        break
    print(i)
    i += 1

# Continue Statement:-
# The Continue statement is used to skip the current iteration of the loop and continue with the next iteration.
i = 1
while i <= 10:
    if(i == 5):
        i += 1
        continue #skip
    print(i)
    i += 1 

# for Loop:- it is used for sequential traversing,iterating either list,tuples,string etc

nums  = [1,2,3,4,5]
for val in nums:
    print(val)

veggies = ["potato","ladyfinger","cucumber","brinjal"]
for val in veggies:
    print(val)

tup = (1,2,3,4,56,89,0)
for val in tup:
    print(val)

str = "adamjeegovernmentsciencecollege"
for char in str:
    print(char)
else:
    print("END")

for char in str:
    if(char == 'a'):
        print('o found')
        break
    print(char)
else:
    print("END")


for char in str:
    if(char == 'a'):
        print('o found')
        break
    print(char)

print("END")


# for Loops
# Print the elements of the following list using a loop
nums = [1,4,9,16,25,36,49,64,81,100]

for el in nums:
    print(el, end=" ")


print()

# Search for a number x in this tuple using loop
nums = (1,4,9,16,25,36,49,64,81,100)

x = 49
idx = 0
for el in nums:
    if(el == x):
        print("number 49 at found idx!", idx)
    idx += 1


# Separate numbers by a space
# for i in range(1, 6):
#     print(i, end=" ")
# # Output: 1 2 3 4 5

# # Separate numbers without spaces
# for i in range(1, 6):
#     print(i, end="")
# # Output: 12345

print(range(5))
print(range(1,4))
seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])
print(type(seq))

for i in range(10): # range(stop)
    print(i,end=" ")

print()

for i in range(2,10): # range(start, stop)
    print(i,end=" ")

print()
for i in range(0,10,2): # range(stop)
    print(i,end=" ")

print()

for i in range(1,101):
    print(i,end=" ")

for i in range(100,0,-1):
    print(i,end=" ")

n = int(input("Enter a number : "))

print()
for i in range(1,10):
    print(n , " x ",i, " = " , n*i )


for i in range(10):
    #some work
    pass

if i > 12:
   pass

print("Work Completed!")

# Write a Program to find the sum of first n natural numbers(using while)
n = int(input("Enter a number :- "))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

# for i in range(1,n+1):
#     sum += i

print("Total Sum = " , sum)

# Write a Program to find the factorial of first n natural numbers(using for)
n = int(input("Enter a number :- "))

factorial = 1

for i in range(1,n):
    factorial *= i

print("Factorial = " , factorial)


