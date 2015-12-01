from IO_Interface import IO_Network
from queue import Queue
import _thread
import time


BROKER_PORT = 8888
DEFAULT_PORT = 6666


class Broker(object):
    def __init__(self):
        self.messageQueue = Queue()
        self.netReader = IO_Network(BROKER_PORT, 'localhost')
        self.netReader.bind()
        self.netWriter = IO_Network(DEFAULT_PORT, 'localhost')
        self.subscribers = []

    def listen(self):
        while True:
            msg = self.netReader.read(None)
            self.messageQueue.put(msg)

    def send(self):
        while True:
            msg = self.messageQueue.get()
            if msg.type == 'subscription':
                print('received subscription from: ' + msg.senderID)
                self.subscribers.append(msg.body)
            elif msg.type == 'message':
                for subscriber in self.subscribers:
                    if subscriber.id == msg.receiverID:
                        self.netWriter.port = subscriber.port
                        self.netWriter.host = subscriber.ip
                        print('message for ' + str(subscriber))
                        self.netWriter.write(msg.receiverID, msg)
                        break

    def main(self):
        print('here')
        _thread.start_new_thread(self.send, ())
        self.listen()


def main():
    broker = Broker()
    broker.main()


if __name__ == "__main__":
    main()
