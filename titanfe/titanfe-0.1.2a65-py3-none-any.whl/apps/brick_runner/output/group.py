#
# Copyright (c) 2019-present, wobe-systems GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# found in the LICENSE file in the root directory of this source tree.
#

"""Group represents multiple consumers of the same type"""

import asyncio
from collections import deque

from titanfe.utils import cancel_tasks, pairwise


class ConsumerGroup:
    """Group consumers of same type and distribute packets between them"""
    def __init__(self, name, queue, autoscale_queue_level=0, slow_queue_alert_cb=None):
        self.name = name

        self.consumers = []
        self.packets = queue

        self.new_consumer_entered = asyncio.Event()

        self.tasks = [
            asyncio.create_task(self.send_packets()),
            asyncio.create_task(
                self.check_scaling_required(autoscale_queue_level, slow_queue_alert_cb)
            ),
        ]

    def __iter__(self):
        return iter(self.consumers)

    async def close(self):
        await asyncio.gather(*[consumer.close_connection() for consumer in self])
        await cancel_tasks(self.tasks, wait_cancelled=True)

    async def check_scaling_required(
            self, autoscale_queue_level=0, slow_queue_alert_cb=None, check_interval=1
    ):
        """ watch the queue and dispatch an alert if it grows continuously,
            then wait for a new consumer before resetting the queue history - repeat."""
        if not autoscale_queue_level or not slow_queue_alert_cb:
            return

        # wait for the first consumer to come in
        await self.new_consumer_entered.wait()
        self.new_consumer_entered.clear()

        history = deque(maxlen=5)

        while True:
            await asyncio.sleep(check_interval)
            current_queue_size = self.packets.qsize()
            history.append(current_queue_size)

            if current_queue_size < autoscale_queue_level or len(history) < 3:
                continue

            queue_is_growing = all(0 < prev <= curr for prev, curr in pairwise(history))
            if queue_is_growing:
                await slow_queue_alert_cb(self.name)
                await self.new_consumer_entered.wait()

            self.new_consumer_entered.clear()
            history.clear()

    def add(self, consumer):
        self.consumers.append(consumer)
        self.new_consumer_entered.set()
        self.tasks.append(asyncio.create_task(self.handle_disconnect(consumer)))

    async def handle_disconnect(self, consumer):
        await consumer.disconnected.wait()
        self.consumers.remove(consumer)

    async def enqueue(self, packet):
        await self.packets.put(packet)

    async def send_packets(self):
        while True:
            packet = await self.packets.get()
            consumer = await self.get_receptive_consumer()
            await consumer.send(packet)
            self.packets.task_done()

    async def get_receptive_consumer(self):
        """wait until any of the consumers is ready to receive and then return it"""
        while not self.consumers:
            await asyncio.sleep(0.1)

        while self.consumers:
            done, pending = await asyncio.wait(
                {consumer.is_receptive() for consumer in self}, return_when=asyncio.FIRST_COMPLETED
            )
            await cancel_tasks(pending)
            return done.pop().result()
