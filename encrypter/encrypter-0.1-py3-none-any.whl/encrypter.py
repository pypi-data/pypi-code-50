import random
import sys

def create_code():
    while True:
        try:
            code = random.randint(random.randint(0, 100), random.randint(0, 100))
            if code != None:
                return code
        except:
            continue

def encrypt(message):
    code = create_code()

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
    return (message, code)

def decrypt(info):
    message, code = info
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

