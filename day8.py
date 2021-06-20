# merge two dictionaries
d1 = {'a': 1, 'b': 2}
d2 = {'b': 1, 'c': 3}
d1.update(d2)
print(d1)

# sort the list from des to ascen and convert list into set

lst = ["xyz", "abc", "20", "16", "11"]
print("list is:", lst)
lst.sort()
print("list in ascending order:", lst)
set = set(lst)
print("set is", set)

# list number of items in a dictionary and sort the dictinary
dict = {
    "a": 12,
    "b": 11,
    "c": 13,
    "d": 20
}
print("no of items in a dictionary is:", len(dict.keys()))
srt_dict = sorted(dict.items(), key=lambda x: x[1])
print(srt_dict)


def sort_dict():
    print("the sorted dict is:", sorted(dict.items(), key=lambda x: x[1]))


sort_dict()
# replace the first instance of word with a user given input
str = "hello welcome"
print("befor change the first word of string is:", str)
my_str = input("enter a word:")
a = str.replace("hello", my_str, 1)
print("after changing the first word of string:", a)

# capitalize the first char of given string

s = "hi and welcome to my world"
print(" ")
print("the string before capitalize all first char:", s)
q = s.title()
print(" ")
print("the string after capitalize all first char:", q)
print(" ")


# to find a repeated item in a list
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


list = [10, 20, 30, 20, 20, 30, 40,
        50, -20, 60, 60, -20, 'a', 'a', 'abc']
print('the list is:', list)
print("the repeated item in a list is:", Repeat(list))

x = input("Input the first number")
y = input("Input the second number")
z = input("Input the third number")
print("Median of the above three numbers -")
# find median
if y < x and x < z:
    print(x)
elif z < x and x < y:
    print(x)

elif z < y and y < x:
    print(y)
elif x < y and y < z:
    print(y)

elif y < z and z < x:
    print(z)
elif x < z and z < y:
    print(z)

# swap case of given string

az = "HeLLo HOw aRe YOu "
print("string before swap case:", az)
print("string after swap case:", az.swapcase())


# convert integer to binary

def intToBinary(num):
    if num >= 1:
        intToBinary(num // 2)
    print(num % 2, end='')


if __name__ == '__main__':
    int_val = 24

print(intToBinary(int_val))