#!/bin/env/python3
host = input('enter your ip:') 
port = input('enter your port:') 
server = socket.socket()
server.bind ((host, port)) 
server.listen
conn, addr = server.accept() 
conn.close
