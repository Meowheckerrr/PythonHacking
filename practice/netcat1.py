import argparse
import textwrap
import subprocess
import shlex
import socket
import threading


parser = argparse.ArgumentParser(
    description="use python to instead with netcat" ,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=textwrap.dedent(
        '''
        meow meow meow meow
        '''
        )    
    )
        
parser.add_argument('-t', '--target', help="target host")
parser.add_argument('-p', "--port", type=int, help="target port")

parser.add_argument('-l', "--listen", help="Listening on the target!!",action="store_true")
parser.add_argument('-c', "--commend", help="Input the commend")
parser.add_argument('-o', "--order", help="Execute order and send messages to clientend")
args = parser.parse_args()

class netCat:
    def __init__(self,args,buffer):
        self.args=args
        self.buffer=buffer
        self.socket=socket.socket(socket.socket(socket.AF_INET,socket.SOCK_STREAM))
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.target=args.target
        self.port=args.port

    def listen(self):
        server=self.socket
        server.bind((self.target,self.port))
        print(f"Server start to listening on {self.target}:{self.port}")
        server.listen(10)
        while 1:
            clientSocket,address = server.accept()
            print(f"connection from {address[0]}:{address[1]}")
            thread=threading.Thread(target=self.clientHandler,args=(clientSocket))
            thread.start()

    def clientHandler(self,clientSocket):
        with clientSocket as socket:
            if self.args.order:
                cmdOutput=self.executeShellCommend(self.args.order)
                

            if self.args.commend:
                self.connectCLientSend()
                        
                    
    def connectClientSend(self):
        self.socket.connect((self.target,self.port))

        if self.buffer:
            self.buffer.send(1024)

        while 1:
            try:
                receLen = 1 
                buffer=""
                while receLen:
                    message += socket.recv(1024)
                    

                
            except:

        

                    

                

            

            
            
        

        



def executeShellCommend(commend):
    commend = commend.strip()
    if not commend:
        return

    commendOutput=subprocess.check_output(shlex.split(commend), stderr=subprocess.STDOUT)
    return commendOutput



if __name__ == "__main__":
    #print(executeShellCommend(args.commend))
    if args.listen:
        buffer=""
    nc = netCat(args, buffer.encode())
    nc.run()
    


        #print("connection from {sef.args.target}:{sef.args.target} has been established !!!")
    