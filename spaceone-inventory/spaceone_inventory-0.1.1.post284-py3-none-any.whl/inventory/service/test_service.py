# -*- coding: utf-8 -*-
import logging
from spaceone.core.service import *
from spaceone.inventory.manager.test_manager import TestManager
from spaceone.inventory.error import *

import threading
import queue

import multiprocessing
from pebble import ProcessPool, ThreadPool
from concurrent.futures import TimeoutError
import time


_LOGGER = logging.getLogger(__name__)
QUEUE_BUFSIZE = 64
MAX_THREAD = 3
TIMEOUT = 3
MAX_TIMEOUT = 30

@authentication_handler
@authorization_handler
@event_handler
class TestService(BaseService):

    def __init__(self, metadata):
        super().__init__(metadata)
        self.test_mgr: TestManager = self.locator.get_manager('TestManager')
        self.q = queue.Queue(QUEUE_BUFSIZE)

    def _thread_manager(self, func, tests):
        _LOGGER.debug("====== MANAGER START ======")

        threads = []
        for num in range(MAX_THREAD):
            _LOGGER.debug("==== THREAD " + str(num) + " START =====")
            threads.append(threading.Thread(target=self._thread_worker, args=(func,)))

        list(map(lambda test: self.q.put(test), tests))
        list(map(lambda t: t.start(), threads))
        list(map(lambda t: t.join(), threads))

    def _thread_worker(self, func):
        while True:
            if self.q.empty():
                break

            test = self.q.get()
            # _LOGGER.debug("*** " + test + " ***")
            _t = threading.Thread(target=func, args=(test,))
            _t.start()
            _t.join()

    @transaction
    def test_mt(self, params):
        tests = params.get('test', [])

        _LOGGER.debug("====== START ======")
        t = threading.Thread(target=self._thread_manager, args=(self.test_mgr.test, tests))
        t.start()
        t.join()

        return params

    @transaction
    def test_mt2(self, params):
        tests = params.get('test', [])

        results = []
        _LOGGER.debug("====== START ======")
        with ThreadPool(max_workers=MAX_THREAD) as pool:
            start = time.time()
            future = pool.map(self.test_mgr.test, tests)
            _iter = future.result()

            while True:
                try:
                    _res = next(_iter)
                    _LOGGER.debug(_res)
                    results.append(_res)
                except StopIteration:
                    break
                except TimeoutError:
                    _LOGGER.debug('TIMEOUT')
                except Exception as e:
                    _LOGGER.debug(e)

            end = time.time()
            _LOGGER.debug(end - start)

        _LOGGER.debug(results)
        return params

    @transaction
    def test_mp(self, params):
        tests = params.get('test', [])
        results = []
        _LOGGER.debug("====== START ======")
        with ProcessPool(max_workers=MAX_THREAD) as pool:
            start = time.time()
            future = pool.map(self.test_mgr.test, tests, timeout=TIMEOUT)
            _iter = future.result()

            while True:
                try:
                    _res = next(_iter)
                    _LOGGER.debug(_res)
                    results.append(_res)
                except StopIteration:
                    break
                except TimeoutError:
                    _LOGGER.debug('TIMEOUT')
                except Exception as e:
                    _LOGGER.debug(e)

            end = time.time()
            _LOGGER.debug(end - start)

            pool.close()

        _LOGGER.debug(results)
        return params