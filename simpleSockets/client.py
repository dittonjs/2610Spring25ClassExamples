import socket

# 144.39.196.110

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        data = input("Tell therapybot how you feel: ")
        if data == "exit":
            break
        s.connect(("144.39.196.110", 8000))
        s.sendall(data.encode())
        response = s.recv(8192)
        print(f"Therapybot: {str(response, 'utf-8')}")
