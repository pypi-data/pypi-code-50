import asyncio
from typing import Optional, TYPE_CHECKING

from .objects import Package, IngActuator, ACTUATOR_BLIND, IngMeterBus, IngSif, IngThermostat

if TYPE_CHECKING:
    from .api import IngeniumAPI


class CustomProtocol(asyncio.Protocol):
    api: 'IngeniumAPI'
    transport: asyncio.Transport
    interrupted_buffer: bytes = bytes()

    def __init__(self, api: 'IngeniumAPI'):
        self.api = api

    def connection_made(self, transport: asyncio.Transport):
        self.transport = transport

    def data_received(self, original_data: bytes):
        data = self.interrupted_buffer + original_data
        self.interrupted_buffer = bytes()
        data_len = len(data)

        loop = asyncio.get_event_loop()

        if data_len >= 9:
            i = 0
            while i <= data_len - 9:
                # Skip until valid header
                if data[i] != 0xFE or data[i + 1] != 0xFE:
                    print("Invalid header, skipped!")
                    i += 1
                    continue

                p = Package(
                    ((data[i + 5] << 8) + data[i + 6]) & 0xFFFF,
                    ((data[i + 3] << 8) + data[i + 4]) & 0xFFFF,
                    data[i + 2], data[i + 7], data[i + 8])
                # print("Received: " + str(p))
                loop.create_task(self._notify_package(p))

                i += 9

            if i != data_len:
                self.interrupted_buffer = data[i:]
                print("Interruped! Creating buffer of size " + str(len(self.interrupted_buffer)))

    async def _notify_package(self, p: Package):
        for o in self.api.objects:
            if await o.update_state(p):
                for c in o.components:
                    try:
                        c.update_notify()
                    except RuntimeError:
                        print("Error notifying of change!")

    def connection_lost(self, exc):
        print("Connection lost!")


class CustomConnection:
    def __init__(self, api: 'IngeniumAPI', host: str, port: int):
        self.api = api
        self.host = host
        self.port = port
        self.transport: Optional[asyncio.Transport] = None
        self.protocol: Optional[CustomProtocol] = None

        self._is_closed = False
        self.trying_to_connect = False

    async def async_connect(self):
        if self.trying_to_connect or self._is_closed:
            return
        self.trying_to_connect = True

        loop = asyncio.get_event_loop()

        # If we don't have a connection or it's closing, we make a new one
        if self.transport is None or self.transport.is_closing():
            # Retry a couple of times
            for i in range(0, 6):
                try:
                    self.transport, self.protocol = await loop.create_connection(lambda: CustomProtocol(self.api),
                                                                                 host=self.host, port=self.port)
                    break
                except OSError:
                    print("Error connecting, retrying in 5 seconds...")
                    await asyncio.sleep(5)

        self.trying_to_connect = False

    async def send(self, data: Package):
        if self._is_closed:
            return

        # print("Sent: " + str(data))
        if self.transport.is_closing():
            print("Transport is closed, reconnecting...")
            await self.async_connect()
        try:
            self.transport.write(data.as_bytes())
        except BaseException as e:
            print("Exception sending: " + str(e))

    async def send_ka(self):
        if self._is_closed:
            return
        if self.transport.is_closing():
            print("Transport KA is closed, reconnecting...")
            await self.async_connect()
        try:
            self.transport.write(Package(0xFFFF, 0xFE, 0x7A, 0xFF, 0xFF).as_bytes())
        except BaseException as e:
            print("Exception sending KA: " + str(e))

    async def send_cpolling(self):
        if self._is_closed:
            return
        if self.transport.is_closing():
            print("Transport CP is closed, reconnecting...")
            await self.async_connect()
        try:
            self.transport.write(Package(0xFFFF, 0xFFFF, 10, 0, 0).as_bytes())
        except BaseException as e:
            print("Exception sending CP: " + str(e))

    def close(self):
        self._is_closed = True
        try:
            self.transport.close()
        except BaseException as e:
            print("Exception closing conn: " + str(e))


async def delay_cpolling(conn: CustomConnection):
    await asyncio.sleep(5)
    await conn.send_cpolling()


async def keep_alive(conn: CustomConnection):
    while True:
        await asyncio.sleep(10)
        await conn.send_ka()


async def initial_read(api: 'IngeniumAPI'):
    for o in api.objects:
        if isinstance(o, IngMeterBus) or isinstance(o, IngThermostat):
            await api.connection.send(Package(0xFFFF, o.address, 10, 0, 0))

        elif isinstance(o, IngSif) or isinstance(o, IngActuator) and o.mode == ACTUATOR_BLIND:
            await o.read_state()
        else:
            continue
        await asyncio.sleep(0.3)


async def start_connection(api: 'IngeniumAPI', host: str, port: int):
    conn = CustomConnection(api, host, port)
    api._connection = conn
    await conn.async_connect()

    loop = asyncio.get_event_loop()

    loop.create_task(delay_cpolling(conn))
    loop.create_task(keep_alive(conn))
    loop.create_task(initial_read(api))
