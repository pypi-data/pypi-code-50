# -*- coding:utf-8 -*-
import sys
def print_lol(the_list, indent=False, level=0, fn = sys.stdout):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item, indent, level + 1, fn)
        else:
            if indent:
                print("t" * level, end='', file=fn)
            print(each_item, file=fn)




def print_yoy(the_list,fn = sys.stdout):
    for each_item in the_list:
        print(each_item,fn)
