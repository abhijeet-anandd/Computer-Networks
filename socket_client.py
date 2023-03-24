import socket as sk
server=sk.socket()
port=1026
server.connect(('127.0.0.1',port))
print server.recv(1024)
while True:
	print server.recv(1024)
	message=raw_input("Enter a message for server : ")
	server.send(message)
server.close()