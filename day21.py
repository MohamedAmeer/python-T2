# using zip() function and list() function, create a merged list of tuples from the two lists given.

s1 = [2, 3, 1]
s2 = ['b', 'a', 'c']
t = tuple(zip(s1, s2))
print(t)

# First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list
# of tuples.

lst1 = ["airport", "railway station", "Industry", "college", "school", "Forest", "bus stand"]

rang = list(range(1, 8))

lst = zip(lst1, rang)

print(lst)

# Using sorted() function, sort the list in ascending order.

ls1 = [3, 82, 2, 1, 0, 22, 33]

s = sorted(ls1)
print(s)

# filter the even numbers so that only odd numbers are passed to the new list


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst1 = list(filter(lambda x: x % 2 == 1, lst))

print(lst1)
