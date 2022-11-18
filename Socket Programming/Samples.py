import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTERGET PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "benign" , hashlib.sha256("benignpasswordnew".encode()).hexdigest()
username2, password2 = "attacker" , hashlib.sha256("benignpassword".encode()).hexdigest()
cur.execute("INSERT INTO userdata (username , password) VALUES (?, ?)", (username1 , password1))
cur.execute("INSERT INTO userdata (username , password) VALUES (?, ?)", (username2 , password2))

conn.commit()

print(password1)
print(password2)