


'''
import socket
import threading



ip= '0.0.0.0'
port= 9997

def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((ip,port))
    server.listen(5)
    print(f'[*] Listening on {ip}:{port}')

    while True:
        client,address = server.accept()
        print(f'[*] Acepted connection from {address[0]:address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as socket:
        request = socket.recv(1024)
        print(f'[*]Rrceived :{request.decode("utf-8")}')
        socket.send(b"ACK")

if __name__ == '__main__':
    main()
'''

'''P1
import socket
import threading

rHost="meowhecker.com"
rPort=6969

def job(clientData):
    with clientData as socket:
        request=socket.recv(4096)
        print(f'Received:{request.decode("utf-8")}')
        socket.send(b'serverACK')

     
        if request==b"clientACK":
            print(1)
            print("thress way shakehand compelete!!!!")

def mainServer():
    server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((rHost,rPort))
    server.listen(10) #排隊
    print(f'listening on {rHost}:{rPort}')
    
    while 1:
        clientData,address =server.accept()   # declare cleintData is client detail information
        # print(f'Acepted connection from {address[0]:address[1]}')
        thread = threading.Thread(target=job,args=(clientData,))
        thread.start()
        thread.join
        
if __name__ =="__main__":
    mainServer()

'''
#p2
import socket
import threading
import argparse
import textwrap
parser=argparse.ArgumentParser(
        description="TCP meowhecer sever ",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="example= tcpServer.py -i meowhecker.com -r 6669\n"
        )
parser.add_argument("-i", "--LHOST", help="set self host address !!", default="meowhecker.com",required=True)
parser.add_argument("-p", "--LPORT", type=int, help="set self host Port !!", default=6669, required=True)
args = parser.parse_args()
       
def clientHandler(socketClient):  # job 1 
    with socketClient as sockets:
        password = sockets.recv(1024)
        print(f'Receive from clientHost, password is {password.decode("utf-8")}')

        socketClient.send(bytes(  #Due to TCP is stream-oriented, we need to use byts() or b'' to send and incoding
            textwrap.dedent('''
                welcome to meowhecer TCP server!!!!!!!!!
                meow meow meow meow~~ 
                ServerACK'''),
            "utf-8" 
            ))       #send (bytes("messages","encoding"))
        socketClient.close()  # if you don't close, it will occur problems but I don't know why XD oh noooooooo!

def server(LHOST,LPORT):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((LHOST,LPORT))
    server.listen(10) # queue 
    print(f'[*] listening on {LHOST}:{LPORT}')

    while 1:
        socketClient, address = server.accept()
        print(f'[*] Connection form {address[0]}:{address[1]} has been edstablished !!!!')
        thread = threading.Thread(target=clientHandler,args=(socketClient,))
        thread.start()
        thread.join() #無聊亂寫 haaaaa (Berfore subthreading job has been all down, the following program will wait for it. 
        
if __name__=="__main__":
    server(args.LHOST,args.LPORT)




