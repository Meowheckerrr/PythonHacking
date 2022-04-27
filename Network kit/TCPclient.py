import socket
from urllib import response


#to set up variables
targetHost ="www.google.com"  
targetPort= 80                



#to establish the socker object
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# to connect to the server/host 
client.connect((targetHost,targetPort))

#to sent date to the server
client.send(b"GET /HTTP/1.1\1.1\r\nHOST: google.com\r\n\r\n") #\r == enter 

#Receiver the date from server

response= client.recv(4096)

print(response.decode())
client.close()





