from enum import Enum


class MessageType(Enum):
    REPLY = 0
    AUDIO = 1
    DOCUMENT = 2
    ANIMATION = 3
    IMAGE = 4
    STICKER = 5
    VIDEO = 6
    VOICE = 7
    VIDEO_NOTE = 8
    CONTACT = 9
    LOCATION = 10
    VENUE = 11
    TEXT = 12
    COMMAND = 13
