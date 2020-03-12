import json
import asyncio

from glutemulo.config import config
from glutemulo.errors import ProducerError, SerializerError
from glutemulo.async_producer import AsyncProducer
from aiokafka import AIOKafkaProducer as AsyncKafkaProducer
from aiokafka.errors import KafkaError


class AsyncKafka(AsyncProducer):
    def __init__(self, loop, topic=None, **producer_config):
        if not "bootstrap_servers" in producer_config:
            producer_config["bootstrap_servers"] = config["ingestor_bootstap_servers"]
        if topic is None:
            topic = config["ingestor_topic"]
        self.topic = topic

        self.producer = AsyncKafkaProducer(loop=loop, **producer_config)
        self.started = False

    async def start_producer(self):
        if not self.started:
            await self.producer.start()
            self.started = True

    async def produce(self, topic, value, **options):
        await self.start_producer()
        if topic is None:
            topic = self.topic
        return await super().produce(topic, value, **options)

    async def send(self, topic, serialized_data):
        try:
            return await self.producer.send(topic, serialized_data)
        except KafkaError as error:
            raise ProducerError(f"Kafka error: {error.args}")


class AsyncJsonKafka(AsyncKafka):
    def serialize(self, message):
        return json.dumps(message).encode("utf-8")
