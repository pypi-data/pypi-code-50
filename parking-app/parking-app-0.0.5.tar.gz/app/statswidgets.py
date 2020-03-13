from datetime import datetime
import time
import pyqtgraph as pg
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import *
from pyqtgraph import PlotDataItem


class TimeAxisItem(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setLabel(text='Time', units=None)
        self.enableAutoSIPrefix(False)

    def tickStrings(self, values, scale, spacing):
        return [datetime.fromtimestamp(value).strftime("%D %H:%M") for value in values]


class StatsWidget(QWidget):
    def __init__(self, parent, title):
        super(QWidget, self).__init__(parent)
        self.setMinimumHeight(250)
        self.layout = QVBoxLayout()
        self.graphWidget = pg.PlotWidget(parent=self, axisItems={'bottom': TimeAxisItem(orientation='bottom')},
                                         autoRange=True)
        self.graphWidget.setXRange(time.time(), time.time() + 100)
        # Add Background colour to white
        # Add Title
        self.graphWidget.setTitle(title)
        # Add Axis Labels
        # self.graphWidget.setLabel('left', 'Temperature (°C)', color='red', size=30)
        # self.graphWidget.setLabel('bottom', 'Hour (H)', color='red', size=30)
        # Add legend
        self.graphWidget.addLegend()
        # Add grid
        self.graphWidget.showGrid(x=True, y=True)
        # Set Range
        # self.graphWidget.setXRange(0, 100, padding=0)
        # self.graphWidget.setYRange(20, 555, padding=0)

        # self.plot(hour, temperature_1, "Sensor1", 'r')
        # self.plot(hour, temperature_2, "Sensor2", 'b')
        self.layout.addWidget(self.graphWidget)
        self.setLayout(self.layout)
        self.plotItems = {}

    def setXRange(self, x1, x2):
        self.graphWidget.setXRange(x1, x2)

    def setYRange(self, y1, y2):
        self.graphWidget.setYRange(y1, y2)

    def plot(self, x, y, plotname, color):
        if plotname in self.plotItems:
            pitem = self.plotItems[plotname]
            pitem.setData(x, y, connect="finite")
            self.graphWidget.replot()
        else:
            pen = pg.mkPen(color=color)
            pitem = PlotDataItem(x, y, name=plotname, pen=pen, symbol='o', symbolSize=3, symbolBrush=(color),
                                 connect="finite")
            self.plotItems[plotname] = pitem
            self.graphWidget.addItem(pitem, params={})

    def clear(self):
        for x in self.plotItems:
            item = self.plotItems[x]
            self.graphWidget.removeItem(item)
        self.plotItems.clear()

class NumberWidget(QWidget):
    def __init__(self, parent, title, main_op, ops, style):
        super(QWidget, self).__init__(parent)
        self.parent = parent
        self.style = style
        # self.color = 'rgb(153,255,153)'
        self.setMaximumHeight(self.style['height'])
        self.setMinimumHeight(self.style['height'] - 100)
        self.setMaximumWidth(self.style['width'])
        self.setMinimumWidth(self.style['width'] - 100)
        layout = QHBoxLayout()

        main_num_widget = QWidget()
        main_num_layout = QVBoxLayout()
        label_title = QLabel()
        label_title.setText(title)
        label_title.setStyleSheet(self.style['subtitle'])
        main_num_layout.addWidget(label_title)
        self.label_main_op = QLabel()
        self.label_main_op.setStyleSheet(self.style['title'])
        main_num_layout.addWidget(self.label_main_op)
        self.label_subtitle = QLabel()
        main_num_layout.addWidget(self.label_subtitle)
        main_num_widget.setLayout(main_num_layout)
        layout.addWidget(main_num_widget)

        ops_num_widget = QWidget()
        ops_num_layout = QVBoxLayout()
        self.ops = {}
        for op in ops:
            label_title = QLabel()
            label_title.setText(op)
            label_title.setStyleSheet("font-size: 8pt;")
            ops_num_layout.addWidget(label_title)
            num_title = QLabel()
            num_title.setStyleSheet(self.style['numtitle'])
            ops_num_layout.addWidget(num_title)
            self.ops[op] = num_title

        ops_num_layout.addStretch(1)
        ops_num_widget.setLayout(ops_num_layout)
        layout.addWidget(ops_num_widget)
        layout.addStretch(1)
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)
        self.main_op = main_op
        self.title = title

    def getLastVal(self, stat):
        found = None
        for val in reversed(stat):
            if val:
                found = val
                break
        return found

    def clear(self):
        self.label_main_op.setText('')
        self.label_subtitle.setText('')
        for op in self.ops:
            op_w = self.ops[op]
            op_w.setText('')

    def setStat(self, stat, subtitle):
        if not stat or not self.main_op in stat:
            return

        main_val = self.getLastVal(stat[self.main_op])
        self.label_subtitle.setText("{}/{}".format(self.main_op, subtitle))
        if main_val:
            if 'multi' in self.style and self.style['multi']:
                main_val = main_val / self.style['multi']
            self.label_main_op.setText(self.style['num_format'].format(main_val))
        else:
            self.label_main_op.setText('')

        for op in self.ops:
            op_w = self.ops[op]
            op_val = self.getLastVal(stat[op])
            if op_val:
                op_w.setText(self.style['num_format'].format(op_val))
            else:
                op_w.setText('')
