# write a program to loop through a list of numbers and add +2 to every value in a list

l = [1, 3, 5, 7, 9]

a =2

res = [x+a for x in l]
print ("The list after adding +2 to each element : " +  str(res))

# write a program to reduce the value one by one and print each value
n = int(input('Enter number: '))
for i in range(n):
 print(''.join(map(str,range(n-i,0,-1))))

# fibonacci sequence

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

if nterms <= 0:
 print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
 print("Fibonacci sequence upto",nterms,":")
 print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

# armstrong number

# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

# multiplication table of 9

num = 9

for i in range(1, 11):
 print(num, 'x', i, '=', num*i)

# check if a program is positive or negative

num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

# to convert a number of days to ages


print("Enter the days::")

d = int(input())

# Conversion of days in to ages
y = (int)(d / 365)


# Output
print("the age is",y)

# solve trignometry problem using math function

import math
import math as ma
def trig(n,m):
	if n=="sin":
		return ma.sin(m)
	elif n=='cos':
		return ma.cos(m)
	elif n=='cosin':
		return ma.cosine(m)
	elif n=='tan':
		return ma.tan(m)
	elif n=='sec':
		return ma.sec(m)
	elif n=='cosec':
		return ma.cosec(m)

# create  a calculator

def add(num1, num2):
	return num1 + num2

def subtract(num1, num2):
	return num1 - num2


# Function to multiply two numbers
def multiply(num1, num2):
	return num1 * num2


# Function to divide two numbers
def divide(num1, num2):
	return num1 / num2


print("Please select operation -\n" \
	  "1. Add\n" \
	  "2. Subtract\n" \
	  "3. Multiply\n" \
	  "4. Divide\n")

select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
	print(number_1, "+", number_2, "=",
		  add(number_1, number_2))

elif select == 2:
	print(number_1, "-", number_2, "=",
		  subtract(number_1, number_2))

elif select == 3:
	print(number_1, "*", number_2, "=",
		  multiply(number_1, number_2))

elif select == 4:
	print(number_1, "/", number_2, "=",
		  divide(number_1, number_2))
else:
	print("Invalid input")