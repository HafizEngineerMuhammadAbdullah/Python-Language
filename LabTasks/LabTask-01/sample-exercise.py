# ------------------------------------------------------------------------------
# Exercise Python input / output basic operations
# ------------------------------------------------------------------------------

# 1. Write a Python Program to swap 4 variables values(input four values)
a = int(input("Enter first number:..."))
b = int(input("Enter second number:..."))
c = int(input("Enter third number:..."))
d = int(input("Enter fourth number:..."))


print("Numbers Before Swapping :...")
print("a : ", a, "b : " , b, "c : ", c, "d : ", d)
# perform swapping 
temp = a
a = d
d = temp
temp = b
b = c
c = temp

print("Numbers After Swapping :...")
print("a : ", a, "b : " , b, "c : ", c, "d : ", d)

# 2. Write a Python Program to convert temperatures(T°) to & from Celsius , Fahrenheit (°C or 0°F)

print("\nIn which measurement unit you would like to enter temperature(T°)?")
print("1.Celsius(°C)")
print("2.Fahrenheit(°F)")

user_choice = input("\nSelect an option (1-2): ").strip()