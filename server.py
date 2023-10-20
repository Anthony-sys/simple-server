#!/bin/env/python3
import socket
host = input('enter your ip:') 
port = input('enter your port:') 
server = socket.socket()
server.bind ((host, int(port))) 
server.listen(5)
conn, addr = server.accept() 
conn.close
