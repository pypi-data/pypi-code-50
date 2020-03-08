import json

from google.cloud import pubsub_v1


class TopicPublisher:
    def __init__(self, project: str, topic: str):
        """
        Simple Interface to the Publisher mechanism for the pub/sub suite.

        Provide the Project and Topic in the constructor and call the publish method to publish data.

        :param project: Project ID from the GCP console. i.e. "fxqlabs-net-3a8ea"
        :param topic: Topic name from the GCP console. i.e. "etl-event"
        """
        self._publisher = pubsub_v1.PublisherClient()
        self._topic_path = self._publisher.topic_path(project, topic)

    def publish(self, data: dict) -> str:
        """
        Publish the provided data to the topic

        Example Usage::

            publisher.publish({"name": "elf", "age": 21})


        :param data: Data must be dict that can be converted to json string.
        :return: Returns the Event ID as a string i.e. '1029474508993984'
        """
        future = self._publisher.publish(self._topic_path, data=json.dumps(data).encode("utf-8"))
        if future.exception():
            raise Exception(future.exception())
        else:
            return future.result()


if __name__ == '__main__':
    publisher = TopicPublisher("fxqlabs-net-3a8ea", "etl-event")
    r = publisher.publish({"name": "elf", "age": 21})
    print(r)
