
import socket, sys, hashlib
from datetime import datetime

SERVER_IP = '192.168.5.100'
SERVER_PORT = 2000
BUFFER_SIZE = 2048

try:
        Client_Obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.err as e:
        print("Error creating socket: %s" %e)
        sys.exit(1)

Client_Obj.connect((SERVER_IP,SERVER_PORT))

while True:
        MESSAGE = input("Enter the message and end with . :")
        if MESSAGE == '.':
                break
        Client_Obj.send(MESSAGE)
        hashdata_c = hashlib.sha512(MESSAGE).hexdigest()
        print ("HASH VALUE of Client Text:", hashdata_c)
        data = Client_Obj.recv(BUFFER_SIZE)
        print("MESSAGE Recieved Time:" , datetime.now().time())
        print ("Data recieved from server: ", data)
        hashdata_s = hashlib.sha512(data).hexdigest()
        print ("HASH VALUE of Serer Text:",hashdata_s)

Client_Obj.close()

        