from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class HorizontalTabBar(QTabBar):

    def __init__(self, parent=None,  icons= None):
        QTabBar.__init__(self, parent)
        self.icons = icons

    def paintEvent(self, event):
        painter = QStylePainter(self)
        option = QStyleOptionTab()
        for index in range(self.count()):
            self.initStyleOption(option, index)
            painter.drawControl(QStyle.CE_TabBarTabShape, option)
            # painter.drawText(self.tabRect(index),
            #                 Qt.AlignCenter | Qt.TextDontClip,
            #                 self.tabText(index))
            if self.icons:
                rect = self.tabRect(index)
                rect.adjust(12,12,-12,-12)
                if index > len(self.icons):
                    continue
                img = QImage(self.icons[index])
                painter.drawImage(rect, img)


    def tabSizeHint(self, index):
        size = QTabBar.tabSizeHint(self, index)
        size.setHeight(64)
        size.setWidth(64)
        if size.width() < size.height():
            size.transpose()
        return size


class TabWidget(QTabWidget):
    def __init__(self, parent=None, icons=None):
        QTabWidget.__init__(self, parent)
        self.setTabBar(HorizontalTabBar(icons=icons))
