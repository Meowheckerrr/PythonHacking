import argparse #user interface 
import subprocess #execute cmd 
import sys        #shell 
import socket 
import textwrap
import threading
import shlex

# use argarse to create the commend interface.

# parser: argument container 
parser = argparse.ArgumentParser(
    description="NetCat by meowhecker!!!",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=textwrap.dedent('''
    example:
    netcatMeowhecker.py -t 0.0.0.0 -p 6669 -l #connect to the targetHost
    netcatMeowhecker.py -t 0.0.0.0 -p 6669 -l -c # shell mode
    netcatMeowhecker.py -t 0.0.0.0 -p 6669 -l -u=upload.txt # uploadfile
    netcatMeowhecker.py -t 0.0.0.0 -p 6669 -l -e=~~~# execute commend
    '''))

parser.add_argument("-c", "--commend", action="store_true", help="commend shell")
parser.add_argument("-e", "--execute", help="execute special commend")
parser.add_argument("-l", "--listen", action="store_true", help="listen")
parser.add_argument("-p", "--port", type=int, help="specified port")
parser.add_argument("-t", "--target", help="specified target")
parser.add_argument("-u", "--upload", help="upload the file")
args = parser.parse_args()

def execute(cmd):
    cmd=cmd.strip()
    if not cmd:
        return
    output=subprocess.check_output(shlex.split(cmd),stderr=subprocess.STDOUT)
    return output.decode()


class netCat:
    def __init__(self, args, buffer=None):
        self.args=args
        self.buffer=buffer
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#setsockopt(level,optionName,value) 
        # socket.SQL_SOCKET:　socket is using this option
        # socket.SO_REUEADDR: socket release port instantly 

    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()


    def job(self, clientSocket):
        if self.args.execute:
            commend = execute(self.args.execute)
            clientSocket.send(commend.encode())
        elif self.args.upload:
            fileBuffer=b''

            while True:
                fileData = clientSocket.recv(4096)
                if fileData:
                    fileBuffer += fileData
                else:
                    break
            with open(self.args.upload,"wb") as fileupload:
                fileupload.write(fileBuffer)
            message = f'file save{self.args.upload}'
            clientSocket.send(message.encode())

        elif self.args.commend:
            commendBuffer=b''
            #print("meow")
            while True:
                try:
                    clientSocket.send(b'Meowhecker#>')
                    while '\n' not in commendBuffer.decode():
                        #print("meowB")
                        commendBuffer += clientSocket.recv(64)
                        #print("meowC")
                    response = execute(commendBuffer.decode())
                    #print("meowD")
                    if response:
                        clientSocket.send(response.encode())
                        #print("meow1")
                    #print("meowA")
                    commendBuffer=b''
                except Exception as e:
                    print(f'sever killed {e}')
                    self.socket.close
                    sys.exit()
    def listen(self):
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)
        print(f'listening on {self.args.target}:{self.args.port}')
        while 1:
            clientSocket, address= self.socket.accept()
            print(f'connection from {address[0]}:{address[1]}')
            thread = threading.Thread(target=self.job, args=(clientSocket,))
            thread.start()
        
    def send(self):
        #print("meow2")
        self.socket.connect((self.args.target,self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)

        try:
            receiveLen = 1
            response=''
            while receiveLen:
                message = self.socket.recv(4096)
                receiveLen = len(message)
                response += message.decode
                if receiveLen < 2:
                    break

                if response:
                    print(response)
                    buffer=input('MeowheckerShellResponse:#>')
                    buffer+='\n'
                    self.socket.send(buffer.encode())
            
        except KeyboardInterrupt:
            print("Netcat terminated")
            self.socket.close()
            sys.exit()
             
if __name__ =="__main__":
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()
    nc =netCat(args,buffer.encode)
    nc.run()
