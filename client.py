import socket

SERVER_ADDRESS = input("Server IP: ")
SERVER_PORT = int(input("Server Port: "))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
print("Connected...")

while True:
	traffic = input("> ")
	client_socket.sendall(traffic.encode())
client_socket.close()
