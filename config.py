from enum import Enum


class Connection(Enum):
    UDPv4 = 0
    TCPv6 = 1


MODE = Connection.TCPv6

PORT = 6666
IP = '127.0.0.1' if MODE == Connection.UDPv4 else '::1'
DEFAULT_ADDRESS = (IP, PORT) if MODE == Connection.UDPv4 else (IP, PORT, 0, 0)

LOST_PERCENTAGE = 20
TIMEOUT = 1.0
PING_NUM = 10
