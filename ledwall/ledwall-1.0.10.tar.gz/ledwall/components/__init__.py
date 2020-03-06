from .display import Display, WireMode
from .color import Color
from .colortable import ColorTable
from .hsvcolor import HSVColor
from .rgbcolor import RGBColor
from .serialsender import SerialSender
from .mqttsender import MqttSender
from .asyncsender import AsyncSender
from .consolesender import ConsoleSender
from .sender import Sender
from .progmemsender import ProgMemSender
from .listsender import ListSender
from .udpsender import UDPSender
from .tcpsender import TCPSender
from .application import Application, Game, Animation

from .multidisplay import RegionSender

__all__ = [
    "Color",
    "Display",
    "ColorTable",
    "RGBColor",
    "HSVColor",
    "SerialSender",
    "MqttSender",
    "Sender",
    "ConsoleSender",
    "AsyncSender",
    "ProgMemSender",
    "ListSender",
    "UDPSender",
    "TCPSender",
    "Application",
    "LEDWallError",
    "TransmissionError",
    "CoordinateError",
    "Game",
    "Animation",
    "WireMode",
    "RegionSender",
]

name = "ledwall"


class LEDWallError(Exception):
    pass


class TransmissionError(LEDWallError):
    pass


class CoordinateError(LEDWallError):
    pass


def rgb_to_hsv(val):
    return RGBColor.fromIntValues(val[0], val[1], val[2]).hsv
