import os

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
    f = open("demo.txt", "a+")
    f.write("\nHi,I will learn AI tomorrow as my exam is going to come!")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Error: The file 'demo.txt' does not exist in this directory.")

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

# Deleting a File using Module
# os.remove("sample.txt")


# Qs:01 Write a function that replaces all the occurrences of "Java" with "Python" in file practice.txt
# Qs:02 search if the word "learning" exists in the file or not
# with open("practice1.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\nusing Java.\n I like programming in Java")

# Read File -> changes done in file data -> Overwrite the file data
with open("practice1.txt", "r") as f:
    data = f.read()

    new_data = data.replace("Java", "Python")
    print(new_data)


with open("practice1.txt", "w") as f:
    f.write(new_data)


def check_for_word():
    word = "learning"
    with open("practice1.txt") as f:
        data = f.read()
    if data.find(word) != -1:
        print("Learning word exist!")
    else:
        print("Learning word doesn't exist!")


check_for_word()


# Qs:03 Write a function to find in which line of the file does the word "learning" occur first.
# print -1 if word not found
def check_for_line():
    word = "learning"
    with open("practice1.txt", "r") as f:
        data = True
        line_no = 0
        # loop through when data has valid value
        while data:
            data = f.readline()
            line_no += 1
            if word in data:
                print(f"Line no where {word} exist is : ", line_no)
                return

    return -1


check_for_line()

# from a file containing  numbers separated  by comma,print the count of even numbers
# with open("practice2.txt","w") as f:
#     f.write("1, 2, 76, 84, 90, 101")


# find individual number from a file
# parse the number / casting the  number to integer value
def check_for_number():
    number_list = []
    with open("practice2.txt", "r") as f:
        data = f.read()
        number = ""
        for char in data:
            if char != " " and char != ",":
                number += char
            elif char == ",":
                if number:  # Check to ensure 'number' is not empty
                    number_list.append(int(number))
                    number = ""

        # FIX: Catch the last number left in the buffer
        if number:
            number_list.append(int(number))
    print(number_list)


check_for_number()


# def check_for_number():
#     number_list = (
#         []
#     )  # Avoid using 'list' as a variable name as it is a built-in keyword

#     with open("practice2.txt", "r") as f:
#         data = f.read()  # Reads the entire file content as a single string

#     # Split the string by commas, clean up spaces, and convert to integers
#     # This replaces the entire while loop and manual string construction
#     for item in data.split(","):
#         cleaned_item = item.strip()
#         if cleaned_item:  # Ensures we don't try to convert empty strings
#             number_list.append(int(cleaned_item))

#     print(number_list)


# Call the function to test it
# check_for_number()

def check_for_number():
    number_list = []
    with open("practice2.txt", "r") as f:
        data = f.read()
        print(data)
        number = ""
        for i in range(len(data)):
            if(data[i] == ","):
                print(int(number))
                number = ""
            else:
                number += data[i]


    print(number_list)


check_for_number()



def check_for_number():
    count = 0
    with open("practice2.txt", "r") as f:
        data = f.read()
        print(data)
        number_list = data.split(",")
        for val in number_list:
            if(int(val) % 2 == 0):
                count += 1

    print("Count of Even Number : ", count)
check_for_number()

