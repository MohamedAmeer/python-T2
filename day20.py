
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="king786",database="mydatabase")

mycursor = mydb.cursor()

sql ="INSERT INTO employee(emp_id, emp_name, emp_salary) VALUES (%s, %s, %s)"

val = [("1","mohamed","200000"),
("1","mohamed","200000"),
("2","ameer","20000"),
("3","vinoth","30000"),
("4","vicky","50000"),
("5","rogith","10000")]

mydb.commit()

print(mycursor.rowcount,"record inserted")

# GET A MAX & MIN SALARY FROM EMPLOYEE
mydb = mysql.connector.connect(host="localhost", user="root", password="king786",database="mydatabase")

mycursor = mydb.cursor()


mycursor.execute("SELECT emp_name,MAX(emp_salary), MIN(emp_salary) FROM employee")
max_min = mycursor.fetchmany()

for x in max_min:
    print(x)

# GET THE NO OF EMPLOYEES WORKING IN COMPANY
mydb = mysql.connector.connect(host="localhost", user="root", password="king786",database="mydatabase")

mycursor = mydb.cursor()

mycursor.execute("SELECT COUNT(*) FROM employee")
myres = mycursor.fetchall()

for x in myres:
    print(x)

# FIRST THREE CHAR OF FIRST NAME FROM EMPLOYEE TABLE
mydb = mysql.connector.connect(host="localhost", user="root", password="king786",database="mydatabase")

mycursor = mydb.cursor()
mycursor.execute("SELECT LEFT(emp_name,3) FROM employee")
myres1 = mycursor.fetchone()
print(myres1)
