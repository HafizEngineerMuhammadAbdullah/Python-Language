a = 10
b = 30
sum = a + b
print(sum)

# more lines of code

a = 24
b = 35
sum = a + b
print(sum)

# more lines of code

a = 34
b = 56
sum = a + b
print(sum)

# this is the entire function to calculate the sum of two numbers
def calc_sum(a,b):
    sum = a + b
    print(sum)
    return sum

calc_sum(2,3)

# function definition
def calc_sum(a,b): #parameters
    return a + b

calc_sum(1,2) # function call;arguments 

def print_hello():
    print("hello")

output = print_hello()
print(output)



# average of 3 nums
def calc_avg(a,b,c):
    sum = a + b + c
    avg = sum / 3
    print("Average is", avg)
    return avg


calc_avg(1,2,3)

print("mycollege","abdullah") #sep(separator) = " "
print("mycollege") #end = "\n"
print("abdullah")