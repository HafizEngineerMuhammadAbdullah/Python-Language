# Tuples in Python is a built-in data type that let us create immutable sequences of values just like string which is almost similar to Lists in Python
# Tuples is a brother of Lists
# Tuple values can't be changed if once inserted
# we use parenthesis to create tuple rather than square bracket notation
tuple = (2, 4, 2, 1, 6, 5)
print(tuple)
print(tuple[0])
print(tuple[1])
print(type(tuple))
# assignment is not allowed in tuple
# tuple[0] = 10 # the error is similar to one we got when we are trying to assign a value in a particular index of string

# create an empty & valid tuple
tup = ()
print(tup)
print(type(tup))

# not a tuple but an integer/float/string value
tup = 1
tup = "hello"
tup = 3.4
tup = None
print(tup)
print(type(tup))

# when there is a single element in a tuple,so comma must be place after a single element in order to create.percieve tuple
list = (1,)
print(list)
print(type(list))

print(tuple[1:3])
print(tuple.index(2))  # returns idx of first occurrence of element
print(tuple.count(2))  # returns the total count of element

# Q1. Write a Program to  enter names of their 3 favourite movies % store them in a list
movies = []

# movie1 = input("Enter your first favourite Movie name :")
# movie2 = input("Enter your second favourite Movie name : ")
# movie3 = input("Enter your third favourite Movie name : ")

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)

# print(movies)

movies.append(input("Enter your first favourite Movie name :"))
movies.append(input("Enter your second favourite Movie name : "))
movies.append(input("Enter your third favourite Movie name : "))
print(movies)


# 2.Write a program if a list contains a palindrome of elements(Hint: use copy()) method)
# list1 = [1,2,3,2,1]
# list1 = [1,2,3]
list1 = ["m", "a", "a", "m"]

copy_list = list1.copy()

copy_list.reverse()
if copy_list == list1:
    print("The list  is a Palindrome!")
else:
    print("The List is not a Palindrome!")

# Q3. Write a Program to count the number of students with the 'A' grade in the following tuple
grades = ('C', 'D', 'A', 'A', 'B', 'B', 'A')
print("Count of Grade A : " , grades.count("A"))

grades = ['C', 'D', 'A', 'A', 'B', 'B', 'A']
grades.sort()
print(grades)


