#!/usr/bin/env python

from tempfile import TemporaryDirectory
import urllib.request
import urllib.error
import pkg_resources
import subprocess
import threading
import socket
import zipfile
import sys
import os

import socks

TEMP_DIR = TemporaryDirectory().name
NOT_READY_PORTS = []  # Stores ports for port_checker(). Maximum len - number of threads
FINISHED = False  # True when all processes start (they may not be ready)


def ports_checker():
    while not FINISHED or NOT_READY_PORTS:
        if NOT_READY_PORTS:
            port = NOT_READY_PORTS[0]
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", port)
            socket.socket = socks.socksocket
            ip = None
            while not ip:
                try:
                    ip = urllib.request.urlopen('http://icanhazip.com').read().decode()[:-1]  # Get an external ip
                except urllib.error.URLError:
                    pass
            print(f'READY: {port} ({ip})')
            del NOT_READY_PORTS[0]


def start(count, threads=8):
    global FINISHED
    devnull = open(os.devnull, 'w')
    ports_data = dict()  # port: process

    platform = sys.platform
    if platform == 'linux' or platform == 'win32' or platform == 'darwin':
        with zipfile.ZipFile(pkg_resources.resource_filename('torloc', f'tor_{platform}.zip'), 'r') as zip_ref:
            zip_ref.extractall(TEMP_DIR)
        if platform != 'win32':
            subprocess.Popen(['chmod', '+x', f'{TEMP_DIR}/tor'], stdout=devnull, stderr=devnull)  # Permission denied
    else:
        print('Your system is not supported. There are only Windows, Linux and OSX support.')
        sys.exit()

    # It will work as a second thread and check the connection
    # Removes already checked ports from NOT_READY_PORTS
    ports_checker_process = threading.Thread(target=ports_checker)
    ports_checker_process.start()

    for port in range(49152, 49152 + count):  # The range 49152-65535 contains dynamically allocated or private ports
        while len(NOT_READY_PORTS) >= threads:
            pass
        print(f'STARTING: {port}... ')
        process = subprocess.Popen(
            [f'{TEMP_DIR}/tor', '-SOCKSPort', str(port), '-DataDirectory', f'{TEMP_DIR}/Data{port}'],
            stdout=devnull, stderr=devnull)
        NOT_READY_PORTS.append(port)
        ports_data[port] = process
    FINISHED = True
    ports_checker_process.join()  # Waiting for the latest ports to be checked
    return ports_data


def stop(ports_data):
    print(f'\nStooping {", ".join(str(port) for port in ports_data)}... ', end='')
    for port in ports_data:
        ports_data[port].kill()  # Close the connection
    print('OK')
