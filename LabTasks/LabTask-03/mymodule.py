# import math
# from math import sqrt
# import math.sqrt as squareroot
from math import sqrt as squareroot 
import glob
import time
import random
# help(math)
# help(math.sqrt)
# print(sqrt(9))
print("Square root of 81 is", squareroot(81))
def greeting(name):
   print("Hello,Welcome to " , name)

current_time = time.time()
print("Current time in miliseconds : ", current_time)

print("current time : ",time.ctime(current_time))
print("current time : ",time.ctime())

print(time.sleep(4))


print(glob.glob("*"))

print(glob.glob("*.txt"))

# generates a random  integer between a and b inclusive
print(random.randint(1,5))

# generates a random  inumber between 0 and 1
print(random.random())

list = [1,2,34,56,78]
random.shuffle(list)
print(list)


# random.shuffle(list,1)
# print(x)
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)










