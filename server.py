import random

from engine import *
from config import LOST_PERCENTAGE

server = start_server()

while True:
    servcon = establish_connection(server)
    message, address = use_recv(servcon)

    if random.randint(0, 99) < LOST_PERCENTAGE:
        print('Package lost!', end='\n\n')
    else:
        message = message.upper()
        use_send(servcon, message, address)
        print('Package sent!', end='\n\n')
