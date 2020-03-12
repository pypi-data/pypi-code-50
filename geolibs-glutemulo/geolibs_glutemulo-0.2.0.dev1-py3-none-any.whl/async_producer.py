from glutemulo.errors import SerializerError, ProducerError


class AsyncProducer:
    async def produce(self, topic, value, **options):
        message, extra_options = self.get_message_and_options(topic, value, options)
        data = self.serialize(message, **extra_options)
        return await self.send(topic, data)

    def get_message_and_options(self, topic, value, options):
        """Driver specific. Serialize options and build message"""
        return value, options

    def serialize(self, message, *extra_options):
        """Driver specific. Serialize message to send to kafka"""
        raise SerializerError("Implement this!")

    async def send(self, topic, data):
        raise ProducerError("Implement this!")
