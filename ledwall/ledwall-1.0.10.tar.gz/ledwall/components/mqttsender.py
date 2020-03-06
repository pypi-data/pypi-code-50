from __future__ import print_function

from .sender import Sender
from .color import Color

import paho.mqtt.client as mqtt
from socket import error as SocketError


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("$SYS/#")
    client.loop_start()


def on_message(client, userdata, msg):
    print(msg.topic)


class MqttSender(Sender):
    """

    """

    MAX_PAYLOAD_SIZE = 80
    """The maximum length for the payload part of mqtt 
    message in bytes. This includes the command part as well
    as the data patr of every command.
    """

    def __init__(self, server="nebuhr", port=1883):
        """Server is the server name or the ip of the mqtt server.
        This class was successfully tested with the mosquitto.

        :param str server: Name or IP of the MqttServer.
        :param int port: The port of the MqttServer
        """
        super().__init__()
        self._server = server
        self._port = port
        self._client = mqtt.Client()

        self._client.on_connect = on_connect
        self._client.on_message = on_message

        self._client.connect(server, port, 60)

    # The callback for when a PUBLISH message is received from the server.

    def update(self):
        max_payload_size = MqttSender.MAX_PAYLOAD_SIZE - 7
        data = self.panel.data
        panel_data_size = len(data)

        for i in range(0, panel_data_size, max_payload_size):
            self.raw_write(i, [Color.gammaCorrection(x) for x in data[i : i + max_payload_size]])

        self.raw_show()

    def _set_pixel(self, offset, r, g, b):
        self._publish([Sender.CMD_SET_PIXEL] + self.itob(offset) + self._frame_number + [r, g, b])

    def raw_write(self, offset, data):
        size = len(data)
        if offset >= self.panel.byte_count:
            raise ValueError("Offset to high")
        if offset < 0:
            raise ValueError("Offset may not be negative")
        if (offset + size) > self.panel.byte_count:
            raise ValueError("Data exceeds buffer size")

        self._publish(
            [Sender.CMD_WRITE_RAW]
            + self._frame_number
            + self.itob(offset)
            + self.itob(size)
            + [x for x in data]
        )

    def raw_show(self):
        self._publish([Sender.CMD_SHOW] + self._frame_number)

    def init(self, panel):
        """

        :param panel:
        :return:
        """
        super().init(panel)
        data = [Sender.CMD_INIT_PANEL, self.panel.columns, self.panel.rows] + self._frame_number
        self._publish(data)

    def _publish(self, data):
        try:
            self._client.publish(self.panel.id, bytearray(data))
        except SocketError:
            print("Could not send data.")

    @staticmethod
    def itob(value):
        return [(value >> 8) & 0xFF, value & 0xFF]

    @property
    def _frame_number(self):
        return self.itob(self.panel.frame)
