#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# the spider walks following command from PC(ble direct connection) or internet(mqtt remote control)

from m2controller import m2controller
from m2controller import m2Const
from m2controller import constShared
import time
from pynput import keyboard
import usrCfg
import signal

requestExit = False
def signal_handler(sig, frame):
    global requestExit
    print('user Ctrl-C exit request')
    quit()
    
signal.signal(signal.SIGINT, signal_handler)

controller = m2controller.BleCtrller(m2Const.etLocalNet,None,None,None,0,usrCfg.IntranetHostIPaddr)
controller.connect()
       
def stopEverything():
    controller.motorHbridgeCtrl_pm1(m2Const.spiderPWMchSpeed,0.0)
    controller.motorHbridgeCtrl_pm1(m2Const.spiderPWMchSteer,0.0)
    controller.SendCmdTransBlking(False,True)
    
def on_press(key):
    global requestExit
    #print('%s key pressed'%key)
    if key == keyboard.Key.left:
        controller.motorHbridgeCtrl_pm1(m2Const.spiderPWMchSteer,-1.0)
    elif key == keyboard.Key.right:
        controller.motorHbridgeCtrl_pm1(m2Const.spiderPWMchSteer,1.0)
        
    if key == keyboard.Key.up:
        controller.motorHbridgeCtrl_pm1(m2Const.spiderPWMchSpeed,-1.0)
    elif key == keyboard.Key.down:
        controller.motorHbridgeCtrl_pm1(m2Const.spiderPWMchSpeed,1.0)
    
    emotionID = -1
    if key == keyboard.KeyCode(char='a'):
        emotionID = constShared.emoPic_angry
    elif key == keyboard.KeyCode(char='c'):
        emotionID = constShared.emoPic_cry
    elif key == keyboard.KeyCode(char='d'):
        emotionID = constShared.emoPic_disappoint
    elif key == keyboard.KeyCode(char='h'):
        emotionID = constShared.emoPic_happy
    elif key == keyboard.KeyCode(char='k'):
        emotionID = constShared.emoPic_kiss
    elif key == keyboard.KeyCode(char='s'):
        emotionID = constShared.emoPic_surprise
    controller.set_wallpaper(emotionID)
    controller.playMP3withID(emotionID)
        
    if key == keyboard.Key.esc:
        listener.stop()
        quit()
        
    # TODO: add key combination later    
    controller.SendCmdTransBlking(False,False)

def on_release(key):
    if key == keyboard.Key.left or key == keyboard.Key.right:
        controller.motorHbridgeCtrl_pm1(m2Const.spiderPWMchSteer,0.0)
    if key == keyboard.Key.up or key == keyboard.Key.down:
        controller.motorHbridgeCtrl_pm1(m2Const.spiderPWMchSpeed,0.0)  
    controller.SendCmdTransBlking(False,True)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    while not requestExit:
        time.sleep(0.01)

        
        

