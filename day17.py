# create a connection for db
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="king786")

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)


# creating multiple tables and insert values

mydb =mysql.connector.connect(host="localhost", user="root", password="king786", database ='db1')
mycursor = mydb.cursor()

sql = "INSERT INTO student(name, studid ) VALUES (%s, %s)"

val = ("mohamed", "01")

mycursor.execute(sql, val)
mydb.commit()

mydb =mysql.connector.connect(host="localhost", user="root", password="king786", database ='db1')
mycursor = mydb.cursor()

sql = "INSERT INTO student1(name, stud_id ) VALUES (%s, %s)"

val = ("AMEER", "02")

mycursor.execute(sql, val)
mydb.commit()

# create employee table

mydb =mysql.connector.connect(host="localhost", user="root", password="king786", database ='db1')
mycursor = mydb.cursor()

sql = "INSERT INTO employee(name, emp_id ) VALUES (%s, %s)"

val = [("AMEER", "02"),
       ("ARUN", "03"),
       ("THARUN", "04"),
       ("ANAND", "05"),
       ("VICKY", "06")]

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "was inserted")

mycursor.execute("SELECT name FROM employee")
myres = mycursor.fetchall()

for x in myres:
    print(x)