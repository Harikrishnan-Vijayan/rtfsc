import socket      
import datetime

s = socket.socket()        
print ("Socket Created")

port = 12345               
s.bind(('', port))        
s.listen(5)   

file1 = open('report.txt', 'w')
L = ["TRIP NUMBER \t","LAST STOP \t", "PASSENGERS COUNT\t", "DATE AND TIME\t","\n"]
file1.writelines(L)
t1 = 1

trip_id = 1234
l_stop = "Stop Name"

while t1:
   
  c, addr = s.accept()    
  print ('Got connection from client with address', addr )
  print ('Total seat count : 50')
   
  t2 = 1
  while t2:
    cam1 = c.recv(1024).decode()
    
    if((float(cam1)) % 1 == 0):
      print ("Free Seats in the bus :", + 50-int(cam1))
      print ('Occupied Seats/Number of People : ' + cam1)
      current_time = datetime.datetime.now()
      t_date = current_time
      L = [str(trip_id),"\t \t \t",str(l_stop),"\t \t", str(cam1),"\t \t", str(t_date),"\t","\n"]
      file1.writelines(L)

    else:
      t1 = t2 = 0
      c.close()
      file1.close()
      exit(0)