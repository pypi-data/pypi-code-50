import logging
import threading
import pyautogui
import time
import ctypes



lformat = '[*] %(asctime)s ::: %(levelname)s - %(message)s'
logging.basicConfig(format=lformat)

logger = logging.getLogger("pccbot_log")
logger.setLevel(logging.DEBUG)


class SSStream(threading.Thread):
    def __init__(self,chat_id):
        threading.Thread.__init__(self)
        self.mcontext = None
        self.mupdate = None
        self.chat_id = chat_id
        self.is_streaming = False;


    def set_c_u(self,context,update):
        self.mcontext = context
        self.mupdate = update


    def run(self):
        self.is_streaming = True
        while True:
            ss = pyautogui.screenshot()
            ss_path = tmp_ROOT+"tmp_s_ss.png"
            ss.save(ss_path)
            self.mcontext.bot.send_photo(chat_id=self.chat_id,photo=open(ss_path,"rb"))
            time.sleep(3)

    def get_id(self):
        if hasattr(self,'_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def stop_stream(self):
        self.is_streaming = False
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,0)