import unittest
import asyncio, time

from kafka_transport import init, finalize, subscribe, push, Listener

loop = asyncio.get_event_loop()

TO_TOPIC = 'totest'
FROM_TOPIC = 'fromtest'

class TestListener(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        loop.run_until_complete(init('192.168.250.10:9092'))

    @classmethod
    def tearDownClass(cls):
        loop.run_until_complete(finalize())


    def test_double_answers(self):
        async def start_requester():
            listener = Listener(FROM_TOPIC, TO_TOPIC)
            await listener.start()

            try:
                result = await listener.fetch('test data', timeout=1, key="12")
            finally:
                if "12" in listener.msg_to_wait:
                    raise Exception("Key not deleted")
                return

        loop.run_until_complete(start_requester())