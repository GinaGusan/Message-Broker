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

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((self.myLocation.ip, self.myLocation.port))

            while True:
                data, addr = sock.recvfrom(1024)

                if not data:
                    break
                else:
                    data = pickle.loads(data)
                    break
            sock.close()

            # create a TransportClient() with data as location
            
        except socket.error as err:
            print("Failed to create socket", err.args[1])
            sys.exit()


