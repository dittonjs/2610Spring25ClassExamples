import hashlib
import secrets

# password123a4363fc
# Better version
def hash_password(password, salt=secrets.token_hex(8), rounds=10):

    hash = hashlib.sha256(bytes(password + salt, "UTF-8")).hexdigest()

    for _ in range(rounds):
        hash = hashlib.sha256(bytes(hash, "UTF-8")).hexdigest()

    return (hash, salt)


# Bad version
# def hash_password(password):
#     hash = hashlib.sha256(bytes(password, "UTF-8")).hexdigest()

#     return hash
