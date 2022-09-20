# first of all import the socket library
import socket            
import mysql.connector
import datetime

# next create a socket object
s = socket.socket()        
print ("Socket Created")
port = 12345               
s.bind(('', port))      

# put the socket into listening mode
s.listen(5)    

mydb = mysql.connector.connect(
  host="localhost",
  user="mscproject",
  password="1234567eight",
  database="RTFSD"
)

mycursor = mydb.cursor()

bustrip_id = 1
bus_id = 1
trip_no = 1

t1 = 1

while t1:
 
# Establish connection with client.
  c, addr = s.accept()    
  print ('Got connection from client with address', addr )
  t2 = 1
 
  while t2:
  	cam1 = c.recv(1024).decode()
  	ex = 'ex'
  	if(cam1 == ex):
      tot_pass = cam1 + 0
      print ('Occupied Seats/Number of People : ' + tot_pass)

      sql = "INSERT INTO TRIP_001 (bustrip_id, bus_id, trip_no, t_date, t_day, t_time, last_stop, passenger_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
      
      current_time = datetime.datetime.now()
      
      t_date = current_time
      t_day = current_time.day
      t_time = current_time
      last_stop = xyz
      passenger_count = tot_pass
      
      val = (str(bustrip_id), str(bus_id), str(trip_no), str(t_date), str(t_day), str(t_time), str(last_stop), str(passenger_count))
      mycursor.execute(sql, val)
      bustrip_id = bustrip_id + 1

  	else:
      t1 = t2 = 0
      c.close()
      mydb.commit()
      exit(0)
