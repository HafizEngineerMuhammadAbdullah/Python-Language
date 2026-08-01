# Set is the collection of unordered items, where each element must be a unique & immutable value
# boolean,int,float,string, can be stored in Python
# but List & Dictionary can't be stored in Python as they are mutable by nature
# duplicates are ignored(not allowed) in set DS of Python
# Set is created using curly braces '{}' and elements come inside this curly braces
collection = {1,2,2,3,4,5, "hello", "world", "world"}
print(collection) 
print("Type of Collection : " , type(collection))
# returns the total number of items contained in the set
print("Length of Collection : ", len(collection))

# this is not an empty set,this is an empty dictionary
collection1 = {}
print(collection1)
print(type(collection1))

# create an empty set by following this syntax
collection2 = set()
print(collection2)
print(type(collection2))