from utils.Discovery import DiscoveryListener
from utils.utils import Location


class Node(object):
    def __init__(self):
        self.discoListener = DiscoveryListener()
        self.groupLocation = Location('239.192.1.100', 50000)
        self.myLocation = Location('127.0.0.1', 5555)

    def run(self):
        data = self.discoListener.listen(ip=self.groupLocation.ip, port=self.groupLocation.port)
        print('Received client location: ', data)
        self.discoListener.send(ip=data.ip, port=data.port, data=self.myLocation)


if __name__ == '__main__':
    node = Node()
    node.run()
