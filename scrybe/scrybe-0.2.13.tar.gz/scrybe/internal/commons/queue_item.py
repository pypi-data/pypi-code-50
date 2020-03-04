class PriorityQueueItem(object):

    def __init__(self, priority_number, created_timestamp_micros, datastr):
        """

        :param int priority_number:
        :param int created_timestamp_micros:
        :param str datastr:
        :return:
        """
        self.priority_number = priority_number
        self.created_timestamp_micros = created_timestamp_micros
        self.datastr = datastr

    def __lt__(self, other):
        """

        :param SharedQueueItem other:
        :return:
        """
        if self.priority_number < other.priority_number:
            return True
        elif self.priority_number > other.priority_number:
            return False
        else:
            if self.created_timestamp_micros < other.created_timestamp_micros:
                return True
            elif self.created_timestamp_micros > other.created_timestamp_micros:
                return False
            else:
                return True
