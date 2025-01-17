import socket

# HTTP Request format:
# <start line>
# header1
# header2
# header3
#
# body

# Start Line:
# <verb> <uri> <http version>
# GET POST PUT PATCH DELETE
# GET / HTTP/1.1
# GET /exports/data HTTP/1.1

# HTTP Response format:
# <start line>
# header1
# header2
# header3
#
# body

# Start Line:
# <http version> <status code> <status message|reason>
# HTTP/1.1 200 Ok
# HTTP/1.1 404 Not Found


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 8001))
    s.listen()
    print("listening on port 8001")

    while True:
        connection, addr = s.accept()
        with connection:
            data = connection.recv(8192)
            if not data:
                continue

            print(f"Received data:\n\n{data.decode('UTF-8')}")

            #TODO: parse the request, send through middleware and encode the response
            res = "HTTP/1.1 200 Ok\nConnection: close\n\n<h1>Hello, world! This is really cool!</h1>"

            connection.send(bytes(res, "UTF-8"))
