import socket

HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Enter message: ")

    if message.lower() == "exit":
        break

    client.sendto(message.encode(), (HOST, PORT))

    data, server_address = client.recvfrom(1024)

    print("Server:", data.decode())

client.close()
