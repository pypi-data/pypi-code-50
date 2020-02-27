from typing import Optional
import time
import logging
from threading import Lock, Condition
from queue import Queue, Empty


logger = logging.getLogger(__name__)


class QueueBuffer:
    def __init__(self):
        self.buffer = bytes()
        self.lock = Lock()
        self.tag = ''

    def size(self):
        return len(self.buffer)

    def clear(self):
        with self.lock:
            self.buffer = bytes()

    def read(self, num_bytes: Optional[int]=None, timeout: Optional[float]=None) -> bytes:
        data = bytes()
        size = self.size()
        remaining = size if not num_bytes else num_bytes

        if num_bytes == 0:
            return b''

        if self.tag:
            logger.debug(f'Buffer ({self.tag}) read: num_bytes={num_bytes}, timeout={timeout}')

        end_time = time.time() + timeout if timeout is not None else 0
        while remaining > 0:
            if timeout is not None and time.time() > end_time:
                break

            if len(self.buffer) > 0 and self.lock.acquire(blocking=False):
                if self.tag:
                    logger.debug(f'Buffer ({self.tag}) read lock acquired')
                chunk = self.buffer[:remaining]
                chunk_len = len(chunk)
                self.buffer = self.buffer[chunk_len:]
                data += chunk
                remaining -= chunk_len
                self.lock.release()
                if self.tag:
                    logger.debug(f'Buffer ({self.tag}) read lock released')

        return data

    def read_all(self, timeout: Optional[float]=None):
        return self.read(self.size(), timeout=timeout)

    def write(self, data: bytes):
        if self.tag:
            logger.debug(f'Buffer ({self.tag}) write: {data}')
        try:
            self.lock.acquire(timeout=1.0)
            if self.tag:
                logger.debug(f'Buffer ({self.tag}) write lock acquired')
            self.buffer += data
            if self.tag:
                logger.debug(f'Buffer ({self.tag}) write lock released')
            self.lock.release()
        except Exception as err:
            print(err)