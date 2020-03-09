from abc import ABC, abstractmethod


class Message(ABC):
    @abstractmethod
    def serialize(self) -> bytes:
        pass

    @classmethod
    @abstractmethod
    def deserialize(cls, data: bytes) -> 'Message':
        pass
