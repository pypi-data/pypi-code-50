import os
from os import path

baseDir = os.path.dirname(__file__)

def readModuleMapping(mapFile):
    with open(mapFile,'r') as f:
        return {item[0]:item[1] for item in \
                        (line.strip().split('=') for line in f.readlines() \
                        if line.strip() and not line.strip().startswith('#'))}

def getLocalIp():
    import socket, fcntl, struct
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8',80))
    ip = s.getsockname()[0]
    return ip

def getEnvLabel(host_ip):
    if '192.168.7' in host_ip or '192.168.8' in host_ip or '192.168.9' in host_ip:
        return 'online'
    elif '10.9' in host_ip:
        return 'test'
    else:
        return 'dev'

mapConf = readModuleMapping(baseDir + '/config/module_map_url.txt')
supportConf = readModuleMapping(baseDir + '/config/support_conf.txt')
bertModelConf = readModuleMapping(baseDir + '/config/bert_models.txt')
