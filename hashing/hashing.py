import hashlib

string = input("Enter a string: ")

hash = hashlib.sha256(string.encode("UTF-8")).hexdigest()

print(f"Hash: {hash}")
