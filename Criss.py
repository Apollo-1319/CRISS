import socket

serverIP = '172.17.29.11'
serverPORT = 6000

serveraddress = (serverIP, serverPORT)
buffersize = 1024

LDPClientSocket = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)

message = 'Hi, My name is G Puneeth Kumar. I am attending CRISS Workshop'

bytestosend = str.encode(message)

LDPClientSocket.sendto(bytestosend, serveraddress)