
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

print(info)

