from telegram.ext import *
import logging
import os
import pyautogui
import subprocess
import time
import win32gui, win32com.client
from telegram.error import *

from dspc_bot_ctrl.window_manager import WindowMgr
from dspc_bot_ctrl.ss_stream import SSStream


lformat = '[*] %(asctime)s ::: %(levelname)s - %(message)s'
logging.basicConfig(format=lformat)

logger = logging.getLogger("pccbot_log")
logger.setLevel(logging.DEBUG)


class BotFunctions:
    cmds_list = {"shutdownsys":"Shut down system","killbot":"Kills bot","screenssys":"Takes a screenshot of the system",
                        "runcmd <command>":"runs command in CMD and send the screenshot of the output","runcmdop":"runs command in CMD and sends text stream as output",
                        "clearcmd":"Clear cmd context and start anew.","showprocesses":"Sends list of running processes","wintitles":"Sends window titles of running programs(for use in switch)",
                        "switchto <exact window_title":"Finds window title and sets it as active window.","switchtoin <word in title>":"Finds window title containing input and sets it as active window",
                        "startssstream":"Starts a screenshot stream with delay of 3 secs","stopssstream":"Stops screenshot stream started with startssstream","sendkeys":"Types sentence in Controlled PC",
                        "sendhotkeys":"Types hot keys in Controlled PC. For combinations, use + as delimiter. For sequences, use spaces.","sendkeynames":"Sends valid key names."}

    def __init__(self,update,context,tmp_ROOT,chat_id):
            self.update = update
            self.context = context
            self.chat_id = chat_id
            self.ss_stream = SSStream(self.chat_id)
            self.tmp_ROOT = tmp_ROOT

    #system shudown
    def sys_sd(self):
            logger.info("System shutdown initiated")
            self.context.bot.send_message(chat_id=self.chat_id,text="Shutting down server....")
            os.system('shutdown -s')
    #bot shutdown
    def bot_sd(self):
            logger.info("Killing bot and polling program.")
            self.context.bot.send_message(chat_id=self.chat_id,text="Shutting down bot....")
            os._exit(1)

    #system screenshot
    def sys_ss(self):
            logger.info("Screenshot Capture request being fulfilled")
            ss = pyautogui.screenshot()
            ss_path = self.tmp_ROOT+"tmp_ss.png"
            ss.save(ss_path)
            self.context.bot.send_photo(chat_id=self.chat_id,photo=open(ss_path,"rb"))
            logger.info("Screenshot Capture request fulfilled")

    #running cmd commands
    def os_cmd_run(self,command):
            logger.info("Running command '{}' in CMD Prompt".format(command))
            bat_file = open(self.tmp_ROOT+"cmdrunner.bat","a+")
            bat_file.write(command+"\n")
            bat_file.close()
            subprocess.call([self.tmp_ROOT+"cmdrunner.bat"])
            logger.info("Command '{}' executed in CMD Prompt".format(command))
            self.context.bot.send_message(chat_id=self.chat_id,text="Will take SS of output in 5 seconds...")
            for i in range(5,0,-1):
                self.context.bot.send_message(chat_id=self.chat_id,text=str(i))
                time.sleep(1)
            self.sys_ss()

    def os_cmd_getop(self,command):
            logger.info("Running command '{}' via pipeline in CMD".format(command))
            bat_file = open(self.tmp_ROOT+"cmdrunner.bat","a+")
            bat_file.write(command+"\n")
            bat_file.close()
            output= subprocess.Popen((self.tmp_ROOT+"cmdrunner.bat"),stdout=subprocess.PIPE).stdout
            op = ""
            for line in output:
                if line.decode('utf-8').strip() != "":
                    self.context.bot.send_message(chat_id=self.chat_id,text=line.decode('utf-8')+" ")
            logger.info("Command '{}' executed via pipeline".format(command))

    def clear_os_cmd(self):
            bat_file = open(self.tmp_ROOT+"cmdrunner.bat","w")
            bat_file.write("")
            bat_file.close()
            self.context.bot.send_message(chat_id=self.chat_id,text="Cleared CMD context..")
            logger.info("CMD Context cleared")

    #task_list
    def task_list(self):
            logger.info("Sending running process list")
            output= subprocess.Popen(("wmic process get description,executablepath"),stdout=subprocess.PIPE).stdout
            op = ""
            for line in output:
                if line.decode('utf-8').strip() != "":
                    self.context.bot.send_message(chat_id=self.chat_id,text=line.decode('utf-8')+" ")
            logger.info("Process list sent")


    def winEnumHandler(self, hwnd, ctx ):
            if win32gui.IsWindowVisible( hwnd ):
                if win32gui.GetWindowText( hwnd ) != "":
                    self.context.bot.send_message(chat_id=self.chat_id,text=win32gui.GetWindowText( hwnd ))

    def get_window_titles(self):
        logger.info("Providing running window titles")
        mupdate = self.update
        mcontext = self.context
        win32gui.EnumWindows( self.winEnumHandler, None )
        

    def change_window(self,title):
            logger.info("Received request for window change with input as '{}' for exact wildcard".format(title))
            try:
                w = WindowMgr(0)
                w.find_window_wildcard(title)
                w.set_foreground()
                self.context.bot.send_message(chat_id=self.chat_id,text="Activated provided window. Will take SS in 5 seconds.")
                for i in range(5,0,-1):
                    self.context.bot.send_message(chat_id=self.chat_id,text=str(i))
                    time.sleep(1)
                self.sys_ss()
            except Exception as e:
                logger.error(str(e))
                self.context.bot.send_message(chat_id=self.chat_id,text="Can't find window handler.")

    def change_window_within(self,title):
            logger.info("Received request for window change with input as '{}' for 'within' wildcard".format(title))
            try:
                w = WindowMgr(1)
                w.find_window_wildcard(title)
                w.set_foreground()
                self.context.bot.send_message(chat_id=self.chat_id,text="Activated provided window. Will take SS in 5 seconds.")
                for i in range(5,0,-1):
                    self.context.bot.send_message(chat_id=self.chat_id,text=str(i))
                    time.sleep(1)
                self.sys_ss()
            except Exception as e:
                logger.error(str(e))
                self.context.bot.send_message(chat_id=self.chat_id,text="Can't find window handler.")
                pass

    def start_streaming(self):
        if ss_stream.is_streaming == False:
            logger.info("SS Stream request being fulfilled")
            self.context.bot.send_message(chat_id=self.chat_id,text="Starting SS Stream...")
            self.ss_stream.set_c_u(context,update)
            self.ss_stream.start()
            logger.info("SS Stream request fulfilled")
        else:
            logger.error("SS Stream request rejected.")
            self.context.bot.send_message(chat_id=self.chat_id,text="SS Stream is already piping...")


    def stop_streaming(self):
        if ss_stream.is_streaming == True:
            self.context.bot.send_message(chat_id=self.chat_id,text="Stopping SS Stream...")
            self.ss_stream.stop_stream()
            logger.info("SS Stream abort request fulfilled.")
        else:
            logger.error("SS Stream abort request rejected.")
            self.context.bot.send_message(chat_id=self.chat_id,text="No SS stream available to stop...")


    def send_keys(self,sentence):
        logger.info("Typing input '{}'".format(sentence))
        self.context.bot.send_message(chat_id=self.chat_id,text="Typing sentence....")
        pyautogui.write(sentence,interval=0.10)
        time.sleep(2)
        self.sys_ss()

    def send_key_names(self):
        logger.info("Providing valid keys list")
        self.context.bot.send_message(chat_id=self.chat_id,text=str(pyautogui.KEY_NAMES))

    def send_hot_keys(self,command_string):
        logger.info("Pressing hotkey input '{}'".format(command_string))
        if "+" in command_string:
            input_keys = command_string.split("+")
            valid = True
            for k in input_keys:
                if k not in pyautogui.KEY_NAMES:
                    valid=False
                    break
            if valid == False:
                logger.error("Hot key request failed")
                self.context.bot.send_message(chat_id=self.chat_id,text="Some keys inputed are not valid.Here is a list of valid keys.")
                self.send_key_names()
            else:
                for i in input_keys:
                    pyautogui.keyDown(i)
                for i in range(len(input_keys)-1,-1,-1):
                    pyautogui.keyUp(input_keys[i])
                self.context.bot.send_message(chat_id=self.chat_id,text="Will take SS in 5 seconds.")
                for i in range(5,0,-1):
                    self.context.bot.send_message(chat_id=self.chat_id,text=str(i))
                    time.sleep(1)
                self.sys_ss()
                logger.info("Hot key request fulfilled.")
        elif " " in command_string:
            input_keys = command_string.split(" ")
            valid = True
            for k in input_keys:
                if k not in pyautogui.KEY_NAMES:
                    valid=False
                    break
            if valid == False:
                logger.error("Hot key request failed")
                self.context.bot.send_message(chat_id=self.chat_id,text="Some keys inputed are not valid.Here is a list of valid keys.")
                self.send_key_names()
            else:
                for i in input_keys:
                    pyautogui.press(i)
                self.context.bot.send_message(chat_id=self.chat_id,text="Will take SS in 5 seconds.")
                for i in range(5,0,-1):
                    context.bot.send_message(chat_id=update.effective_chat.id,text=str(i))
                    time.sleep(1)
                self.sys_ss()
                logger.info("Hot key request fulfilled.")
        else:
            if command_string.strip() in pyautogui.KEY_NAMES:
                pyautogui.press(command_string)
                self.context.bot.send_message(chat_id=self.chat_id,text="Will take SS in 5 seconds.")
                for i in range(5,0,-1):
                    self.context.bot.send_message(chat_id=self.chat_id,text=str(i))
                    time.sleep(1)
                self.sys_ss()
                logger.info("Hot key request fulfilled.")
            else:
                logger.error("Hot key request failed")
                self.context.bot.send_message(chat_id=self.chat_id,text="Invalid command string.Here is a list of valid keys.")
                self.send_key_names()

    def commands_list(self):
            logger.info("Providing commands list")
            cop = ""
            for command in self.cmds_list:
                cop += "*"+command+"* - "
                cop += self.cmds_list[command]
                cop += "\n\n"


            self.context.bot.send_message(chat_id=self.chat_id, text=cop,parse_mode=telegram.ParseMode.MARKDOWN)