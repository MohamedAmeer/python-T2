# multiply two arguments
mul = lambda n1, n2: n1 * n2
n1 = 5
n2 = 15
print("the multiplication of n1&n2 is", mul(5, 15))


# fibonacci series
def fib(m):
    r = [0, 1]
    any(map(lambda _: r.append(r[-1] + r[-2]), range(2, m)))
    print("the fibonacci series is", r)


n = int(input("Enter number:"))
print(fib(n))

# multiply a number to the list
l1 = list(range(10))
l2 = list(map(lambda m: m * 3, l1))
print("The list before multiply of given no  is:", l1)
print("The list after multiply of given no  is:", l2)

# divisible by 9
l = list(range(90))
l3 = list(filter(lambda m: (m % 9 == 0), l))
print(l3)

# count of even no.
l = list(range(1, 11))
c = len(list(filter(lambda n: (n % 2 == 0), l)))
print("The number of even number in a list is:", c)
