from pydnserver import DNSServer

ip = u'192.168.199.173'  # Set this to the IP address of your network interface.

dns = DNSServer(interface=ip, port=5353)
dns.start()

try:
    while True:
        pass

except KeyboardInterrupt:
    dns.stop()
