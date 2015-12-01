import socket
import sys
import pickle


class IO_Interface(object):
    def __init__(self):
        pass

    def read(self, location):
        pass

    def write(self, location, data):
        pass


class IO_File(IO_Interface):
    def __init__(self):
        pass

    def read(self, location):
        f = open(location, 'r')
        content = f.read()
        return content

    def write(self, location, data):
        f = open(location, 'w')
        f.write(data)
        return


class IO_Network(IO_Interface):
    def __init__(self, port, host):
        self.port = port
        self.host = host
        self.sock = None

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error:
            print "Failed to create socket"
            sys.exit()

        return

    def bind(self):
        try:
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.bind((self.host, self.port))
        except socket.error, err:
            print 'Bind failed. Error Code : ' + str(err[0]) + ' Message ' + err[1]
            print err
            sys.exit()

    def close_socket(self):
        self.sock.close()

    def read(self, location):
        while True:
            data, addr = self.sock.recvfrom(1024)

            if not data:
                break
            else:
                return pickle.loads(data)

    def write(self, location, data):
        try:
            self.sock.sendto(pickle.dumps(data), (self.host, self.port))
        except socket.error, err:
            print "Error Code : " + str(err[0]) + "Message" + err[1]
            sys.exit()
        return
