from IO_Interface import IO_Network
from Queue import Queue
import thread


BROKER_PORT = 8888
DEFAULT_PORT = 7777


class Broker(object):
    def __init__(self):
        self.messageQueue = Queue()
        self.netReader = IO_Network(BROKER_PORT, 'localhost')
        self.netReader.bind()
        self.netWriter = IO_Network(DEFAULT_PORT, 'localhost')
        self.subscribers = []

    def listen(self):
        while True:
            msg = self.netWriter.read(None)
            self.messageQueue.put(msg)

    def send(self):
        while True:
            msg = self.messageQueue.get()
            if msg.type == 'subscription':
                self.subscribers.append(msg.body)
            elif msg.type == 'message':
                for subscriber in self.subscribers:
                    if subscriber.id == msg.receiver:
                        self.netWriter.port = subscriber.port
                        self.netWriter.host = subscriber.ip
                        break
                if msg.body == 'close':
                    self.netWriter.write(msg.receiver, msg)
                    self.netReader.close_socket()
                    self.netWriter.close_socket()

    def main(self):
        print 'here'
        thread.start_new_thread(self.listen, ())
        # thread.start_new_thread(self.send, ())
        self.send()


def main():
    broker = Broker()
    broker.main()


if __name__ == "__main__":
    main()

    # create a thread for listener
    # create a thread for sender
    # use Queue for communication
