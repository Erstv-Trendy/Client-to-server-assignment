import socket

SERVER_IP = '127.0.0.1'  # Replace with server IP if remote
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

print("Connected to server.")

while True:
    message = input("You: ")
    client.send(message.encode())

    data = client.recv(1024)
    print(f"Server: {data.decode()}")

client.close()

