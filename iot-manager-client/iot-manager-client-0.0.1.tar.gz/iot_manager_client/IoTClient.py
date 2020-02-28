# default lib imports
import socket
import threading
import json
import time
import logging
from typing import Union

# module imports
from .ReservedBytes import ReservedBytes
from .Packet import Packet


# Client class
class IoTClient:
    # an exception raised when the client ends the connection, useful so the manager knows if a given client has
    # ended communications at any point
    class ConnectionEnd(Exception):
        pass

    def __init__(self, client_uuid: str, client_type: str, client_data: dict, logging_level: int):
        # client uuid
        self.uuid = client_uuid

        # client type
        self.type = client_type

        # client data
        self.data = client_data

        # marks if the client connection is alive
        self.is_alive = False

        # client logger
        self.logger = logging.getLogger("[Client](ID: " + self.uuid + ")")
        self.logger_level = logging_level
        self.logger.setLevel(self.logger_level)

        # a lock preventing multiple threads from using the __connection at the same time
        self.connection_lock = threading.RLock()

        # socket object representing the connection between the client and the server
        self.__connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # thread container
        self.__thread_pool = []

    # end the connection with the server
    def end(self, raise_exception: bool = False):
        # set as false
        self.is_alive = False

        # logging output
        self.logger.warning("(end) Ending connection with server.")

        try:
            # tell the server the client is connection ending the connection
            self.__connection.send(Packet(ReservedBytes.END_CONNECTION.value).bytes)

        finally:
            # shutdown the socket connection
            self.__connection.shutdown(socket.SHUT_RDWR)

            # close the socket connection
            self.__connection.close()

            if raise_exception:
                # raise a connection end error
                raise self.ConnectionEnd

    # send data to the server
    def send(self, data: bytes):
        self.logger.debug("(send) Attempting to send a Packet.")

        # init the lock
        with self.connection_lock:
            try:
                # send the string to to the client
                self.__connection.sendall(Packet(data).bytes)

                self.logger.debug("(send) Packet sent successfully.")

                return True

            # in case of a socket error return None
            except socket.error:
                self.logger.debug("(send) Packet was unable to be sent.")
                return False

    # recvs using the protocol of [2B - Message Size][Message] -> ignore rest
    def __smart_recv(self, timeout: int) -> Union[bytes, None]:
        # init the lock
        with self.connection_lock:
            # if a timeout is specified then set the timeout
            if timeout is not None:
                self.__connection.settimeout(timeout)

            # read the first two bytes to get the size of the message
            message_size = self.__connection.recv(2)

            # if the buffer is empty return none
            if message_size is None:
                return None

            # if it has a value convert it into an integer
            message_size = int.from_bytes(message_size, 'big', signed=False)

            # recv up to the number of bytes we should recv
            message = self.__connection.recv(message_size)

            # check if the message len in bytes matches the length given, if it did not give a warning
            if message_size != len(message):
                # logging output
                self.logger.warning("(recv) Message length did not match the length specified in the message header.")

            return message

    # receives data from a client (optional timeout)
    def recv(self, timeout: int = 15) -> Union[Packet, None]:
        # blank response
        response = None

        # put the recv in a try catch to check for a timeout
        try:
            # read data from buffer
            response = self.__smart_recv(timeout)

        # in case of socket timeout
        except socket.timeout:
            return None

        # in case of another socket error
        except socket.error:
            return None

        finally:
            # if response is non return None
            if response is None:
                return None

            self.logger.debug("(recv) Returning received packet.")

            # return data as a packet object
            return Packet(response, sending=False)

    # loop which receives data from the server
    def __message_handler(self):
        while True:
            # check if the server has sent some data
            packet = self.recv(0)

            # if the server has not sent data continue to loop
            if packet is None:
                continue
            # if the client has sent some data then process it using the on_message function
            else:
                # logging message
                self.logger.debug("(__message_handler) Data received from server.")

                # check for a default command
                if not self.__handle_defaults(packet):
                    # send the message to the on message function
                    self.on_message(packet)

            # wait one second
            time.sleep(1)

    # handle default messages like getinfo and heartbeat
    def __handle_defaults(self, data: Packet) -> bool:
        # handle the get data command
        if data.bytes == ReservedBytes.GET_DATA.value:
            self.send((self.uuid + "##" + self.type + "##" + json.dumps(self.data)).encode())
            return True
        # handle heartbeat command
        if data.bytes == ReservedBytes.HEARTBEAT.value:
            self.send(ReservedBytes.HEARTBEAT.value)
            return True
        # handle end connection command
        if data.bytes == ReservedBytes.END_CONNECTION.value:
            # call on_disconnect function
            self.on_disconnect()

            # call the end function
            self.end()
            return True

        return False

    # start client connection to the server
    def connect(self, host: str, port: int = 8595):
        try:
            # logging output
            self.logger.info("(connect) Connecting to server.")

            # connect to the server
            self.__connection.connect((host, port))
        # return false if an exception occurs
        except socket.error:
            return False

        # logging output
        self.logger.info("(connect) Adding threads to thread pool.")

        # add the __message_handler thread
        self.__thread_pool.append(threading.Thread(target=self.__message_handler, daemon=True, name="__message_handler"))

        # logging output
        self.logger.info("(connect) Starting all threads to thread pool.")

        # start all threads
        for thread in self.__thread_pool:
            thread.start()

        self.is_alive = True

        # logging output
        self.logger.info("(connect) Executing on_connect handler.")

        # execute the on_connect function
        self.on_connect()

        return True

    def on_connect(self):
        pass

    def on_message(self, data: Packet):
        pass

    def on_disconnect(self):
        pass
