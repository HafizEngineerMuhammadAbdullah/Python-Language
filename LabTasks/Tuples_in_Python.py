# Tuples in Python is a built-in data type that let us create immutable sequences of values just like string which is almost similar to Lists in Python
# Tuples is a brother of Lists
# Tuple values can't be changed if once inserted
# we use parenthesis to create tuple rather than square bracket notation
tuple = (2,4,2,1,6,5)
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
tup = (1)
tup = ("hello")
tup = (3.4)
tup = (None)
print(tup)
print(type(tup))

# when there is a single element in a tuple,so comma must be place after a single element in order to create.percieve tuple
list = (1,)
print(list)
print(type(list))

print(tuple[1:3])
print(tuple.index(2)) # returns idx of first occurrence of element
print(tuple.count(2)) # returns the total count of element