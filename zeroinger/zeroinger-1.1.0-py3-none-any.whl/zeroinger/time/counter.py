import time
from zeroinger.time.stopwatch import StopWatch
from logzero import logger


class Counter:
    def __init__(self, name, log_interval=100, total_count=None):
        self.name = name
        self.timer = StopWatch.create_instance()
        self.count_value = 0
        self.log_interval = log_interval
        self.total_count = total_count

    def count(self, value=1):
        self.count_value += value
        if self.count_value % self.log_interval == 0:
            if self.total_count is None:
                logger.info('{}|{}ms|{}'.format(self.name, self.timer.duration(), self.count_value))
            else:
                logger.info(
                    '{}|{}ms|{}/{}={}'.format(self.name, self.timer.duration(), self.count_value, self.total_count,
                                              self.count_value / max(self.total_count, 1)))

        pass
