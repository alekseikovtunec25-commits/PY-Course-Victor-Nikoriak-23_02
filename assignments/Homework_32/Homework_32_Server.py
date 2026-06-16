#Task1
socket.sendto()
socket.recvfrom()

# Сервер

import socket

HOST = "127.0.0.1"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((HOST, PORT))

print(f"UDP Server started on {HOST}:{PORT}")

while True:
    data, address = server.recvfrom(1024)

    message = data.decode()

    print(f"Received from {address}: {message}")

    response = f"Server received: {message}"

    server.sendto(response.encode(), address)



