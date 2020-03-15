import math
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

class Painter(Tk):
    def __init__(self, startX=0, startY=0,curX=0, curY=0, endX=0, endY=0, line=False, rect=False, oval=False, arc=False, circle=False, polygon=False):
        Tk.__init__(self, )
        self.title('绘图工具v1.0')
        self.geometry('800x600')
        self.resizable(width=False, height=False)
        # 布尔值指定画相应的图形 
        self.line = line
        self.rect = rect
        self.oval = oval
        self.arc = arc
        self.circle = circle
        self.polygon = polygon
        # 鼠标位置信息参数
        self.startX = startX
        self.startY = startY
        self.curX = curX
        self.curY = curY
        self.endX = endX
        self.endY = endY
        # 初始化控件
        self.createWidgets()
    
    def createWidgets(self):
        self.menubar = Menu(self)
        self.canvasmenu = Menu(self.menubar, tearoff=False)
        self.canvasmenu.add_command(label='椭圆', command=self.create_oval)
        self.canvasmenu.add_command(label='圆', command=self.create_circle)
        self.canvasmenu.add_command(label='圆弧', command=self.create_arc)
        self.canvasmenu.add_command(label='矩形', command=self.create_rect)
        self.canvasmenu.add_command(label='多边形', command=self.create_polygon)
        self.canvasmenu.add_command(label='直线', command=self.create_line)
        self.canvasmenu.add_separator()
        self.canvasmenu.add_command(label='清空画板', command=self.clean)
        self.canvasmenu.add_separator()
        self.canvasmenu.add_command(label='退出', command=self.destroy)
        self.menubar.add_cascade(label='绘图', menu=self.canvasmenu)
        self.settingmenu = Menu(self.menubar, tearoff=False)
        self.settingmenu.add_command(label='设置图形样式...', command=self.settings)
        self.menubar.add_cascade(label='设置', menu=self.settingmenu)
        self.helpmenu = Menu(self.menubar, tearoff=False)
        self.helpmenu.add_command(label="关于...", command=self.about)
        self.helpmenu.add_command(label='使用帮助', command=self.helps)
        self.menubar.add_cascade(label='帮助', menu=self.helpmenu)
        self.config(menu=self.menubar)
        self.canvas = Canvas(self, width=500, height=400,)
        self.canvas.bind('<Button-1>', self.getStartInfo)
        self.canvas.bind('<ButtonRelease-1>', self.getEndInfo)
        self.canvas.bind('<Motion>', self.getCurInfo)
        self.canvas.pack(side=TOP, expand=YES, fill=BOTH)
    
    def getStartInfo(self, event):
        self.startX = event.x
        self.startY = event.y
    
    def getCurInfo(self, event):
        self.curX = event.x
        self.curY = event.y
    
    def getEndInfo(self, event):
        self.endX = event.x
        self.endY = event.y
        if self.line == True:
            self.canvas.create_line( self.startX, self.startY, self.endX, self.endY, fill='blue')
        elif self.rect == True:
            self.canvas.create_rectangle(self.startX, self.startY, self.endX, self.endY, fill='red', tags="rect")
        elif self.oval == True:
            self.canvas.create_oval(self.startX, self.startY, self.endX, self.endY, fill='green', tags='oval')
        elif self.arc == True:
            self.canvas.create_arc(self.startX, self.startY, self.endX, self.endY, start=0, extent=90, width=2, fill="yellow", tags="arc")
        elif self.circle == True:
            x = self.startX
            y = self.startY
            r = math.sqrt((self.endX - x) ** 2 + (self.endY - y) ** 2)
            self.canvas.create_oval( x - r, y - r, x + r, y + r, fill='pink', tags='circle')
        elif self.polygon == True:
            n = simpledialog.askinteger("输入", "您要绘制几边形(大于3的整数):", initialvalue=3, minvalue=3, maxvalue=50)
    
    def create_oval(self):
        self.oval = True
        self.rect = False
        self.line = False
        self.arc = False
        self.circle = False
        self.polygon = False
    
    def create_rect(self):
        self.rect = True
        self.line = False
        self.oval = False
        self.arc = False
        self.circle = False
        self.polygon = False
    
    def create_line(self):
        self.line = True
        self.rect = False
        self.oval = False
        self.arc = False
        self.circle = False
        self.polygon = False
    
    def create_arc(self):
        self.arc = True
        self.line = False
        self.rect = False
        self.oval = False
        self.circle = False
        self.polygon = False
    
    def create_circle(self):
        self.circle = True
        self.line = False
        self.rect = False
        self.oval = False
        self.arc = False
        self.polygon = False
    
    def create_polygon(self):
        self.polygon = True
        self.circle = False
        self.line = False
        self.rect = False
        self.oval = False
        self.arc = False
    
    def helps(self):
        self.canvas.delete('all')
        self.canvas.create_text(400, 300, text='\t\t【画图步骤】\n \
            1.从菜单栏中选择想要绘制的图形，移动鼠标至绘图区内；\n \
            2.使用鼠标在主窗口绘图区中单击，选择图e形起始点；\n \
            3.单击后不要松开鼠标，继续拖动至所绘制图形结束点；\n \
            4.松开鼠标即可画出相应的图形\n \
            ***单击菜单"【绘图】-【清空画板】"后此信息消失***', fill='red', font=('微软雅黑', 18))
    
    def settings(self):
        print('开发中...')
    
    def clean(self):
        self.update()
        self.canvas.delete('all')
    
    @staticmethod
    def about():
        messagebox.showinfo('关于...', '绘图工具v1.0')

Painter().mainloop()