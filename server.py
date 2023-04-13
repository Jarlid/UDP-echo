import socket
import random

from config import PORT
LOST_PERCENTAGE = 20

print('Starting server.', end='')
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
print('.', end='')
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
print('.')
server.bind(('', PORT))
print('Server started!', end='\n\n')

while True:
    print('Waiting for connection...')
    message, address = server.recvfrom(1024)
    print('Connected!')

    if random.randint(0, 99) < LOST_PERCENTAGE:
        print('Package lost!', end='\n\n')
    else:
        message = message.upper()
        server.sendto(message, address)
        print('Package sent!', end='\n\n')
