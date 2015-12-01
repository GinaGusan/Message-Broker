import socket
import sys
import pickle

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
        data = self.discoClient.receive(ip=self.myLocation.ip, port=self.myLocation.port)
        print('First node is: ', data)


if __name__ == '__main__':
    client = Client()
    client.run()
