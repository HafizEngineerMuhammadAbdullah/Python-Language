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


