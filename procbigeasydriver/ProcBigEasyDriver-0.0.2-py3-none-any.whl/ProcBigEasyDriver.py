#!/usr/bin/env/ python3

import gpiozero
from time import sleep
import datetime as dt
import multiprocessing as mp
import logging

class buffer:
        def __init__(self, max_len=1):
            self.buffer=list()
            self.max_len = max_len

        def append(self, data):
            self.buffer.append(data)
            if len(self.buffer) > self.max_len:
                del self.buffer[:-self.max_len]

class ProcBigEasyDriver:
    def __init__(self, step, direction, ms1, ms2, ms3, enable,
                 microstepping=1, rpm=1, steps_per_rev=200,
                 Kp=0.2, Ki=0.1):
        
        #Assign GPIO for the big easy driver
        self.dir    = gpiozero.LED(direction)
        self.ms1    = gpiozero.LED(ms1)
        self.ms2    = gpiozero.LED(ms2)
        self.ms3    = gpiozero.LED(ms3)
        self.en     = gpiozero.LED(enable)

        #assign the queue
        self.queue = mp.Queue()

        #Set motor speed
        self.rpm = rpm
        self.spr = steps_per_rev
        self.Kp  = Kp
        self.Ki  = Ki
        self.microstepping = microstepping

        #Set initial pin conditions
        self.set_microstep(self.microstepping)
        self.en.on()

        #Start the motor in the next process
        args = (step, self.queue, self.rpm, self.microstepping, self.spr, self.Kp, self.Ki,)

        try:
            p1 = mp.Process(target=self.turn, args=args)
            p1.start()

        except Exception as e:
                logging.error(e)

    def take_step(self, step, duration):
        step.off()
        sleep(0.000001)
        step.on()
        sleep(duration-0.000001)

    def turn(self, step, queue, rpm, microstepping, spr, Kp, Ki):
        #Init the drive pin
        step = gpiozero.LED(step)

        #Init a buffer
        dur_buffer = buffer(20)
        err_buffer = buffer(200)

        #initial calculation of step period
        per = (rpm/60 * spr * microstepping) ** (-1)
        dur = per
        dur_buffer.append(dur)
                
        t1=dt.datetime.now()
        while True:
            #Check the queue
            if not queue.empty():
                rpm, microstepping = queue.get()

                if rpm == 'end': break
                #calculate the period
                per = (rpm/60 * spr * microstepping) ** (-1)
                
            #turn a step
            self.take_step(step,dur)

            #Measure error
            t2 = dt.datetime.now()
            t_delt = (t2-t1).total_seconds()
            err =100*(per-t_delt)/per
            err_buffer.append(err)
            logging.info('  |  avg_per_err: %6.5f  |  ' % (sum(err_buffer.buffer)/len(err_buffer.buffer),))

            #Do some logging
            if abs(err) > 20: logging.warning('| perc_err: %10.9f  |' % err)
            logging.debug('  |  rpm: %s  |  mstep: %s  |  t: %s  |  dur: %6.5f  |  dt: %6.5f  |  period:  %6.5f  |  perc_err:  %6.5f  |  ' % (rpm, microstepping, t2, dur, t_delt, per, err,))

           

            #Controller?! I hardly know her!
            p = per - t_delt #proportional error
            i = sum(dur_buffer.buffer)/len(dur_buffer.buffer) - dur #integral error
            dur = dur + Kp*p + Ki*i 
            if dur < 0.000001: dur = 0.000001
            dur_buffer.append(dur)

            #Reset the time variable
            t1 = t2

    def set_rpm(self,rpm):
        self.rpm=rpm
        self.queue.put([self.rpm, self.microstepping])

    def set_microstep(self, microstep):
        #Update the ms pins
        if microstep == 16:
            self.microstepping = 16
            self.ms1.on()
            self.ms2.on()
            self.ms3.on()

        elif microstep == 8:
            self.microstepping = 8
            self.ms1.on()
            self.ms2.on()
            self.ms3.off()
            
        elif microstep == 4:
            self.microstepping = 4
            self.ms1.off()
            self.ms2.on()
            self.ms3.off()
            
        elif microstep == 2:
            self.microstepping = 2
            self.ms1.on()
            self.ms2.off()
            self.ms3.off()
            
        elif microstep == 1:
            self.microstepping = 1
            self.ms1.off()
            self.ms2.off()
            self.ms3.off()

        else: logging.error('Invalid Microstep: %s' % microstep)

        #Update the motor
        self.queue.put([self.rpm, self.microstepping])

    def enable(self):
        self.en.off()
        
    def disable(self):
        self.en.on()

    def stop(self):
        self.queue.put(['end', 'end'])

        #release the pins
        self.dir.close()
        self.ms1.close()
        self.ms2.close()
        self.ms3.close()
        self.en.close()

if __name__ =='__main__':

    #Logger
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)
   

    Stepper = ProcBigEasyDriver(step=21, direction=20, ms1=19, ms2=18, ms3=17, enable=16,
                 microstepping=1, rpm=20, steps_per_rev=200)

    Stepper.enable()
    sleep(20)
    Stepper.disable() 
    Stepper.stop()
    

        
