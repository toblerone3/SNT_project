import socket, sys, hashlib
from threading import Thread
from SocketServer import ThreadingMixIn
from datetime import datetime

class Thread_Of_Client(Thread):
	def __init__(self,ip,port):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		print ("Server :" + ip + ":" + str(port))

	def run(self):
		while True:
			data = conn.recv(2048)
			print ("Time:",datetime.now().time())
			print ("Server Received:",data)
			hashdata = hashlib.sha512(data).hexdigest()
			print ("HASH VALUE of client text:", hashdata)
			print ("type the messsage")
			MESSAGE = raw_input("Enter the Response and end with ")
			if MESSAGE == '.':
				break
			conn.send(MESSAGE)
			hashdata_s = hashlib.sha512(MESSAGE).hexdigest()
			print ("HASH VALUE of server text: ", hashdata_s)

SERVER_IP = '192.168.3.100'
SERVER_PORT = 2000
SERVER_SIZE = 2048


try:
	Server_Obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
	print("Error creating socket: %s" % e)
	sys.exit(1)

Server_Obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
Server_Obj.bind((SERVER_IP, SERVER_PORT))
threads = []
while True:
	Server_Obj.listen(5)
	print ("waiting for connection from client ")
	(conn, (ip,port)) = Server_Obj.accept()
	newthread = Thread_Of_Client(ip,port)
	newthread.start()
	threads.append(newthread)
for t_Obj in threads:
	t_Obj.join()

Server_Obj.close()
