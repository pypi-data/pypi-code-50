import json
import time

from queue import PriorityQueue
from typing import List, Iterable, Dict

from ..commons.queue_item import PriorityQueueItem


class DataReceiver(object):
    class InternalReceiver(object):
        def __init__(self, shared_queue: PriorityQueue):
            """

            :param queue.PriorityQueue shared_queue:
            """
            self.shared_queue = shared_queue

        @staticmethod
        def _make_json_serializable(obj):
            try:
                iobj = int(obj)
                fobj = float(obj)
                if iobj == fobj:
                    return iobj
                return fobj
            except:
                return "%s.%s" % (obj.__class__.__module__, obj.__class__.__name__)

        def receive(self, data_dict: Dict):
            """

            :param {} data_dict:
            :return:
            """
            queue_item = PriorityQueueItem(priority_number=1, created_timestamp_micros=int(time.time()*1000000),
                                           datastr=json.dumps(data_dict, default=self._make_json_serializable))
            self.shared_queue.put(queue_item)

        def receive_batch(self, data_dict_list: Iterable[Dict]):
            """

            :param [{}] data_dict_list:
            :return:
            """
            for data_dict in data_dict_list:
                self.receive(data_dict=data_dict)

    INTERNAL_RECEIVER = None

    @classmethod
    def receive(cls, data_dict: Dict):
        if cls.INTERNAL_RECEIVER is not None:
            cls.INTERNAL_RECEIVER.receive(data_dict=data_dict)

    @classmethod
    def receive_batch(cls, data_dict_list: Iterable[Dict]):
        if cls.INTERNAL_RECEIVER is not None:
            cls.INTERNAL_RECEIVER.receive_batch(data_dict_list=data_dict_list)
