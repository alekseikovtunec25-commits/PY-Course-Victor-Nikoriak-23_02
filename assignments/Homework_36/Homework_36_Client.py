import socket

HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect((HOST, PORT))

while True:

    message = input("Enter message: ")

    if message.lower() == "exit":
        break

    client.send(message.encode())

    response = client.recv(1024)

    print(
        "Server:",
        response.decode()
    )

client.close()
