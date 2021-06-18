# create a function to perform addition,subtraction,multiplication,division
def add(x, y):
    return x + y


print("Addition")
a = int(input("Enter Number:"))
b = int(input("Enter Another Number:"))
c = add(a, b)
print("Addition of Two Numbers", a, "+", b, "is:", c)


def sub(x, y):
    return x - y


print(" ")
print("Subtraction")
a = int(input("Enter Number:"))
b = int(input("Enter Another Number:"))
c = sub(a, b)
print("Subtraction of Two Numbers", a, "-", b, "is:", c)


def mul(x, y):
    return x * y


print(" ")
print("Multiplication")
a = int(input("Enter Number:"))
b = int(input("Enter Another Number:"))
c = mul(a, b)
print("Multiplication of Two Numbers", a, "*", b, "is:", c)


def div(x, y):
    return x / y


print(" ")
print("Division")
a = int(input("Enter Number:"))
b = int(input("Enter Another Number:"))
c = div(a, b)
print("Division of Two Numbers", a, "/", b, "is:", c)


# create a function  covid perform some operation

def covid(patient_name, body_temperature = 89):
   print(f"patient name {patient_name} body temperature{body_temperature}")

covid("alex")
