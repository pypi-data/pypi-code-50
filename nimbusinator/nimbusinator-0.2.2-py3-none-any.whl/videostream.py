from threading import Thread
import sys
import cv2
import time
from queue import Queue
import numpy as np


class VideoStream:
    
    def __init__(self, screen_size, transform=None, queue_size=128):
        # initialize the file video stream along with the boolean
        # used to indicate if the thread should be stopped or not
        self.stopped = False
        self.transform = transform
        # initialize the queue used to store frames 
        self.Q = Queue(maxsize=queue_size)
        # intialize thread
        self.thread = Thread(target=self.__update, args=())
        self.thread.daemon = True
        self.border_size = 20
        self.screen_size = screen_size
        self.screen_data = np.zeros((screen_size[1]+1, screen_size[0]+1, 3), dtype=np.uint8)

    def update_screen(self, new_screen_data):
        # change the data displayed on the screen
        self.screen_data = new_screen_data

    def get_screen(self):
        # get the current screen data
        return self.screen_data

    def start(self):
        # start a thread to read frames from the file video stream
        self.thread.start()
        return self

    def __update(self):
        # keep looping infinitely
        while True:
            # if the thread indicator variable is set, stop the
            # thread
            if self.stopped:
                break

            # otherwise, ensure the queue has room in it
            if not self.Q.full():
                frame = self.screen_data
                self.Q.put(frame)
            else:
                time.sleep(0.1)  # Rest for 10ms, we have a full queue

    # Insufficient to have consumer use while(more()) which does
    # not take into account if the producer has reached end of
    # file stream.
    def __running(self):
        return self.__more() or not self.stopped

    def __more(self):
        # return True if there are still frames in the queue. If stream is not stopped, try to wait a moment
        tries = 0
        while self.Q.qsize() == 0 and not self.stopped and tries < 5:
            time.sleep(0.1)
            tries += 1
        return self.Q.qsize() > 0

    def stop(self):
        # indicate that the thread should be stopped    
        self.stopped = True
        # wait until stream resources are released (producer thread might be still grabbing frame)
        self.thread.join()