import socket
from config import Connection, MODE, DEFAULT_ADDRESS


def start_server(bind=DEFAULT_ADDRESS):
    print('Starting server.')
    if MODE == Connection.UDPv4:
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        server.bind(bind)
    else:
        server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        server.bind(bind)
    print('Server started!', end='\n\n')
    return server


def start_client(timeout=None, address=DEFAULT_ADDRESS):
    if MODE == Connection.UDPv4:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    else:
        client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        client.connect(address)
    client.settimeout(timeout)
    return client


def establish_connection(server):
    if MODE == Connection.UDPv4:
        return server
    else:
        print('Waiting for connection...')
        server.listen()
        connection, _ = server.accept()
        print('Connected!')
        return connection


def use_recv(servcon):
    if MODE == Connection.UDPv4:
        return servcon.recvfrom(1024)
    else:
        return servcon.recv(1024), None


def use_send(servcon, message, address):
    if MODE == Connection.UDPv4:
        servcon.sendto(message, address)
    else:
        servcon.send(message)
