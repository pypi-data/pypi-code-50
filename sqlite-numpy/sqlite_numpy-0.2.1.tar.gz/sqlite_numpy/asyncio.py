import asyncio
import concurrent.futures
import contextlib
import typing

import numpy  # type:ignore

import sqlite_numpy.core

ParamDict = typing.Dict[str, typing.Any]


class _AsyncResultProxy:
    def __init__(
        self,
        proxy: sqlite_numpy.core.ResultProxy,
        executor: concurrent.futures.Executor,
    ) -> None:
        self._proxy = proxy
        self._executor = executor

    async def fetchall(self) -> typing.Dict[str, numpy.array]:
        return await asyncio.get_running_loop().run_in_executor(
            self._executor, self._proxy.fetchall
        )

    async def fetchmany(self, count: int) -> typing.Dict[str, numpy.array]:
        return await asyncio.get_running_loop().run_in_executor(
            self._executor, self._proxy.fetchmany, count
        )

    async def close(self) -> None:
        await asyncio.get_running_loop().run_in_executor(
            self._executor, self._proxy.close
        )

    @property
    def closed(self) -> bool:
        return self._proxy.closed


class AsyncDatabase:
    _executor: concurrent.futures.Executor = concurrent.futures.ThreadPoolExecutor()

    @classmethod
    def set_executor(cls, executor: concurrent.futures.Executor) -> None:
        cls._executor = executor

    def __init__(self, path: str) -> None:
        self._database = sqlite_numpy.core.Database(path)

    async def __aenter__(self) -> "AsyncDatabase":
        await asyncio.get_running_loop().run_in_executor(
            self._executor, self._database.open
        )
        return self

    async def __aexit__(
        self, exc_type: typing.Type[Exception], exc_value: Exception, tracebace: object
    ) -> None:
        await self.close()

    @property
    def closed(self) -> bool:
        return self._database.closed

    @contextlib.asynccontextmanager
    async def execute(
        self, sql_statement: str, bind_params: typing.Optional[ParamDict] = None
    ) -> typing.AsyncGenerator[_AsyncResultProxy, None]:
        proxy = await asyncio.get_running_loop().run_in_executor(
            self._executor, self._database.execute, sql_statement, bind_params
        )
        async_proxy = _AsyncResultProxy(proxy, self._executor)
        try:
            yield async_proxy
        finally:
            await async_proxy.close()

    async def close(self) -> None:
        await asyncio.get_running_loop().run_in_executor(
            self._executor, self._database.close
        )
