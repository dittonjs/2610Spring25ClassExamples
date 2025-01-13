import socket

# 144.39.196.110

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("144.39.196.110", 8000))
    print("Waiting for connection...")
    s.listen()
    conn, addr = s.accept()
    print(f"Someone connected to your server! {conn} {addr}")
