import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="mscproject",
  password="1234567eight",
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE myproject")