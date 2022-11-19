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

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(cclient , addr):
    print(f"[NEW CONNECTION] {addr} Connected")
    
    cclient.send("Username:".encode(FORMAT))
    username = cclient.recv(1024).decode(FORMAT)
    print(f"[{addr}] {username}")
    
    cclient.send("Password:".encode(FORMAT))
    password = cclient.recv(1024)
    print(f"[{addr}] {password}")
    
    if (username or password) == DISCONNECT_MESSAGE:
        cclient.close()
    else:
        pass

    password = hashlib.sha256(password).hexdigest()
    

    conn = sqlite3.connect("userdata.db")
    cur = conn.cursor()

  
    cur.execute("SELECT * FROM userdata WHERE username  = ? AND password = ?",(username,password))
    
    if cur.fetchall():
        cclient.send("loging seccessful".encode(FORMAT))

    else:
        cclient.send("loging fail".encode(FORMAT))

        
def start():
    server.listen()
    print(f"server is running and listening on {SERVER}")
    while True:
        client , addr = server.accept()
        threading.Thread(target=handle_client, args = (client, addr)).start()
start()

            

        

