class Message(object):
    def __init__(self):
        self.senderID = None
        self.receiverID = None
        self.type = None
        self.body = None


class Subscriber(object):
    def __init__(self):
        self.id = None
        self.port = None
        self.ip = None
