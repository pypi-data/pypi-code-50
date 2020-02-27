# default lib imports
import socket
import threading
import json
import logging
from typing import Union

# module imports
from .ReservedBytes import ReservedBytes
from .Packet import Packet


# Client class
class Client:
    # an exception raised when the client ends the connection, useful so the manager knows if a given client has
    # ended communications at any point
    class ConnectionEnd(Exception):
        pass

    # an exception raised when the client fails to get the client's info
    class InvalidInfo(Exception):
        pass

    def __init__(self, connection: socket, address: tuple, logging_level: int):
        # client logger
        self.logger = logging.getLogger("[Client](ID: UNKNOWN | IP: " + str(address[0]) + ")")
        self.logger_level = logging_level
        self.logger.setLevel(self.logger_level)

        # a lock preventing multiple threads from using the __connection at the same time
        self.connection_lock = threading.RLock()

        # socket object representing the connection between the client and the server
        self.__connection = connection

        # IP address of the client
        self.address = address

        # the uuid of the client
        self.uuid = None

        # the type of client the client is
        self.type = None

        # the bonus data which varies by client
        self.data = None

    # end the connection with the client
    def end(self, raise_exception: bool = False):
        # logging output
        self.logger.warning("(end) Ending connection.")

        try:
            # tell the client the connection is ending
            self.__connection.send(Packet(ReservedBytes.END_CONNECTION.value))

        finally:
            # shutdown the socket connection
            self.__connection.shutdown(socket.SHUT_RDWR)

            # close the socket connection
            self.__connection.close()

            if raise_exception:
                # raise a connection end error
                raise self.ConnectionEnd

    # send data to the client
    def send(self, packet: Packet):
        self.logger.debug("(send) Attempting to send a Packet.")

        # init the lock
        with self.connection_lock:
            try:
                # send the string to to the client
                self.__connection.sendall(packet.bytes)

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

    # gets the client's info (returns None if successful)
    def get_data(self, timeout: int = 15):
        # logging output
        self.logger.info("(getinfo) Sending getinfo request.")

        # init the lock
        with self.connection_lock:
            # logging output
            self.logger.debug("(getinfo) Sending getinfo packet.")

            # ask the client for their data if the send fails then end the connection
            if not self.send(Packet(ReservedBytes.GET_DATA.value)):
                self.end(True)

            # logging output
            self.logger.debug("(getinfo) Receiving getinfo response")

            # await client response containing their info
            packet = self.recv(timeout=timeout)

            # if the response returned None because of an error end the connection
            if packet is None:
                self.end(True)

            # split the response using "##" as the delimiter
            response = packet.bytes.decode().split("##")

            # if the response is not 3 pieces of data raise an error
            if len(response) != 3:
                # logging output
                self.logger.error("(getinfo) Response invalid formatting.")

                raise self.InvalidInfo

            # get the clients UUID
            client_uuid = response[0]

            # update the client's logger info
            self.logger = logging.getLogger("[Client](ID: " + client_uuid + ")")
            self.logger.setLevel(self.logger_level)

            # check if the UUID is 36 char long to only allow proper UUIDs
            if len(client_uuid) != 36:
                # logging output
                self.logger.error("(getinfo) UUID invalid length, should be 36 characters.")

                raise self.InvalidInfo

            # get the client's type
            client_type = response[1]

            # convert the data from a JSON string to a python dict
            try:
                # get the clients JSON data and convert it to a dict
                client_data = json.loads(response[2])
            except json.JSONDecodeError:
                # logging output
                self.logger.error("(getinfo) Failed to parse JSON.")

                # in case the JSON data provided is formatted incorrectly
                raise self.InvalidInfo

            # store the retrieved data
            self.uuid = client_uuid
            self.type = client_type
            self.data = client_data
            return None

    # check the heartbeat of the client returns None if client has a heartbeat
    def heartbeat(self, heartbeat_timeout: int = 15):
        # logging output
        self.logger.info("(heartbeat) Sending heartbeat request.")

        # init the lock
        with self.connection_lock:
            # logging output
            self.logger.debug("(heartbeat) Sending heartbeat packet.")

            # send the heartbeat command if it fails end the connection
            if not self.send(Packet(ReservedBytes.HEARTBEAT.value)):
                self.end(True)

            # logging output
            self.logger.debug("(heartbeat) Receiving heartbeat response.")

            # await a "beat" response or await timeout error
            beat = self.recv(timeout=heartbeat_timeout)

            # if the recv fails then end the client connection
            if beat is None:
                # logging output
                self.logger.warning("(heartbeat) Failed heartbeat check.")

                self.end(True)

            # if the client's response is not beat then return a incorrect response
            if beat.bytes == ReservedBytes.HEARTBEAT.value:
                # logging output
                self.logger.info("(heartbeat) Passed heartbeat check.")

                # return the alive response
                return True
            else:
                # logging output
                self.logger.warning("(heartbeat) Failed heartbeat check.")

                # end the connection if the response is incorrect
                self.end(True)

    # client info as a dict
    def return_data(self):
        if self.data is not None:
            return {
                "uuid": self.uuid,
                "type": self.type,
                "data": self.data
            }
        else:
            return None
