import threading
import asyncio
from aiohttp import web

def server_config(runner):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(runner.setup())
    site = web.TCPSite(runner, 'localhost', 5000)
    loop.run_until_complete(site.start())
    loop.run_forever()

def aiohttp_config(callback):
    app = web.Application()
    app.add_routes([web.get('/callback', callback)])
    runner = web.AppRunner(app)
    return runner    

def run(callback):
    t = threading.Thread(target=server_config, args=(aiohttp_config(callback),))
    t.start()