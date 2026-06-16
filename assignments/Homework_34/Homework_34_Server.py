import socket
import threading


HOST = "127.0.0.1"
PORT = 12345


def handle_client(client_socket, address):
    print(f"Client connected: {address}")

    while True:
        try:
            data = client_socket.recv(1024)

            if not data:
                break

            message = data.decode()
            print(f"Received from {address}: {message}")

            # Echo
            client_socket.send(data)

        except ConnectionError:
            break

    print(f"Client disconnected: {address}")
    client_socket.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server started on {HOST}:{PORT}")

while True:
    client_socket, address = server.accept()

    client_thread = threading.Thread(
        target=handle_client,
        args=(client_socket, address)
    )

    client_thread.start()