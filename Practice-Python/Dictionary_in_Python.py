
# Dictionary is a builtin data type in python that stores the info/data in the form of key:value pairs where key must be  a unique value
# Key value pairs must be separated by colon
# two or more than key value pairs should be separated by comma (,)
# key must not be a duplicate value(similar to real life dictionary like one word occur one times but it could have multiple meanings)
info = {
    "key" : "value",
    "name" : "ProfAbdullah",
    "age" : 19,
    "cgpa" : 3.2,
    "learning" : "Python",
    "is_adult" : True,
    "subjects" : ["Python", "C", "C++" , "Java" , "Javascript"],
    "topics" : ("dictionary" , "set")
}

print(info)
print(type(info))
print("Name : ", info["name"])
print("Age : ", info["age"])
print("isAdult : ", info["is_adult"])
print("CGPA : " , info["cgpa"])
print("subjects : ", info["subjects"])
print("topics : ", info["topics"])

# change the value of a particular key
info["name"] = "DrProfAbdullah"
info["surname"] = "Khalid"# add a new key value pair in the dictionary
# so it means dictionary in python is mutable(changeable)
# if we want to add a name and it's value as a new key value pair form,so it is not possible in Python
# because in this case old value of name becomes overwrite 
# instead of creating a new key value pair with the same key(existing key),Python overwrite the old value of the existing key
# we can create an empty dictionary as well 

print(info)

null_dict = {}
null_dict["name"] = "mycollege"
print(null_dict)


# Nested Dictionary :-
student = {
   "name" : "ProfAbdul",
   "scores" : {
       "Physics" : 97,
       "Chemistry" : 98,
       "Math" : 99
   }
}

print(student)
# Getting the relevant info from Nested Dictionaries
print("Physics Marks : " , student["scores"]["Physics"])
print("Chemistry Marks : " , student["scores"]["Chemistry"])
print("Math Marks : " , student["scores"]["Math"])

# Dictionary Methods :-
# myDict.key() returns the collection of all keys except nested key
print(student.keys()) 
print(list(student.keys()))  # type casting
print("Length of Dictionary : " , len(student))
print("Length of Dictionary : " , len(list(student.keys())))
# return all the values of dictionary
print(student.values())
print(list(student.values()))
# return all key value pairs (key,value) as(in the form of) tuples
print(student.items())
print(list(student.items()))
pairs = list(student.items())
print("Tuple1 := " , pairs[0])
print("Tuple1 item1 := " , pairs[0][0])
print("Tuple1 item2 := " , pairs[0][1])
print("Tuple2 := " , pairs[1])
print("Tuple2 item1 := " , pairs[1][0])
print("Tuple2 item2 := " , pairs[1][1])





