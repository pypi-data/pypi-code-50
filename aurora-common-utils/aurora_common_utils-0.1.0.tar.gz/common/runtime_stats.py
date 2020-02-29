import os
import time


class RuntimeStats(object):
    def __init__(self, base_path, file_name, log_prefix="-"):
        self.base_path = base_path
        self.file_name = file_name
        self.log_prefix = log_prefix
        self.start_time = None
        self.f = open(os.path.join(self.base_path, self.file_name), "a+")

    def start_stats(self):
        self.start_time = time.time()

    def end_stats(self, key_word=""):
        if not self.start_time:
            return
        cost_time = time.time() - self.start_time
        self.f.write(self.log_prefix + " - " + key_word + " - cost time: " + str(cost_time) + " s\n")
        self.f.flush()

    def dot_stats(self, key_word):
        if not self.start_time:
            self.start_stats()
            return
        self.end_stats(key_word)
        self.start_stats()

    def dispose(self):
        if not self.f:
            self.f.flush()
            self.f.close()
