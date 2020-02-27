from ssl import SSLContext
from typing import Dict, Optional, Union

import trio

from .._exceptions import (
    CloseError,
    ConnectError,
    ConnectTimeout,
    ReadError,
    ReadTimeout,
    WriteError,
    WriteTimeout,
    map_exceptions,
)
from .base import AsyncBackend, AsyncLock, AsyncSemaphore, AsyncSocketStream


def none_as_inf(value: Optional[float]) -> float:
    return value if value is not None else float("inf")


class SocketStream(AsyncSocketStream):
    def __init__(self, stream: Union[trio.SocketStream, trio.SSLStream],) -> None:
        self.stream = stream
        self.read_lock = trio.Lock()
        self.write_lock = trio.Lock()

    def get_http_version(self) -> str:
        if not isinstance(self.stream, trio.SSLStream):
            return "HTTP/1.1"

        ident = self.stream.selected_alpn_protocol()
        return "HTTP/2" if ident == "h2" else "HTTP/1.1"

    async def start_tls(
        self,
        hostname: bytes,
        ssl_context: SSLContext,
        timeout: Dict[str, Optional[float]],
    ) -> "SocketStream":
        connect_timeout = none_as_inf(timeout.get("connect"))
        exc_map = {
            trio.TooSlowError: ConnectTimeout,
            trio.BrokenResourceError: ConnectError,
        }
        ssl_stream = trio.SSLStream(
            self.stream, ssl_context=ssl_context, server_hostname=hostname
        )

        with map_exceptions(exc_map):
            with trio.fail_after(connect_timeout):
                await ssl_stream.do_handshake()
            return SocketStream(ssl_stream)

    async def read(self, n: int, timeout: Dict[str, Optional[float]]) -> bytes:
        read_timeout = none_as_inf(timeout.get("read"))
        exc_map = {trio.TooSlowError: ReadTimeout, trio.BrokenResourceError: ReadError}

        async with self.read_lock:
            with map_exceptions(exc_map):
                with trio.fail_after(read_timeout):
                    return await self.stream.receive_some(max_bytes=n)

    async def write(self, data: bytes, timeout: Dict[str, Optional[float]]) -> None:
        if not data:
            return

        write_timeout = none_as_inf(timeout.get("write"))
        exc_map = {
            trio.TooSlowError: WriteTimeout,
            trio.BrokenResourceError: WriteError,
        }

        async with self.write_lock:
            with map_exceptions(exc_map):
                with trio.fail_after(write_timeout):
                    return await self.stream.send_all(data)

    async def close(self) -> None:
        async with self.write_lock:
            with map_exceptions({trio.BrokenResourceError: CloseError}):
                await self.stream.aclose()

    def is_connection_dropped(self) -> bool:
        # Adapted from: https://github.com/encode/httpx/pull/143#issuecomment-515202982
        stream = self.stream

        # Peek through any SSLStream wrappers to get the underlying SocketStream.
        while hasattr(stream, "transport_stream"):
            stream = stream.transport_stream
        assert isinstance(stream, trio.SocketStream)

        # Counter-intuitively, what we really want to know here is whether the socket is
        # *readable*, i.e. whether it would return immediately with empty bytes if we
        # called `.recv()` on it, indicating that the other end has closed the socket.
        # See: https://github.com/encode/httpx/pull/143#issuecomment-515181778
        return stream.socket.is_readable()


class Lock(AsyncLock):
    def __init__(self) -> None:
        self._lock = trio.Lock()

    def release(self) -> None:
        self._lock.release()

    async def acquire(self) -> None:
        await self._lock.acquire()


class Semaphore(AsyncSemaphore):
    def __init__(self, max_value: int, exc_class: type):
        self.max_value = max_value
        self.exc_class = exc_class

    @property
    def semaphore(self) -> trio.Semaphore:
        if not hasattr(self, "_semaphore"):
            self._semaphore = trio.Semaphore(self.max_value, max_value=self.max_value)
        return self._semaphore

    async def acquire(self, timeout: float = None) -> None:
        timeout = none_as_inf(timeout)

        with trio.move_on_after(timeout):
            await self.semaphore.acquire()
            return

        raise self.exc_class()

    def release(self) -> None:
        self.semaphore.release()


class TrioBackend(AsyncBackend):
    async def open_tcp_stream(
        self,
        hostname: bytes,
        port: int,
        ssl_context: Optional[SSLContext],
        timeout: Dict[str, Optional[float]],
    ) -> AsyncSocketStream:
        connect_timeout = none_as_inf(timeout.get("connect"))
        exc_map = {
            trio.TooSlowError: ConnectTimeout,
            trio.BrokenResourceError: ConnectError,
        }

        with map_exceptions(exc_map):
            with trio.fail_after(connect_timeout):
                stream: trio.SocketStream = await trio.open_tcp_stream(hostname, port)

                if ssl_context is not None:
                    stream = trio.SSLStream(
                        stream, ssl_context, server_hostname=hostname
                    )
                    await stream.do_handshake()

                return SocketStream(stream=stream)

    def create_lock(self) -> AsyncLock:
        return Lock()

    def create_semaphore(self, max_value: int, exc_class: type) -> AsyncSemaphore:
        return Semaphore(max_value, exc_class=exc_class)

    def time(self) -> float:
        return trio.current_time()
