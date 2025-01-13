import socket

# <start line>
# header1
# header2
# header3
#
# body

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 8000))
    s.listen()
    print("listening on port 8000")

    while True:
        connection, addr = s.accept()
        with connection:
            data = connection.recv(8192)
            if not data:
                continue

            print(f"Received data:\n\n{data.decode('UTF-8')}")

            #TODO: parse the request, send through middleware and encode the response
            res = "HTTP/1.1 200 Ok\nConnection: close\n\n<h1>Hello, world!</h1>"

            connection.send(bytes(res, "UTF-8"))
