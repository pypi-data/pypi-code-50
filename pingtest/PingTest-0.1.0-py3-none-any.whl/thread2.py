import threading
import time


class myThread(threading.Thread):
    def __init__(self, ind):
        threading.Thread.__init__(self)
        self.ind = ind
 #       self.lock = lock

    def run(self):
        global results
        print(self.ind)
        time.sleep(1)
#        with self.lock:
        results.append(self.ind)



results = []
#lock = threading.Lock()
threads = [myThread(x) for x in range(1, 18)]
for t in threads:
    t.start()
#for t in threads:
#    t.join()
time.sleep(4)
print(results)
