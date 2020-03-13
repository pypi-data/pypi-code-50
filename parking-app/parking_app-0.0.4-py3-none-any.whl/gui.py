import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from mpipes.common_auth import *
from mpipes.common import *
import qdarkgraystyle
from requests.auth import *
import urllib3

from app.utils import *
from app.async import initAsync, getAsync
from app.horizontaltab import  TabWidget
from app.corrector import CorrectorMainWidget
from app.jobwidgets import JobsWidget
from app.borderlayout import *

os.environ['PYQTGRAPH_QT_LIB'] = 'PyQt5'  # Garantee pyqtgraph uses PyQt5 if avalilable
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Parking desktop app'
        self.setWindowTitle(self.title)
        # drect = QDesktopWidget().availableGeometry()
        # drect.adjust(50,50,-50,-50)
        self.setGeometry(MAIN_WINDOW_SIZE)
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
        self.parking_app_widget = ParkingAppWidget(self)
        self.setCentralWidget(self.parking_app_widget)
        self.setContentsMargins(QMARGIN)
        self.show()


class ParkingAppWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = BorderLayout(margin=MARGIN)

        self.auth_widget = TopWidget(self)
        self.layout.addWidget(self.auth_widget, BorderLayout.North)

        self.status_widget = QStatusBar(self)
        self.layout.addWidget(self.status_widget, BorderLayout.South)

        # Initialize tab screen

        icons = [
            os.path.join(this_dir,'img/webcam-control_record.png'),
            os.path.join(this_dir,'img/slideshow_report.png'),
            os.path.join(this_dir,'img/pictures-ok.png'),
            os.path.join(this_dir,'img/activity_monitor.png')
        ]
        self.tabs = TabWidget(icons=icons)
        self.tabs.setTabPosition(QTabWidget.West)
        # self.tabs.resize(300, 200)
        # self.dashboard_widget = QWidget(self)
        self.jobs_widget = JobsWidget(self)
        self.comm_logs = QTextEdit(self)
        self.comm_logs.setReadOnly(True)
        self.comm_logs.setLineWrapMode(QTextEdit.NoWrap)

        self.corrector_widget = CorrectorMainWidget(self)

        # Add tabs
        self.tabs.addTab(self.jobs_widget, "Jobs")
        # self.tabs.addTab(self.dashboard_widget, "Dashboard")
        self.tabs.addTab(self.corrector_widget,"Corrector")
        self.tabs.addTab(self.comm_logs, "Communication")

        # Add tabs to widget
        self.layout.addWidget(self.tabs, BorderLayout.Center)
        self.setLayout(self.layout)
        initAsync(self.status_widget, self.comm_logs)

    def status_message(self, string):
        self.status_widget.showMessage(string)

    def reloadUI(self):
        idx = self.tabs.currentIndex()
        if idx == 0:
            self.jobs_widget.reloadJobs()
        elif idx == 1:
            self.corrector_widget.reloadJobs()


    def getPrec(self):
        return self.auth_widget.getPrec()

    def getVals(self):
        return self.auth_widget.getVals()


class TopWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.parent = parent
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(QMARGIN)
        title = QLabel('Authentication')
        self.layout.addWidget(title)
        self.auths = QComboBox()
        auths_ = self.list_auths()
        for auth in auths_:
            self.auths.addItem(auth)
        if len(auths_):
            self.auths.setCurrentText(get_default_authentication())
        self.auths.currentIndexChanged.connect(self.selectionchange)
        self.layout.addWidget(self.auths)
        self.layout.addStretch(1)
        self.selections = QWidget()
        slayout = QHBoxLayout()
        slayout.addStretch(1)
        slayout.addWidget(QLabel('Stats time range'))
        self.precs = QComboBox()
        for prec in ['20s', '10m', '1h', '1d']:
            self.precs.addItem(str(prec))
        self.precs.setCurrentText('10m')
        slayout.addWidget(self.precs)
        slayout.addWidget(QLabel('Stats values'))
        self.vals = QComboBox()
        for val in [1, 3, 5, 10, 20, 30, 40, 50, 60]:
            self.vals.addItem(str(val))
        self.vals.setCurrentText(str(10))
        slayout.addWidget(self.vals)
        self.selections.setLayout(slayout)
        self.layout.addWidget(self.selections)
        self.timer = QTimer()
        self.timer.setSingleShot(False)
        self.timer.start(10000)
        self.timer.timeout.connect(self.reload)
        self.layout.addWidget(QLabel('Update speed'))
        self.uspeed = QComboBox()
        for speed in [5, 10, 20, 30, 50, 60]:
            self.uspeed.addItem(str(speed))
        self.uspeed.setCurrentText('10')
        self.uspeed.currentIndexChanged.connect(self.speedselectionchange)
        self.layout.addWidget(self.uspeed)
        # self.layout.addWidget(QLabel('Style'))
        # self.styles = QComboBox()
        # for style in QStyleFactory.keys():
        #     self.styles.addItem(style)
        # self.styles.addItem('Qdarkstyle')
        # self.styles.currentIndexChanged.connect(self.styleselectionchange)
        # self.layout.addWidget(self.styles)
        self.setLayout(self.layout)

    def styleselectionchange(self, i):
        global app
        style = self.styles.currentText()
        if style == 'Qdarkstyle':
            app.setStyleSheet(qdarkgraystyle.load_stylesheet())
        else:
            app.setStyle(style)

    def speedselectionchange(self, i):
        spd = self.uspeed.currentText()
        spdi = 1000 * int(spd)
        self.timer.stop()
        self.timer.start(spdi)

    def selectionchange(self, i):
        auth = self.auths.currentText()
        self.parentWidget().status_message('Setting default authentication to {}'.format(auth))
        set_default_authentication(auth)
        async = getAsync()
        async.reloadCon()
        self.parent.reloadUI()


    def list_auths(self):
        basedir = base_dir()
        rt = []
        for f in os.listdir(basedir):
            if f.endswith(AUTH_FILE_SUFFIX):
                rt.append(os.path.splitext(f)[0])
        return rt

    def reload(self):
        # print('Reload')
        self.parentWidget().reloadUI()

    def getPrec(self):
        return self.precs.currentText()

    def getVals(self):
        return self.vals.currentText()



def main(argv=sys.argv[1:]):
    global app
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkgraystyle.load_stylesheet())
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QStyleFactory, 'AA_UseHighDpiPixmaps'):
        app.setAttribute(Qt.AA_UseHighDpiPixmaps)
    # app.setStyle('Fusion')
    ex = App()
    sys.exit(app.exec_())



if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))