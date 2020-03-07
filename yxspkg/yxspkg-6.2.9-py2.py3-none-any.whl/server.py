#!/usr/bin/env python3
from . import server_core
if __name__=='__main__':
    x=server_core.getip()
    print('本机ip：{ip}'.format(ip=x))
    # print(sys.argv)
    # if '-server' not in sys.argv:
    #     sys.argv.pop(1)
    #     os.system('python "{}" -server'.format(sys.argv[0]))
    #     exit()
    # it = -1
    # for i,s in enumerate(sys.argv):
    #     if s == '-server':
    #         it = i 
    # if it >= 0:
    #     sys.argv.pop(it)
    server_core.website()