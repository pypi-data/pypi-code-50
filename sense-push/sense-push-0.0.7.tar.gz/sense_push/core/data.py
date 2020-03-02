from sense_push.util import *
from sense_push.common import *
import sense_core as sd


class PushDataHandler(object):

    def __init__(self, database=None, table=None, queue_configs=None):
        self.database = database
        self.table = table
        self.queue_configs = queue_configs

    def insert_data(self, data):
        message = build_push_message(PUSH_ACTION_INSERT, self.database, self.table, data)
        self.push_queue_message(message)

    def update_data(self, data):
        message = build_push_message(PUSH_ACTION_UPDATE, self.database, self.table, data)
        self.push_queue_message(message)

    def delete_data(self, data):
        message = build_push_message(PUSH_ACTION_DELETE, self.database, self.table, data)
        self.push_queue_message(message)

    def push_queue_message(self, message):
        for config in self.queue_configs:
            producer = sd.RabbitProducer(config_info=config)
            producer.send_safely(config['queue'], sd.dump_json(message), True, 1000000)
