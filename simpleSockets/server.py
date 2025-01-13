import socket

# 144.39.196.110

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("144.39.196.110", 8000))
    print("Waiting for connection...")
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Someone connected to your server! {conn} {addr}")

            data = conn.recv(8192)
            if not data:
                continue
            print(f"Message recieved: {str(data, 'utf-8')}")
            response = "Interesting... Tell me more."
            conn.sendall(response.encode())
