import socket

HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server listening on {HOST}:{PORT}")

conn, addr = server.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break

    message = data.decode()
    print(f"Client: {message}")

    response = input("Server reply: ")
    conn.send(response.encode())

conn.close()
server.close()