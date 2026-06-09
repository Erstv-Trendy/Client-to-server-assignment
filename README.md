# TCP Chat Application

A simple two-way chat application built with Python's `socket` module over a TCP connection.

## Files

| File | Description |
|------|-------------|
| `server.py` | Starts a TCP server and waits for a single client connection |
| `client.py` | Connects to the server and begins a chat session |

## Requirements

- Python 3.x (no external dependencies)

## Usage

### 1. Start the Server

Run this first on the host machine:

```bash
python server.py
```

The server listens on all network interfaces (`0.0.0.0`) on port `5000`.

### 2. Connect the Client

Run this on the same machine (or a remote machine):

```bash
python client.py
```

By default, the client connects to `127.0.0.1` (localhost). To connect to a remote server, edit `SERVER_IP` in `client.py`:

```python
SERVER_IP = '192.168.1.100'  # Replace with your server's IP address
```

### 3. Chat

Once connected, both sides type messages and press **Enter** to send. The conversation alternates — the client sends first, then the server replies.

```
# Client side
Connected to server.
You: Hello!
Server: Hi there!

# Server side
Server listening on 0.0.0.0:5000
Connected by ('127.0.0.1', 54321)
Client: Hello!
Server reply: Hi there!
```

## Configuration

| Variable | File | Default | Description |
|----------|------|---------|-------------|
| `HOST` | `server.py` | `0.0.0.0` | Interface to listen on |
| `PORT` | `server.py` | `5000` | Port to listen on |
| `SERVER_IP` | `client.py` | `127.0.0.1` | Server IP to connect to |
| `PORT` | `client.py` | `5000` | Port to connect to |

## Limitations

- Supports **one client at a time** — the server does not handle multiple concurrent connections.
- The conversation is **strictly turn-based** — client sends, server replies, repeat.
- Messages are limited to **1024 bytes** per transmission.
