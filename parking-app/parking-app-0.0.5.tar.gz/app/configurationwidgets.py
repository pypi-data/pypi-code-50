from abc import abstractmethod
import json
from datetime import datetime

import cv2
import numpy as np
import requests
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import *
from requests.auth import *
import pyqtgraph as pg

from app.imagewidgets import JobImageWidget, JobImageFilesDialog
from app.utils import *
from app.borderlayout import *
import matplotlib.image as mpimg
import mimetypes
from app.asnc import AsyncComunicator, getAsync

pg.setConfigOptions(imageAxisOrder='row-major')

class Configuration(QMainWindow):

    def __init__(self, parent, title, width, height, job_step_type):
        super().__init__()
        self.parent = parent
        self.setWindowModality(Qt.ApplicationModal)
        self.title = title
        self.setWindowTitle(self.title.format(''))
        self.left = 0
        self.top = 0
        self.width = width
        self.height = height
        self.setGeometry(self.left, self.top, self.width, self.height)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        # centerPoint = mainWindow().geometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.main_widget = QWidget()
        self.job_step_type = job_step_type
        self.job = None
        top_tabs = QTabWidget()
        top_tabs.addTab(self.main_widget, 'Configuration')
        self.raw = QTextEdit(parent)
        self.raw.setReadOnly(True)
        self.raw.setLineWrapMode(QTextEdit.NoWrap)
        top_tabs.addTab(self.raw, "Raw")
        top_tabs.currentChanged.connect(self.onTabChange)

        self.setCentralWidget(top_tabs)
        self.setContentsMargins(QMARGIN)

    def getConfiguration(self):
        if not self.job:
            return None
        if not 'required_workers' in self.job:
            self.job['required_workers'] = [
                {
                    "worker_type": self.job_step_type,
                    "configuration": {
                    }
                }
            ]
        worker = None
        for wrk in self.job['required_workers']:
            if wrk['worker_type'] == self.job_step_type:
                worker = wrk
                break
        if not worker:
            worker = {
                "worker_type": self.job_step_type,
                "configuration": {
                }
            }
            self.job['required_workers'].append(worker)
        return worker['configuration']

    def removeConfiguration(self):
        if not self.job:
            return
        if not 'required_workers' in self.job:
            return
        found = None
        for wrk in self.job['required_workers']:
            if wrk['worker_type'] == self.job_step_type:
                found = wrk
                break
        if found:
            self.job['required_workers'].remove(found)

    def configure(self, job):
        self.job = job
        self.setWindowTitle(self.title.format(job['name']))

    def ensureGet(self, cfg, varname, editname, default_val):
        if not varname in cfg:
            cfg[varname] = default_val
        editname.setText(str(cfg[varname]))

    def ensureSet(self, cfg, varname, editname, is_float = False):
        if is_float:
            cfg[varname] = float(editname.text())
        else:
            cfg[varname]  = editname.text()

    @abstractmethod
    def saveConfiguration(self):
        pass

    def onTabChange(self, int_t):
        if int_t > 0:
            self.saveConfiguration()
            cfg = self.getConfiguration()
            self.raw.clear()
            self.raw.insertPlainText(json.dumps(cfg, indent=4, sort_keys=True))


class ConfigurationArchive(Configuration):

    def __init__(self, parent, job_step_type):
        super().__init__(parent, 'Archive configuration - {}', 400, 200, job_step_type)
        self.parent = parent

        layout = QVBoxLayout()
        self.archiveStrategy = QComboBox()
        self.archiveStrategy.addItem('all')
        self.archiveStrategy.addItem('delete')
        self.archiveStrategy.addItem('changes')
        layout.addWidget(self.archiveStrategy)
        desc = QLabel()
        desc.setText('Archive strategy - what to do with data in every cycle\nall - keep all on disk (for 1 day)\n'
                     'delete - always delete (just send notifications)\nchanges - keep only changes for 1 day\n')
        layout.addWidget(desc)
        layout.addStretch(1)
        self.main_widget.setLayout(layout)

    def configure(self, job):
        super().configure(job)
        cfg = self.getConfiguration()
        if cfg != None:
            if not 'archive_strategy' in cfg:
                cfg['archive_strategy'] = 'changes'
            self.archiveStrategy.setCurrentText(cfg['archive_strategy'])

    def closeEvent(self, event):
        pass

    def saveConfiguration(self):
        text = self.archiveStrategy.currentText()
        cfg = self.getConfiguration()
        cfg['archive_strategy'] = text

