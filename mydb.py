

import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    port=3360,
    user='root',
    passwd='root'
)

# prepare a cursor object

cursorObject = dataBase.cursor()

# Create a DataBase

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")
