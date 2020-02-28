#!/usr/bin/env/python3

import time
import multiprocessing as mp
import picamera
import tifffile
import imageio as iio
import numpy as np
import cv2
import datetime as dt
import logging
import collections
from ProcessedPiRecorder.Latency import Latency


# Class of raspberrypi video recorder based on Picamera and multiprocessing.
# Outputs into a big tiff appropriate for downstream use in Deep Lab Cut or other whatever.
# Supports the stereopi.


#OK, meat and potatoes time
class ProcessedPiRecorder:
    #initialize 
    def __init__(self,
                 tif_path=None, x_resolution=0, y_resolution=0, scale_factor=1, framerate=0, 
                 rec_length=0, display_proc='camera_reader', stereo=False,
                 timestamp=False, report_Hz=False, monitor_qs= False, Hz_buffer=10,
                 callback=None, blocking=True, 
                 tif_compression=6, 
                 aquisition_log=None, latency_log=None, cb_log=None):      
        
        #Set up logging
        self.latency_log = latency_log
        self.cb_log = cb_log
                     
        #Stereo or mono
        self.stereo = stereo
        
        #Camera sensor and downscaling
        if stereo: self.cam_width  = int((x_resolution+31)/32)*32 #must be factor of 32
        else:      self.cam_width  = int((x_resolution+15)/16)*16 #must be factor of 16
        self.cam_height            = int((y_resolution+15)/16)*16 #must be factor of 16
        
        self.img_width  = int(self.cam_width  * scale_factor)
        self.img_height = int(self.cam_height * scale_factor)
        self.tif_compression = tif_compression
        
        #Camera recording
        self.framerate  = framerate
        self.rec_length = rec_length
        self.video_path = tif_path
        self.timestamp  = timestamp
        self.reportHz   = report_Hz
        
        #init the numpy array
        self.capture = np.zeros((self.img_height, self.img_width, 4), dtype=np.uint8)

        #Callbacks
        self.display_proc  = display_proc
        self.blocking      = blocking
        self.callback      = callback
        self.monitor_qs    = monitor_qs
        self.Hz_buffer     = Hz_buffer
        
        

        
    #Reads in the video stream, timestamps, monitors framerate and passes frames
    def camera_reader(self, pass_frame, end_queue, queue, queue_list):        

        #Set up logging
        cam_logger = logging.getLogger('acquisition_logger')
        
        #set up the camera
        if self.stereo:
            camera = picamera.PiCamera(stereo_mode='side-by-side',stereo_decimate=False)
            camera.hflip = True
        else:
            camera = picamera.PiCamera()

        camera.resolution = (self.cam_width, self.cam_height)
        camera.framerate  = self.framerate
        time.sleep(0.1) #let camera warm up
        
        #Get the start time for latency and prep the counter variable
        t0 = dt.datetime.now()
        t1 = t0
        per=collections.deque(maxlen=self.Hz_buffer)
        counter=0
        if self.timestamp: camera.annotate_text = '0'

        #Read frames
        for frame in camera.capture_continuous(self.capture, format='bgra', use_video_port=True,
                                                    resize=(self.img_width, self.img_height)):
            #Track performance
            #Framerate
            t2=dt.datetime.now() 
            counter = counter + 1
            per.append((t2-t1).total_seconds())
            t1=t2
            Hz = 1/(sum(per)/len(per))
            elapsed = (t1-t0).total_seconds()

            #Queueing
            Q_depth=''
            for q in queue_list:
                Q_depth += '%s,' % (q.qsize())
            Q_depth = Q_depth[:-1] #trim a comma

            #Variable to accumulate logs across processes
            lat = Latency()
            lat.log('Queue_depths', Q_depth)
            lat.log('Camera_reader_in', t2)
            cam_logger.debug('t: %s__Qs: %s' % (t2, Q_depth,)) 

            #Annotate the frame/gather the dubugging data
            annot_str = ''
            if self.timestamp:  annot_str += 't: %.3fs, ' % elapsed
            if self.reportHz:   annot_str += 'FR: %.3f, ' % Hz
            if self.monitor_qs: annot_str += Q_depth   
            if self.timestamp or self.reportHz or self.monitor_qs:
                camera.annotate_text = annot_str
                camera.annotate_background = picamera.Color('black')
         
            #Check if we're displaying video
            if self.display_proc == 'camera_reader':
                cv2.imshow('camera_reader_display', frame)
                key = cv2.waitKey(1) & 0xFF
                lat.log('Camera_reader_display')

            #Break if time runs our or stop has been given
            if (elapsed > self.rec_length) or (not end_queue.empty()):
                if pass_frame: queue.put((True, frame, lat))
                lat.log('Camera_reader_out')
                
                cam_logger.info('Average Framerate: %.3f Hz' % (counter/elapsed,))
                if abs(counter/elapsed/self.framerate-1) >0.05: cam_logger.warning('Camera ONLY averaged %.3f Hz' % (counter/elapsed,))
                break

            else:
                #write the frame to the queue
                if pass_frame: queue.put((False, frame, lat))
                lat.log('Camera_reader_out')
    

    #Write the buffer to file
    def file_writer(self, queue, vid_path):

        #Setup logging
        fw_logger = logging.getLogger('latency_logger')
        if self.latency_log != None:
            fw_logger.setLevel('DEBUG')
            fw_logger.addHandler(logging.FileHandler(self.latency_log, 'w')) #needs to ouput to here       


        #define our tiff writer
        with iio.get_writer(vid_path, bigtiff=True, software='ProcessedPiRecorder') as tif:

            #infinite loop
            while True:
                #Grab the next entry in the queue
                if not queue.empty():
                    end, frame, lat = queue.get()
                    lat.log('File_writer_in')

                    #Check if we're displaying video
                    if self.display_proc == 'file_writer' and frame is not None:
                       cv2.imshow('file_writer_display', frame)
                       key = cv2.waitKey(1) & 0xFF
                       lat.log('File_writer_display')
                            
                    #save to tif
                    if frame is not None:
                        tif.append_data(frame)
                        lat.log('File_writer_saved')

                    #Write the log
                    fw_logger.debug(lat)

                    #Catch the break condition
                    if end is True: break
    
    def proc_callback(self, queue1, queue2, cb_queue):
        #Set up a logger
        cb_logger = logging.getLogger('callback_logger')
        if self.cb_log != None:
            cb_logger.setLevel('DEBUG')
            cb_logger.addHandler(logging.FileHandler(self.cb_log, 'w')) #needs to ouput to here       

        #Run provided callback
        self.callback(queue1, queue2, cb_queue, cb_logger)
                
    #Starts the recorder            
    def recordVid(self):
        #setup the queues and args
        #queues
        self.end_queue = mp.Queue()
        queue1         = mp.Queue()
        queue2         = mp.Queue()
        self.cb_queue  = mp.Queue()

        if self.callback != None or self.video_path != None: pass_frame = True
        else: pass_frame = False
            
        #args
        args1 = (pass_frame, self.end_queue, queue1, [queue1, queue2, self.cb_queue],)

        #if no callback, bypass it by routing queue1 into the file_writer
        if self.callback != None: args2 = (queue2, self.video_path,)
        else: args2 = (queue1, self.video_path,)

        args3 = (queue1, queue2, self.cb_queue,)
      
        #Run it
        try:
            #Init
            p1 = mp.Process(target=self.camera_reader, args=args1)
            if self.video_path != None: p2 = mp.Process(target=self.file_writer,   args=args2)
            if self.callback != None:   p3 = mp.Process(target=self.proc_callback, args=args3)

            #Start
            p1.start()
            if self.video_path != None: p2.start()
            if self.callback != None:   p3.start()

            #Blocking?
            if self.blocking:
                p1.join()
                if self.video_path != None: p2.join()
                if self.callback != None:   p3.join()

        #handle exceptions    
        except Exception as e:
            logging.error(e)

    #Stop the recorder prematurely
    def stopVid(self):
        self.end_queue.put(['This does nothing'])
        
