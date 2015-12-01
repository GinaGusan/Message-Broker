import socket
import pickle


class DiscoveryClient(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def send(self, port, ip, data):
        self.sock.sendto(pickle.dumps(data), (ip, port))


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
        # Do some magic stuff

        self.sock.setsockopt(socket.SOL_IP, socket.IP_DROP_MEMBERSHIP,
                socket.inet_aton(ip) + socket.inet_aton('0.0.0.0'))

        self.sock.close()
        return pickle.loads(data)

