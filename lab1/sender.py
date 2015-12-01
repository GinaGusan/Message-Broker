from IO_Interface import IO_Network
from utils import Subscriber, Message
import time
import xml.etree.ElementTree as ET

BROKER_PORT = 8888
DEFAULT_PORT = 9999


class Sender(object):
    def __init__(self):

        self.netWriter = IO_Network(BROKER_PORT, "localhost")

    def send(self):
        myself = Subscriber()
        myself.port = DEFAULT_PORT  # sender port
        myself.ip = 'localhost'
        myself.id = 'app1'

        message = Message()
        message.type = 'subscription'
        message.senderID = 'app1'
        message.receiverID = 'broker'
        message.body = myself

        self.netWriter.write('broker', message)

        message.type = 'message'
        tree = ET.parse('country_data.xml')
        root = tree.getroot()

        recipient = 'app2'
        message.body = open('country_data.xml').read()
        message.receiverID = recipient
        self.netWriter.write('app2', message)


def main():
    sender = Sender()
    sender.send()

if __name__ == "__main__":
    main()
