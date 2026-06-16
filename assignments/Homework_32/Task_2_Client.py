import socket

HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

message = input("Enter message: ")
key = input("Enter key: ")

client.send(f"{message}|{key}".encode())

encrypted = client.recv(1024).decode()

print("Encrypted message:", encrypted)

client.close()