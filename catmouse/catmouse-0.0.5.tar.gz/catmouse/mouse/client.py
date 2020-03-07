import pynput.mouse as mouse
from time import time,sleep
from requests import post
from json import dumps
from sys import getsizeof

REMOTE_API=f'https://mouse.iotabet.pw/add'
LOCAL_API=f'http://localhost:3663/add'

# Possible states
MOUSE_MOVE     = int('0b00000001',2)
MOUSE_CLICK    = int('0b00000010',2)
MOUSE_RIGHT    = int('0b00000100',2)
MOUSE_LEFT     = int('0b00001000',2)
MOUSE_PRESSED  = int('0b00010000',2)
MOUSE_RELEASED = int('0b00100000',2)

class Recorder(mouse.Listener):
    def __init__(self):
        super(Recorder,self).__init__(
            on_click = self.on_click,
            on_move  = self.on_move,
        )
        self.data=[]


    # Store mouse datum
    def log(self,t,x,y,state):
        self.data.append((t,x,y,state))

    # Send dataset to server
    def emit(self):
        if len(self.data) == 0: return
        data=self.data
        self.data=[]
        s=time()
        print('Sending data to server...')
        payload=data
        post(REMOTE_API,data={'events': dumps(payload)})
        duration = time()-s
        payloadSize = getsizeof(data)
        rate = payloadSize/duration/1024 #kB/s
        print(f'Sent {payloadSize} bytes in {duration:.02f}sec for a rate of {rate:.02f} kB/s.')
        

        
    def on_move(self,x,y):
        self.log(time(),x,y,MOUSE_MOVE)
        
    def on_click(self,x,y,button,pressed):
        state=MOUSE_CLICK
        if button == mouse.Button.left:
            state |= MOUSE_LEFT
        elif button == mouse.Button.right:
            state |= MOUSE_RIGHT
        if pressed:
            state |= MOUSE_PRESSED
        else:
            state |= MOUSE_RELEASED
        self.log(time(),x,y,state)
def run():
    m=Recorder() 
    m.start() # Start mouse recording
    try:
        while True:
            # Sending data to server every second.
            sleep(1)
            m.emit()
    except Exception as e:
        print(e)

    
if __name__=='__main__':
    run()
