import thread
import time

from receiver import Receiver
from sender import Sender


def main():
    receiver = Receiver()
    sender = Sender()

    thread.start_new_thread(receiver.listen, ())
    time.sleep(1)
    sender.send()


if __name__ == "__main__":
    print 'here'
    main()
