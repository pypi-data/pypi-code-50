#1/usr/bin/env python3

#quick list buffer class with collections.deque like append
#didn't use a collections.deque because they don't allow for random indexing
class buffer:
    def __init__(self, max_len=1):
        self.buffer = list()
        self.max_len = max_len
        
    def append(self, data):
        self.buffer.append(data)

        #if over the max len trim
        if len(self.buffer) > self.max_len:
            del self.buffer[:-self.max_len]
