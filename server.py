import socket

SERVER_ADDRESS = input("Server IP: ")
SERVER_PORT = int(input("Server Port: "))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
server_socket.listen(1)
print("Listening...")
client_socket, client_address = server_socket.accept()
print("Connected...")

while True:
	try:
		traffic = client_socket.recv(4096)
		if not traffic: 
			break
		print(traffic.decode('utf-8'))
	except:
		break
client_socket.close()
