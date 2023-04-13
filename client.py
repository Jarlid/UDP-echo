import socket
from datetime import datetime
import math

from config import PORT
TIMEOUT = 1.0
PING_NUM = 10


class Data:
    def __init__(self):
        self.packages_got = 0
        self.packages_lost = 0
        self.max_rtt = 0
        self.min_rtt = math.inf
        self.sum_rtt = 0

    def got_update(self, rtt):
        self.packages_got += 1
        self.max_rtt = max(rtt, self.max_rtt)
        self.min_rtt = min(rtt, self.min_rtt)
        self.sum_rtt += rtt
        self.print_data()

    def lost_update(self):
        self.packages_lost += 1
        self.print_data()

    def print_data(self):
        flag = self.packages_got > 0
        print('Maximum RTT:', self.max_rtt if flag else "NONE")
        print('Minimum RTT:', self.min_rtt if flag else "NONE")
        print('Average RTT:', self.sum_rtt // (self.packages_got + self.packages_lost) if flag else "NONE")
        print('Lost percentage:', self.packages_lost / (self.packages_got + self.packages_lost), end='\n\n')


data = Data()

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
client.settimeout(TIMEOUT)

for num in range(1, PING_NUM + 1):
    send_time = datetime.now()
    message = 'Ping #' + str(num) + ', time: ' + send_time.strftime('%H:%M:%S.%f')
    client.sendto(message.encode('ascii'), ('127.0.0.1', PORT))

    try:
        message, _ = client.recvfrom(1024)
        get_time = datetime.now()
        print(message.decode('ascii'))
        data.got_update((get_time - send_time).microseconds)

    except socket.timeout:
        print('Request timed out.')
        data.lost_update()
