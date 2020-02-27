import json
import asyncio

from typing import cast, Any, Dict, List, Tuple, Union

from .command_reply import CommandReply
from .container import Container
from .output import Output
from .protocol import Event, EventReplyType, MessageType, ReplyType
from .protocol import build, decode
from .sockpath import get_socket_path
from .version import Version
from .workspace import Workspace

from .binding_event import BindingEvent
from .mode_event import ModeEvent
from .window_event import WindowEvent
from .workspace_event import WorkspaceEvent


async def ipc_receive(sock) -> Tuple[Union[ReplyType, EventReplyType], str]:
    header = await sock.read(14)
    t, size = decode(header)
    payload = await sock.read(size)
    return t, payload.decode('utf-8')


EventType = Union[BindingEvent, ModeEvent, WindowEvent, WorkspaceEvent]


EVENT_TYPES = {
    EventReplyType.BINDING: BindingEvent,
    EventReplyType.MODE: ModeEvent,
    EventReplyType.WINDOW: WindowEvent,
    EventReplyType.WORKSPACE: WorkspaceEvent,
}  # type: Dict[EventReplyType, Any]


def make_event(ev_type: EventReplyType,
               data: Dict[str, Any]) -> EventType:
    return EVENT_TYPES[ev_type].from_dict(data)


class AsyncStream:
    def __init__(self, sockpath: str = None) -> None:
        self.sockpath = get_socket_path(sockpath)

    @classmethod
    async def create(cls, *args, **kwargs):
        instance = cls(*args, **kwargs)
        instance.reader, instance.writer = (
            await asyncio.open_unix_connection(instance.sockpath)
        )
        return instance

    async def send(self, msg_type: MessageType, msg: str = ''):
        message = build(msg_type, msg)
        self.writer.write(message)
        await self.writer.drain()

    async def receive(self) -> str:
        _, payload = await ipc_receive(self.reader)
        return payload


class AsyncBaseConnection:
    @classmethod
    async def create(cls, *args, **kwargs):
        instance = cls(*args, **kwargs)
        return instance


class AsyncQueryConnection(AsyncBaseConnection):
    @classmethod
    async def create(cls, *args, **kwargs):
        instance = await super().create(*args, **kwargs)
        instance.stream = await AsyncStream.create(*args, **kwargs)
        return instance

    async def get(self, msg_type: MessageType, msg: str = '') -> Any:
        await self.stream.send(msg_type, msg)
        return json.loads(await self.stream.receive())

    async def command(self, command: str):
        replies = await self.get(MessageType.COMMAND, command)
        return [CommandReply.from_dict(reply) for reply in replies]

    async def get_workspaces(self) -> List[Workspace]:
        wss = await self.get(MessageType.GET_WORKSPACES)
        return [Workspace.from_dict(ws) for ws in wss]

    async def get_outputs(self) -> List[Output]:
        outs = await self.get(MessageType.GET_OUTPUTS)
        return [Output.from_dict(out) for out in outs]

    async def get_tree(self) -> Container:
        return Container.from_dict(await self.get(MessageType.GET_TREE))

    async def get_marks(self) -> str:
        return await self.get(MessageType.GET_MARKS)

    async def get_bar_config(self) -> List[str]:
        return await self.get(MessageType.GET_BAR_CONFIG)

    async def get_version(self) -> Version:
        version = await self.get(MessageType.GET_VERSION)
        return Version.from_dict(version)

    async def get_binding_modes(self) -> List[str]:
        return await self.get(MessageType.GET_BINDING_MODES)


class AsyncSubscriptionConnection(AsyncBaseConnection):
    @classmethod
    async def create(cls, *args, **kwargs):
        instance = await super().create(*args, **kwargs)
        instance.sub_stream = await AsyncStream.create(*args, **kwargs)
        return instance

    async def subscribe(self, events: List[Event]):
        events_json = json.dumps([e.value for e in events])
        await self.sub_stream.send(MessageType.SUBSCRIBE, events_json)
        return await self.sub_stream.receive()

    async def next_event(self) -> EventType:
        t, payload = await ipc_receive(self.sub_stream.reader)
        return make_event(cast(EventReplyType, t), json.loads(payload))


class AsyncConnection(AsyncQueryConnection, AsyncSubscriptionConnection):
    pass
