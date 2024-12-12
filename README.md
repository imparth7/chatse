# CLI Messaging App

## Overview
The CLI Messaging App is a simple Python-based chat application that allows multiple users to connect to a server and exchange messages in real time. Each user is authenticated with a username and password. Users can send messages to the chat or use the `leave` command to exit the chat.

## Features
- **Multi-client Support:** Multiple users can connect to the server simultaneously.
- **User Authentication:** Users can log in with their username and password or create a new account.
- **Real-Time Messaging:** Messages are broadcast to all connected users.
- **Leave Command:** Users can type `leave` to exit the chat.
- **User-Friendly Interface:** Simplified and clean chat display for better usability.

## Requirements
- Python 3.6+

## Installation
1. Clone the repository or download the source code.
   ```bash
   git clone https://github.com/imparth7/chatse.git
   cd chatse
   ```
2. Run the `main.py` script to start the application.

## Usage
### Server Mode
1. Run the application in server mode to host the chat server:
   ```bash
   python main.py
   ```
2. When prompted, enter `server` and specify the port number to host the server.

### Client Mode
1. Run the application in client mode to connect to the server:
   ```bash
   python main.py
   ```
2. When prompted, enter `client`, the server's IP address, and port number.
3. Log in with your username and password or create a new account.
4. Start chatting!

### Commands
- **Send Messages:** Type your message and press Enter to send it to all users.
- **Leave Chat:** Type `leave` to exit the chat.

## Example
### Starting the Server
```plaintext
Welcome to CLI Messaging App
Enter mode (server/client): server
Enter port to host the server: 8080
Server started on port 8080. Waiting for connections...
```

### Connecting a Client
```plaintext
Welcome to CLI Messaging App
Enter mode (server/client): client
Enter server IP address: 192.168.x.x
Enter server port: 8080
Connected to the server at 192.168.x.x:8080

Welcome to the chat server!
Enter username: john
Enter password: secret123
New user created successfully!
> Hello everyone!
```

### Chat Example
```plaintext
john: Hello everyone!
mary: Hi, John!
```

### Leaving the Chat
```plaintext
> leave
You have left the chat.
```

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contribution
Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue first to discuss your ideas.

## Acknowledgments
Special thanks to the Python community for providing excellent resources and support!