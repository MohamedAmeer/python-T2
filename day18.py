# Create a DB with doctor and doctor ID & patients visited
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="king786")
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for i in mycursor:
    print(i)

# Get the doctor(s) who have more than 5 patients visited
mydb = mysql.connector.connect(host="localhost", user="root", password="king786", database="doctor")
mycursor = mydb.cursor()

sql =("INSERT INTO doctor (doc_name, doc_id, patient_visited) VALUES (%s,%s,%s)")
val = [("aravind", "123", "10"),
       ("vikram", "124", "0"),
       ("josh", "12", "7"),
       ("jack", "22", "0")]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted")

# Get the doctors with no patients visit

mydb = mysql.connector.connect(host="localhost", user="root", password="king786", database="doctor")
mycursor = mydb.cursor()

mycursor.execute("SELECT *FROM doctor WHERE patient_visited>5")
myres =mycursor.fetchall()

for x in myres:
    print(x)