class ConfigurationImageInput(Configuration):

    def __init__(self, parent, job_step_type):
        super().__init__(parent, 'Camera input - {}', 1200, 500, job_step_type)
        self.parent = parent

        top_layout = QHBoxLayout()
        self.image_widget = JobImageWidget(self)
        top_layout.addWidget(self.image_widget)

        url_label = QLabel('Url')
        user_label = QLabel('Username')
        pass_label = QLabel('Password')
        delay_label = QLabel('Delay (sec.)')

        self.url_edit = QLineEdit()
        self.user_edit = QLineEdit()
        self.pass_edit = QLineEdit()
        self.pass_edit.setEchoMode(QLineEdit.Password)
        self.delay_edit = QLineEdit()
        delay_validator = QDoubleValidator(0.001, 3600, 3)
        self.delay_edit.setValidator(delay_validator)

        stretch_widget = QWidget()
        stretch = QVBoxLayout()

        attribs_widget = QWidget()
        grid = QGridLayout()
        grid.setSpacing(MARGIN)
        etuples = [
            (url_label, self.url_edit),
            (user_label, self.user_edit),
            (pass_label, self.pass_edit),
            (delay_label, self.delay_edit),
        ]
        for x in range(len(etuples)):
            grid.addWidget(etuples[x][0], x + 1, 0)
            grid.addWidget(etuples[x][1], x + 1, 1)

        attribs_widget.setLayout(grid)
        stretch.addWidget(attribs_widget)
        stretch.addStretch(1)
        self.status_messages = QTextEdit(parent)
        self.status_messages.setReadOnly(True)
        self.status_messages.setLineWrapMode(QTextEdit.NoWrap)
        stretch.addWidget(self.status_messages)
        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout()
        self.test_button = QPushButton('Start test')
        self.test_button.setCheckable(True)
        self.test_button.clicked.connect(self.test_cam)
        buttons_layout.addWidget(self.test_button)
        buttons_layout.addStretch(1)
        # set_map_button = QPushButton('Set as map')
        # set_map_button.clicked.connect(self.set_map)
        # buttons_layout.addWidget(set_map_button)
        buttons_widget.setLayout(buttons_layout)

        stretch.addWidget(buttons_widget)
        stretch_widget.setLayout(stretch)

        top_layout.addWidget(stretch_widget)
        self.main_widget.setLayout(top_layout)

        self.communicator = AsyncComunicator(None, self.status_messages)

        self.timer = QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.test_cam_reload)
        self.timer_stop()


    def configure(self, job):
        if self.job and self.job['id'] != job['id']:
            self.status_messages.clear()
            self.image_widget.clearImage()
        super().configure(job)
        cfg = self.getConfiguration()
        if cfg != None:
            self.ensureGet(cfg, 'img_url', self.url_edit, 'https://')
            self.ensureGet(cfg, 'img_url_username', self.user_edit, '')
            self.ensureGet(cfg, 'img_url_pass', self.pass_edit, '')
            self.ensureGet(cfg, 'delay_sec', self.delay_edit, 30)

    def timer_stop(self):
        self.timer.stop()
        self.test_button.setText('Start test')
        self.test_button.setStyleSheet("background-color:rgb(153,255,153); color:rgb(0,0,0);")
        self.test_button.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))

    def timer_start(self):
        self.timer.start(1000)
        self.test_button.setText('Stop test')
        self.test_button.setStyleSheet("background-color:rgb(255,153,153); color:rgb(0,0,0);")
        self.test_button.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaStop))

    def closeEvent(self, event):
        self.timer_stop()
        self.saveConfiguration()

    def saveConfiguration(self):
        cfg = self.getConfiguration()
        if cfg != None:
            self.ensureSet(cfg, 'img_url', self.url_edit)
            self.ensureSet(cfg, 'img_url_username', self.user_edit)
            self.ensureSet(cfg, 'img_url_pass', self.pass_edit)
            self.ensureSet(cfg, 'delay_sec', self.delay_edit, True)

    def test_cam(self, start):
        if start:
            self.timer_start()
        else:
            self.timer_stop()

    # def grab_data(self):
    #     try:
    #         img_url = self.url_edit.text()
    #         img_url_user = self.user_edit.text()
    #         img_url_pass = self.pass_edit.text()
    #         self.status_messages.append('{} Connecting to {} as {} with {}'.format(str(datetime.now().isoformat()), img_url, img_url_user, img_url_pass))
    #         response = requests.get(img_url, auth=HTTPDigestAuth(img_url_user, img_url_pass), verify=False)
    #         self.status_messages.append('{} Response status is {} - {}'.format(str(datetime.now().isoformat()), response.status_code, response.reason))
    #         if response.status_code == 200:
    #             btra = bytearray(response.content)
    #             return cv2.imdecode(np.asarray(btra), 1), len(btra)
    #     except Exception as e:
    #         self.status_messages.append(
    #             '{} error {}'.format(str(datetime.now().isoformat()), e))
    #     return None, 0

    def test_data_loaded(self, result_tuple):
        img, bytes_count = result_tuple
        if bytes_count > 0:
            img_url = self.url_edit.text()
            self.image_widget.setImage(img, img_url, str(datetime.now().isoformat()))
            self.save_cv_img(img)

    def save_cv_img(self, cv_img):
        try:
            tmpname = local_img_name(self.job['id'])
            cv2.imwrite(tmpname, cv_img)
        except Exception as e:
            print(e)

    def test_cam_reload(self):
        self.communicator.grabData(self.test_data_loaded, self.url_edit.text(), self.user_edit.text(), self.pass_edit.text() )




    # def set_map(self):
    #     self.parent.setTemporaryImageMap(self.image_widget.get_cv_img())

