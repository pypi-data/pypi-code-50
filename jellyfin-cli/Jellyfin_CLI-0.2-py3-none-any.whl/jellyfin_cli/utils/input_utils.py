from asyncio import Queue, get_event_loop
from concurrent.futures import ThreadPoolExecutor

class KeyPressWatcher:
    def __init__(self, window):
        self.window = window
        self.loop = get_event_loop()
        self.executor = ThreadPoolExecutor()
        self.queue = Queue(10)

    async def _run(self):
        while True:
            key = await self.loop.run_in_executor(self.executor, self.window.getch)
            await self.queue.put(key)
        
    def run(self):
        self.loop.create_task(self._run())