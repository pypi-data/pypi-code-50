#---------Imports
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sqlalchemy import create_engine
import pandas
import time
#---------End of imports

UPDATE_RATE = 1000

class TrafficLights(tk.Frame):

    def __init__(self, master):

        tk.Frame.__init__(self, master)
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().pack()
        self.initial_window()
        #ax1 = fig.add_subplot(111)
        self.updater_window()

    def initial_window(self):

        sqlEngine       = create_engine('mysql+pymysql://colin:colin@127.0.0.1/colin', pool_recycle=3600)
        dbConnection    = sqlEngine.connect()
        df1             = pandas.read_sql("select downloadspeed from colin.downloadtest", dbConnection);
        pandas.set_option('display.expand_frame_repr', False)
        print(df1)
        dbConnection.close()
        fig = plt.Figure(figsize=(5,5), dpi=100)
        ax1 = fig.add_subplot(111)
        bar1 = FigureCanvasTkAgg(fig, root)
        bar1.get_tk_widget().pack()
        ax1.plot(df1)


    def update_window(self):


        sqlEngine       = create_engine('mysql+pymysql://colin:colin@127.0.0.1/colin', pool_recycle=3600)
        dbConnection    = sqlEngine.connect()
        line             = pandas.read_sql("select uploadspeed from colin.downloadtest", dbConnection);
        pandas.set_option('display.expand_frame_repr', False)

        ax1.plot(line)


    def updater_window(self):
        self.update_window()
        self.after(UPDATE_RATE, self.updater_window)

fig = plt.Figure()
root = tk.Tk()
app = TrafficLights(root)
tk.mainloop()
