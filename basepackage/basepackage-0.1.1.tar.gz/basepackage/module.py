"""
Lucifer Monao, copyright 2020.1.29, for more infos see README.md

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

See LICENCE.txt for more information
"""

from tkinter import messagebox
import colorama as c
import sys
import math
import psutil
import platform
from datetime import datetime
from string import *
import random

#PRINT

def pa(arg1, arg2):

    #prepare deleting of lines
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'

    f = open("data.txt", "w")

    #def delete line function for easier use
    def deleteline():
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)

    #search for f
    if ("f" in arg1) == True:
        #po s= position
        pos = arg1.find("f")
        #poscc = positioncharactercolor
        poscc = arg1[pos + 1]
        if poscc == "k":
            print(c.Fore.BLACK)
        elif poscc == "g":
            print(c.Fore.GREEN)
        elif poscc == "y":
            print(c.Fore.YELLOW)
        elif poscc == "r":
            print(c.Fore.RED)
        elif poscc == "m":
            print(c.Fore.MAGENTA)
        elif poscc == "l":
            print(c.Fore.BLUE)
        elif poscc == "c":
            print(c.Fore.CYAN)
        elif poscc == "w":
            print(c.Fore.WHITE)
        deleteline()

    if ("b" in arg1) == True:
        #pos = position
        pos = arg1.find("b")
        #poscc = positioncharactercolor
        poscc = arg1[pos + 1]
        if poscc == "k":
            print(c.Back.BLACK)
        elif poscc == "g":
            print(c.Back.GREEN)
        elif poscc == "y":
            print(c.Back.YELLOW)
        elif poscc == "r":
            print(c.Back.RED)
        elif poscc == "m":
            print(c.Back.MAGENTA)
        elif poscc == "l":
            print(c.Back.BLUE)
        elif poscc == "c":
            print(c.Back.CYAN)
        elif poscc == "w":
            print(c.Back.WHITE)
        deleteline()
    
    if ("s" in arg1) == True:
        #pos = position
        pos = arg1.find("s")
        #poscs = positioncharacterstyle
        poscs = arg1[pos + 1]
        if poscs == "d":
            print(c.Style.DIM)
        elif arg1 == "n":
            print(c.Style.NORMAL)
        elif arg1 == "h":
            print(c.Style.BRIGHT)
        deleteline()
        
    print(arg2)
    if (("clear" in arg1) == True) or (("reset" in arg1) == True) or (("c" in arg1) == True) or (("r" in arg1) == True):
        print(c.Style.RESET_ALL)
        print("RESET")
        deleteline()
        f.write("")
    else:
        f.write(arg1)

def p(arg1):

    #prepare deleting of lines
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'

    #def delete line function for easier use
    def deleteline():
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)
    
    f = open("data.txt", "r")

    filetext = str(f.read())
    print(filetext)

    if len(filetext) > 0:

        if ("f" in filetext) == True:
            #po s= position
            pos = filetext.find("f")
            #poscc = positioncharactercolor
            poscc = filetext[pos + 1]
            if poscc == "k":
                print(c.Fore.BLACK)
            elif poscc == "g":
                print(c.Fore.GREEN)
            elif poscc == "y":
                print(c.Fore.YELLOW)
            elif poscc == "r":
                print(c.Fore.RED)
            elif poscc == "m":
                print(c.Fore.MAGENTA)
            elif poscc == "l":
                print(c.Fore.BLUE)
            elif poscc == "c":
                print(c.Fore.CYAN)
            elif poscc == "w":
                print(c.Fore.WHITE)
            deleteline()

        if ("b" in filetext) == True:
            #pos = position
            pos = filetext.find("b")
            #poscc = positioncharactercolor
            poscc = filetext[pos + 1]
            if poscc == "k":
                print(c.Back.BLACK)
            elif poscc == "g":
                print(c.Back.GREEN)
            elif poscc == "y":
                print(c.Back.YELLOW)
            elif poscc == "r":
                print(c.Back.RED)
            elif poscc == "m":
                print(c.Back.MAGENTA)
            elif poscc == "l":
                print(c.Back.BLUE)
            elif poscc == "c":
                print(c.Back.CYAN)
            elif poscc == "w":
                print(c.Back.WHITE)
            deleteline()
        
        if ("s" in filetext) == True:
            #pos = position
            pos = filetext.find("s")
            #poscs = positioncharacterstyle
            poscs = filetext[pos + 1]
            if poscs == "d":
                print(c.Style.DIM)
            elif arg1 == "n":
                print(c.Style.NORMAL)
            elif arg1 == "h":
                print(c.Style.BRIGHT)
            deleteline()


        if ("---" in arg1) == True:
            pos = arg1.find("---")
            #deleteline()
            text = arg1[(pos + 3):]
            print(text, c.Style.RESET_ALL)
            print("Spaceline------Spaceline------Spaceline")
            print("Spaceline------Spaceline------Spaceline")
            deleteline()
            deleteline()
            f = open("data.txt", "w")
            f.write("")
        else:
            print(arg1)
    else:
        deleteline()
        print(arg1)


# INFO

def info(name, text):
    messagebox.showinfo(name, text)

def error(name, text):
    messagebox.showinfo(name, text)

def help(name, text):
    messagebox.showinfo(name, text)

def askokcancel(name, text):
    answer = messagebox.askokcancel(name, text)
    return(answer)

def askyesno(name, text):
    answer = messagebox.askyesno(name, text)
    return(answer)

def askyesnocancel(name, text):
    answer = messagebox.askyesnocancel(name, text)
    return(answer)

def askretrycancel(name, text):
    answer = messagebox.askretrycancel(name, text)
    return(answer)

def askquestion(name, text):
    answer = messagebox.askquestion(name, text)
    return(answer)


#COMPUTERINFO

#general system info
def geninf():
    uname = platform.uname()
    sys = uname.system
    node = uname.node
    release = uname.release
    version = uname.version
    machine = uname.machine
    processor = uname.processor
    return(sys, node, release, version, machine, processor)

#boot time
def bt():
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    return(bt.year, bt.month, bt.day, bt.hour, bt.minute, bt.second)

#CPU
# number of cores
def cpucores():
    pcores =  psutil.cpu_count(logical=False)
    lcores = psutil.cpu_count(logical=True)
    return(pcores, lcores)

# CPU frequencies
def cpufreq():
    cpufreq = psutil.cpu_freq()
    maxfreq = cpufreq.max
    minfreq = cpufreq.min
    curfreq = cpufreq.current
    return(maxfreq, minfreq, curfreq)

# CPU usage
def cpuusage():
    cpuusge = psutil.cpu_percent()
    return(cpuusge)

# Memory Information
# get the memory details
def memory():
    svmem = psutil.virtual_memory()
    totmem = svmem.total
    avamem = svmem.available
    usdmem = svmem.used
    return(totmem,avamem,usdmem)

# get the swap memory details (if exists)
def swap():
    swap = psutil.swap_memory()
    totswap = swap.total
    avaswap = swap.free
    usdswap = swap.used
    return(totswap,avaswap,usdswap)

#PRIMENUMBER

def ptest(num):
    a = [0]
    end = int(num)
    for x in range(2, end):
        end = int(num) / x
        if int(num) % x == 0:
                return("n")
                break
    else:
    # loop fell through without finding a factor
            return("p")

def rstring(lenght):
    letters = ascii_letters + digits + punctuation
    return(''.join(random.choice(letters) for i in range(lenght)))