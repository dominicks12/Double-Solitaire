from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

connectionSocket1, addr = serverSocket.accept()
connectionSocket1.send("Start".encode())

connectionSocket2, addr = serverSocket.accept()
