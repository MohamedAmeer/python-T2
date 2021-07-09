# import json into sql db
import json
import mysql.connector

import pyodbc as pyodbc

a = [
    {
        "name": "ameer",
        "id": 2,
        "address": "abcjssladjdj",
        "gmail": "asdfg123@gmail",
        "ph_no": 9876543210,
        "dec": "true"
    },

    {
        "name": "arun",
        "id": 2,
        "address": "ujadifojefed",
        "gmail": "abc@gmail",
        "ph_no": 123456789,
        "dec": "true"

    }
]
b = json.dumps(a)
print(b)

mydb =mysql.connector.connect(host="localhost", user="root", password="king786", database='db1')
mycursor = mydb.cursor()



conn = pyodbc.connect('DRIVER={SQL Server};SERVER={localhost};DATABASE={db1}')
cursor = conn.cursor()
for a in json:
    print(json.dumps(a))
    cursor.execute("Insert Into egad values ?", json.dumps(a))
    cursor.commit()
cursor.close()
conn.close()

