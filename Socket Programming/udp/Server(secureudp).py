import socket
import threading
import hashlib
import sqlite3

HEADER = 64
PORT = 5510
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER ,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
server.bind(ADDR)

def handle_client(message ,addr):
    message = message.decode(FORMAT)
    for i in message:
        if message == "":
            send = "Username:".encode(FORMAT)
            server.sendto( send , (addr))
        message , addr = server.recvfrom(1024)
        print("received")
        username = message.decode(FORMAT)
        print(f"[{addr}] {username}")

    req2 = "Password:".encode(FORMAT)
    server.sendto( req2 , (addr))
    message , addr = server.recv(1024)
    password = message
    print(f"[{addr}] {password}")



    # password = hashlib.sha256(password).hexdigest()
    

    # conn = sqlite3.connect("userdata.db")
    # cur = conn.cursor()

  
    # cur.execute("SELECT * FROM userdata WHERE username  = ? AND password = ?",(username,password))
    
    # # if cur.fetchall():
    # #     cclient.send("loging seccessful".encode(FORMAT))

    # # else:
    # #     cclient.send("loging fail".encode(FORMAT))

        

    
print(f"server is running and listening on {SERVER}")
while True:
    message , addr = server.recvfrom(1024)
    threading.Thread(target=handle_client, args = (message , addr)).start()


            

        

