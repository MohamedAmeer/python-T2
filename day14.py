# List down all the error types and check all the errors using a python program for all errors.

ZeroDivisionError


class ZeroDivisionError:
 try:
     print(3 / 0)
except ZeroDivisionError:
print("Unable to divide by zero")


IndexError


class IndexError:
    Ie = [1, 2, 3]


try:
    print(Ie[3])
except IndexError:
    print('Index not found in array')

#Indexnot found in array

ModuleNotFoundError


class ModuleNotFoundError:
    try:
        import modules

except ModuleNotFoundError:
print("Module not found")

#Modulenot found
KeyError


class KeyError:
    dicti = {"1": 1, "2": 2, "3": 3}
try:
    print(dicti["4"])
except KeyError:\
    print('key not found in dictionary')

#keynot found in dictionary

# Design a simple calculator app with try and except for all use cases.

symbols = '+ - x / % \n'
try:
    a = int(input('Enter a :'))
    print(symbols)
    calculator = input('Choose symbol from above :')
    b = int(input('Enter b :'))

    if calculator in symbols:
        if calculator == '+':
            print(a + b)
        elif calculator == '-':
            print(a - b)
        elif calculator == 'x':
            print(a * b)
        elif calculator == '/':
            print(a / b)
        elif calculator == '%':
            print(a % b)

except ValueError:
    print("Enter proper number !")
except ZeroDivisionError:
 print("Zero is not possible in divide !")

#Entera: 20+ - x / %+

#Choosesymbolfrom above: %Enterb: sEnterpropernumber !
# print one message if the try block raises a NameError and another for other errors
try:
    print("Errorname")
except NameError:
    print("Errorname is not found")
except:
 print("Unknown Error")

# Errorname is not found

# When try-except scenario is not required?
# The ANS is-:try-except scenario is not required if you are not going to have any runtime error in your python program.

# Try getting an input inside the try catch block

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid number")
