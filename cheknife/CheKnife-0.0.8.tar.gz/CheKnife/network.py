from netaddr import IPNetwork, IPAddress


def is_ip_in_network(ip, cidr):
    return IPAddress(ip) in IPNetwork(cidr)
