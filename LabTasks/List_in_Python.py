marks1 = 94.4
marks2 = 85.5
marks3 = 75.9
marks4 = 45.6
marks5 = 56.7

# Lists In Python :-
# A built-in data type that stores set of values
# it can store elements of different type(like int,float,double,string,boolean,none etc)
# List of Python is slightly different from the array that we created in C++/Java(generally all data must be of same type)
# in Python,we can store elements of different type togetherin a single list
# Multiple types of data can be stored together in a single list
marks = [94.4, 85.5,75.9, 45.6, 56.7]
print(marks)
print(type(marks))
print("Marks : " , marks[0])
print("Marks : " , marks[1])
print("Marks : " , marks[2])
print("Marks : " , marks[3])
print("Marks : " , marks[4])
print("Length of marks : ", len(marks))

student = ["DrAbdullah", 95.4,17, "Karachi", True, None]
print(student)
print(student[0])
print(type(student))

# Strings & Lists in  Python they both are different Data types
# Strings is immutable(can't be changed) but can access only
# Lists is mutable(can be changed) but also can access
# we can access elements of lists within the range
str = "Hello, Welcome to Python HomeLand"
print(str[0])
# str[0] = "Y"
student[0] = "ProfAbdullah"
print(student)
# print(student[6])#index out of bound exception

# Slicing in Lists called Sublist
# syntax : list_name = [starting_idx, ending_idx] => ending idx is not included
# similar to string slicing
# negative index ke basis per bhi slicing possible hai
marks = [87, 95, 78, 63, 46]
print(marks[1: 4])
print(marks[: 4])
print(marks[0:])
print(marks[-3: -1])


# Lists Specific Methods
#1. Adds the element at the end
list = [65,67,87,43,56]
list.append(4) # mutating the list allowed in list
print(list)
# sort the lists in ascending order
print(list.append(5))# return nothing
print(list.sort())# return nothing
list.sort()
print(list)

list.sort(reverse = True)
print("Sorted List in Descending order : " , list)

# Sorted List
l = ['a', 'd', 'e' , 'f', 'c', 'b']
l.sort()
print("Sorted List : " , l)

# Reverses List
l.reverse()
print("Reverse List : " , l)

# Insert Element at particular index
list.insert(2,44)
print("Add element 44 at index 2 : ", list)

# Removes First occurrence of element
list.remove(67)
print("Removes 67 from list : " , list)

# Removes element at particular index
list.pop(0)
print("Removes 0 index value : " , list)
