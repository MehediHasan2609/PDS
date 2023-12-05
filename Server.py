import socket
import threading

def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"Received from client {threading.current_thread().name}: {message}")

            # Echo back to the client
            client_socket.send(message.encode())
    except Exception as e:
        print(f"Error handling client {threading.current_thread().name}: {e}")
    finally:
        client_socket.close()
        print(f"Connection with client {threading.current_thread().name} closed.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8080))
    server.listen(5)

    print("Server is listening on port 8080...")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")

        # Handle client communication in a separate thread
        client_handler = threading.Thread(target=handle_client, args=(client_socket,), name=str(addr))
        client_handler.start()

if __name__ == "__main__":
    start_server()
