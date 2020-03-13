import os
import json
from datetime import timezone

from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QMessageBox, QWidget, QVBoxLayout, QTreeView, QListView, QListWidget, QListWidgetItem, \
    QGridLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QCheckBox
from PyQt5.QtGui import QImage, QStandardItemModel, QStandardItem, QColor
import pyqtgraph as pg
import matplotlib.image as mpimg

from app.borderlayout import BorderLayout
from app.asnc import getAsync, AsyncComunicator
from app.utils import get_job_step_configuration, local_job_dir
from app.parking_dataset import ParkingDataset


class CorrectorMainWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        # Interpret image data as row-major instead of col-major
        self.parent = parent

        self.layout = BorderLayout(margin=5)

        self.job_treeview = QTreeView(self)
        self.job_treeview.setHeaderHidden(True)
        self.job_treeview.clicked.connect(self.job_selected)

        self.layout.addWidget(self.job_treeview, BorderLayout.West)

        self.job_widget = CorrectorJobWidget(self)
        self.layout.addWidget(self.job_widget, BorderLayout.Center)

        self.setLayout(self.layout)
        self.jobs = []

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
            self.job = item.data()
            self.job_widget.setJob(self.job)

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
            return
        self.jobs = rt_items
        self.reload_list()
        # self.job_edit_widget.updateJob()


    def reloadJobs(self):
        try:
            asnc = getAsync()
            asnc.list_jobs(self.jobsLoaded)
        except Exception as e:
            self.parent.status_message(str(e))

    def getVals(self):
        return self.parent.getVals()

    def getPrec(self):
        return self.parent.getPrec()


class CorrectorJobWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        # Interpret image data as row-major instead of col-major
        self.parent = parent

        self.layout = BorderLayout(margin=5)


        self.items_list = QListWidget()
        self.items_list.clicked.connect(self.job_detection_selected)
        self.layout.addWidget(self.items_list, BorderLayout.West)

        self.job_corrector = CorrectorRegions(self)
        self.layout.addWidget(self.job_corrector, BorderLayout.Center)

        self.setLayout(self.layout)
        self.job = None

    def setJob(self, job):
        self.job = job
        self.job_corrector.setJob(self.job)
        self.reloadList()


    def setJobFiles(self, items):
        self.items_list.clear()
        count = 0
        for item in items:
            if 'entry' in item and str(item['entry']).endswith('.json'):
                i = QListWidgetItem(os.path.splitext(item['entry'])[0])
                i.setData( Qt.UserRole, item)
                # if count > 20:
                #    i.setBackground(QColor(153,255,153))
                self.items_list.addItem(i)
                count += 1

    def reloadList(self):
        if not self.job:
            return
        asnc = getAsync()
        asnc.loadJobFiles(self.setJobFiles, self.job['id'])


    def job_detection_selected(self, idx):
        item  = self.items_list.currentItem()
        self.job_corrector.setDetection(item.text())


