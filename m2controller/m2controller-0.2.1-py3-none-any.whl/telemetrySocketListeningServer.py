#http://sebastiandahlgren.se/2014/06/27/running-a-method-as-a-background-thread-in-python/ 

# FastLanePython.pdf
# simple illustration client/server pair; client program sends a string
# to server, which echoes it back to the client (in multiple copies),
# and the latter prints to the screen


import socket
import sys
import threading
import time
from m2controller import m2Const, constShared
from m2controller import bleDataDecoder
import json

class telemListeningServer(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, callback = None, etFwType = constShared.fwImage_generic):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.callback = callback
        self.m_bRequestExit = False
        self.m_etFwType = etFwType

    def request_exit(self):
        self.m_bRequestExit = True
    
    def runAsThread(self):
        thread = threading.Thread(target=self.socketThread, args=())
        thread.daemon = False                            # Daemonize thread
        thread.start()                                  # Start the execution

    def socketThread(self):
        # create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # associate the socket with a port
        host = '' # can leave this blank on the server side
        port = m2Const.socketServerPORT_SDKapp2py
        s.bind((host, port)) # two-element tuple, rather than two scalar arguments
        
        # accept "call" from client
        s.listen(1) # total # of connection, active+pendings
        
        while True:
            conn, addr = s.accept() # block operation, wait for connection request
            bytedata = b''
            #print ('connection request from IP%s'%(addr,)) # addr is tuple, not scalar
            while True:
                if self.m_bRequestExit:
                    break
                data = conn.recv(65536)
                if len(data) > 0:
                    bytedata = bytedata+data
                else:
                    break
            # close the connection
            conn.close()
            
            if self.m_bRequestExit:
                break
            else:
                if bytedata is not None:
                    dataJson = json.loads(bytedata)
                    ch4data = dataJson['m_baCh4telem']
                    decodedTelem = bleDataDecoder.decodeRawBleTelemetry(ch4data,self.m_etFwType)
                    self.callback(decodedTelem)

                        


                    

