# 1
# create a list of n integer values

my_list = [5, 6, 10, 7, 20, 15, 25]

L = int(input("enter the number you want to add:"))
my_list.append(L)
print(my_list)

# delete particular element in a list
L = int(input("enter number u want to delete"))
my_list.remove(L)
print(my_list)

# sort the list
my_list.sort()
print(my_list)

# largest number in list
print("smallest number is:", my_list[0])

# smallest number in list
print("largest number is:", my_list[-1])
# 2
# create a tuple
my_tuple = (7, 14, 10.0, 'helloha')

print("My tuple",(my_tuple))

# reverse the tuple
x = reversed(my_tuple)
print("My reversed tuple :", tuple(x))
# 3
# convert the tuple into a list
T = (1, 2, 3, 'tracaris')
print("my tuple is:", T)
List = list(T)
print("my list is:", List)
