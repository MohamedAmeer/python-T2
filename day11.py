def abc():
    l1 = ['a', 123, 'list', 'hello', 765]
    print("the list is", l1)


abc()
# generate random numbers from 1 to 100
import random

mylist = []

for i in range(0, 100):
    x = random.randint(1, 10)
    mylist.append(x)

print(mylist)

# importing sys module
import sys

# appending a path
sys.path.append('C:\Users\Ameer')

# printing all paths
sys.path
