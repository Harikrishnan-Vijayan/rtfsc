import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="mscproject",
  password="1234567eight",
  database="RTFSD"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")