# ------------------------------------------------------------------------------
# Exercise Python input / output basic operations
# ------------------------------------------------------------------------------

# 1. Write a Python Program to swap 4 variables values(input four values)
a = int(input("Enter first number:..."))
b = int(input("Enter second number:..."))
c = int(input("Enter third number:..."))
d = int(input("Enter fourth number:..."))


print("Numbers Before Swapping :...")
print("a : ", a, "b : ", b, "c : ", c, "d : ", d)
# perform swapping
temp = a
a = d
d = temp
temp = b
b = c
c = temp

print("Numbers After Swapping :...")
print("a : ", a, "b : ", b, "c : ", c, "d : ", d)

# 2. Write a Python Program to convert temperatures(T°) to & from Celsius , Fahrenheit (°C or 0°F)

print("\nIn which measurement unit you would like to enter temperature(T°)?")
print("1.Celsius(°C)")
print("2.Fahrenheit(°F)")

user_choice = input("\nSelect an option (1-2): ").strip()

if user_choice == "1":
    temp_in_celsius = float(input("Enter Temperature in Celsius scale(°C):..."))
    temp_in_fahrenheit = 9 * (temp_in_celsius / 5) + 32
    print("Temperature in Fahrenheit(°C) will be : ", temp_in_fahrenheit)
elif user_choice == "2":
    temp_in_fahrenheit = float(input("Enter Temperature in Fahrenheit scale(°C):..."))
    temp_in_celsius = 5 * (temp_in_fahrenheit - 32) / 9
    print("Temperature in Centigrade Scale(°C) will be : ", temp_in_celsius)
else:
    print("Invalid Selection,Please try again Later!")


# 3.Write a Python program to count the number of strings where the string length is 2 or more and the first & last character are same from a given list of strings
list = ['abc', 'xyz','aba','1221','cca','bcb']
count = 0
for item in list :
  if(type(item) is str and len(item) >= 2):
      if(item[0] == item[-1]): # if the first character matches with the last character,increment the count by 1
          count += 1

print("Result of count : " , count)


# 4.Write a Python Script to concatenate the following dictionaries to create a new one
# Sample Dictionary :-
# dic1 = {1:10 , 2: 20}
# dic2 = {3:30 , 4: 40}
# dic2 = {5:50 , 6: 60}


dict1 = {1:10 , 2: 20}
dict2 = {3:30 , 4: 40}
dict3 = {5:50 , 6: 60}
# Merge the dictionaries
combined = dict1 | dict2 | dict3
print(combined)  


# Write a Python Program to print a specified list after removing the 0th, 4th & 5th elements
# Python provides two built-in ways to delete an item using it's index 
# Using pop(): This removes the item at the index and returns its value
my_list = ["Red", "Green", "White", "Black","Pink","Yellow","Teapink"]
removed_item = my_list.pop(2)  # Removes 'c'
print(my_list)  # Output: ['a', 'b', 'd']


# Using del: This deletes the item directly without returning it
del my_list[2]  # Removes 'c'
print(my_list)  # Output: ['a', 'b', 'd']

println()