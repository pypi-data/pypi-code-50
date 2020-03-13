import asyncio
import importlib
import importlib.metadata
import typing


__version__: str = importlib.metadata.version("aioimport")


async def import_module(name: str, package: typing.Optional[str] = None) -> None:
    await asyncio.get_event_loop().run_in_executor(
        None, importlib.import_module, name, package,
    )


async def reload(module) -> None:
    await asyncio.get_event_loop().run_in_executor(
        None, importlib.reload, module,
    )
