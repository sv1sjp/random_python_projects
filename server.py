# Import socket module
import socket		 	 
import sys
from _struct import *

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		

# Get local machine name
host = "localhost"                 
port = 5001

# Bind to the port
s.bind((host, port)) 			 
s.listen(5) 			        

# Now wait for client connection.
print("Server is up and running")

while True:
     # Establish connection with client.
     c, addr = s.accept() 		
     print( addr , "is connected")

     while True:
          try:

               #Receiving the 2 numbers
               r=c.recv(4)
               
               x,y=unpack('hh',r)
               

               #Receiving which function 
               answer=c.recv(1024).decode("utf-8")
               

               
               if (x<0 or y<0) or (x>3000 or y>3000):
                    result="Invalid numbers"
               elif answer=="add":
                    result= str(x+y)
                    
               elif answer=="remove":
                    result= str(x-y)
                    
               elif answer=="multi":
                    result= str(x*y)
                    
               elif answer=="divide":
                    if y==0:
                         result="You can't divide with zero"
                    else:
                         result= str(x/y)
               else:
                    result="Invalid Parameter"

               c.send(bytes(result,"utf-8"))

               
                    
               
               

          
          
     
          except:
               break

# Close the connection.
     c.close() 			
