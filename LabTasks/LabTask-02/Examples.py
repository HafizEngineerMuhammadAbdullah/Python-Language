import math;
import cmath;
import random;
# Example : 1 Print square root of negative or positive number using if and operators.

n = int(input("Enter a number to find Square root:... ")) 
if(n > 0):
    print("Square root of" , n, "is :", math.sqrt(n))
else:
    print("Can't find Square root of negative real numbers")

# Example : 2 Write conditional statements to print value of 0 to 1 and 1 to 0 and numbers in between. 
value = 0.5  

if value == 0:
    print("The value is exactly 0")
elif value == 1:
    print("The value is exactly 1")
elif 0 < value < 1:
    print(f"The value {value} is between 0 and 1")
else:
    print(f"The value {value} is outside the 0 to 1 range")

# OR
# Generate steps from 0.0 to 1.0 (stepping by 0.2)
for i in range(11):
    value = round(i * 0.1, 1)  # Generates 0.0, 0.1, 0.2 ... 1.0
    
    # Conditional logic to identify boundaries and the numbers in between
    if value == 0.0:
        print(f"{value} -> This is the starting point (0)")
    elif value == 1.0:
        print(f"{value} -> This is the ending point (1)")
    elif 0.0 < value < 1.0:
        print(f"{value} -> This is a number in between")

# OR
# Generate steps backwards from 1.0 down to 0.0
for i in range(10, -1, -1):
    value = round(i * 0.1, 1)
    
    if value == 1.0:
        print(f"{value} -> This is the starting point (1)")
    elif value == 0.0:
        print(f"{value} -> This is the ending point (0)")
    elif 0.0 < value < 1.0:
        print(f"{value} -> This is a number in between")

# Example : 3 Print Karachi Pakistan 100 times in a separate line 
i = 0
while(i < 100):
    print("Karachi Pakistan!❤")
    i += 1

# Example # 4 
# Take collection of number input from user. Print the total positive and negative number.

# Example # 5 
# Fixed a Letter from a to e and then ask the user to guess that letter until correct letter entered.

lists = ['a','b','c','d','e']

# Set the secret letter
secret_letter = lists[random.randint(0, 4)]

# Start the guessing loop
while True:
    # Ask the user for a guess
    guess = input("Guess the secret letter: ").lower()
    
    # Check if the guess is correct
    if guess == secret_letter:
        print(f"Correct! The secret letter is '{guess}'.")
        break
    else:
        print("Try again!")
