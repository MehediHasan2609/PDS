import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 8080))

    while True:
        message = input("Enter a message (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break

        client.send(message.encode())

        # Receive and print the echoed message from the server
        response = client.recv(1024).decode()
        print(f"Server response: {response}")

    client.close()

if __name__ == "__main__":
    start_client()
