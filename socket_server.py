import socket as sk
server=sk.socket()
port=1026
server.bind(('',port))
print "Socket bound to " + str(port)
server.listen(5)
print "Listening for activity"
while True:
	c, addr=server.accept()
	print "Connected to "+str(addr)
	c.send("You are now connected!")
	while True:
		message=raw_input("Enter the message :  ")
		c.send(message)
		print c.recv(1024)
	c.close()