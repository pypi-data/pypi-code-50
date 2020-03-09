from message_bus_redis.abc import Message
from typing import AsyncGenerator, List, Union


class MessageBus:
    def __init__(self):
        pass

    async def send(self, message: Message) -> None:
        pass

    async def receive(self, message: Union[Message, List[Message]],
                      *, status: Union[str, List[str]] = None) -> AsyncGenerator[Message]:
        pass
