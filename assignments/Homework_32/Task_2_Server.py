import socket


def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        else:
            result += char

    return result


HOST = "127.0.0.1"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server started...")

while True:
    client_socket, address = server.accept()

    print(f"Connected: {address}")

    data = client_socket.recv(1024).decode()

    message, key = data.split("|")

    encrypted_message = caesar_encrypt(message, int(key))

    client_socket.send(encrypted_message.encode())

    client_socket.close()
