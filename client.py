from socket import *
serverName = '0.tcp.ngrok.io'
serverPort = 11517
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# print(clientSocket.recv(1024).decode())
while True:
    sentence = input()
    clientSocket.send(sentence.encode())