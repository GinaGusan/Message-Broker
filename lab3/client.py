import socket

from utils.Discovery import DiscoveryClient
from utils.Transport import TransportClient
from utils.utils import Location, Employee


class Client(object):
    def __init__(self):
        self.discoClient = DiscoveryClient()
        self.transClient = TransportClient()
        self.myLocation = Location('127.0.0.1', 3456)
        self.groupLocation = Location('239.192.1.100', 50000)

    def run(self):
        self.discoClient.send(ip=self.groupLocation.ip, port=self.groupLocation.port, data=self.myLocation)

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error:
            print("Failed to create socket")
            sys.exit()

