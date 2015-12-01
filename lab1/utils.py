class Message(object):
    def __init__(self):
        self.senderID = None
        self.receiverID = None
        self.type = None
        self.body = None

    def __repr__(self):
        return self.type + self.senderID + self.receiverID + self.body

    def __str__(self):
        return self.type + ' ' + self.senderID + ' ' + self.receiverID + ' ' + self.body


class Subscriber(object):
    def __init__(self):
        self.id = None
        self.port = None
        self.ip = None

    def __repr__(self):
        return self.id + ' ' + self.ip + ':' + str(self.port)

    def __str__(self):
        return self.id + ' ' + self.ip + ':' + str(self.port)
