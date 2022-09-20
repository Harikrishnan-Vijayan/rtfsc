import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="mscproject",
  password="1234567eight",
  database="RTFSD"
)

file1 = open('report.txt', 'w')

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM TRIP_001")

myresult = mycursor.fetchall()

file1.write(myresult)

file1.close()
