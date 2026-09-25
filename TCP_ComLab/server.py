import socket

from utlitiy.logger import create_logger
from protocol.message import encode_message, decode_message

logger = create_logger("TCP-Server")


class ServerSocket:

    def __init__(self, ip_address, port):
        self.ip_address= ip_address
        self.port = port
        self.server_socket = None
        self.connection_socket = None

    def create_socket(self):

        # Ask the OS to create an IPv4 TCP socket
        self.server_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

    def start(self):

        # Assign the local IP address and port
        self.server_socket.bind(
            (self.ip_address, self.port)
        )

        # Turn the socket into a listening socket
        self.server_socket.listen()

        print(f"Server listening on {self.ip_address}:{self.port}")

        # Wait for a client connection
        self.connection_socket, client_address = (
            self.server_socket.accept()
        )

        print(f"Client connected: {client_address}")

        # Wait for up to 1024 bytes from the client
        data = self.connection_socket.recv(1024)

        print(f"Received: {data}")

        # Send application bytes to the client
        self.connection_socket.sendall(b"TCP Communication Server ...")


    def close(self):
        
        # Close the connected client socket first
        if self.connection_socket is not None:
            self.connection_socket.close()
            print("Connection socket closed")

        # Then close the listening socket
        if self.server_socket is not None:
            self.server_socket.close()
            print("Server socket closed")

if __name__ == "__main__":

    server = ServerSocket("127.0.0.1", 5000)

    try:
        server.create_socket()
        server.start()
    finally:
        server.close()