import socket
from _thread import *
import sys
from player import Player
import pickle

server = "192.168.2.150"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((server, port))
except socket.error as e:
	str(e)

s.listen(2) #argument is how many clients can connect (if blank, unlimited)
print("Waiting for connection, Server Started")

players = [Player(0, 0, 50, 50, (255, 0, 0)), Player(100, 100, 50, 50, (0, 0, 255))]

def threaded_client(conn, player):
	conn.send(pickle.dumps(players[player]))
	reply = ""
	while True:
		try:
			data = pickle.loads(conn.recv(2048))
			players[player] = data

			if not data:
				print("Disconnected")
				break
			else:
				if player == 1:
					reply = players[0]
				else:
					reply = players[1]

				print("Received: ", data)
				print("Sending: ", reply)

			conn.sendall(pickle.dumps(reply))
		except:
			break

	print("Lost connection")
	conn.close()

currentPlayer = 0
while True:
	conn, addr = s.accept()
	print("Connected to: " + str(addr))

	start_new_thread((threaded_client), (conn, currentPlayer))
	currentPlayer += 1
