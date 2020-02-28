from time import time


class ExecutionTime(object):
    def __init__(self):
        self.times = []

    def start_time_calculation(self, scope):
        t1 = time()
        self.times.append((scope, t1))

    def stop_time_calculation(self, scope, message=''):
        t2 = time()

        t1 = None
        for s, t in self.times:
            if s == scope:
                t1 = t
        if t1:
            t = (t2 - t1) * 1000
            print('{} executed in {} ms'.format(message, int(t)))
        else:
            print('Time with {} scope not found'.format(scope))
