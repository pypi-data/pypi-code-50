# (224.0.0.0 through 230.255.255.255)
import sys
import time
import socket
import struct
import sys
import uuid

from common.cli import CLI


DEFAULT_MULTICAST_GROUP = "224.3.29.71"
DEFAULT_MULTICAST_GROUP = "224.0.0.0"
DEFAULT_IP_ADDRESS = "224.0.0.0"
DEFAULT_PORT = 10000

server_address = ("", 10000)


class Callback:
    def __init__(self):
        pass

    def on_joined(self, groupinfo):
        pass

    def on_group_left(self):
        pass

    def on_member_joined(self):
        pass

    def on_member_left(self):
        pass


class UDPServer:
    def __init__(
        self,
        name: str = None,
        ip_address: str = DEFAULT_IP_ADDRESS,
        port: int = DEFAULT_PORT,
    ):
        if name is None:
            name = str(uuid.uuid4())
        self.name = name
        self.ip_address = ip_address
        self.port = port
        self.sock = None
        self.thread_pool = None
        self.callbacks = []

    def start(self):
        """
        starts listening on the socket, starts the receiver thread
        :return:
        """
        # Create the datagram socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Set a timeout so the socket does not block indefinitely when trying
        # to receive data.
        sock.settimeout(0.2)

        # Set the time-to-live for messages to 1 so they do not go past the
        # local network segment.
        ttl = struct.pack("b", 1)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

        self.sock = sock

        if self.threadpool is None:
            thread_pool = utils.ThreadPool()
            self.thread_pool = thread_pool
            thread_pool.add(self)

    def stop(self):
        self.threadpool.quit()
        while self.threadpool.is_running():
            time.sleep(0.2)

    def is_listening(self):
        return self.threadpool.is_running()

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        self.callbacks.remove(callback)

    def execute(self):
        """
        called by the threadpool
        :return:
        """
        sock = self.sock
        # Look for responses from all recipients
        while True:
            print(sys.stderr, "waiting to receive")
            try:
                data, server = sock.recvfrom(16)
                self.on_receive(data, server)
            except socket.timeout:
                print(sys.stderr, "timed out, no more responses")
                break
            else:
                print(sys.stderr, 'received "%s" from %s' % (data, server))

    def send(self, message):
        sock = self.sock
        multicast_group = (self.ip_address, self.port)
        # Send data to the multicast group
        print(sys.stderr, 'sending "%s"' % message)
        sent = sock.sendto(bytes(message, "utf-8"), multicast_group)
        return sent


"""
def receiver():
    import socket
    import struct
    import sys

    # Create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind to the server address
    sock.bind(server_address)

    # Tell the operating system to add the socket to the multicast group
    # on all interfaces.
    group = socket.inet_aton(multicast_group)
    mreq = struct.pack("4sL", group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    # Receive/respond loop
    while True:
        print(sys.stderr, "\nwaiting to receive message")
        data, address = sock.recvfrom(1024)

        print(sys.stderr, "received %s bytes from %s" % (len(data), address))
        print(sys.stderr, data)

        print(sys.stderr, "sending acknowledgement to", address)
        sock.sendto(bytes("ack", "utf-8"), address)


def main():
    if sys.argv[1] == "send":
        sender()
    else:
        receiver()
"""


class Client:
    def __init__(self, name=None):
        if name is None:
            self.name = str(uuid.uuid4())
        else:
            self.name = name
        server = UDPServer(name=self.name)
        server.add_callback(Callback())
        self.server = server

    def main(self):
        quit = False
        while not quit:
            user_input = CLI.read(prompt="(" + self.name + ") > ")
            quit = self.process(user_input)
        print("Bye")

    @staticmethod
    def get_command_from_user_input(user_input):
        command = user_input.split(" ")[0]
        remainder = user_input[len(command) :].strip()
        return command, remainder

    def process(self, user_input):
        command, remainder = self.get_command_from_user_input(user_input)
        fn_name = "on_" + command.lower()

        try:
            print("command=" + command + ", remainder=" + remainder)
            attr = getattr(self, fn_name)
            try:
                return attr(remainder)
            except Exception as e:
                print("Problem calling function '" + fn_name + "'")
                print(e)
        except Exception as e:
            print(e)
            print("I don't know how to %s" % command)
            return False

    def on_q(self, user_input):
        return self.on_quit(user_input)

    def on_quit(self, user_input):
        server = self.server
        server.bye()
        return True

    def on_send(self, user_input):
        server = self.server
        server.send(user_input)
        return False

    def on_ping(self, user_input):
        server = self.server
        server.ping()

    def on_ls(self, user_input):
        server = self.server
        clients = server.ls(user_input)
        for c in clients:
            print(c)

    def on_list(self, user_input):
        return self.on_ls(user_input)


if __name__ == "__main__":
    c = CLI()
    name = c.get_or_die("-id", uuid.uuid4())
    client = Client(name)
    client.main()