class ConfigurationRegions(Configuration):

    def __init__(self, parent, job_step_type):
        super().__init__(parent, 'Regions configuration - {}', 1200, 800, job_step_type)
        self.parent = parent

        layout = BorderLayout()
        selected_region_widget = QWidget()
        selected_region_layout = QGridLayout()
        selected_region_layout.addWidget(QLabel('Selected area'), 1,0)
        self.selected_area_name = QLineEdit()
        selected_region_layout.addWidget(self.selected_area_name, 1,1)
        selected_region_layout.addWidget(QLabel('Coordinates'), 2,0)
        self.selected_area_coords = QLabel()
        selected_region_layout.addWidget(self.selected_area_coords, 2,1)

        buttons = QWidget()
        set_background_button = QPushButton("Select background map")
        set_background_button.clicked.connect(self.set_background_map)
        delete_button = QPushButton("Delete region")
        delete_button.clicked.connect(self.roiDelete)
        edit_button = QPushButton("Save name")
        edit_button.clicked.connect(self.roiNameChanged)
        hbox = QHBoxLayout()
        hbox.addWidget(edit_button)
        hbox.addWidget(delete_button)
        hbox.addStretch(1)
        hbox.addWidget(set_background_button)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        buttons.setLayout(vbox)
        selected_region_layout.addWidget(buttons,3, 1)
        selected_region_widget.setLayout(selected_region_layout)
        layout.addWidget(selected_region_widget, BorderLayout.North)
        self.gv = pg.GraphicsLayoutWidget(parent=self)
        self.gv_view = self.gv.addPlot(lockAspect=True)
        self.gv_view.invertY()

        layout.addWidget(self.gv, BorderLayout.Center)
        self.main_widget.setLayout(layout)
        self.blue_pen = pg.mkPen(color='b', width=3)
        self.counter = 0
        self.rois = []
        self.rois_texts = []
        self.region_selected = None



    def configure(self, job):
        super().configure(job)
        cfg = self.getConfiguration()
        self.gv_view.clear()
        self.rois.clear()
        self.rois_texts.clear()
        self.counter = 0
        if cfg != None:
            self.ima = pg.ImageItem()
            self.ima.mouseClickEvent = self.mouseClickArea
            self.gv_view.addItem(self.ima)
            if 'map' in cfg:
                jdir = local_job_dir(self.job['id'])
                ffname = os.path.join(jdir, cfg['map'])
                if not os.path.exists(ffname):
                    self.downloadUsedMap(cfg['map'])
                else:
                    self.setUsedMap(ffname)

            if not 'regions' in cfg:
                cfg['regions'] = []
            self.regions = cfg['regions']
            if not self.regions:
                return
            for item in self.regions:
                roi = pg.PolyLineROI([], pen=self.blue_pen, closed=True, removable=True)
                roi.setState(item['roi'])
                roi.setAcceptedMouseButtons(Qt.LeftButton)
                roi.sigRemoveRequested.connect(self.removeRoi)
                roi.sigRegionChangeFinished.connect(self.roiChanged)
                roi.sigClicked.connect(self.roiClicked)
                self.gv_view.addItem(roi)
                text = pg.TextItem()
                # text.setAnchor(-10)
                text.setText(str(item['name']), color='w')
                text.setParentItem(roi)
                rect = roi.boundingRect()
                text.setPos(rect.x(), rect.y())
                self.rois.append(roi)
                self.rois_texts.append(text)
                self.counter += 1


    def closeEvent(self, event):
        # transform points - adjust pos to 0,0
        cfg = self.getConfiguration()
        self.regions = cfg['regions']
        if not self.regions:
            return
        for item in self.regions:
            pos0, pos1 = item['roi']['pos']
            if pos0 == 0 and pos1 == 0:
                continue
            points = item['roi']['points']
            points2 = []
            for p0, p1 in points:
                p0 += pos0
                p1 += pos1
                points2.append((p0,p1))
            item['roi']['pos'] = (0,0)
            item['roi']['points'] = points2


    def saveConfiguration(self):
        pass


    def mouseClickArea(self, event):
        mouse_x = round(event.pos().x())
        mouse_y = round(event.pos().y())
        if event.double():
            # print( 'Click at {} {} '.format(mouse_x,mouse_y))
            pen = pg.mkPen(color='b', width=3)
            roi = pg.PolyLineROI(
                [[mouse_x, mouse_y], [mouse_x + 40, mouse_y], [mouse_x + 40, mouse_y + 40], [mouse_x, mouse_y + 40]],
                pen=pen, closed=True, removable=True)
            roi.setAcceptedMouseButtons(Qt.LeftButton)
            roi.sigRemoveRequested.connect(self.removeRoi)
            roi.sigRegionChangeFinished.connect(self.roiChanged)
            roi.sigClicked.connect(self.roiClicked)
            self.gv_view.addItem(roi)
            #
            name = 'place_{}'.format(self.counter+1)
            text = pg.TextItem()
            # # text.setAnchor(-10)
            text.setText(name, color='w')
            text.setParentItem(roi)
            text.setPos(mouse_x, mouse_y)
            #
            rois_data_item = {
                'name':name,
                'roi': roi.saveState()
                # ,'rect': self.rect(roi)
            }

            self.regions.append(rois_data_item)
            self.rois.append(roi)
            self.rois_texts.append(text)
            #
            # self.table.cellChanged.disconnect(self.tableChanged)
            # self.table.setData(self.regions)
            # self.table.cellChanged.connect(self.tableChanged)
            self.counter += 1

    def removeRoi(self, roi):
        idx = self.rois.index(roi)
        self.rois.pop(idx)
        self.regions.pop(idx)
        self.rois_texts.pop(idx)
        self.gv_view.removeItem(roi)
        return True


    def roiChanged(self, roi):
        idx = self.rois.index(roi)
        self.regions[idx]['roi'] = roi.saveState()

    def roiClicked(self, roi):
        # print(roi)
        idx = self.rois.index(roi)
        if self.region_selected and self.region_selected in self.regions:
            pidx = self.regions.index(self.region_selected)
            self.rois_texts[pidx].setColor('w')
        self.region_selected = self.regions[idx]
        self.selected_area_name.setText(str(self.region_selected['name']))
        self.selected_area_coords.setText(str(self.region_selected['roi']))
        self.rois_texts[idx].setColor('y')

    def roiNameChanged(self):
        if not self.region_selected or not self.region_selected in self.regions:
            return
        idx = self.regions.index(self.region_selected)
        self.regions[idx]['name'] = self.selected_area_name.text()
        self.rois_texts[idx].setText(self.selected_area_name.text(), color='w')

    def roiDelete(self):
        if not self.region_selected or not self.region_selected in self.regions:
            return
        idx = self.regions.index(self.region_selected)
        roi = self.rois[idx]
        self.rois.pop(idx)
        self.regions.pop(idx)
        self.rois_texts.pop(idx)
        self.gv_view.removeItem(roi)

    def set_background_map(self):
        dialog = JobImageFilesDialog(self, self.job['id'])
        dialog.exec_()
        if dialog.selected_file:
            cfg = self.getConfiguration()
            if cfg:
                cfg['map'] = dialog.selected_file
                self.configure(self.job)


    def setUsedMap(self, ffname):
        if ffname and os.path.exists(ffname):
            self.map_data = mpimg.imread(ffname)
            self.ima.setImage(self.map_data)

    def downloadUsedMap(self, mapfile):
        asnc = getAsync()
        asnc.download_used_map(self.setUsedMap, self.job['id'], mapfile)


