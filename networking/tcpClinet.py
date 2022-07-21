
'''
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

'''
#p1 
'''
#serverIP="www.google.com"
serverIP="meowhecker.com"
serverPort= 6969

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((serverIP,serverPort))  # connect() takes exactly one argument (2 given)

client.send(b"meowhacker")   #client.send(b"GET /HTTP/1.1\r\nHOST: google.com\r\n\r\n")

receive = client.recv(4096)

if(receive == b"serverACK"):
    client.send(b"clientACK")
    print(1)

print(receive.decode())
client.close() 
'''
#p2
import socket
import argparse
import time
parser = argparse.ArgumentParser(
    description="Meohw hecker client programs",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="example\n"
    "python tcpClient.py -i meowhecker.com -p 6669 "
    )
# User interface 
parser.add_argument("-i", "--RHOST", help="input the server name", default="127.0.0.1", required=True)
parser.add_argument("-p", "--RPORT", type=int, help="input the server ports", default="6669", required=True)
group = parser.add_mutually_exclusive_group()
group.add_argument("-q", "--quite", help="don't display ditail information", action="store_true")
group.add_argument("-v", "--verbose", help="show detial information", action="store_true")
args= parser.parse_args()

def main():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((args.RHOST,args.RPORT))
    client.send(bytes("fwer564 ","utf-8"))
    '''
    message = client.recv(1024)
    print(message.decode("utf-8"))
    '''
    fullMessage=""
    while 1:
        message = client.recv(8)  # flow control (The receiver tells the sender how many bytes he could send) 1byte = char
        if len(message)<=0:
            break
        else:
            fullMessage += message.decode("utf-8")        
    print(fullMessage)

if __name__ == "__main__":
    main()
    connectFlag=1
    #group
    
    if args.verbose and connectFlag == 1:
        x=0
        while 1:
            x+=1
            print(f"Throught time = {x}")
            time.sleep(1)






