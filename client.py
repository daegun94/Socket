# Import socket module
import socket            
 
# Create socket
s = socket.socket()        
 
# Define the port on which you want to connect
port = 1500               
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))
 
# recv-> data receive (bufsize)
# return value is byte object which indicate receive data
print (s.recv(1024).decode())
# close the connection
s.close()    