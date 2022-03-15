
import socket		 
import sys
from _struct import *
# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	  		 

try:
    # Reading IP Address
    host = "localhost"
    port = 5001                       # Reading port number
    # Connecting to server
    s.connect((host, port))                           
    print("Connected to server: ",  host, " in port: ",  port)
   

    while(True):
        answer=input("Do you want to read numbers from file or via keyboard? \n Type keyboard or file: ")
        if answer=="file" or answer=="keyboard":

            #To check if te filename exists
            found=True


            try:
                if answer=="file":
                    
                    filename=input("Name of the file: ")
                    try:
                        f= open(filename, 'r', encoding='utf8')
                        slist = f.read().splitlines()
                        x=int(slist[0])
                        y=int(slist[1])
                        z=slist[2]
                    except FileNotFoundError:
                        print("File Does not Exist. Try again! ")
                        found=False


                elif answer=="keyboard":
                    x=int(input("Read a Number: "))
                    y=int(input("Read a Second Number: "))
                    z=input("Type: \n add \n remove \n multi \n divide: ")

                if found==True and type(x)==int and type(y)==int and type(z)==str:    
                    s.send(pack('hh',x,y))
                    s.send(bytes(z,"utf-8"))

                    result=s.recv(1024).decode("utf-8")
                    print("The result is: " + result)
                else:
                    print("Invalid data. Try again.")
            except (IndexError, ValueError):
                print("Invalid data")


        else:
            print("Invalid data. Try again.")

        
 # Close the socket when done
    s.close 				

except (IndexError, ValueError):
                print("Invalid data")
except KeyboardInterrupt:
    print("\n Bye")
except ConnectionRefusedError:
    print("Server can't be found.")

