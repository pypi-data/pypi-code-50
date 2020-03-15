import logging
logging.basicConfig(level=logging.DEBUG)

from .bridge import main, stopEvent
import asyncio, signal

loop = asyncio.get_event_loop()

try:
    loop.add_signal_handler(signal.SIGINT, stopEvent.set)
    loop.add_signal_handler(signal.SIGTERM, stopEvent.set)
except NotImplementedError:
    pass  # Ignore if not implemented. Means this program is running in windows.

try: 
    loop.run_until_complete(main('test.mosquitto.org', None))
except KeyboardInterrupt:
    pass