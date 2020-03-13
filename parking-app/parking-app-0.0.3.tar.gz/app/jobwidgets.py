from datetime import timezone

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from mpipes.common import *

from app.borderlayout import BorderLayout
from app.configurationwidgets import *
from app.statswidgets import *

from app.async import getAsync


class RawView(QMainWindow):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowModality(Qt.ApplicationModal)
        self.title = "Raw view - {}"
        self.setWindowTitle(self.title.format(''))
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
        self.setContentsMargins(QMARGIN)

        layout = BorderLayout()
        self.raw = QTextEdit(parent)
        self.raw.setReadOnly(True)
        self.raw.setLineWrapMode(QTextEdit.NoWrap)
        layout.addWidget(self.raw, BorderLayout.Center)
        self.main_widget.setLayout(layout)

    def setJob(self, job):
        self.raw.clear()
        if not job:
            return
        self.setWindowTitle(self.title.format(job['name']))
        self.raw.insertPlainText(json.dumps(job, indent=4, sort_keys=True))



class JobAttributesWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.parent = parent
        self.main_layout = BorderLayout(margin=MARGIN)

        job_name_label = QLabel('Name')
        job_id_label = QLabel('ID')
        job_created_label = QLabel('Created')
        job_autostart_label = QLabel('Autostart')
        job_priority_label = QLabel('Priority')
        job_status_label = QLabel('Status')

        self.job_id_edit = QLabel()
        self.job_name_edit = QLineEdit()
        self.job_name_edit.textChanged.connect(self.changeName)
        self.job_status_edit = QLabel()
        self.job_created_edit = QLabel()
        self.job_autostart_edit = QCheckBox()
        self.job_priority_edit = QLineEdit()

        self.attribs_widget = QWidget(self)
        grid = QGridLayout()
        grid.setSpacing(MARGIN)
        etuples = [
            (job_name_label, self.job_name_edit),
            (job_priority_label, self.job_priority_edit),
            (job_autostart_label, self.job_autostart_edit),
            (job_id_label, self.job_id_edit),
            (job_created_label, self.job_created_edit),
            (job_status_label, self.job_status_edit),
        ]
        for x in range(len(etuples)):
            grid.addWidget(etuples[x][0], x + 1, 0)
            grid.addWidget(etuples[x][1], x + 1, 1)

        buttons = QWidget()
        view_button = QPushButton()
        view_button.setIcon(QApplication.style().standardIcon(QStyle.SP_FileDialogInfoView))
        view_button.clicked.connect(self.rawView)
        self.add_button = QPushButton("Clone")
        self.add_button.clicked.connect(self.cloneJob)
        self.edit_button = QPushButton("Save")
        self.edit_button.clicked.connect(self.saveJob)
        # edit_button.setIcon(QApplication.style().standardIcon(QStyle.SP_BrowserReload))
        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.startStopJob)
        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.deleteJob)
        hbox = QHBoxLayout()
        hbox.addWidget(view_button)
        hbox.addStretch(1)
        hbox.addWidget(self.add_button)
        hbox.addWidget(self.edit_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.delete_button)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        buttons.setLayout(vbox)
        grid.addWidget(buttons, len(etuples) + 1, 1)
        self.attribs_widget.setLayout(grid)
        self.main_layout.addWidget(self.attribs_widget, BorderLayout.North)
        self.setLayout(self.main_layout)
        self.job = None
        self.rawViewWindow = RawView(self)
        self.setButtonsState()

    def setJob(self, job):
        self.job = job
        if job:
            if 'id' in job:
                id = job['id']
                self.job_id_edit.setText(id)
            if 'status' in job:
                self.job_status_edit.setText(job['status'])
            else:
                self.job_status_edit.setText('')
            if 'name' in job:
                self.job_name_edit.setText(job['name'])
            else:
                self.job_name_edit.setText('')
            if 'created' in job:
                self.job_created_edit.setText(job['created'])
            else:
                self.job_created_edit.setText('')
            if 'priority' in job:
                self.job_priority_edit.setText(str(job['priority']))
            else:
                self.job_priority_edit.setText('0')
            if 'autostart' in job:
                self.job_autostart_edit.setChecked(job['autostart'])
            else:
                self.job_autostart_edit.setChecked(False)
        else:
            self.job_id_edit.setText('')
            self.job_name_edit.setText('')
            self.job_status_edit.setText('')
            self.job_created_edit.setText('')
            self.job_priority_edit.setText('')
            self.job_autostart_edit.setChecked(False)
        self.setButtonsState()

    def setButtonsState(self):
        if not self.job:
            self.add_button.setEnabled(False)
            self.edit_button.setEnabled(False)
            self.stop_button.setEnabled(False)
            self.delete_button.setEnabled(False)
            return
        if not 'created' in self.job:
            self.add_button.setEnabled(False)
            self.edit_button.setEnabled(True)
            self.stop_button.setEnabled(False)
            self.delete_button.setEnabled(False)
        else:
            self.add_button.setEnabled(True)
            self.edit_button.setEnabled(True)
            self.stop_button.setEnabled(True)
            self.delete_button.setEnabled(True)
        if 'status' in self.job:
            if 'created' in self.job:
                if self.job['status'] == 'status.started':
                    self.stop_button.setText('Stop')
                else:
                    self.stop_button.setText('Start')


    def changeName(self, name):
        if self.job:
            self.job['name'] = name

    def rawView(self):
        if not self.job:
            return
        self.saveValues()
        self.rawViewWindow.setJob(self.job)
        self.rawViewWindow.show()

    def saveValues(self):
        if not self.job:
            return
        self.job['name'] = self.job_name_edit.text()
        self.job['priority'] = int(self.job_priority_edit.text())
        self.job['autostart'] = self.job_autostart_edit.isChecked()


    def cloneJob(self):
        if self.job:
            self.saveValues()
            job = self.job.copy()
            job['id'] = track_uuid()
            if 'status' in job:
                job.pop('status')
            if 'created' in job:
                job.pop('created')
            self.parent.setJob( job )

    def jobOperationDone(self, success):
        if success:
            self.parent.reloadJobs()

    def jobDeleteDone(self, success):
        if success:
            self.parent.clearJob()
            self.parent.reloadJobs()

    def saveJob(self):
        if not self.job:
            return
        self.saveValues()
        async = getAsync()
        if  'created' in self.job:
            async.jobEdit(self.jobOperationDone, self.job['id'], json.dumps(self.job))
        else:
            async.jobAdd(self.jobOperationDone, json.dumps(self.job))


    def deleteJob(self):
        if not self.job:
            return
        ret = QMessageBox.warning(self, "Delete job warning", "Current job will be wiped from server and all data will be lost, are you sure?",
                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ret == QMessageBox.No:
            return
        async = getAsync()
        async.jobDelete(self.jobDeleteDone, self.job['id'])

    def startStopJob(self):
        if self.job and 'status' in self.job and 'created' in self.job:
            if self.job['status'] == 'status.started':
                # stop
                operation = 'stop'
            else:
                # start
                operation = 'start'

            async = getAsync()
            async.jobStartStop(self.jobOperationDone, self.job['id'], operation)


class JobStepWidget(QWidget):

    def __init__(self, parent, description, job_step_type, config_window):
        super(QWidget, self).__init__(parent)
        self.parent = parent
        self.job_step_type = job_step_type
        layout = QHBoxLayout()
        label = QLabel(description)
        layout.addWidget(label)
        self.is_enabled = QCheckBox()
        self.is_enabled.clicked.connect(self.enabledChanged)
        layout.addWidget(self.is_enabled)
        self.config_button = QPushButton("Configure")
        self.config_button.clicked.connect(self.configure)
        layout.addWidget(self.config_button)
        self.setLayout(layout)
        self.job = None
        self.config_window = config_window

    def configure(self):
        if not self.job:
            return
        self.config_window.configure(self.job)
        self.config_window.show()

    def enabledChanged(self, enabled):
        if not self.job:
            return
        if enabled:
            self.config_button.setEnabled(True)
            self.addStep()
            self.config_window.configure(self.job)
        else:
            self.config_button.setEnabled(False)
            self.config_window.configure(self.job)
            self.config_window.removeConfiguration()
            self.removeStep()

    def removeStep(self):
        if not self.job:
            return
        if 'routes' in self.job and len(self.job['routes']) > 0:
            steps = self.job['routes'][0]['steps']
            found = None
            for step in steps:
                if 'worker_type' in step and step['worker_type'] == self.job_step_type:
                    found = step
                    break
            if found:
                steps.remove(found)

    def insertAfter(self, steps, precedesor, mystep):
        for x in range(len(steps)):
            step = steps[x]
            if 'worker_type' in step and step['worker_type'] == precedesor:
                steps.insert(x + 1, mystep)
                return True
        return False

    def addStep(self):
        if not self.job:
            return
        if 'routes' in self.job and len(self.job['routes']) > 0:
            steps = self.job['routes'][0]['steps']
            found = None
            for step in steps:
                if 'worker_type' in step and step['worker_type'] == self.job_step_type:
                    found = step
                    break
            if not found:
                mypos = STEPS_ORDER.index(self.job_step_type)
                precs = STEPS_ORDER[:mypos]
                mystep = {
                    'name': 'step_{}'.format(self.job_step_type),
                    'worker_type': self.job_step_type
                }
                inserted = False
                for precedesor in reversed(precs):
                    if self.insertAfter(steps, precedesor, mystep):
                        inserted = True
                        break
                if not inserted:
                    steps.insert(0, mystep)

    def setJob(self, job):
        self.job = job
        if not job:
            return
        if 'routes' in job and len(job['routes']) > 0:
            steps = job['routes'][0]['steps']
            for step in steps:
                if 'worker_type' in step and step['worker_type'] == self.job_step_type:
                    self.is_enabled.setChecked(True)
                    self.config_button.setEnabled(True)
                    return
        self.is_enabled.setChecked(False)
        self.config_button.setEnabled(False)


class JobStepsWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.parent = parent
        layout = QVBoxLayout()
        layout.setContentsMargins(QMARGIN)
        self.steps = [
            JobStepWidget(self, 'Camera input', 'parking_image_input',
                          ConfigurationImageInput(self, 'parking_image_input')),
            JobStepWidget(self, 'Regions', 'parking_checker',
                          ConfigurationRegions(self, 'parking_checker')),
            JobStepWidget(self, 'Notification', 'notifier',
                          ConfigurationMqttNotifier(self, 'notifier')),
            JobStepWidget(self, 'Metrics', 'metrics_collector',
                          ConfigurationMetricsCollector(self, 'metrics_collector')),
            JobStepWidget(self, 'Archive', 'archiver',
                          ConfigurationArchive(self, 'archiver'))
        ]
        for x in range(len(self.steps)):
            layout.addWidget(self.steps[x])

        layout.addStretch(1)
        self.setLayout(layout)
        # self.temporaryImageMap = None

    def setJob(self, job):
        # self.temporaryImageMap = None
        for step in self.steps:
            step.setJob(job)


    # def setTemporaryImageMap(self, img):
    #     self.temporaryImageMap = img
    #
    # def getTemporaryImageMap(self):
    #     return self.temporaryImageMap

class JobWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.parent = parent
        self.layout = QVBoxLayout()

        top = QWidget()
        top_layout = QHBoxLayout()
        self.image_widget = JobImageWidget(self)
        self.attributes_widget = JobAttributesWidget(self)
        self.overview_widget = JobOverviewWidget(self)
        self.steps_widget = JobStepsWidget(self)
        top_tabs = QTabWidget()
        top_tabs.addTab(self.overview_widget, 'Overview')
        top_tabs.addTab(self.attributes_widget, "Edit")
        top_tabs.addTab(self.steps_widget, "Steps")
        top_layout.addWidget(self.image_widget)
        top_layout.addWidget(top_tabs)
        top.setLayout(top_layout)

        self.layout.addWidget(top)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab_dashboard = JobStatsWidget(self)
        self.tab_files = QWidget()
        self.tab_logs = JobLogsWidget(self)
        # self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab_dashboard, "Stats")
        self.tabs.addTab(self.tab_files, "Server files")
        self.tabs.addTab(self.tab_logs, "Server logs")

        # Add tabs to widget
        self.layout.addWidget(self.tabs, Qt.AlignTop)
        # self.layout.setAlignment(Qt.AlignTop)

        # self.logs_widget = JobLogsWidget(self)
        # self.layout.addWidget(self.logs_widget, BorderLayout.South)

        self.setLayout(self.layout)
        self.job = {}

    def setJob(self, job):
        self.initialState()
        self.job = job
        self.attributes_widget.setJob(job)
        self.steps_widget.setJob(job)
        self.tab_dashboard.setJob(job)
        self.overview_widget.setJob(job)
        self.tab_logs.setJob(job)

        self.loadLastJobImage()
        self.tab_dashboard.loadStats(self.parent.getPrec(), self.parent.getVals())
        self.overview_widget.loadStats(self.parent.getPrec(), self.parent.getVals())
        self.tab_logs.loadLogs(self.parent.getVals())

    def initialState(self):
        self.image_widget.clearImage()
        self.image_widget.name_label.setText('')

    def updateJob(self):
        if self.job and 'created' in self.job:
            self.loadLastJobImage()
            self.tab_dashboard.loadStats(self.parent.getPrec(), self.parent.getVals())
            self.overview_widget.loadStats(self.parent.getPrec(), self.parent.getVals())
            self.tab_logs.loadLogs(self.parent.getVals())

    def getJob(self):
        return self.job

    def reloadJobs(self):
        self.parent.reloadJobs()
        # self.parent.job_selected(0)

    def clearJob(self):
        self.setJob(None)
        self.parent.job = None

    def lastJobImageLoaded(self, rt_tuple):
        if not rt_tuple:
            return
        img, img_name, img_time = rt_tuple
        if not img_name:
            return
        self.image_widget.setImage(img, img_name, img_time)

    def loadLastJobImage(self):
        job = self.getJob()
        if not job or not 'created' in job:
            return
        self.image_widget.name_label.setText(job['name'])
        async = getAsync()
        async.loadLastJobImage( self.lastJobImageLoaded, job['id'])


class JobsWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        # Interpret image data as row-major instead of col-major
        self.parent = parent

        self.layout = BorderLayout(margin=5)
        # self.layout = QHBoxLayout(self)
        job_list = QWidget()
        job_list_layout = QVBoxLayout()

        self.job_treeview = QTreeView(self)
        self.job_treeview.setHeaderHidden(True)
        self.job_treeview.clicked.connect(self.job_selected)

        self.add_job_button = QPushButton('Add job')
        self.add_job_button.clicked.connect(self.add_job)
        job_list_layout.addWidget(self.add_job_button)
        job_list_layout.addWidget(self.job_treeview)
        job_list.setLayout(job_list_layout)
        self.layout.addWidget(job_list, BorderLayout.West)

        self.job_edit_widget = JobWidget(self)
        self.layout.addWidget(self.job_edit_widget, BorderLayout.Center)

        self.setLayout(self.layout)
        self.jobs = []
        self.con = None

        self.defered = QTimer()
        self.defered.setSingleShot(True)
        self.defered.timeout.connect(self.reloadJobs)
        self.defered.start(500)

        self.job = None


    def job_selected(self, qmodelindex):
        if len(self.jobs) > 0:
            idx = self.job_treeview.currentIndex()
            item = self.model.itemFromIndex(idx)
            if not item.data():
                return
            if self.job and not 'created' in self.job:
                ret = QMessageBox.warning(self, "Unsaved data warning", "Current job is unsaved, really select different one ?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if ret ==  QMessageBox.No:
                    return
            self.job = item.data()
            self.job_edit_widget.setJob(self.job)

    def reload_list(self):
        statuses = {}
        selected_item = None
        self.model = QStandardItemModel()
        rootNode = self.model.invisibleRootItem()
        for job in self.jobs:
            status = 'unknown'
            if 'status' in job:
                status = job['status']
            if status in statuses:
                stat_branch = statuses[status]
            else:
                stat_branch =  QStandardItem(status)
                rootNode.appendRow(stat_branch)
                statuses[status] = stat_branch
            childnode = QStandardItem(job['name'])
            childnode.setData(job)
            stat_branch.appendRow(childnode)
            if self.job and job['id'] == self.job['id']:
                selected_item = childnode

        self.job_treeview.setModel(self.model)
        for st in statuses:
            item = statuses[st]
            idx = self.model.indexFromItem(item)
            self.job_treeview.expand(idx)

        if selected_item:
            sidx = self.model.indexFromItem(selected_item)
            self.job_treeview.setCurrentIndex(sidx)


    def jobsLoaded(self, rt_items):
        if not rt_items:
            self.jobs = []
        else:
            self.jobs = rt_items
        self.reload_list()
        self.job_edit_widget.updateJob()


    def reloadJobs(self):
        try:
            async = getAsync()
            async.list_jobs(self.jobsLoaded)
        except Exception as e:
            self.parent.status_message(str(e))

    def getVals(self):
        return self.parent.getVals()

    def getPrec(self):
        return self.parent.getPrec()

    def add_job(self):
        self.job = new_job_template.copy()
        self.job['id'] = track_uuid()
        self.job_edit_widget.setJob( self.job )


class JobLogsWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = BorderLayout()
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab_debug = QTextEdit(self)
        self.tab_debug.setReadOnly(True)
        self.tab_debug.setLineWrapMode(QTextEdit.NoWrap)

        self.tab_info = QTextEdit(self)
        self.tab_info.setReadOnly(True)
        self.tab_info.setLineWrapMode(QTextEdit.NoWrap)

        self.tab_error = QTextEdit(self)
        self.tab_error.setReadOnly(True)
        self.tab_error.setLineWrapMode(QTextEdit.NoWrap)
        # self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab_debug, "DEBUG")
        self.tabs.addTab(self.tab_info, "INFO")
        self.tabs.addTab(self.tab_error, "ERROR")

        # Add tabs to widget
        self.layout.addWidget(self.tabs, BorderLayout.Center)
        self.setLayout(self.layout)

        self.job = None


    def setJob(self, job):
        self.job = job
        self.initialState()

    def initialState(self):
        self.tab_debug.clear()
        self.tab_error.clear()
        self.tab_info.clear()

    def logsInfo(self, all):
        self.tab_info.clear()
        if not all:
            return
        LOCAL_TIMEZONE = datetime.now(timezone.utc).astimezone().tzinfo

        for m in all:
            t = str(datetime.strptime(
                m['time'], "%Y-%m-%dT%H:%M:%S.%f").replace(tzinfo=timezone.utc).astimezone(
                LOCAL_TIMEZONE))
            msg = "{} - {} - {}\n".format(t, m['worker_type'], m['message'])
            self.tab_info.insertPlainText(msg)
        self.tab_info.verticalScrollBar().setValue(
            self.tab_info.verticalScrollBar().maximum())

    def logsError(self, all):
        self.tab_error.clear()
        if not all:
            return
        LOCAL_TIMEZONE = datetime.now(timezone.utc).astimezone().tzinfo

        for m in all:
            t = str(datetime.strptime(
                m['time'], "%Y-%m-%dT%H:%M:%S.%f").replace(tzinfo=timezone.utc).astimezone(
                LOCAL_TIMEZONE))
            msg = "{} - {} - {}\n".format(t, m['worker_type'], m['message'])
            self.tab_error.insertPlainText(msg)
        self.tab_error.verticalScrollBar().setValue(
            self.tab_error.verticalScrollBar().maximum())

    def logsDebug(self, all):
        self.tab_debug.clear()
        if not all:
            return
        LOCAL_TIMEZONE = datetime.now(timezone.utc).astimezone().tzinfo

        for m in all:
            t = str(datetime.strptime(
                m['time'], "%Y-%m-%dT%H:%M:%S.%f").replace(tzinfo=timezone.utc).astimezone(
                LOCAL_TIMEZONE))
            msg = "{} - {} - {}\n".format(t, m['worker_type'], m['message'])
            self.tab_debug.insertPlainText(msg)
        self.tab_debug.verticalScrollBar().setValue(
            self.tab_debug.verticalScrollBar().maximum())

    def loadLogs(self, vals):
        if not self.job or not 'created' in self.job:
            return
        async = getAsync()
        async.loadJobLogs(self.logsInfo, self.job['id'], 'INFO', vals)
        async.loadJobLogs(self.logsError, self.job['id'], 'ERROR', vals)
        async.loadJobLogs(self.logsDebug, self.job['id'], 'DEBUG', vals)

class JobOverviewWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.parent = parent
        layout = QVBoxLayout()

        stats_numbers_widget = QWidget()
        stats_numbers_layout = QHBoxLayout()
        self.number_stats = {
            'parking.checker.places_free': NumberWidget(self, 'Free places', 'avg', ['min', 'max'],
                                                        style={
                                                            'num_format': '{0:.0f}',
                                                            'title': 'font-weight: bold; color: rgb(153,255,153); font-size: 60pt;',
                                                            'subtitle': 'font-weight: bold; font-size: 20pt;',
                                                            'numtitle': 'font-weight: bold; color: rgb(153,255,153); font-size: 8pt;',
                                                            'width': 500,
                                                            'height': 250
                                                        }
                                                        ),
            'calculated.occupied': NumberWidget(self, 'Occupied', 'avg', [],
                                                style={
                                                    'num_format': '{0:.0f}',
                                                    'title': 'font-weight: bold; color: rgb(255,153,153); font-size: 60pt;',
                                                    'subtitle': 'font-weight: bold; font-size: 20pt;',
                                                    'numtitle': 'font-weight: bold; color: rgb(255,153,153); font-size: 8pt;',
                                                    'width': 500,
                                                    'height': 250
                                                }
                                                ),
        }
        for x in self.number_stats:
            stats_numbers_layout.addWidget(self.number_stats[x])

        stats_numbers_layout.addStretch(1)
        stats_numbers_widget.setLayout(stats_numbers_layout)
        layout.addWidget(stats_numbers_widget)

        small_stats_numbers_widget = QWidget()
        small_stats_numbers_layout = QHBoxLayout()
        small_number_stats = {
            'collector.job.logs.INFO': NumberWidget(self, 'Infos', 'count', [],
                                                    style={
                                                        'num_format': '{0:.0f}',
                                                        'title': 'font-weight: bold; color: rgb(153,153,153); font-size: 32pt;',
                                                        'subtitle': 'font-weight: bold; font-size: 12pt;',
                                                        'numtitle': 'font-weight: bold; color: rgb(153,153,153); font-size: 8pt;',
                                                        'width': 300,
                                                        'height': 150
                                                    }
                                                    ),
            'collector.job.logs.ERROR': NumberWidget(self, 'Problems', 'count', [],
                                                     style={
                                                         'num_format': '{0:.0f}',
                                                         'title': 'font-weight: bold; color: rgb(153,153,153); font-size: 32pt;',
                                                         'subtitle': 'font-weight: bold; font-size: 12pt;',
                                                         'numtitle': 'font-weight: bold; color: rgb(153,153,153); font-size: 8pt;',
                                                         'width': 300,
                                                         'height': 150
                                                     }
                                                     ),
            'parking.image_input.bytes_read': NumberWidget(self, 'Data read', 'sum', [],
                                                           style={
                                                               'num_format': '{0:.2f} MB',
                                                               'title': 'font-weight: bold; color: rgb(153,153,153); font-size: 22pt;',
                                                               'subtitle': 'font-weight: bold; font-size: 12pt;',
                                                               'numtitle': 'font-weight: bold; color: rgb(153,153,153); font-size: 8pt;',
                                                               'width': 350,
                                                               'height': 150,
                                                               'multi': 1024 * 1024
                                                           }
                                                           )

        }
        for x in small_number_stats:
            small_stats_numbers_layout.addWidget(small_number_stats[x])
            self.number_stats[x] = small_number_stats[x]

        small_stats_numbers_layout.addStretch(1)
        small_stats_numbers_widget.setLayout(small_stats_numbers_layout)
        layout.addWidget(small_stats_numbers_widget)

        layout.addStretch(1)
        # layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)
        self.prec = None
        self.vals = None
        self.job = None


    def setJob(self, job):
        self.job = job
        self.initialState()

    def initialState(self):
        for x in self.number_stats:
            widget = self.number_stats[x]
            widget.clear()

    def calcOccupied(self, all, prec, op):
        if not all or not prec:
            return
        occup = []
        for x in range(len(all[prec]['parking.checker.places_all'][op])):
            all_v = all[prec]['parking.checker.places_all'][op][x]
            free_v = all[prec]['parking.checker.places_free'][op][x]
            if not all_v or not free_v:
                occup.append(None)
            else:
                occup.append(all_v - free_v)
        all[prec]['calculated.occupied'] = {
            op: occup
        }

    def statsLoaded(self, all):
        if not all:
            return
        self.calcOccupied(all, self.prec, 'avg')
        for stat_name in sorted(all[self.prec]):
            if not stat_name in self.number_stats:
                continue
            widget = self.number_stats[stat_name]
            widget.setStat(all[self.prec][stat_name], self.prec)

    def loadStats(self, prec, vals):
        self.prec = prec
        self.vals = vals
        job = self.parent.getJob()
        if not job or not 'created' in job:
            return
        async = getAsync()
        async.loadJobStats(self.statsLoaded, job['id'], prec, vals)



class JobStatsWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.parent = parent
        self.layout = QVBoxLayout()

        scroll = QtGui.QScrollArea()
        stats_all = QWidget()
        stats_all_layout = QVBoxLayout()

        self.stats = {
            'parking.checker.places_free': (StatsWidget(self, 'Free places'), ['avg', 'min', 'max']),
            'parking.checker.places_all': (StatsWidget(self, 'All places count'), ['max']),
            'parking.checker.check_place.time': (StatsWidget(self, 'Place check time (s)'), ['avg', 'min', 'max']),
            'parking.checker.check_image.time': (
            StatsWidget(self, 'Whole image check time (s)'), ['avg', 'min', 'max']),
            # 'parking.notifier.mqtt_messages_sent': StatsWidget(self,'Počet zaslaných mqtt správ')
        }
        for x in self.stats:
            stats_all_layout.addWidget(self.stats[x][0])
        stats_all.setLayout(stats_all_layout)

        scroll.setWidget(stats_all)
        scroll.setWidgetResizable(True)
        # scroll.setFixedHeight(400)

        self.layout.addWidget(scroll)
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)

        self.palette = {
            'avg': (153, 255, 255),
            'count': (255, 255, 153),
            'min': (153, 255, 153),
            'max': (255, 153, 204),
            'sum': (153, 153, 255)
        }
        self.prec = None
        self.vals = None
        self.job = None

    def setJob(self, job):
        self.job = job
        self.initialState()

    def initialState(self):
        for x in self.stats:
            widget = self.stats[x][0]
            widget.clear()


    def convertTime(self, times):
        if not times:
            return []
        LOCAL_TIMEZONE = datetime.now(timezone.utc).astimezone().tzinfo
        rt = []
        for t in times:
            rt.append(time.mktime(datetime.strptime(t, "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc).astimezone(
                LOCAL_TIMEZONE).timetuple()))
        return rt

    def withoutNones(self, time_vals, vals):
        rt_vals = []
        rt_times = []
        for x in range(len(vals)):
            if not vals[x] is None:
                rt_vals.append(vals[x])
                rt_times.append(time_vals[x])
        return rt_times, rt_vals

    def statsLoaded(self, all):
        if not all:
            return
        for stat_name in sorted(all[self.prec]):
            if not stat_name in self.stats:
                continue
            widget = self.stats[stat_name][0]
            time = all[self.prec][stat_name]['time']
            time = self.convertTime(time)
            widget.setXRange(time[0], time[-1])

            # min = self.min( all[prec][stat_name]['min'])
            # max = self.min( all[prec][stat_name]['max'])
            # widget.setYRange(min, max)
            ops = self.stats[stat_name][1]
            for op in ops:
                x, y = self.withoutNones(time, all[self.prec][stat_name][op])
                widget.plot(x, y, op, self.palette[op])

    def loadStats(self, prec, vals):
        self.prec = prec
        self.vals = vals
        job = self.parent.getJob()
        if not job or not 'created' in job:
            return
        async = getAsync()
        async.loadJobStats(self.statsLoaded, job['id'], prec, vals)