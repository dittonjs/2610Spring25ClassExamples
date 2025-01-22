import socket
from decoder import decode, encode
from router import router

# HTTP Request format:
# <start line>
# header1
# header2
# header3
#
# body

# headers
# key: value
# Content-Type: application/json

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
    s.bind(("127.0.0.1", 8000))
    s.listen()
    print("listening on port 8000")

    while True:
        connection, addr = s.accept()
        with connection:
            data = connection.recv(8192)

            if not data:
                continue

            request = decode(data)
            response = router(request)
            responseBytes = encode(response)

            connection.send(responseBytes)
