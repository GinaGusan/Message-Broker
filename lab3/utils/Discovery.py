import socket
import pickle
import sys


class DiscoveryClient(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def send(self, port, ip, data):
        self.sock.sendto(pickle.dumps(data), (ip, port))

    def receive(self, port, ip):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((ip, port))

            while True:
                data, addr = sock.recvfrom(1024)

                if not data:
                    break
                else:
                    data = pickle.loads(data)
                    break
            sock.close()

        except socket.error as err:
            print("Failed to create socket", err.args[1])
            sys.exit()

        return data



class DiscoveryListener(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        except AttributeError as err:
            print(err)

        self.sock.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_TTL, 20)
        self.sock.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_LOOP, 1)

    def listen(self, port, ip):
        self.sock.bind(('', port))

        intf = socket.gethostbyname(socket.gethostname())
        self.sock.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(intf))
        self.sock.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP,
                socket.inet_aton(ip) + socket.inet_aton(intf))

        data, sender_addr = self.sock.recvfrom(1024)

        self.sock.setsockopt(socket.SOL_IP, socket.IP_DROP_MEMBERSHIP,
                socket.inet_aton(ip) + socket.inet_aton('0.0.0.0'))

        self.sock.close()
        return pickle.loads(data)

    def send(self, ip, port, data):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.sendto(pickle.dumps(data), (ip, port))
