from socket import *
import time

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

connectionSocket1, addr = serverSocket.accept()
connectionSocket1.send("Welcome".encode())
connectionSocket1.send("1".encode())
connectionSocket2, addr = serverSocket.accept()
connectionSocket2.send("Welcome".encode())
connectionSocket2.send("2".encode())

connectionSocket1.send("Other player connected.".encode())
connectionSocket2.send("Other player connected.".encode())

count = 5
while count >= 0:
    connectionSocket1.send(("Game starting in" + count).encode())
    connectionSocket2.send(("Game starting in" + count).encode())
    time.sleep(1)
    count = count - 1

start_time = time.clock()

player1_score_update = connectionSocket1.recv(1024)
player2_score_update = connectionSocket2.recv(1024)

player1_score = 0
player2_score = 0

while not player1_score_update == "-1" and not player2_score_update == "-1":
    if player1_score_update == "5":
        player1_score = player1_score + 5
    elif player1_score_update == "10":
        player1_score = player1_score = 10

    if player2_score_update == "5":
        player2_score = player2_score + 5
    elif player2_score_update == "10":
        player2_score = player2_score + 10

    connectionSocket1.send(str(player1_score).encode())
    connectionSocket1.send(str(player2_score).encode())
    connectionSocket2.send(str(player1_score).encode())
    connectionSocket2.send(str(player2_score).encode())

    curr_time = time.clock()
    time_elapsed = curr_time - start_time

    connectionSocket1.send(str(time_elapsed).encode())
    connectionSocket2.send(str(time_elapsed).encode())

    connectionSocket1.send("continue".encode())
    connectionSocket2.send("continue".encode())

if player1_score_update == "-1":
    connectionSocket1.send(str(player1_score).encode())
    connectionSocket1.send(str(player2_score).encode())
    connectionSocket2.send(str(player1_score).encode())
    connectionSocket2.send(str(player2_score).encode())
    connectionSocket1.send(str(time_elapsed).encode())
    connectionSocket2.send(str(time_elapsed).encode())
    connectionSocket2.send("Player 1 has quit.".encode())
if player2_score_update == "-1":
    connectionSocket1.send(str(player1_score).encode())
    connectionSocket1.send(str(player2_score).encode())
    connectionSocket2.send(str(player1_score).encode())
    connectionSocket2.send(str(player2_score).encode())
    connectionSocket1.send(str(time_elapsed).encode())
    connectionSocket2.send(str(time_elapsed).encode())
    connectionSocket1.send("Player 2 has quit.".encode())

if player1_score > player2_score:
    connectionSocket1.send("Player 1 has won the game!".encode())
    connectionSocket2.send("Player 2 has won the game!".encode())
elif player2_score > player1_score:
    connectionSocket1.send("Player 2 has won the game!".encode())
    connectionSocket2.send("Player 2 has won the game!".encode())
else:
    connectionSocket1.send("Player 1 and Player 2 have tied!".encode())
    connectionSocket2.send("Player 1 and Player 2 have tied!".encode())
