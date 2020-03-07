import asyncio
import concurrent.futures
import functools
import importlib
import importlib.metadata
import types
import typing


__version__: str = importlib.metadata.version("aioimport")


class Importer:
    _executor_factory: typing.Callable[..., concurrent.futures.ThreadPoolExecutor]
    _executor: typing.Optional[concurrent.futures.ThreadPoolExecutor] = None

    def __init__(
        self,
        max_workers: typing.Optional[int] = None,
        thread_name_prefix: str = "",
        initializer: typing.Optional[typing.Callable] = None,
        initargs: typing.Tuple = (),
    ) -> None:
        # See https://github.com/python/mypy/issues/708 for type ignore reason
        self._executor_factory = functools.partial(  # type: ignore
            concurrent.futures.ThreadPoolExecutor,
            max_workers=max_workers,
            thread_name_prefix=thread_name_prefix,
            initializer=initializer,
            initargs=initargs,
        )

    def _get_executor(self) -> concurrent.futures.ThreadPoolExecutor:
        if self._executor is None:
            self._executor = self._executor_factory()
        return self._executor

    def shutdown(self, wait: bool = True) -> None:
        if self._executor is not None:
            self._executor.shutdown(wait=wait)
            self._executor = None

    async def import_module(
        self, name: str, package: typing.Optional[str] = None
    ) -> types.ModuleType:
        executor = self._get_executor()
        return await asyncio.get_event_loop().run_in_executor(
            executor, functools.partial(importlib.import_module, name, package=package)
        )

    async def cache_module(
        self, name: str, package: typing.Optional[str] = None
    ) -> None:
        await self.import_module(name, package=package)


default = Importer()


async def import_module(
    name: str, package: typing.Optional[str] = None
) -> types.ModuleType:
    return await default.import_module(name, package=package)


async def cache_module(name: str, package: typing.Optional[str] = None) -> None:
    await default.cache_module(name, package=package)
