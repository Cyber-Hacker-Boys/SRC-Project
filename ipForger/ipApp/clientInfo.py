import socket
from getmac import get_mac_address as gma


class ClientInfo:
    def __init__(self):
        hostname = socket.gethostname()
        self.local_ip = socket.gethostbyname(hostname)
        self.local_mac = gma()
