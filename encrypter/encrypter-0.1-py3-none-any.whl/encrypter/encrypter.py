import random
import sys

class Encrypter:
    def __init__(self):
        self.code = 0
        self.message = ""

    def create_code(self):
        while True:
            try:
                self.code = random.randint(random.randint(0, 100), random.randint(0, 100))
                if self.code != None:
                    return self.code
            except:
                continue

    def encrypt(self, message):
        code = self.create_code()
        self.code = code
        msg_str_list = []
        msg_int_list = []
        msg_symbol_list = []
        space_index_list = []

        for i in message:
            msg_str_list.append(i)
        for i in msg_str_list:
            msg_int_list.append(ord(i))
        for i in range(len(msg_int_list)):
            msg_int_list[i] *= code
        for i in msg_int_list:
            msg_symbol_list.append(chr(i))
            if i == 32*code:
                space_index_list.append(msg_int_list.index(i))
        for i in range(len(msg_symbol_list)):
            for i in space_index_list:
                msg_symbol_list[i] = " "
        
        message = "".join(msg_symbol_list)
        self.message = message
        return self.message

    def decrypt(self, info):
        message = self.message
        code = self.code
        msg_symbol_list = []
        msg_int_list = []
        msg_str_list = []
        space_index_list = []

        for i in message:
            msg_symbol_list.append(i)
        for i in msg_symbol_list:
            num = int(ord(i)/code)
            if num == 32:
                space_index_list.append(msg_symbol_list.index(i))
            msg_int_list.append(num)
        for i in msg_int_list:
            msg_str_list.append(chr(i))
        
        message = "".join(msg_str_list)
        
        return message