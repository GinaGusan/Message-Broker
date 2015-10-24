from IO_Interface import IO_Network
from utils import Subscriber, Message
import thread

BROKER_PORT = 8888
DEFAULT_PORT = 9999


class Sender(object):
    def __init__(self):

        self.netWriter = IO_Network(BROKER_PORT, "localhost")

    def send(self):
        myself = Subscriber()
        myself.port = DEFAULT_PORT  # sender port
        myself.ip = 'localhost'
        myself.id = 'sender'

        message = Message()
        message.type = 'subscription'
        message.senderID = 'sender'
        message.receiverID = 'receiver'
        message.body = myself

        self.netWriter.write('broker', message)

        message.type = 'message'

        while True:
            text = raw_input("Enter message to send: ")
            if text == 'close':
                self.netWriter.close_socket()
                break
            recipient = raw_input('Enter receiver: ')
            message.body = text
            message.receiverID = recipient
            self.netWriter.write('receiver', message)
        return


def main():
    sender = Sender()
    sender.send()

if __name__ == "__main__":
    main()
