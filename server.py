import socket
import _thread
import time
from deck import Deck
import pickle


def new_client(clientSocket, client_num):
    clientSocket.send(str(client_num).encode())

    start_time = time.perf_counter()

    global score1
    global score2
    global player1_status
    global player2_status
    global player_deck

    # deck = pickle.dumps(player_deck)
    # clientSocket.send(deck)
    score_update = clientSocket.recv(2000).decode()

    while player1_status == "continue" and player2_status == "continue":
        if not score_update == "-1":
            if score_update == "5":
                if client_num == 1:
                    score1 = score1 + 5
                if client_num == 2:
                    score2 = score2 + 5
            elif score_update == "10":
                if client_num == 1:
                    score1 = score1 + 10
                if client_num == 2:
                    score2 = score2 + 10
            clientSocket.send(str(score1).encode())
            clientSocket.send(str(score2).encode())

            curr_time = time.perf_counter()
            elapsed_time = curr_time - start_time

            clientSocket.send(str(elapsed_time).encode())
            clientSocket.send("continue".encode())

            if client_num == 1:
                player1_status = clientSocket.recv(2000).decode()
            elif client_num == 2:
                player2_status = clientSocket.recv(2000).decode()

    if player1_status == "quit":
        clientSocket.send("Player 1 has quit the game.".encode())
    elif player2_status == "quit":
        clientSocket.send("Player 2 has quit the game.".encode())

    if score1 > score2:
        clientSocket.send("Player 1 has won!".encode())
    elif score2 > score1:
        clientSocket.send("Player 2 has won!".encode())
    else:
        clientSocket.send("Both players have tied!".encode())


sock = socket.socket()
host_name = socket.gethostname()
port = 12000

sock.bind((host_name, port))
sock.listen(5)

client_number = 0

score1 = 0
score2 = 0

player1_status = "continue"
player2_status = "continue"

player_deck = Deck()

while True:
    client, address = sock.accept()
    client_number = client_number + 1
    _thread.start_new_thread(new_client(client, address, client_number))

sock.close()