# coding: utf-8
# !/usr/bin/python
"""
@File       :   Welcome.py
@Author     :   jiaming
@Modify Time:   2020/1/16 14:06
@Contact    :   https://blog.csdn.net/weixin_39541632
@Version    :   1.0
@Desciption :   None
"""
import os
import tkinter as tk
import os
from tkinter import filedialog

from cylinder_qrcode_project.cqrcode.app.scan_figure import scan_cylinder_qr_code
from cylinder_qrcode_project.cqrcode.app.run import main
from cylinder_qrcode_project.cqrcode.app.QRcode import create_QRcode
from view.GUI_view import window

scaleValue = None
rawPath = os.path.abspath(__file__)
dataPath = rawPath[:rawPath.find('view')] + r'static'


def load_data():
    """
    读入 static/_input.txt 文本内容作为二维码的填充数据
    :return:
    """
    global dataPath
    file = dataPath + r'\_input.txt'
    with open(file, 'r', encoding='utf-8') as f:
        dataString = f.read()
    return dataString



def hello():
    """
    键入文本初始界面
    :return:
    """
    global dataPath
    root = tk.Tk()
    root.iconbitmap(dataPath + r'\icon\welcome.ico')
    root.title("Welcome")
    root.geometry('300x260+504+248')
    root.resizable(False, False)
    # root.resizable(True, True)

    # 放置图片
    def putImage():
        """
        :return:
        """
        photoLabel = tk.Label()
        path = dataPath + r'\root\blank.png'
        bm = tk.PhotoImage(file=path)
        photoLabel.x = bm
        photoLabel['image'] = bm
        photoLabel.pack()
    putImage()

    def click_btn_scan_figure(btn=None):
        """

        :param btn:
        :return:
        """
        file_path = filedialog.askopenfilename()
        print(file_path) # 打印文件的路径
        scan_cylinder_qr_code(filePath=file_path, real=True) # 调用扫描器
    scanBtn = tk.Button(root, text='select and scan figure', bd=5, height=1,
                        relief=tk.GROOVE, width=27, activeforeground="#ffffff")
    scanBtn.config(command=lambda: click_btn_scan_figure(scanBtn))
    scanBtn.pack()

    # 键入文本按钮
    def click_btn_cmd(btn=None):
        """
        :param btn:
        :return:
        """
        input_text_path = dataPath + r'\_input.txt'
        if not os.path.exists(dataPath + r'\_input.txt'):
            with open(dataPath + r'\_input.txt', 'w') as f:
                pass
        os.startfile(input_text_path)

    editBtn = tk.Button(root, text='Type the text', bd=5, height=1,
                        relief=tk.GROOVE, width=27, activeforeground="#ffffff")
    editBtn.config(command=lambda: click_btn_cmd(editBtn))
    editBtn.pack()

    def scale_command(ev=None):
        """
        :return:
        """
        global scaleValue
        scaleValue = horizontalScale.get()

    # 滑动条
    horizontalScale = tk.Scale(root, from_=0, to=1.5, tickinterval=0.5,
                               resolution=0.01, length=200,
                               orient=tk.HORIZONTAL, command=scale_command)
    horizontalScale.set(1.25)
    horizontalScale.pack()

    # label
    tk.Label(
        root,
        text='Length / Cylindrical radius',
        font='Helvetica -11').pack()

    v = tk.IntVar()

    def callCheckbutton():
        # 设置数值
        if v.get() == 1:
            print("二维码边长 / 圆柱体半径： ", float(horizontalScale.get()))
    checkButton = tk.Checkbutton(root, variable=v, text="expand figure",
                                 offvalue=0, onvalue=1,
                                 command=callCheckbutton)
    checkButton.pack()
    v.set(0)
    def create_code_cmd(btn=None):
        """

        :return:
        """
        # 生成传统二维码
        img, FILE = create_QRcode()
        img.save(FILE, dpi=(254.0, 254.0))  # 生成图片
        if v.get() == 1:
            # 生成延展的柱体二维码
            plane_qecode_filePath, expand_filePath = main(data=load_data(),
                    version=None, box=4, Boundary=4, exps=True, rate=float(
                    horizontalScale.get()))
            window(FILE, plane_qecode_filePath, expand_filePath)
        else:
            # 生成未延展后的二维码
            plane_qecode_filePath = main(data=load_data(), version=None,
                    box=4, Boundary=4, exps=False, rate=-1)
            print(plane_qecode_filePath)
            window(FILE, plane_qecode_filePath, file2Path='')
        # showMsg(title='结果', message='创建完毕')
    # 导出按钮
    createCodeBtn = tk.Button(root, width=15, height=2, text='outPut',
                              font='Helvetica -18', fg='red',
                              activebackground='#f0f0f0', relief=tk.FLAT)
    createCodeBtn.config(command=create_code_cmd)
    createCodeBtn.pack()
    root.mainloop()


if __name__ == "__main__":
    hello()
