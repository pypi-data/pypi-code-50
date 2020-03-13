import os
import json
import time
import cv2
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PIL import Image
import tempfile

from app.utils import *
from app.borderlayout import *

class ImgFullView(QMainWindow):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowModality(Qt.ApplicationModal)
        self.title = "Image full scale view "
        self.setWindowTitle(self.title)
        # drect = QDesktopWidget().availableGeometry()
        # drect.adjust(SUBWINDOW_ADJUST,SUBWINDOW_ADJUST,-SUBWINDOW_ADJUST,-SUBWINDOW_ADJUST)
        self.setGeometry(SUB_WINDOW_SIZE)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        # centerPoint = mainWindow().geometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        layout = QHBoxLayout()
        scroll = QtGui.QScrollArea()
        self.ilabel = QLabel(self)
        self.ilabel.setAlignment(Qt.AlignCenter)
        scroll.setWidget(self.ilabel)
        scroll.setWidgetResizable(True)

        layout.addWidget(scroll)
        self.main_widget.setLayout(layout)

    def setPixmap(self, pixmap):
        self.ilabel.setPixmap(pixmap)


class JobImageWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.parent = parent
        self.img_width = 640
        self.img_height = 480
        self.setMinimumHeight(420)
        # self.setMinimumWidth(900)
        self.layout = QVBoxLayout()
        self.name_label = QLabel()
        self.name_label.setStyleSheet('font-weight: bold; font-size: 16pt;')
        self.ilabel = QLabel(self)
        self.nlabel = QLabel(self)
        self.tlabel = QLabel(self)
        self.ilabel.resize(self.img_width, self.img_height)
        self.full_view = ImgFullView(self)

        self.clearImage()
        self.layout.addWidget(self.name_label)

        hlayout = QHBoxLayout()
        hwidget = QWidget()
        hlayout.setAlignment(Qt.AlignTop)
        hlayout.addWidget(self.ilabel)
        zoombutton = QPushButton()
        zoombutton.setIcon(QApplication.style().standardIcon(QStyle.SP_FileDialogContentsView))
        zoombutton.clicked.connect(self.show_zoomed)
        hlayout.addWidget(zoombutton)
        hwidget.setLayout(hlayout)


        self.layout.addWidget(hwidget)
        self.layout.addWidget(self.nlabel)
        self.layout.addWidget(self.tlabel)
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.addStretch(1)
        self.setLayout(self.layout)
        self.src_pixmap = None
        # self.cv_img = None


    def clearImage(self):
        name = os.path.join(this_dir,'img','noimage.png')
        cvImg = cv2.imread(name)
        self.setImage(cvImg, name)

    def setImage(self, cvImg, name, time=''):
        # self.cv_img = cvImg.copy()
        cvImg = cv2.cvtColor(cvImg, cv2.COLOR_BGR2RGB)
        height, width, channel = cvImg.shape
        bytesPerLine = 3 * width
        qImg = QImage(cvImg.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qImg)
        self.src_pixmap = pixmap
        pixmap = pixmap.scaled(self.img_width, self.img_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ilabel.setPixmap(pixmap)
        self.nlabel.setText("{} {}x{} {}".format(name,width,height,channel))
        self.tlabel.setText(time)
        self.full_view.setPixmap(self.src_pixmap)

    def show_zoomed(self):
        if self.src_pixmap:
            self.full_view.setPixmap(self.src_pixmap)
            self.full_view.show()

    # def get_cv_img(self):
    #     try:
    #         tmpname = os.path.join(tempfile.gettempdir(),str(time.time())+'.jpg')
    #         cv2.imwrite(tmpname, self.cv_img)
    #         print('saved in {}'.format(tmpname))
    #         return tmpname
    #     except Exception as e:
    #         print(e)
    #         return None

class JobImageFilesDialog(QDialog):

    def __init__(self, parent, job_id):
        super(QDialog, self).__init__(parent)
        self.parent = parent
        self.setContentsMargins(QMARGIN)
        layout = BorderLayout(margin=MARGIN)
        info = QLabel('If this list is empty, do test in Camera Input configuration, to get some camera images.')
        layout.addWidget(info, BorderLayout.North)
        self.list = QListWidget()
        self.list.clicked.connect(self.file_selected)
        layout.addWidget(self.list, BorderLayout.West)
        self.img = JobImageWidget(self)
        layout.addWidget(self.img, BorderLayout.Center)
        button_ok = QPushButton('Use selected')
        button_ok.clicked.connect(self.close)
        layout.addWidget(button_ok, BorderLayout.South)
        self.setLayout(layout)
        self.job_id = job_id
        self.load_files()
        self.selected_file = None

    def load_files(self):
        dir = local_job_dir(self.job_id)
        files = os.listdir(dir)
        for f in files:
            self.list.addItem(f)

    def file_selected(self, qmodelindex):
        self.selected_file = self.list.currentItem().text()
        ffname = os.path.join(local_job_dir(self.job_id), self.selected_file)
        try:
            img_cv = cv2.imread(ffname)
            self.img.setImage(img_cv, self.selected_file, '')
        except:
            pass
