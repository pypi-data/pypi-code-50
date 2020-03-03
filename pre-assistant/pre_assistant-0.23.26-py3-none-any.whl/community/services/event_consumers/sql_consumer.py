import logging

from typing import Text, List, Optional, Union, Dict

import rasax.community.config as rasa_x_config

import time

from rasa.utils import endpoints

from rasax.community.constants import DEFAULT_RASA_ENVIRONMENT
from rasax.community.services.event_consumers.event_consumer import EventConsumer

logger = logging.getLogger(__name__)


class SQLEventConsumer(EventConsumer):
    type_name = "sql"

    def __init__(
        self,
        dialect: Text = "postgresql",
        host: Optional[Text] = None,
        port: Optional[int] = None,
        db: Text = "events",
        username: Optional[Text] = None,
        password: Optional[Text] = None,
        should_run_liveness_endpoint: bool = False,
    ):
        from rasa.core.brokers.sql import SQLProducer, SQLEventBroker
        print("###################### WE ARE USING SQL EVENT CONSUMER")

        self.producer = SQLEventBroker(dialect, host, port, db, username, password)
        super().__init__(should_run_liveness_endpoint)


    @classmethod
    def from_endpoint_config(
        cls,
        consumer_config: Optional[endpoints.EndpointConfig],
        should_run_liveness_endpoint: bool = not rasa_x_config.LOCAL_MODE,
    ) -> Optional["SQLEventConsumer"]:
        if consumer_config is None:
            logger.debug(
                "Could not initialise `SQLEventConsumer` from endpoint config."
            )
            return None

        return cls(
            host=consumer_config.url,
            **consumer_config.kwargs,
            should_run_liveness_endpoint=should_run_liveness_endpoint,
        )    

    def consume(self):
        logger.info("Start consuming SQLite events from database 'events.db'.")
        with self.producer.session_scope() as session:
            while True:
                new_events = (
                    session.query(self.producer.SQLBrokerEvent)
                    .order_by(self.producer.SQLBrokerEvent.id.asc())
                    .all()
                )

                for event in new_events:
                    self.log_event(
                        event.data,
                        sender_id=event.sender_id,
                        event_number=event.id,
                        origin=DEFAULT_RASA_ENVIRONMENT,
                    )
                    session.delete(event)
                    session.commit()

                time.sleep(0.01)
