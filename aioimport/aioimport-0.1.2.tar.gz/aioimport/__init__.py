import asyncio
import concurrent.futures
import functools
import importlib
import importlib.metadata
import typing


__version__: str = importlib.metadata.version("aioimport")


class Importer:
    __executor_factory: typing.Callable[..., concurrent.futures.ThreadPoolExecutor]
    __executor: typing.Optional[concurrent.futures.ThreadPoolExecutor] = None

    def __init__(
        self,
        max_workers: typing.Optional[int] = None,
        thread_name_prefix: str = "aioimport",
        initializer: typing.Optional[typing.Callable] = None,
        initargs: typing.Tuple = (),
    ) -> None:
        # See https://github.com/python/mypy/issues/708 for type ignore reason
        self.__executor_factory = functools.partial(  # type: ignore
            concurrent.futures.ThreadPoolExecutor,
            max_workers=max_workers,
            thread_name_prefix=thread_name_prefix,
            initializer=initializer,
            initargs=initargs,
        )

    def __get_executor(self) -> concurrent.futures.ThreadPoolExecutor:
        if self.__executor is None:
            self.__executor = self.__executor_factory()
        return self.__executor

    async def shutdown(self, wait: bool = False) -> None:
        if self.__executor is not None:
            self.__executor.shutdown(wait=wait)
            self.__executor = None

    async def __aenter__(self) -> "Importer":
        return self

    async def __aexit__(self, *_) -> None:
        await self.shutdown()

    async def import_module(
        self, name: str, package: typing.Optional[str] = None
    ) -> None:
        await asyncio.get_event_loop().run_in_executor(
            self.__get_executor(),
            functools.partial(importlib.import_module, name, package=package),
        )

    async def reload(self, module) -> None:
        # can't convince mypy that i can pass reload to run_in_executor
        await asyncio.get_event_loop().run_in_executor(
            self.__get_executor(), importlib.reload, module  # type: ignore
        )


importer = Importer()


async def import_module(name: str, package: typing.Optional[str] = None) -> None:
    await importer.import_module(name, package=package)


async def reload(module) -> None:
    await importer.reload(module)
