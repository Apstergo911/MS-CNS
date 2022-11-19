import socket

FORMAT = 'utf-8'
server   = ("127.0.0.1", 5510)
bufferSize          = 1024

# Create a UDP socket at client side
client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)




msgFromClient       = input() 
bytesToSend         = msgFromClient.encode(FORMAT)

# Send to server using created UDP socket

client.sendto(bytesToSend, server)
while (True):
    client.sendto(input().encode(FORMAT),server)
    message , address = client.recvfrom(bufferSize)
    servermessage = message.decode(FORMAT)
    

    msg = f"{address} {servermessage}"

    print(msg)