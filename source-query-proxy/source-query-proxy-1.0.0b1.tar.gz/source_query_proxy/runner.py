import asyncio
import logging
from contextlib import suppress

import uvloop
from pid.decorator import pidfile

from source_query_proxy import config

from .proxy import QueryProxy

logger = logging.getLogger('sqproxy')


@pidfile('sqproxy', piddir=config.settings.piddir.as_posix())
def run():
    uvloop.install()
    with suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(_run_servers())


async def _run_servers():
    if not config.servers:
        logger.warning('No one server to run. Please check config')
        return

    coros = []
    for name, server in config.servers:
        # TODO: import QueryProxy implementation and use it
        coros.append(QueryProxy(server, name=name).run())

    await asyncio.gather(*coros)


if __name__ == '__main__':
    run()
