from fileinput import close
import socket


'''
#to set up variables
targetHost ="127.0.0.1" 
targetPort= 443



#to establish the socker object
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#to sent date to the server
client.sendto(b"AAABBBCCC",(targetHost,targetPort)) #\r == enter

#Receiver the date from server

data, addr =client.recvfrom(4096)

print(data.decode())
client.close()
'''

serverIp= "meowhecker.com"
serverPort= 80

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto(b"MEOWHECKER",(serverIp,serverPort))
receive = client.recvfrom(4096)

print(receive.decode())
client.close



