import matplotlib.pyplot as plt
import mysql.connector
import tkinter as tkinter
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def DrawUpDown (tkinter.Frame):

    mydb = mysql.connector.connect(
            host="localhost",
            user="colin",
            passwd="colin",
            database="colin")

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM downloadtest")

    myresult = mycursor.fetchall()

    t = []
    s = []

    for x in myresult:
        print(x)
        t.append(x[2])
        s.append(x[3])

    print(x[2])
    print(x[3])

    plt.figure("ISP Speed TEST")
    plt.subplot(211)
    plt.plot(t)
    plt.ylabel('Mbits per sec')
    plt.xlabel('DATE/TIME')
    plt.title('Download Speed')

    plt.subplot(212)
    plt.plot(s)
    plt.title("Upload Speed")
    plt.ylabel('Mbits per sec')
    plt.xlabel('DATE/TIME')

    plt.tight_layout()
    plt.show()

def main(tkinter.Frame):

    DrawUpDown(tkinter.Frame)

if __name__ == '__main__':
    main()



