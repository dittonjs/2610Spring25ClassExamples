import hashlib
import sqlite3
from hash_password import hash_password

def compare(password, db_hash, db_salt):
    hash, _ = hash_password(db_hash, db_salt)

    return db_hash == hash

# Connect to database
conn = sqlite3.connect("my_app_db.sqlite")

# prompt user for email and password
email = input("Type in your email: ")
password = input("Type in your password: ")

#find the user by their email
cursor = conn.cursor()
cursor.execute("SELECT * FROM user WHERE email=?", (email,))
user = cursor.fetchone()

#print result
if not user:
    print("User not found")
elif not compare(password, user[2], user[3]):
    print("Password does not match")
else:
    print("Logged in!")