class CorrectorRegions(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.parent = parent

        layout = BorderLayout()
        selected_region_widget = QWidget()
        selected_region_layout = QGridLayout()
        selected_region_layout.addWidget(QLabel('Selected area'), 1,0)
        self.selected_area_name = QLineEdit()
        selected_region_layout.addWidget(self.selected_area_name, 1,1)
        selected_region_layout.addWidget(QLabel('Occupied'), 2,0)
        self.regionOccupied = QCheckBox()
        selected_region_layout.addWidget(self.regionOccupied, 2,1)

        buttons = QWidget()
        correct_button = QPushButton("Correct")
        correct_button.clicked.connect(self.roiCorrect)
        save_regions_button = QPushButton('Save corrected regions')
        save_regions_button.clicked.connect(self.saveRegions)
        hbox = QHBoxLayout()
        hbox.addWidget(correct_button)
        hbox.addStretch(1)
        hbox.addWidget(save_regions_button)
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
        self.setLayout(layout)
        self.blue_pen = pg.mkPen(color='b', width=3)
        self.red_pen = pg.mkPen(color='r', width=3)
        self.green_pen = pg.mkPen(color='g', width=3)
        self.rois = []
        self.rois_texts = []
        self.region_selected = None
        self.job = None
        self.detection_name = None
        self.corrected_regions = {}
        self.roi_selected = None
        self.parking_dataset = ParkingDataset('Z:\datasets\parking')



    def setJob(self, job):
        self.job = job
        self.detection_name = None
        cfg = get_job_step_configuration(self.job, 'parking_checker')
        self.gv_view.clear()
        self.rois.clear()
        self.rois_texts.clear()
        if cfg != None:
            self.ima = pg.ImageItem()
            self.gv_view.addItem(self.ima)
            if 'map' in cfg:
                jdir = local_job_dir(self.job['id'])
                self.used_img_file = os.path.join(jdir, cfg['map'])
                if not os.path.exists(self.used_img_file):
                    self.downloadUsedMap(cfg['map'])
                else:
                    self.setUsedMap(self.used_img_file)

            if not 'regions' in cfg:
                cfg['regions'] = []
            self.regions = cfg['regions']
            if not self.regions:
                return
            for item in self.regions:
                roi = pg.PolyLineROI([], pen=self.blue_pen, closed=True, removable=False)
                roi.setState(item['roi'])
                roi.setAcceptedMouseButtons(Qt.LeftButton)
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


    def getRegionStatus(self, region_name):
        for item in self.detections:
            if item['name'] == region_name:
                return str(item['occupancy']).lower() == 'true'
        return False

    def roiClicked(self, roi):
        # print(roi)
        idx = self.rois.index(roi)
        if self.region_selected and self.region_selected in self.regions:
            pidx = self.regions.index(self.region_selected)
            # self.rois_texts[pidx].setColor('w')
        self.region_selected = self.regions[idx]
        self.selected_area_name.setText(str(self.region_selected['name']))
        self.regionOccupied.setChecked(self.getRegionStatus(str(self.region_selected['name'])))
        self.roi_selected = roi
        # self.rois_texts[idx].setColor('y')

    def roiCorrect(self):
        if not self.region_selected or not self.region_selected in self.regions:
            return
        rname = str(self.region_selected['name'])
        occu = str(self.regionOccupied.isChecked()).lower()
        occuItem = {
            'name': rname,
            'occupancy': occu,
        }
        self.corrected_regions[rname] = occuItem
        pidx = self.regions.index(self.region_selected)
        self.rois_texts[pidx].setColor('y')
        if self.roi_selected:
            pen = self.blue_pen
            if occu == 'false':
                pen = self.green_pen
            else:
                pen = self.red_pen
            self.roi_selected.setPen(pen)
        # self.regions[idx]['name'] = self.selected_area_name.text()
        # self.rois_texts[idx].setText(self.selected_area_name.text(), color='w')


    def saveRegions(self):
        if not self.job or len(self.corrected_regions.keys()) == 0:
            return

        detf, imf = self.parking_dataset.add_src_entry(
            job_id=self.job['id'],
            regions_map=self.regions,
            detections_map=list(self.corrected_regions.values()),
            img_src_file=self.used_img_file)
        QMessageBox.information(self, "Corrections saved", f"Corrections saved to\n detections_file={detf}\n image_file={imf}",
                                  QMessageBox.Ok)

    def setUsedMap(self, ffname):
        if ffname and os.path.exists(ffname):
            self.used_img_file = ffname
            self.map_data = mpimg.imread(ffname)
            self.ima.setImage(self.map_data)

    def downloadUsedMap(self, mapfile):
        asnc = getAsync()
        asnc.download_used_map(self.setUsedMap, self.job['id'], mapfile)



    def detectionLoaded(self, ffname):
        if not ffname:
            return
        with open(ffname,'r') as fp:
            cfg_detection = json.load(fp)
        cfg = get_job_step_configuration(self.job, 'parking_checker')
        self.gv_view.clear()
        self.rois.clear()
        self.rois_texts.clear()
        self.corrected_regions = {}
        self.roi_selected = None
        if cfg != None:
            self.ima = pg.ImageItem()
            self.gv_view.addItem(self.ima)
            jdir = local_job_dir(self.job['id'])
            fname = '{}.jpg'.format(self.detection_name)
            self.used_img_file = os.path.join(jdir,fname)
            if not os.path.exists(self.used_img_file):
                asnc = getAsync()
                asnc.download_file( self.setUsedMap, self.job['id'],  'd',
                             fname)
            else:
                self.setUsedMap(self.used_img_file)

            if not 'regions' in cfg:
                cfg['regions'] = []
            self.regions = cfg['regions']
            if not self.regions:
                return
            self.detections = cfg_detection['detections']
            if not self.detections:
                return
            for x in range(len(self.regions)):
                item = self.regions[x]
                checked = self.detections[x]
                pen = self.blue_pen
                if 'occupancy' in checked and checked['occupancy'] == 'false':
                    pen = self.green_pen
                else:
                    pen = self.red_pen

                roi = pg.PolyLineROI([], pen=pen, closed=True, removable=False)
                roi.setState(item['roi'])
                roi.setAcceptedMouseButtons(Qt.LeftButton)
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


    def setDetection(self, detection_name):
        if not self.job:
            return
        self.detection_name = detection_name
        jdir = local_job_dir(self.job['id'])
        fname = '{}.json'.format(self.detection_name)
        ffname = os.path.join(jdir, fname)
        if not os.path.exists(ffname):
            asnc = getAsync()
            asnc.download_file(self.detectionLoaded, self.job['id'], 'd',
                                fname)
        else:
            self.detectionLoaded(ffname)


