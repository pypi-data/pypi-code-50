#!/usr/bin/env python3 

#Imports
from ProcessedPiRecorder.Buffer import buffer
import logging

#The class
class QueueHandler:
    def __init__(self, inputQueue, outputQueue, max_len=1):
        #Define the mp.Queues
        self.q1 = inputQueue
        self.q2 = outputQueue

        #Does the Handler have a frame?
        self.empty = True
        self.full_buffer = False
        self.finished = False

        #The buffers
        self.max_len = max_len
        self.frames  = buffer(max_len)
        self.ends    = buffer(max_len)
        self.lats    = buffer(max_len)

        #Give it a logger
        self.logger = logging.getLogger('qhandler_logger')

    #If q1 not empty get vals, update full/empty vars
    def get(self):
        #Check if the Queue is empty
        if self.q1.empty(): self.empty = True
        else:
            end, frame, lat = self.q1.get()

            #log frame arrival
            lat.log('Queue_hanlder_in')

            #append
            self.ends.append(end)
            self.frames.append(frame)
            self.lats.append(lat)

            #Check for end condition
            if self.ends.buffer[0] is True: self.finished = True

            #check status
            self.empty = False

            #provide frame for callback
            return frame

        #Check if the buffers are full
        if len(self.frames.buffer) != self.max_len: self.full_buffer = False
        else: self.full_buffer = True

    #Put into q2
    def put(self,idx=0):

        self.lats.buffer[idx].log('Queue_handler_out')        
        self.q2.put((self.ends.buffer[idx], self.frames.buffer[idx], self.lats.buffer[idx]))


    #Push the entire buffer through the queue
    def put_all(self):
        for r in range(len(self.frame.buffer)): self.put(r)
