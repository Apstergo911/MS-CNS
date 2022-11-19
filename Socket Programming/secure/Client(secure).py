import socket

FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

HEADER = 64
PORT = 5510

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER , PORT)


client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

client.connect(ADDR)

message  = client.recv(1024).decode(FORMAT)
client.send(input(message).encode(FORMAT))

message  = client.recv(1024).decode(FORMAT)
client.send(input(message).encode(FORMAT))


print(client.recv(1024).decode(FORMAT))


