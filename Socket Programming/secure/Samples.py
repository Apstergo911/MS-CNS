import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTERGET PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    iteration VARCHAR(255)
)
""")

username1, password1 , iteration1 = "benign" , hashlib.sha256("benignpasswordnew".encode()).hexdigest() , 2
username2, password2 , iteration2 = "attacker" , hashlib.sha256("benignpassword".encode()).hexdigest() , 1

cur.execute("INSERT INTO userdata (username , password , iteration) VALUES (?, ? , ?)", (username1 , password1 , iteration1))
cur.execute("INSERT INTO userdata (username , password , iteration) VALUES (?, ? , ?)", (username2 , password2 , iteration2))

conn.commit()

print(password1 , f"iteration: {iteration1}")
print(password2 , f"iteration: {iteration2}")