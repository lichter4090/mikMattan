import socket
import json


def open_socket(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(True)
    try:
        sock.connect((ip, port))

        return sock
    except Exception:
        return None


def send_data(sock, data):
    sock.sendall(json.dumps(data).encode())


def receive_data(sock):
    try:
        return json.loads(sock.recv(2048).decode())
    except Exception:
        return None


def close_socket(sock):
    sock.close()
