import socket
import hashlib
import sqlite3

localIP     = "127.0.0.1"
localPort   = 5510
bufferSize  = 1024
FORMAT = 'utf-8'
 
# Create a datagram socket
server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 
# Bind to address and ip
server.bind((localIP, localPort))

 
print(f"UDP server up and listening on {localIP , localPort}")

msgFromServer       = "Hello UDP Client"
bytesToSend         = msgFromServer.encode(FORMAT)

def passcheck(username , password):
    password = password.encode(FORMAT)
    password = hashlib.sha256(password).hexdigest()
    db = sqlite3.connect("userdata.db")
    cur = db.cursor()
    cur.execute("SELECT * FROM userdata WHERE username  = ? AND password = ?",(username,password))
    
    if cur.fetchall():
        print('correct')

    else:
        print('correct')



# Listen for incoming datagrams
while(True):
    message , address = server.recvfrom(bufferSize)
    server.sendto("welcome".encode(FORMAT), address)
    username = message.decode(FORMAT)
    clientMsg = f"{address}: {username}"
    print(f"username is: {username}")
    break

while(True):
    message , address = server.recvfrom(bufferSize)
    server.sendto("welcome".encode(FORMAT), address)
    password = message.decode(FORMAT)
    clientMsg = f"{address}: {password}"
    print(f"password is: {password}")
    break


passcheck(username = username , password = password)

while(True):
    message , address = server.recvfrom(bufferSize)
    print(message.decode(FORMAT))
    server.sendto("welcome".encode(FORMAT), address)