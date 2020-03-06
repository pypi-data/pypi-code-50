import socket
import datetime


def get_hostname_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_name, host_ip
    except:
        print("Unable to get Hostname and IP")
        raise


def get_datetime():
    return str(datetime.datetime.now())
