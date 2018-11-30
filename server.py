from socket import *
import _thread
import time
import asyncio
from deck import Deck
import pickle


def new_client(clientSocket, this_client_num):
    # lock = asyncio.Lock()

    # async with lock:
    clientSocket.send(str(this_client_num).encode())

    global player1_status
    global player2_status
    global score1
    global score2
    global start_time

    # deck = pickle.dumps(player_deck)
    # clientSocket.send(deck)
    # score_update = clientSocket.recv(1024).decode()

    while player1_status == "continue" and player2_status == "continue":
        # lock = asyncio.Lock()
        # async with lock:
        score_update = clientSocket.recv(1024).decode('utf-8')
        print("Received score update from " + str(client_number) + ": " + str(score_update))
        if not score_update == "-1":
            if score_update == "5":
                if this_client_num == 1:
                    score1 = score1 + 5
                    print("Added 5 points to Player 1's score.")
                    # print("made it here" + str(this_score1))
                if this_client_num == 2:
                    score2 = score2 + 5
                    print("Added 5 points to Player 2's score.")
                    # print("made it here" + str(this_score2))
            elif score_update == "10":
                if this_client_num == 1:
                    score1 = score1 + 10
                    print("Added 10 points to Player 1's score.")
                if this_client_num == 2:
                    score2 = score2 + 10
                    print("Added 10 points to Player 2's score.")
            # lock = asyncio.Lock()
            # async with lock:
            message = clientSocket.recv(1024).decode('utf-8')

            # lock = asyncio.Lock()
            # async with lock:
            if message == "ready":
                # time.sleep(.1)
                clientSocket.send(str(score1).encode())

            # lock = asyncio.Lock()
            # async with lock:
            message = clientSocket.recv(1024).decode('utf-8')

            # lock = asyncio.Lock()
            # async with lock:
            if message == "ready":
                clientSocket.send(str(score2).encode())

            print("Sent Player 1 and Player 2 scores to Player " + str(client_number))
            curr_time = time.clock()
            elapsed_time = curr_time - start_time
            # print("made it here too")

            # lock = asyncio.Lock()
            # async with lock:
            message = clientSocket.recv(1024).decode('utf-8')

            # lock = asyncio.Lock()
            # async with lock:
            if message == "ready":
                # time.sleep(.1)
                clientSocket.send(str(elapsed_time).encode())
            print("Sent elapsed time to Player " + str(client_number))

            # lock = asyncio.Lock()
            # async with lock:
            message = clientSocket.recv(1024).decode('utf-8')

            # lock = asyncio.Lock()
            # async with lock:
            if message == "ready":
                # time.sleep(.1)
                clientSocket.send("continue".encode())

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
sock.listen()

client_number = 0

score1 = 0
score2 = 0

player1_status = "continue"
player2_status = "continue"

start_time = time.clock()

# player_deck = Deck()
while True:
    client, address = sock.accept()
    client_number = client_number + 1
    _thread.start_new_thread(new_client, (client, client_number))

# sock.close()
