from socket import *
import _thread
import time
from deck import Deck
import pickle


def new_client(clientSocket, this_client_num, this_score1, this_score2):
    clientSocket.send(str(this_client_num).encode())

    start_time = time.process_time()

    global player1_status
    global player2_status
    global player_deck

    # deck = pickle.dumps(player_deck)
    # clientSocket.send(deck)
    # score_update = clientSocket.recv(1024).decode()

    while player1_status == "continue" and player2_status == "continue":
        score_update = clientSocket.recv(1024).decode()
        print(score_update)
        print(this_score1)
        print(this_client_num)
        if not score_update == "-1":
            if score_update == "5":
                if this_client_num == 1:
                    this_score1 = this_score1 + 5
                    print("made it here" + str(this_score1))
                if this_client_num == 2:
                    this_score2 = this_score2 + 5
                    print("made it here" + str(this_score2))
            elif score_update == "10":
                if this_client_num == 1:
                    this_score1 = this_score1 + 10
                if this_client_num == 2:
                    this_score2 = this_score2 + 10

            clientSocket.send(str(this_score1).encode())
            clientSocket.send(str(this_score2).encode())

            curr_time = time.process_time()
            elapsed_time = curr_time - start_time
            print("made it here too")
            clientSocket.send(str(elapsed_time).encode())
            clientSocket.send("continue".encode())

            # if client_num == 1:
                # player1_status = clientSocket.recv(2000).decode()
            # elif client_num == 2:
                # player2_status = clientSocket.recv(2000).decode()

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

    global sock
    sock.close()


sock = socket(AF_INET, SOCK_STREAM)
port = 12000

sock.bind(("", port))
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
    _thread.start_new_thread(new_client(client, client_number, score1, score2), ())

sock.close()