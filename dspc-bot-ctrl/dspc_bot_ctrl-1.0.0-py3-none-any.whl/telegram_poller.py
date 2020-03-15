from telegram.ext import *
import logging
import os
import threading
import ctypes
import telegram
from telegram.error import *
import requests
import json

from dspc_bot_ctrl.bot_functions import BotFunctions


lformat = '[*] %(asctime)s ::: %(levelname)s - %(message)s'
logging.basicConfig(format=lformat)

logger = logging.getLogger("pccbot_log")
logger.setLevel(logging.DEBUG)


class TelegramPoller(threading.Thread):
        def __init__(self,tmp_ROOT,chat_id,telegram_token):
                self.chat_id = chat_id
                self.tmp_ROOT = tmp_ROOT
                threading.Thread.__init__(self)
                self.updater = Updater(token=telegram_token,use_context = True)
                self.dispatcher = self.updater.dispatcher
                if os.path.exists(self.tmp_ROOT) == False:
                    os.mkdir(self.tmp_ROOT)
                
        def run(self):
                self.dispatcher.add_handler(MessageHandler(Filters.text, self.echo))
                self.dispatcher.add_handler(CommandHandler('start', self.bot_start))
                self.dispatcher.add_error_handler(self.error_callback)
                logger.info("Started Polling Phase")
                # job_queue = self.updater.job_queue
                self.updater.start_polling()

        def bot_start(self,update, context):
                logger.info("Bot started")
                context.bot.send_message(chat_id=update.effective_chat.id, text="Control Bot for PC, type commands to see list of available commands..")
                commands_list(update,context)

        def echo(self,update, context):
                msg = update.message.text.lower()
                if "identify_me" not in msg and "identity_me" not in msg:
                    logger.info("Received message - '{}'".format(update.message.text))
                bf = BotFunctions(update,context,self.tmp_ROOT,self.chat_id)
                ran = False
                if msg.strip() == "start" or msg.strip() == "/start":
                    ran = True
                    self.bot_start(update,context)
                if "shutdownsys" in msg:
                        ran = True
                        bf.sys_sd()
                if ("shutdownbot" in msg) or ("killbot" in msg):
                        ran = True
                        bf.bot_sd()
                if "screenssys" in msg:
                        ran = True
                        bf.sys_ss()
                if "runcmd" in msg.split():
                        ran = True
                        bf.os_cmd_run(msg.replace("runcmd ",""))
                if "runcmdop" in msg.split():
                        ran = True
                        bf.os_cmd_getop(msg.replace("runcmdop ",""))
                if "clearcmd" in msg.split():
                        ran = True
                        bf.clear_os_cmd()
                if "commands" in msg.split():
                    ran = True
                    bf.commands_list()
                if "showprocesses" in msg.split():
                    ran = True
                    bf.task_list()
                if "switchto" in msg.split():
                    ran = True
                    bf.change_window(update.message.text.replace("switchto ",""))
                if "switchtoin" in msg.split():
                    ran = True
                    bf.change_window_within(update.message.text.replace("switchtoin ",""))
                if "wintitles" in msg.split():
                    ran = True
                    bf.get_window_titles()
                if "startssstream" in msg:
                    ran = True
                    bf.start_streaming()
                if "stopssstream" in msg:
                    ran = True
                    bf.stop_streaming()
                if "sendkeys" in msg.split():
                    ran = True
                    bf.send_keys(update.message.text.replace("sendkeys ",""))
                if "sendhotkeys" in msg.split():
                    ran = True
                    bf.send_hot_keys(update.message.text.replace("sendhotkeys ","").lower())
                if "sendkeynames" in msg.split():
                    ran = True
                    bf.send_key_names()
                if ran == False and "identify_me" not in msg and "identity_me" not in msg:
                    context.bot.send_message(chat_id=self.chat_id,text="Command not recognized. Type 'commands' to see a list of valid commands.")

        def error_callback(self, update, context):
                try:
                    raise context.error
                except Exception as e:
                    logger.error("TELEGRAM_ERROR - "+str(e))