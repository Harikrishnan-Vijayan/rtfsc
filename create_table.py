import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="mscproject",
  password="1234567eight",
  database="RTFSD"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE TRIP_001 (bustrip_id INT(25) PRIMARY KEY, bus_id INT(25) NOT NULL, trip_no INT(25) NOT NULL, t_date VARCHAR(55) NOT NULL, t_day VARCHAR(55) NOT NULL, t_time VARCHR(55) NOT NULL, last_stop VARCHAR(55), passenger_count INT(10))")
