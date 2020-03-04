from time import time, sleep


class Timenote:
    def __init__(self, words=None, intimeshow=False):
        self.time_start = 0
        self.time_spec = []
        self.name = []
        self.n = 0
        self.intimeshow = intimeshow
        self.pause_a = 0
        self.pause_b = 0
        self.paused = False
        if words:
            self.words = words
        else:
            self.words = "阶段[{}]：{}时间花费 {} 秒"

    def start(self, name=None):
        if self.paused:
            self.paused = False
            self.pause_b = time()
            self.time_start += self.pause_b - self.pause_a
        else:
            self.n += 1
            self.time_start = time()
            if name:
                self.name.append(name)
            else:
                self.name.append(str(self.n))

    def end(self):
        if self.paused:
            self.paused = False
            self.pause_b = time()
            self.time_start += self.pause_b - self.pause_a
        self.time_spec.append(time() - self.time_start)
        if self.intimeshow:
            print(self.words.format(self.name[-1], '', self.time_spec[-1]))

    def note(self, name=None):
        self.end()
        self.start(name=name)

    def pause(self):
        if not self.paused:
            self.paused = True
            self.pause_a = time()

    def show(self):
        long = max([len(i) for i in self.name])
        for i in range(self.n):
            print(self.words.format(self.name[i], ' '*(long - len(self.name[i]) + 1), self.time_spec[i]))

    def sleep(self, n):
        sleep(n)
