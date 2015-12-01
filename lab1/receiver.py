from IO_Interface import IO_Network
from utils import Subscriber, Message
import thread

BROKER_PORT = 8888
DEFAULT_PORT = 7777


class Receiver(object):
    def __init__(self):
        self.netReader = IO_Network(DEFAULT_PORT, 'localhost')
        self.netReader.bind()
        self.netWriter = IO_Network(BROKER_PORT, 'localhost')
        print 'Socket bind complete'

    def listen(self):
        while True:
            msg = self.netReader.read(None)
            print '\nReceived message:{0}'.format(msg.body)

    def send(self):
        myself = Subscriber()
        myself.port = DEFAULT_PORT
        myself.ip = 'localhost'
        myself.id = 'app2'

        message = Message()
        message.type = 'subscription'
        message.senderID = 'app2'
        message.receiverID = 'broker'
        message.body = myself

        self.netWriter.write('broker', message)


def main():
    receiver = Receiver()
    thread.start_new_thread(receiver.send, ())
    receiver.listen()


if __name__ == "__main__":
    print 'here'
    main()
