# try:
#     f = open("demo.txt", "r")
#     # data = f.read()
#     # print(data)
#     # data = f.read(7)
#     line1 = f.readline()
#     print(line1)
#     line2 = f.readline()
#     print(line2)
#     line3 = f.readline()
#     print(line3)
#     # print(type(data))
#     f.close()  # Always close the file
# except FileNotFoundError:
#     print("Error: The file 'demo.txt' does not exist in this directory.")



# I am Learning too many computer science core subjects in this semester
# like Operating System, Database Management System(DBMS),Artificial Intelligence(AI),
# Computer Organization and Assembly Language(COAL) etc

try:
    f = open("demo.txt","r+")
    f.write("\nHi,I will learn AI tomorrow as my exam is going to come!")
    print(f.read())
    f.close()
except FileNotFoundError:
   print("Error: The file 'demo.txt' does not exist in this directory.")

