import socket

FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

HEADER = 64
PORT = 5511

CLIENT = socket.gethostbyname(socket.gethostname())
ADDR = (CLIENT , PORT)
SERVER = (CLIENT , 5510)

client = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

client.bind(ADDR)


client.sendto("".encode(FORMAT) , SERVER)

message ,addr = client.recvfrom(1024)
message = message.decode(FORMAT)

# if message == "Username:":
#     print(message)
#     send = f"{message}{input()}"
#     client.sendto(send.encode(FORMAT),(addr))
# elif message == "Password:":
#     print(message)
#     send = f"{message}{input()}"
#     client.sendto(send.encode(FORMAT),(addr))
# else:
#     print(message)





