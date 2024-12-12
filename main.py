import socket
import threading

users = {}  # Dictionary to store usernames and passwords


def authenticate_user(connection):
    """Authenticates a user by asking for username and password over the socket."""
    while True:
        connection.send("Enter username: ".encode("utf-8"))
        username = connection.recv(1024).decode("utf-8").strip()
        connection.send("Enter password: ".encode("utf-8"))
        password = connection.recv(1024).decode("utf-8").strip()

        if username in users and users[username] == password:
            connection.send("Login successful!".encode("utf-8"))
            return username
        elif username not in users:
            users[username] = password
            connection.send("New user created successfully!".encode("utf-8"))
            return username
        else:
            connection.send("Invalid credentials. Try again.".encode("utf-8"))


def broadcast(message, connections, sender):
    """Broadcasts a message to all connected clients except the sender."""
    for conn in connections:
        if conn != sender:
            try:
                conn.send(message.encode("utf-8"))
            except Exception():
                connections.remove(conn)


def handle_client(connection, address, connections):
    """Handles individual client communication."""
    connection.send("Welcome to the chat server!\n".encode("utf-8"))
    username = authenticate_user(connection)
    print(f"{username} connected from {address}")
    broadcast(f"{username} has joined the chat!", connections, connection)

    while True:
        try:
            message = connection.recv(1024).decode("utf-8")
            if message.lower() == "leave":
                break
            if message:
                formatted_message = f"{username}: {message}"
                broadcast(formatted_message, connections, connection)
        except Exception as e:
            print(f"Error with {username}: {e}")
            break

    connections.remove(connection)
    connection.close()
    broadcast(f"{username} has left the chat.", connections, None)


def start_server(port):
    """Starts the server for multiple users."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(5)
    print(f"Server started on port {port}. Waiting for connections...")

    connections = []

    while True:
        connection, address = server_socket.accept()
        connections.append(connection)
        threading.Thread(
            target=handle_client, args=(connection, address, connections)
        ).start()


def start_client(ip, port):
    """Starts the client to send messages to the server."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((ip, port))
        print(f"Connected to the server at {ip}:{port}\n")

        def receive_messages():
            while True:
                try:
                    message = client_socket.recv(1024).decode("utf-8")
                    if message:
                        print(f"\r{message}\n> ", end="", flush=True)
                    else:
                        print("\nConnection closed by the server.")
                        break
                except Exception as e:
                    print(f"Error receiving message: {e}")
                    break

        threading.Thread(target=receive_messages, daemon=True).start()

        while True:
            user_input = input("> ").strip()
            if user_input.lower() == "leave":
                client_socket.send("leave".encode("utf-8"))
                print("You have left the chat.")
                break
            if user_input:
                client_socket.send(user_input.encode("utf-8"))

    except Exception as e:
        print(f"Error connecting to server: {e}")

    client_socket.close()


if __name__ == "__main__":
    print("Welcome to CLI Messaging App")
    mode = input("Enter mode (server/client): ").strip().lower()

    if mode == "server":
        port = int(input("Enter port to host the server: "))
        start_server(port)
    elif mode == "client":
        ip = input("Enter server IP address: ").strip()
        port = int(input("Enter server port: "))
        start_client(ip, port)
    else:
        print("Invalid mode! Please enter 'server' or 'client'.")
