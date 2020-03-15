import os

from dspc_bot_ctrl.user_identifier import UserIdentifier

class DSPCBOT():
    should_config = True
    possible_tmp_fol = ["C://dspcc-bot-controller-cfg/"]
    tmp_ROOT = ""
    telegram_token = ""
    password = ""
    def init(self):
        self.init_block()
        self.config_state()
        UserIdentifier(self.tmp_ROOT,self.telegram_token,self.password).identify()


    def init_block(self):
        version = "1.0.0"
        init_art = """       
               __                           __          __ 
          ____/ /________  __________      / /_  ____  / /_
         / __  / ___/ __ \\/ ___/ ___/_____/ __ \\/ __ \\/ __/
        / /_/ (__  ) /_/ / /__/ /__/_____/ /_/ / /_/ / /_  
        \\__,_/____/ .___/\\___/\\___/     /_.___/\\____/\\__/
                 /  /
                /_ /                                       
                """


        init_creator = "dspcc-bot-controller v"+version+"  -  Created by Rojit George"

        init_note = """
        Note : This is a controller for the telegram bot that you will create
        specifically for controlling your pc, therefore the Telegram android
        app is needed. To create the bot that will serve you in telegram,
        contact @Botfather and type '/newbot'. Follow instructions and note the
        HTTP API token thatBotfather provides.

        To revoke previous telegram bot HTTP API token, type 'revoke' in password input stage.
        """

        init_text_block = [init_art,init_creator,init_note]

        print(("*"*30))
        print(("="*30))
        for i in init_text_block:
            print(i)
            print(("="*30))


        print(("*"*30)+"\n")

    def config_state(self):
        for p in self.possible_tmp_fol:
            if os.path.exists(p) == False:
                os.mkdir(p)
                self.tmp_ROOT = p
            else:
                self.tmp_ROOT = p
                break


        

        if os.path.exists(self.tmp_ROOT+"config.txt") == True:
            self.telegram_token = open(self.tmp_ROOT+"config.txt","r").read().splitlines()[0]
            self.should_config = False


        if self.should_config == True:
            self.telegram_token = input("Enter bot HTTPS API token (will be saved) : ")
            f = open(self.tmp_ROOT+"config.txt","w+")
            f.write(self.telegram_token)
            f.close()
            print("To revoke inputed token in the future, type 'revoke' in password input stage.")
        self.password = input("Enter a password for security identification : ")

        if self.password == "revoke":
            if os.path.exists(self.tmp_ROOT+"config.txt"):
                os.remove(self.tmp_ROOT+"config.txt")
            self.should_config = True
            self.config_state()