class ConfigurationMqttNotifier(Configuration):

    def __init__(self, parent, job_step_type):
        super().__init__(parent, 'Mqtt notifier - {}', 800, 500, job_step_type)
        self.parent = parent

        mqtt_camera_name_label = QLabel('mqtt_camera_name')
        mqtt_user_name_label = QLabel('mqtt_user_name')
        mqtt_api_key_label = QLabel('mqtt_api_key')
        mqtt_url_label = QLabel(' mqtt_url')
        mqtt_device_model_label = QLabel('mqtt_device_model')
        mqtt_urn_prefix_label = QLabel('mqtt_urn_prefix')
        mqtt_data_topic_label = QLabel('mqtt_data_topic')

        self.mqtt_camera_name_edit = QLineEdit()
        self.mqtt_user_name_edit = QLineEdit()
        self.mqtt_api_key_edit =QLineEdit()
        self.mqtt_url_edit =QLineEdit()
        self.mqtt_device_model_edit = QLineEdit()
        self.mqtt_urn_prefix_edit = QLineEdit()
        self.mqtt_data_topic_edit = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(MARGIN)
        etuples = [
            (mqtt_camera_name_label, self.mqtt_camera_name_edit),
            (mqtt_user_name_label,  self.mqtt_user_name_edit),
            (mqtt_api_key_label, self.mqtt_api_key_edit),
            (mqtt_url_label, self.mqtt_url_edit),
            (mqtt_device_model_label, self.mqtt_device_model_edit),
            (mqtt_urn_prefix_label, self.mqtt_urn_prefix_edit),
            (mqtt_data_topic_label, self.mqtt_data_topic_edit),
        ]
        for x in range(len(etuples)):
            grid.addWidget(etuples[x][0], x + 1, 0)
            grid.addWidget(etuples[x][1], x + 1, 1)

        self.main_widget.setLayout(grid)



    def configure(self, job):
        super().configure(job)
        cfg = self.getConfiguration()
        if cfg != None:
            self.ensureGet(cfg, 'mqtt_camera_name', self.mqtt_camera_name_edit, 'camera:__location__')
            self.ensureGet(cfg, 'mqtt_user_name', self.mqtt_user_name_edit, 'json+device')
            self.ensureGet(cfg, 'mqtt_api_key', self.mqtt_api_key_edit, '')
            self.ensureGet(cfg, 'mqtt_url', self.mqtt_url_edit, 'liveobjects.orange-business.com')
            self.ensureGet(cfg, 'mqtt_device_model', self.mqtt_device_model_edit, 'parkingCameraSpot_v1_0')
            self.ensureGet(cfg, 'mqtt_urn_prefix', self.mqtt_urn_prefix_edit, 'urn:lo:nsid:mqtt:')
            self.ensureGet(cfg, 'mqtt_data_topic', self.mqtt_data_topic_edit, 'dev/data')


    def closeEvent(self, event):
        self.saveConfiguration()

    def saveConfiguration(self):
        cfg = self.getConfiguration()
        if cfg != None:
            self.ensureSet(cfg, 'mqtt_camera_name', self.mqtt_camera_name_edit)
            self.ensureSet(cfg, 'mqtt_user_name', self.mqtt_user_name_edit)
            self.ensureSet(cfg, 'mqtt_api_key', self.mqtt_api_key_edit)
            self.ensureSet(cfg, 'mqtt_url', self.mqtt_url_edit)
            self.ensureSet(cfg, 'mqtt_device_model', self.mqtt_device_model_edit)
            self.ensureSet(cfg, 'mqtt_urn_prefix', self.mqtt_urn_prefix_edit)
            self.ensureSet(cfg, 'mqtt_data_topic', self.mqtt_data_topic_edit)


class ConfigurationMetricsCollector(Configuration):

    def __init__(self, parent, job_step_type):
        super().__init__(parent, 'Metrics collector configuration - {}', 400, 200, job_step_type)
        self.parent = parent

        layout = QVBoxLayout()
        # self.archiveStrategy = QComboBox()
        # self.archiveStrategy.addItem('all')
        # self.archiveStrategy.addItem('delete')
        # self.archiveStrategy.addItem('changes')
        # layout.addWidget(self.archiveStrategy)
        desc = QLabel()
        desc.setText('Collect and save metrics')
        layout.addWidget(desc)
        layout.addStretch(1)
        self.main_widget.setLayout(layout)

    def configure(self, job):
        super().configure(job)

    def closeEvent(self, event):
        self.saveConfiguration()

    def saveConfiguration(self):
        cfg = self.getConfiguration()
        cfg['dummy'] = 'dummy'
