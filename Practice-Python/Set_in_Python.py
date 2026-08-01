# Set is the collection of unordered items, where each element must be a unique & immutable value
# Set is itself a mutable but it's elements are immutable
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


# crete a set using set() constructor
collection3 = set([1,2,3,4,5,6])
# Set Methods
# add() method is used to add an element to the set
collection3.add(7)
collection3.add(3) # this will be ignored as 3 is already present in the set
collection3.add("mycollege")
collection3.add(("Haha", 'Wow!', "Alas!"))
collection3.add("hello")
collection3.add("mycollege")
collection3.add("world")
collection3.add("coding")
collection3.add("Python")
# collection3.add(["Haha", 'Wow!', "Alas!"])
# remove() is used to remove an element from the set 
# collection3.remove(0) # KeyError occurs 

# clear() empties the set
# collection3.clear()
# pop() removes a random element
print(collection3.pop())

print("Length of set : " , len(collection3))
print(collection3)

# union() combines both set values & returns new set,it doesn't change in the original set
# duplicate values counts only one time
set1 = {1,2,3}
set2 = {3,4,5}
print("Combined/Union of two Sets : ", set1.union(set2))
print("Combined/Intersection of Two Sets : ", set1.intersection(set2))