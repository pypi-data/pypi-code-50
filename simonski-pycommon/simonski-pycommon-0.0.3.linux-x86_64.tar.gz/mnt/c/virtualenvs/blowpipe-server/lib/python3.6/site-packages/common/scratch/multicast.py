# (224.0.0.0 through 230.255.255.255)
import sys

multicast_group = "224.3.29.71"
multicast_group = "224.0.0.0"
group_address = "224.0.0.0"
server_address = ("", 10000)


def adder(num1: int, num2: int) -> int:
    """
    Adds two integers together
    :param num1: the first int to add
    :param num2: the second int to add
    :return: the sum of num1 and num2
    """
    return num1 + num2


def sender():
    import socket
    import struct
    import sys

    message = "very important data"
    multicast_group = (group_address, 10000)

    # Create the datagram socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set a timeout so the socket does not block indefinitely when trying
    # to receive data.
    sock.settimeout(0.2)

    # Set the time-to-live for messages to 1 so they do not go past the
    # local network segment.
    ttl = struct.pack("b", 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    try:

        # Send data to the multicast group
        print(sys.stderr, 'sending "%s"' % message)
        sent = sock.sendto(bytes(message, "utf-8"), multicast_group)

        # Look for responses from all recipients
        while True:
            print(sys.stderr, "waiting to receive")
            try:
                data, server = sock.recvfrom(16)
            except socket.timeout:
                print(sys.stderr, "timed out, no more responses")
                break
            else:
                print(sys.stderr, 'received "%s" from %s' % (data, server))

    finally:
        print(sys.stderr, "closing socket")
        sock.close()




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


if __name__ == "__main__":
    main()
