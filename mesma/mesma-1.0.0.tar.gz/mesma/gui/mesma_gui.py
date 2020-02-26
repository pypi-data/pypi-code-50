# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------------
| Date                : June 2018
| Copyright           : (C) 2018 by Ann Crabbé (KU Leuven)
| Email               : ann.crabbe@kuleuven.be
|
| This program is free software; you can redistribute it and/or modify it under the terms of the GNU
| General Public License as published by the Free Software Foundation; either version 3 of the
| License, or any later version.
| ----------------------------------------------------------------------------------------------------------------------
"""
import os
import sys
import time
import datetime
import numpy as np
from copy import deepcopy
from qgis.gui import QgsFileWidget
from qgis.utils import iface
from qgis.PyQt.uic import loadUi
from qgis.PyQt.QtGui import QColor
from qgis.PyQt.QtCore import QModelIndex, Qt
from qgis.PyQt.QtWidgets import QDialog, QHBoxLayout, QFrame, QGroupBox, QFileDialog, QTreeWidgetItem, QDialogButtonBox
from mesma.io import EmittingStream
from mesma.io.imports import import_library, detect_reflectance_scale_factor, import_image
from mesma.io.operators import MesmaOperator, GUIProgressBar
from mesma.gui.logo_gui import LogoWidget
from mesma.scripts.mesma import MesmaModels
from mesma.sitepackages.hubdc.applier import Applier, ApplierInputRaster, ApplierOutputRaster
from mesma.gui.mesma_visualisation_gui import ModelVisualizationWidget


class MesmaWidget(QDialog):
    """ Main GUI widget to set up the MESMA environment (library, constraints, image, ...) """

    def __init__(self):
        super(MesmaWidget, self).__init__()
        loadUi(os.path.join(os.path.dirname(__file__), 'mesma.ui'), self)
        sys.stdout = EmittingStream(self.tabWidget)
        sys.stderr = EmittingStream(self.tabWidget)

        # Logo
        self.logoLayout.addWidget(LogoWidget(parent=self.logoWidget))

        # Library
        self.browseLibrary.lineEdit().setReadOnly(True)
        self.browseLibrary.fileChanged.connect(self._library_browse)
        self.classDropDown.currentIndexChanged.connect(self._get_class_from_list)
        self.modelButton.clicked.connect(self._model_selection)

        # Input and output image
        self.browseImage.lineEdit().setReadOnly(True)
        self.browseImage.lineEdit().setPlaceholderText('You can select more than one image...')
        self.browseImage.setStorageMode(QgsFileWidget.GetMultipleFiles)
        self.browseImage.fileChanged.connect(self._image_browse)

        self.browseOut.lineEdit().setReadOnly(True)
        self.browseOut.lineEdit().setPlaceholderText('The MESMA result (models) ...')
        self.browseOut.setStorageMode(QgsFileWidget.SaveFile)

        # Shade spectrum
        self.browseShade.lineEdit().setReadOnly(True)
        self.browseShade.fileChanged.connect(self._shade_browse)

        # Open in QGIS?
        try:
            iface.activeLayer
        except AttributeError:
            self.openInQGIS.setChecked(False)
            self.openInQGIS.setDisabled(True)

        # Run mesma, (re-)store settings
        self.OKClose.button(QDialogButtonBox.Ok).setText("Run")
        self.OKClose.accepted.connect(self._run_mesma)
        self.OKClose.rejected.connect(self.close)
        self.store.clicked.connect(self._save_settings)
        self.restore.clicked.connect(self._restore_settings)

        # Mesma widget variables
        self.image_path = None
        self.image_nb = None
        self.library = None
        self.library_name = None
        self.metadata = None
        self.model_object = None
        self.shade = None

        # project timestamp
        self.timestamp = datetime.datetime.fromtimestamp(time.time())

    def __del__(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def _library_browse(self, path):
        """ When the users browses for a library, set the reflectance scale factor and the metadata drop down list.
        :param path: the absolute path to the Spectral Library
        """
        if path == '':
            return

        self.classDropDown.clear()

        try:
            library = import_library(path)
        except Exception as e:
            print(str(e), file=sys.stderr)
            self.browseLibrary.setFilePath('')
            return

        self.library = np.array([np.array(x.values()['y'])[np.where(x.bbl())[0]] for x in library.profiles()]).T
        self.metadata = np.asarray([x.attributes() for x in library.profiles()], dtype=object)
        self.library_name = os.path.basename(path)

        # set the library reflectance scale factor
        self.libraryScaleValue.setValue(detect_reflectance_scale_factor(self.library))

        # add header to drop down
        self.classDropDown.addItems(['Select ...'] + library.fieldNames())

    def _get_class_from_list(self, index):
        """ Initiate MesmaModels with the selected metadata header and display a summary of the initial setup.
        :param index: the index of the metadata headers
        """
        if index in [-1, 0]:
            self.model_object = None
            self.modelSummary.clear()
            return

        self.model_object = MesmaModels()
        self.model_object.setup(self.metadata[:, index-1])

        self.modelSummary.clear()
        self.modelSummary.insertPlainText(self.model_object.summary())

    def _model_selection(self):
        """ Open the MesmaModelsWidget when the user presses the 'change' button, to fine tune the model selection. """
        if self.model_object is None:
            return

        new_model_object = deepcopy(self.model_object)
        x = MesmaModelsWidget(new_model_object)
        x.exec_()
        if x.result() == QDialog.Accepted:
            self.model_object = new_model_object
            self.modelSummary.clear()
            self.modelSummary.insertPlainText(self.model_object.summary())

    def _image_browse(self, input_path):
        """ When the users browses for an image, set the reflectance scale, max number of residual bands and output name
        :param input_path: the absolute path to the image(s)
        """
        if input_path == '':
            return

        paths = QgsFileWidget.splitFilePaths(input_path)

        all_scales = []
        all_nb_bands = []

        # get details of each image
        for path in paths:
            try:
                image = import_image(path)      # check images are all readable
                all_scales.append(detect_reflectance_scale_factor(image))
                all_nb_bands.append(image.shape[0])
                del image
            except Exception as e:
                self.image_path = None
                self.browseImage.setFilePath('')
                print(str(e), file=sys.stderr)
                return

        # set the image reflectance scale value
        if len(set(all_scales)) == 1:
            self.imageScaleValue.setValue(all_scales[0])
        else:
            print('The images have different scale reflectance values. Cannot process. ', file=sys.stderr)
            self.image_path = None
            self.browseImage.setFilePath('')
            return

        # set the max number of residual bands
        if len(set(all_nb_bands)) == 1:
            self.image_nb = all_nb_bands[0]
            self.maxBandsValue.setMaximum(all_nb_bands[0])
        else:
            print('The images have a different number of bands. Cannot process.', file=sys.stderr)
            self.image_path = None
            self.browseImage.setFilePath('')
            return
        self.image_path = paths

        # set default output name(s)
        output = []
        dt_string = self.timestamp.strftime('%Y%m%dT%H%M%S')
        for path in paths:
            path_no_extension = os.path.splitext(path)[0]
            output.append(path_no_extension + '_mesma_' + dt_string)

        self.browseOut.lineEdit().setText(', '.join(output))

        if len(self.image_path) > 1:
            self.browseOut.setFileWidgetButtonVisible(False)
        else:
            self.browseOut.setFileWidgetButtonVisible(True)

    def _shade_browse(self, path):
        """ When the users browses for a shade spectrum, set the reflectance scale factor.
        :param path: the absolute path to the Spectral Library
        """

        if path == '':
            return

        try:
            spectral_library = import_library(path)
        except Exception as e:
            print(str(e), file=sys.stderr)
            self.browseShade.setFilePath('')
            return

        self.shade = np.array([np.array(x.values()['y'])[np.where(x.bbl())[0]] for x in spectral_library.profiles()]).T

        # shade can only be one spectrum
        if self.shade.shape[1] > 1:
            print("Library can only have one spectrum.", file=sys.stderr)
            self.shade = None
            self.browseShade.setFilePath('')
            return

        # set the shade reflectance scale factor
        self.shadeScaleValue.setValue(detect_reflectance_scale_factor(self.shade))

    def _save_settings(self):
        """ Store the MESMA settings as a text file. """

        file_name = QFileDialog.getSaveFileName(parent=self, caption='Save settings as text file',
                                                filter='Text files (*.txt);;All files (*)')[0]
        if file_name == '':
            return

        store_string = 'MESMA Settings: \n \n'
        store_string += '{}\n'.format(self.browseLibrary.lineEdit().text())
        store_string += '{}\n'.format(self.classDropDown.currentIndex())

        # read the constraints
        constraints = [-9999, -9999, -9999, -9999, -9999, -9999, -9999]
        if self.minFracCheck.isChecked():
            constraints[0] = self.minFracValue.value()
        if self.maxFracCheck.isChecked():
            constraints[1] = self.maxFracValue.value()
        if self.minShadeCheck.isChecked():
            constraints[2] = self.minShadeValue.value()
        if self.maxShadeCheck.isChecked():
            constraints[3] = self.maxShadeValue.value()
        if self.maxRMSECheck.isChecked():
            constraints[4] = self.maxRMSEValue.value()
        if self.residualsCheck.isChecked():
            constraints[5] = self.maxThresValue.value()
            constraints[6] = self.maxBandsValue.value()

        store_string += '{}\n'.format(', '.join(map(str, constraints)))
        store_string += '{}\n'.format(self.browseImage.lineEdit().text())
        store_string += '{}\n'.format(self.browseOut.lineEdit().text())
        store_string += '{}\n'.format(self.openInQGIS.isChecked())
        store_string += '{}\n'.format(self.libraryScaleValue.value())
        store_string += '{}\n'.format(self.fusionValue.value())
        store_string += '{}\n'.format(self.browseShade.lineEdit().text())
        store_string += '{}\n'.format(self.shadeScaleValue.value())
        store_string += '{}\n'.format(self.imageScaleValue.value())
        store_string += '{}\n'.format(self.createResidualImage.isChecked())
        store_string += '{}\n'.format(self.spectralWeighingCheck.isChecked())
        store_string += '{}\n'.format(self.bandSelectionCheck.isChecked())
        store_string += '{}\n'.format(self.correlationThreshold.value())
        store_string += '{}\n'.format(self.correlationDecrease.value())
        store_string += self.model_object.save()

        with open(file_name, 'w') as text_file:
            text_file.write(store_string)

    def _restore_settings(self):
        """ Restore the MESMA settings from a text file. """

        file_name = QFileDialog.getOpenFileName(parent=self, caption='Select text file with settings',
                                                filter='Text files (*.txt);;All files (*)')[0]
        if file_name == '':
            return

        with open(file_name) as text_file:
            settings = text_file.read()

        settings = settings.split(sep='\n')

        self.browseLibrary.setFilePath(settings[2])
        self._library_browse(settings[2])
        self.classDropDown.setCurrentIndex(int(settings[3]))
        self._get_class_from_list(int(settings[3]))
        constraints = np.array(settings[4].split(', ')).astype(np.float)
        if constraints[0] == -9999:
            self.minFracCheck.setChecked(False)
        else:
            self.minFracCheck.setChecked(True)
            self.minFracValue.setValue(constraints[0])
        if constraints[1] == -9999:
            self.maxFracCheck.setChecked(False)
        else:
            self.maxFracCheck.setChecked(True)
            self.maxFracValue.setValue(constraints[1])
        if constraints[2] == -9999:
            self.minShadeCheck.setChecked(False)
        else:
            self.minShadeCheck.setChecked(True)
            self.minShadeValue.setValue(constraints[2])
        if constraints[3] == -9999:
            self.maxShadeCheck.setChecked(False)
        else:
            self.maxShadeCheck.setChecked(True)
            self.maxShadeValue.setValue(constraints[3])
        if constraints[4] == -9999:
            self.maxRMSECheck.setChecked(False)
        else:
            self.maxRMSECheck.setChecked(True)
            self.maxRMSEValue.setValue(constraints[4])
        if constraints[5] == -9999:
            self.residualsCheck.setChecked(False)
        else:
            self.residualsCheck.setChecked(True)
            self.maxThresValue.setValue(constraints[5])
            self.maxBandsValue.setValue(int(constraints[6]))

        self.browseImage.lineEdit().setText(settings[5])
        self._image_browse(settings[5])
        self.browseOut.lineEdit().setText(settings[6])

        self.openInQGIS.setChecked(settings[7] == 'True')
        self.libraryScaleValue.setValue(int(settings[8]))
        self.fusionValue.setValue(float(settings[9]))
        if settings[9] == '':
            self.shadeCheck.setChecked(False)
            self.shade = None
        else:
            self.shadeCheck.setChecked(True)
            self.browseShade.lineEdit().setText(settings[10])
            self._shade_browse(settings[10])
            self.shadeScaleValue.setValue(int(settings[11]))

        self.imageScaleValue.setValue(int(settings[12]))
        self.createResidualImage.setChecked(settings[13] == 'True')
        self.spectralWeighingCheck.setChecked(settings[14] == 'True')
        self.bandSelectionCheck.setChecked(settings[15] == 'True')
        self.correlationThreshold.setValue(float(settings[16]))
        self.correlationDecrease.setValue(float(settings[17]))

        levels_yn = settings[19].split(sep=', ')
        for level, state in enumerate(levels_yn):
            self.model_object.select_level(state == 'True', level)
            if level >= 2:
                classes_yn = settings[19 + level][7:].split(sep=', ')
                for index, state2 in enumerate(classes_yn):
                    self.model_object.select_class(state2 == 'True', index, level)

        for line in settings[20 + len(levels_yn):-1]:
            level = int(line[0])
            models_yn = line[7:].split(sep=', ')
            for index, state in enumerate(models_yn):
                self.model_object.select_model(state == 'True', index, level)

        self.modelSummary.clear()
        self.modelSummary.insertPlainText(self.model_object.summary())

    def _run_mesma(self):
        """ Read all parameters and pass them on to the MESMA Applier class 'Mesma'. """

        # Do a lot of checks before running MESMA
        if self.image_path is None:
            print('Choose one ore more images.', file=sys.stderr)
            return
        if self.library is None:
            print('Choose a spectral library.', file=sys.stderr)
            return
        if self.model_object is None:
            print('Choose a class from the spectral library metadata.', file=sys.stderr)
            return

        lut = self.model_object.return_look_up_table()
        if not lut:
            print('Choose at least one model.', file=sys.stderr)
            return

        if self.image_nb != self.library.shape[0]:
            print('The image and library have different number of bands (' + str(self.image_nb) + ' and ' +
                  str(self.library.shape[0]) + '). MESMA not possible.', file=sys.stderr)
            return

        if self.shade is not None and self.shade.size != 0 and self.shade.shape[0] != self.library.shape[0]:
            print('The library and shade spectrum have different number of bands. MESMA not possible.', file=sys.stderr)
            return

        if self.shade is not None:
            self.shade = self.shade/self.shadeScaleValue.value()

        # read the constraints
        constraints = [-9999, -9999, -9999, -9999, -9999, -9999, -9999]
        if self.minFracCheck.isChecked():
            constraints[0] = self.minFracValue.value()
        if self.maxFracCheck.isChecked():
            constraints[1] = self.maxFracValue.value()
        if self.minShadeCheck.isChecked():
            constraints[2] = self.minShadeValue.value()
        if self.maxShadeCheck.isChecked():
            constraints[3] = self.maxShadeValue.value()
        if self.maxRMSECheck.isChecked():
            constraints[4] = self.maxRMSEValue.value()
        if self.residualsCheck.isChecked():
            constraints[5] = self.maxThresValue.value()
            constraints[6] = self.maxBandsValue.value()

        output_files = self.browseOut.filePath().split(sep=', ')

        # band selection/spectral weighing cannot be combined with a residuals image or residual constraint
        if self.spectralWeighingCheck.isChecked() and self.residualsCheck.isChecked():
            print('Spectral Weighing cannot be combined with a constraint on the residuals. Please uncheck.',
                  file=sys.stderr)
            return
        if self.bandSelectionCheck.isChecked() and self.residualsCheck.isChecked():
            print('Band Selection cannot be combined with a constraint on the residuals. Please uncheck.',
                  file=sys.stderr)
            return
        if self.spectralWeighingCheck.isChecked() and self.createResidualImage.isChecked():
            print('Spectral Weighing cannot be combined with a residuals output image. Please uncheck.',
                  file=sys.stderr)
            return
        if self.bandSelectionCheck.isChecked() and self.createResidualImage.isChecked():
            print('Band Selection cannot be combined with a residuals output image. Please uncheck.', file=sys.stderr)
            return

        # set up the applier for each image
        for image, out in zip(self.image_path, output_files):
            applier = Applier()
            applier.controls.setProgressBar(GUIProgressBar(q_progress_bar=self.progressBar))
            applier.inputRaster.setRaster(key='raster', value=ApplierInputRaster(filename=image))
            applier.outputRaster.setRaster(key='models', value=ApplierOutputRaster(filename=out))
            applier.outputRaster.setRaster(key='fractions', value=ApplierOutputRaster(filename=out + '_fractions'))
            applier.outputRaster.setRaster(key='rmse', value=ApplierOutputRaster(filename=out + '_rmse'))

            if self.createResidualImage.isChecked():
                applier.outputRaster.setRaster(key='residuals', value=ApplierOutputRaster(filename=out + '_residuals'))

            # apply MESMA
            applier.apply(operatorType=MesmaOperator,
                          image_scale=self.imageScaleValue.value(),
                          library=self.library/self.libraryScaleValue.value(),
                          look_up_table=lut,
                          em_per_class=self.model_object.em_per_class,
                          unique_classes=self.model_object.unique_classes,
                          constraints=constraints,
                          shade_spectrum=self.shade,
                          fusion_value=self.fusionValue.value(),
                          use_band_weighing=self.spectralWeighingCheck.isChecked(),
                          use_band_selection=self.bandSelectionCheck.isChecked(),
                          bands_selection_values=(self.correlationThreshold.value(),
                                                  self.correlationDecrease.value()),
                          lib_name=self.library_name,
                          residual_image=self.createResidualImage.isChecked())

            if self.openInQGIS.isChecked():
                if self.createResidualImage.isChecked():
                    iface.addRasterLayer(applier.outputRaster.raster(key='residuals').filename(), "Residuals")
                iface.addRasterLayer(applier.outputRaster.raster(key='rmse').filename(), "RMSE")
                iface.addRasterLayer(applier.outputRaster.raster(key='fractions').filename(), "Fractions")
                iface.addRasterLayer(applier.outputRaster.raster(key='models').filename(), "Models")

                widget = ModelVisualizationWidget()
                widget.openImage([applier.outputRaster.raster(key='models').filename()])
                widget.show()


class MesmaModelsWidget(QDialog):
    """ GUI widget to allow the user to fine-tune the model selection. """

    def __init__(self, model_object):
        """
        :param model_object: a MesmaModels object that has been initialised and set up.
        """
        super(MesmaModelsWidget, self).__init__()
        loadUi(os.path.join(os.path.dirname(__file__), 'mesmaModels.ui'), self)

        # Logo
        logo_layout = QHBoxLayout()
        logo_layout.addWidget(LogoWidget(parent=self.logoWidget))
        self.logoWidget.setLayout(logo_layout)

        # make the model object a class variable
        assert isinstance(model_object, MesmaModels)
        self.model_object = model_object

        # Initialise the widget with the correct checkboxes and correct content
        self._setup()

        # Show the preliminary total on screen
        self.total.setDigitCount(self.model_object.max_digits())
        self.display()

    def _setup(self):
        """ Set up the GUI. Dynamically add a LevelWidget for each complexity level. """
        n_classes = self.model_object.n_classes

        self.scrollArea.setFrameShape(QFrame.NoFrame)
        horizontal_layout = self.widget.layout()

        for i in np.arange(2, n_classes + 2):
            level_widget = LevelWidget(self.model_object, i, parent=self.widget)
            horizontal_layout.addWidget(level_widget)

        self.widget.setFixedSize(self.widget.sizeHint())

    def display(self):
        """ Handle the LCD display. """
        total = self.model_object.total()
        if total < 20000:
            colour = QColor(50, 205, 50)
        elif total < 100000:
            colour = QColor(255, 140, 0)
        else:
            colour = QColor(255, 0, 0)

        self.total.display("{:,}".format(total))
        palette = self.total.palette()
        palette.setColor(palette.WindowText, colour)
        self.total.setPalette(palette)


class LevelWidget(QGroupBox):
    """ Part of the MesmaModelsWidget. Handle all models of a given complexity level (e.g. all 3-EM Models). """

    def __init__(self, model_object, level, parent=None):
        """
        :param model_object: a MesmaModels object that has been initialised and set up.
        :param level: the complexity level of the MesmaModels object to which this particular widget belongs
        :param parent: the MesmaModelsWidget in which this LevelWidget is called
        """
        super(LevelWidget, self).__init__(parent)
        loadUi(os.path.join(os.path.dirname(__file__), 'complexityWidget.ui'), self)

        self.model_object = model_object
        self.level = level

        self.setCheckable(True)
        self._update_header()
        self.setChecked(model_object.level_yn[level])
        self.clicked.connect(self._select_level)

        self.classArea.clicked.connect(self._select_class)
        self.modelArea.clicked.connect(self._select_model)

        self._draw_class_list()
        self._draw_model_list()

    # noinspection PyTypeChecker
    def _draw_class_list(self):
        """ Draws a check-list with all possible classes """
        unique_classes = self.model_object.unique_classes
        n_em_per_class = self.model_object.n_em_per_class
        classes_yn = self.model_object.class_per_level[self.level]

        self.classArea.clear()
        self.classArea.header().hide()

        parent = QTreeWidgetItem(self.classArea)
        parent.setText(0, 'Select (all) classes')
        parent.setData(0, Qt.UserRole, -1)
        parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
        parent.setFlags(parent.flags() & ~Qt.ItemIsSelectable)
        parent.setExpanded(True)

        for e, em in enumerate(unique_classes):
            child = QTreeWidgetItem(parent)
            child.setText(0, '{} ({:,})'.format(em,  n_em_per_class[e]).replace(',', ' '))
            child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
            child.setFlags(child.flags() & ~Qt.ItemIsSelectable)
            if classes_yn[e]:
                child.setCheckState(0, Qt.Checked)
            else:
                child.setCheckState(0, Qt.Unchecked)

    # noinspection PyTypeChecker
    def _draw_model_list(self):
        """ Draws a check-list with all possible class-models """

        if self.level in self.model_object.class_models.keys():
            class_models = self.model_object.class_models[self.level]
            class_models_yn = self.model_object.class_models_yn[self.level]
        else:
            class_models = []
            class_models_yn = []

        self.modelArea.clear()

        if class_models:
            self.modelArea.header().hide()

            parent = QTreeWidgetItem(self.modelArea)
            parent.setText(0, 'Select (all) class-models')
            parent.setData(0, Qt.UserRole, -1)
            parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            parent.setFlags(parent.flags() & ~Qt.ItemIsSelectable)
            parent.setExpanded(True)

            for e, em in enumerate(class_models):
                child = QTreeWidgetItem(parent)
                child.setText(0, '{} ({:,})'.format('-'.join(self.model_object.unique_classes[np.array(em)]),
                                                    self.model_object.total_per_class_model(em)).replace(',', ' '))
                child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                child.setFlags(child.flags() & ~Qt.ItemIsSelectable)
                if class_models_yn[e]:
                    child.setCheckState(0, Qt.Checked)
                else:
                    child.setCheckState(0, Qt.Unchecked)

    def _select_level(self, state: bool):
        """ Select/deselect a complete complexity level. When deselecting, the current state is saved.

        :param state: set True for select and False for deselect
        """
        self.model_object.select_level(state, self.level)
        self._draw_model_list()
        self._update_header()
        self.parent().parent().parent().parent().display()

    def _select_class(self, q_index: QModelIndex):
        """ Select/deselect a class. When deselecting, the class is removed from all class-models in the lower box.

        :param q_index: QModelIndex object belonging to the selected class
        """
        header = q_index.data(role=Qt.UserRole)
        index = q_index.row()

        state = q_index.data(role=Qt.CheckStateRole)
        if state == 2:
            state = 1

        if header == -1:
            for i in np.arange(self.model_object.n_classes):
                self.model_object.select_class(state, i, self.level)
        else:
            self.model_object.select_class(state, index, self.level)

        self._draw_model_list()
        self._update_header()
        self.parent().parent().parent().parent().display()

    def _select_model(self, q_index: QModelIndex):
        """ Select/deselect a single class-model.

        :param q_index: QModelIndex object belonging to the selected class-model
        """
        header = q_index.data(role=Qt.UserRole)
        index = q_index.row()
        state = q_index.data(role=Qt.CheckStateRole)
        if state == 2:
            state = 1

        if header == -1:
            for i in np.arange(len(self.model_object.class_models[self.level])):
                self.model_object.select_model(state, i, self.level)
        else:
            self.model_object.select_model(state, index, self.level)
        self._update_header()
        self.parent().parent().parent().parent().display()

    def _update_header(self):
        """ The total number of models the level header and must be updated after each (de-)selection. """
        lev = self.level
        tot = self.model_object.total_per_level(self.level)
        if lev == 2:
            text = '{}-EM Models = {} class + shade ({:,})'.format(lev, lev - 1, tot).replace(',', ' ')
        else:
            text = '{}-EM Models = {} classes + shade ({:,})'.format(lev, lev - 1, tot).replace(',', ' ')

        self.setTitle(text)


def _run():
    from qgis.core import QgsApplication
    app = QgsApplication([], True)
    app.initQgis()

    z = MesmaWidget()
    z.show()

    app.exec_()


if __name__ == '__main__':
    _run()
