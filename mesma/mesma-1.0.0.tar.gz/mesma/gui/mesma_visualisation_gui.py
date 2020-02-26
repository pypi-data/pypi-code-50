# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------------
| Date                : September 2018
| Copyright           : (C) 2018 by Benjamin Jakimow (HU Berlin) and Ann Crabbé (KU Leuven)
| Email               : benjamin.jakimow@geo.hu-berlin.de, ann.crabbe@kuleuven.be
|
| This program is free software; you can redistribute it and/or modify it under the terms of the GNU
| General Public License as published by the Free Software Foundation; either version 3 of the
| License, or any later version.
| ----------------------------------------------------------------------------------------------------------------------
"""
import os
import sys
import copy
import pickle
import statistics
import collections
import numpy as np
from osgeo import gdal
from qgis.core import Qgis, QgsRasterRenderer, QgsRectangle, QgsRasterBlockFeedback, QgsRasterBlock, QgsProject
from qgis.core import QgsProviderRegistry, QgsMapLayerProxyModel, QgsRasterLayer
from qgis.PyQt.Qt import QObject, pyqtSignal, QSize, QFileDialog, QPixmap, QIcon, QAbstractItemModel, QModelIndex, QMenu
from qgis.PyQt.Qt import QVariant, QTreeView, QHeaderView, QCursor, QColorDialog, QSortFilterProxyModel, QRegExp
from qgis.PyQt.Qt import QCloseEvent
from qgis.PyQt.uic import loadUi
from qgis.PyQt.QtGui import QColor
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QMessageBox, QMainWindow
from mesma.io.imports import import_library

MAX_MODELS_SHOWED = 99999  # less models, faster speed
MESMA_CLASS_UNMODELED_VALUE = -1
MESMA_CLASS_NODATA_VALUE = -2
MAX_CLASSES = 32
COLOR_NO_DATA = QColor('white')
COLOR_NO_MODEL = QColor('magenta')
QGIS2NUMPY_DATA_TYPES = {Qgis.Byte: np.byte,
                         Qgis.UInt16: np.uint16,
                         Qgis.Int16: np.int16,
                         Qgis.UInt32: np.uint32,
                         Qgis.Int32: np.int32,
                         Qgis.Float32: np.float32,
                         Qgis.Float64: np.float64,
                         Qgis.CFloat32: np.complex,
                         Qgis.CFloat64: np.complex64,
                         Qgis.ARGB32: np.uint32,
                         Qgis.ARGB32_Premultiplied: np.uint32}
COLORS = [QColor("green"), QColor("yellow"), QColor("lightGray"), QColor("red"), QColor("cyan"), QColor("gray"),
          QColor("darkBlue"), QColor("darkGreen"), QColor("darkYellow"), QColor("black"), QColor("darkRed"),
          QColor("darkCyan"), QColor("darkGray"), QColor("darkMagenta"), QColor("blue")]


class AbstractMesmaModel(object):
    """ Abstract class describing a model and it's features: a color, vector, visibility, name and pixel count. """

    def __init__(self, vector: np.ndarray, color: QColor, name: str, px_count=0):

        assert isinstance(vector, np.ndarray)
        assert vector.ndim == 1
        self._vector = vector

        self._color = QColor('green')
        self._visible = False
        self._name = ''
        self._px_count = 0

        self.setColor(color)
        self.setName(name)
        self.setPxCount(px_count)

    def vector(self) -> np.ndarray:
        """ Get the vector of this AbstractMesmaModel. """
        return self._vector

    def vectorString(self, no_data_string='_', separator=',') -> str:
        """ Get a human readable representation of the underlying vector data.

        :param no_data_string: The string value representing a no data value.
        :param separator: The separator to concatenate the vector values to a string.
        """
        return separator.join([no_data_string if e in [-1, False] else str(e) for e in self._vector])

    def color(self) -> QColor:
        """ Get the color of this AbstractMesmaModel. """
        return self._color

    def setColor(self, color: QColor):
        """ Set the color of this AbstractMesmaModel. """
        if color is not None:
            self._color = color

    def isVisible(self) -> bool:
        """ Get the visibility of this AbstractMesmaModel. """
        return self._visible

    def setVisible(self, b: bool):
        """ Set the visibility of this AbstractMesmaModel. """
        self._visible = b

    def name(self) -> str:
        """ Get the name of this AbstractMesmaModel. """
        return self._name

    def setName(self, name: str):
        """ Set the name of this AbstractMesmaModel. """
        if name is None:
            self._name = self.vectorString()
        else:
            self._name = name

    def pxCount(self) -> int:
        """ Get the pixel count of this AbstractMesmaModel. """
        return int(self._px_count)

    def setPxCount(self, count: int):
        """ Set the pixel count of this AbstractMesmaModel. """
        self._px_count = count

    def matchWithRasterBlock(self, block: np.ndarray) -> np.ndarray:
        """ Check where in the raster block this model can be found. Implement in child class. """
        raise NotImplementedError()

    def numberOfClasses(self) -> int:
        """ Get the total number of classes used in this model, i.e. the number of endmember numbers > -1. """
        return len(self.classIndices())

    def classIndices(self) -> np.ndarray:
        """ Get the class indices of used endmember classes. Implement in child class. """
        raise NotImplementedError()

    def __hash__(self):
        return hash(self.__class__.__name__ + str(self._vector))

    def __repr__(self) -> str:
        return '{}("{}":{})'.format(self.__class__.__name__, self.name(), self.vectorString())

    def __eq__(self, other) -> bool:
        if not isinstance(other, AbstractMesmaModel):
            return False
        else:
            return np.array_equal(self._vector, other._vector)


class MesmaModel(AbstractMesmaModel):
    """ Implementation of AbstractMesmaModel for a MESMA model. e.g. the vector looks like [23,-1,323,3]. """

    def __init__(self, vector: np.ndarray, color: QColor, name: str, px_count=0):
        assert vector.dtype in (np.int64, np.int32, np.int16, np.int8)
        super(MesmaModel, self).__init__(vector, color, name, px_count)

    def classIndices(self) -> np.ndarray:
        """ Get the class indices of used endmember classes, i.e. classes dat do not carry the IGNORED value. """
        return np.where((self._vector != MESMA_CLASS_NODATA_VALUE) * (self._vector != MESMA_CLASS_UNMODELED_VALUE))[0]

    def matchWithRasterBlock(self, block: np.ndarray) -> np.ndarray:
        """ Check where in the raster block this model can be found. """
        n_bands, n_px = block.shape
        vector_block = np.empty((n_bands, n_px), dtype=self._vector.dtype)
        vector_block[:, :] = self._vector.reshape((n_bands, 1))
        return np.all(block == vector_block, axis=0)


class ClassModel(AbstractMesmaModel):
    """ Implementation of AbstractMesmaModel for a CLASS model. e.g. the vector looks like [False,True,True,False]. """

    def __init__(self, vector: np.ndarray, color: QColor, name: str, px_count=0):
        assert vector.dtype == np.bool
        super(ClassModel, self).__init__(vector, color, name, px_count)

    def classIndices(self) -> np.ndarray:
        """ Get the class indices of used endmember classes, i.e. classes that are True. """
        return np.where(self._vector)[0]

    def matchWithRasterBlock(self, block: np.ndarray) -> np.ndarray:
        """ Check where in the raster block this model can be found. """
        n_bands, n_px = block.shape
        vector_block = np.empty((n_bands, n_px), dtype=self._vector.dtype)
        vector_block[:, :] = self._vector.reshape((n_bands, 1))
        return np.all((block != -1) == vector_block, axis=0)


class ClassMembership(ClassModel):
    """ Special case of ClassModel where the vector has only one True value. This does not reference the 2-EM classes,
    but rather all models where this class is used, e.g. GV, GV-WATER, GV-SOIL, GV-WATER-SOIL for 'GV'.
    """

    def __init__(self, vector: np.ndarray, color: QColor, name: str, px_count=0):
        assert vector.dtype == np.bool and np.count_nonzero(vector) <= 1
        super(ClassMembership, self).__init__(vector, color, name, px_count)

    def matchWithRasterBlock(self, block: np.ndarray) -> np.ndarray:
        """ Check where in the raster block this model can be found. """
        n_bands, n_px = block.shape
        result = np.zeros((1, n_px,), dtype=np.bool)
        ones = np.ones((1, n_px,), dtype=np.bool)
        for i in np.where(self._vector):
            result = np.where(block[i, :] != -1, ones, result)
        return result.flatten()

    def vectorString(self, no_data_string='*', separator=',') -> str:
        """ Get a human readable representation of the underlying vector data.

        :param no_data_string: The string value representing a no data value.
        :param separator: The separator to concatenate the vector values to a string.
        """
        return super(ClassMembership, self).vectorString(no_data_string=no_data_string, separator=separator)


class MesmaSummary(QObject):
    """ Provides a summary of all info carried by the MESMA MODELS raster-image. To be used in different kinds of
    QAbstractModel implementations, like MesmaTreeModel and MesmaTableModel. """

    sigLoadingProgress = pyqtSignal(int, int)
    sigSourceWillChange = pyqtSignal(str)
    sigSourceChanged = pyqtSignal(str)

    def __init__(self):
        super(MesmaSummary, self).__init__()

        self._mesma_models = []
        self._class_models = collections.OrderedDict()
        self._class_memberships = collections.OrderedDict()
        self._source = None
        self._class_names = []
        self._spectra_names = np.array([])

    def mesmaModels(self) -> list:
        """" Get a list of all MesmaModels. """
        return self._mesma_models

    def classModels(self) -> list:
        """ Get the list of all ClassModels. """
        return [m for m in self._class_models.keys() if isinstance(m, ClassModel)]

    def classMemberships(self) -> list:
        """ Get a list of all ClassMemberships. """
        return [m for m in self._class_memberships.keys() if isinstance(m, ClassMembership)]

    def source(self):
        """ Return the source. """
        return self._source

    def mesmaModelsByClassModel(self, class_model: ClassModel):
        """
        Get a list of all the MesmaModels of a given ClassModel.

        :param class_model: A ClassModel.
        """
        return self._class_models[class_model]

    def visibleModels(self) -> list:
        """ Get a list of all MesmaModels, ClassModels and ClassMemberships that are visible. """
        models = []
        models += [m for m in self.classMemberships() if m.isVisible()]
        models += [m for m in self.classModels() if m.isVisible()]
        models += [m for m in self.mesmaModels() if m.isVisible()]
        return models

    def usedClassesString(self, model, separator=', ') -> str:
        """ Convert the list of indices of used classes of a MesmaModel to a string with class names. """
        assert isinstance(model, AbstractMesmaModel)
        try:
            return separator.join([self._class_names[c] for c in model.classIndices()])
        except IndexError:
            return "Error"

    def clear(self):
        """" Clear all variables. """
        self._mesma_models.clear()
        self._class_memberships.clear()
        self._class_models.clear()
        self._source = None
        self._class_names.clear()
        self._spectra_names = np.array([])

    def readMesmaModelsImage(self, parent: QMainWindow, path: str, tile_size: QSize = None, testing: bool = False):
        """ Read in the MESMA model raster layer output: MESMA models, Class models, Class Memberships, etc.

        :param parent: the widget calling this function
        :param path: string path pointing to the MESMA models image
        :param tile_size:
        :param testing: set to True in test mode (no popup)
        """

        assert isinstance(path, str)
        if not isinstance(tile_size, QSize):
            tile_size = QSize(128, 128)

        self.sigSourceWillChange.emit(os.path.basename(path))
        self.clear()

        data_set = gdal.Open(path)
        if not isinstance(data_set, gdal.Dataset):
            self.sigSourceChanged.emit(path)
            print('Unable to read "{}".'.format(path), file=sys.stderr)
        if not data_set.GetRasterBand(1).DataType in [gdal.GDT_Int32, gdal.GDT_Byte, gdal.GDT_Int16]:
            self.sigSourceChanged.emit(path)
            print('Raster "{}" is not of type Integer.'.format(path), file=sys.stderr)
        if data_set.RasterCount > MAX_CLASSES:
            self.sigSourceChanged.emit(path)
            print('Raster has more than {} bands/classes. Increase variable MAX_CLASSES.'.format(MAX_CLASSES),
                  file=sys.stderr)
        self._source = path

        # open associated library for spectrum names
        try:
            lib_path = os.path.join(os.path.dirname(path), data_set.GetMetadata('ENVI')['spectral_library'])
        except KeyError:
            lib_path = None
        if not testing :
            if lib_path is None or not os.path.exists(lib_path):
                ans = QMessageBox.question(parent, 'Spectral Library',
                                           'Select the Spectral Library behind this MESMA image for better output.',
                                           buttons=QMessageBox.Yes | QMessageBox.No)
                if ans == QMessageBox.Yes:
                    lib_path, _ = QFileDialog.getOpenFileName(filter='ENVI Spectral Library (*.sli);;All Files (*)')
                    if lib_path != '':
                        spectral_library = import_library(lib_path)
                        self._spectra_names = np.asarray([x.name().strip() for x in spectral_library.profiles()])
                    else:
                        self._spectra_names = None
                else:
                    self._spectra_names = None
            else:
                spectral_library = import_library(lib_path)
                self._spectra_names = np.asarray([x.name().strip() for x in spectral_library.profiles()])
        else:
            self._spectra_names = None

        n_bands = data_set.RasterCount
        ns, nl = data_set.RasterXSize, data_set.RasterYSize

        # set class colors
        ct = data_set.GetRasterBand(1).GetColorTable()  # use class lookup information, if defined
        if isinstance(ct, gdal.ColorTable) and ct.GetCount() >= n_bands:
            class_colors = []
            for i in range(n_bands):
                rgb = ct.GetColorEntry(i)
                class_colors.append(QColor(*rgb))
        else:
            # create own class colors
            class_colors = COLORS[0:n_bands - 1]
            if n_bands > 15:
                class_colors.extend([COLORS[-1]] * (n_bands - 15))
            else:
                class_colors.append(COLORS[-1])  # water is probably at the end
                # newColor = QColor('green')
            # for i in range(n_bands):
            #     classColors.append(newColor)
            #     newColor = self.nextColor(newColor)

        # get the NoDataValues and the ClassMemberships (not yet the pixel_count)
        for b in range(n_bands):
            band = data_set.GetRasterBand(b + 1)
            assert isinstance(band, gdal.Band)

            class_name = band.GetDescription().strip()
            if len(class_name) == 0:
                class_name = 'Class {}'.format(b + 1)
            vector = np.zeros((n_bands,), dtype=np.bool)
            vector[b] = True
            self._class_names.append(class_name)
            class_membership = ClassMembership(vector, class_colors[b], class_name)

            # use self._class_memberships[<class index>] to get <class model>
            # use self._class_memberships[<class model>] to get the list of MESMA models
            self._class_memberships[class_membership] = []
            self._class_memberships[b] = class_membership
            self._class_memberships[class_name] = class_membership

        no_data_vector1 = np.ones((n_bands,), dtype=int) * MESMA_CLASS_NODATA_VALUE
        no_data_vector2 = np.ones((n_bands,), dtype=int) * MESMA_CLASS_UNMODELED_VALUE

        progress_max = max(int(ns / tile_size.width()) * int(nl / tile_size.height()), 1)
        progress_done = 0
        self.sigLoadingProgress.emit(progress_done, progress_max)

        # read unique vectors == unique mesma models
        vectors = dict()
        y0 = 0
        while y0 < nl:
            y1 = min(y0 + tile_size.width(), nl)
            y_size = y1 - y0

            x0 = 0
            while x0 < ns:
                x1 = min(x0 + tile_size.width(), ns)
                x_size = x1 - x0

                data = data_set.ReadAsArray(x0, y0, x_size, y_size)
                data = data.reshape((n_bands, x_size * y_size))
                data = data.astype(int)

                unique_vectors = self.unique_rows(data.transpose())
                for vector in unique_vectors:
                    n_px = np.all(data == vector.reshape(n_bands, 1), axis=0).sum()
                    vector_key = vector.tostring()  # numpy arrays are not hashable. we need a hashable key
                    if vector_key not in vectors.keys():
                        vectors[vector_key] = (vector, n_px)
                    else:
                        v, n = vectors[vector_key]
                        vectors[vector_key] = (vector, n + n_px)

                progress_done += 1
                self.sigLoadingProgress.emit(progress_done, progress_max)
                x0 += x_size
            y0 += y_size

        # create a model object for each vector
        for i, (vector, n_px) in enumerate(vectors.values()):

            if np.array_equal(vector, no_data_vector1):
                vector_name = 'no data pixels'
            elif np.array_equal(vector, no_data_vector2):
                vector_name = 'unclassified'
            elif self._spectra_names is None:
                vector_name = ', '.join([str(x) for x in vector[(vector != MESMA_CLASS_NODATA_VALUE) *
                                                                (vector != MESMA_CLASS_UNMODELED_VALUE)]])
            else:
                vector_name = ', '.join(self._spectra_names[vector[(vector != MESMA_CLASS_NODATA_VALUE) *
                                                                   (vector != MESMA_CLASS_UNMODELED_VALUE)]])
            mesma_model = MesmaModel(vector, color=QColor('grey'), name=vector_name, px_count=n_px)
            self._mesma_models.append(mesma_model)

            class_model_vector = (vector != no_data_vector1) * (vector != no_data_vector2)
            class_model_key = str(class_model_vector)

            class_memberships = [self._class_memberships[c] for c in np.where(class_model_vector)[0]]
            for classMembership in class_memberships:
                assert isinstance(classMembership, ClassMembership)
                # increase count of pixels whose MESMA model uses a spectrum of this class
                classMembership.setPxCount(classMembership.pxCount() + mesma_model.pxCount())
                self._class_memberships[classMembership].append(mesma_model)

            class_model = self._class_models.get(class_model_key)
            if class_model is None:
                class_colors = [m.color() for m in class_memberships]
                if len(class_colors) > 0:
                    r = int(statistics.mean([c.red() for c in class_colors]))
                    g = int(statistics.mean([c.green() for c in class_colors]))
                    b = int(statistics.mean([c.blue() for c in class_colors]))
                    color = QColor(r, g, b, 255)
                else:
                    color = COLOR_NO_MODEL

                assert isinstance(class_model_vector, np.ndarray)
                class_model = ClassModel(class_model_vector, color=color, name=self.usedClassesString(mesma_model))
                self._class_models[class_model] = []
                self._class_models[class_model_key] = class_model
            assert isinstance(class_model, ClassModel)
            class_model.setPxCount(class_model.pxCount() + mesma_model.pxCount())
            mesma_model.setColor(class_model.color())
            self._class_models[class_model].append(mesma_model)

        self.sigSourceChanged.emit(os.path.basename(self._source))

    @staticmethod
    def unique_rows(a, return_index=False, return_inverse=False):
        """ Similar to MATLAB's unique(a, 'rows'), this returns b, i, j where b is the unique rows of a
        and i and j satisfy a = b[i,:] and b = a[i,:]

        Returns i if return_index is True
        Returns j if return_inverse is True """

        a = np.require(a, requirements='C')
        assert a.ndim == 2, "array must be 2-dim'l"

        b = np.unique(a.view([('', a.dtype)] * a.shape[1]),
                      return_index=return_index,
                      return_inverse=return_inverse)

        if return_index or return_inverse:
            return (b[0].view(a.dtype).reshape((-1, a.shape[1]), order='C'),) + b[1:]
        else:
            return b.view(a.dtype).reshape((-1, a.shape[1]), order='C')

    def __iter__(self):
        return iter(self._mesma_models)

    def __len__(self):
        return len(self._mesma_models)

    def __getitem__(self, item):
        return self._mesma_models[item]


class ModelImageRenderer(QgsRasterRenderer):
    """ A raster renderer to colorize the MESMA model output raster. """

    def __init__(self, new_input=None, new_type='MESMAModelRenderer'):
        super(ModelImageRenderer, self).__init__(input=new_input, type=new_type)

        self._models = []
        self._no_data_color = QColor(0, 255, 0, 0)

    def __reduce_ex__(self, protocol):
        return self.__class__, (), self.__getstate__()

    def __getstate__(self):
        dump = pickle.dumps(self.__dict__)
        return dump

    def __setstate__(self, state):
        d = pickle.loads(state)
        self.__dict__.update(d)

    def legendSymbologyItems(self, *args, **kwargs):
        """ Overwritten from parent class. Items for the legend. """
        items = []
        for model in self._models:
            if isinstance(model, ClassMembership):
                items.append(("Class: " + model.vectorString(), QColor(model.color())))
            elif isinstance(model, ClassModel):
                items.append(("Class-model: " + model.vectorString(), QColor(model.color())))
            elif isinstance(model, MesmaModel):
                items.append(("Model: " + model.vectorString(), QColor(model.color())))
        return items

    def setModels(self, models: list):
        """ Sets the MesmaModels to be shown.

        :param models: [list-of-MesmaModels]
        """

        length = None
        for i, model in enumerate(models):
            assert isinstance(model, AbstractMesmaModel)
            if i == 0:
                length = len(model.vector())
            else:
                assert len(model.vector()) == length, 'All model endmember vectors need to have the same length'

        self._models = models

    def block(self, band_nr: int, extent: QgsRectangle, width: int, height: int,
              feedback: QgsRasterBlockFeedback = None):
        """" Overwritten from parent class.

        :param band_nr:
        :param extent:
        :param width:
        :param height:
        :param feedback:
        """

        # see https://github.com/Septima/qgis-hillshaderenderer/blob/master/hillshaderenderer.py
        nb = self.input().bandCount()
        input_missmatch = None
        if len(self._models) == 0:
            input_missmatch = 'No models defined to render pixels for.'
        elif len(self._models[0].vector()) != nb:
            input_missmatch = 'Render settings require raster input of {} bands instead {}.'.format(
                len(self._models[0].endmemberList()), nb)

        if input_missmatch:
            print(input_missmatch, file=sys.stderr)
            output_block = QgsRasterBlock(Qgis.ARGB32_Premultiplied, width, height)

            color_array = np.frombuffer(output_block.data(), dtype=QGIS2NUMPY_DATA_TYPES[output_block.dataType()])
            color_array[:] = self._no_data_color.rgb()
            output_block.setData(color_array.tobytes())
            return output_block

        npx = height * width

        block_data = np.ndarray((nb, height * width), dtype=np.float)
        for b in range(nb):
            band_block = self.input().block(b + 1, extent, width, height)
            assert isinstance(band_block, QgsRasterBlock)
            band_data = np.frombuffer(band_block.data(), dtype=QGIS2NUMPY_DATA_TYPES[band_block.dataType()])
            assert len(band_data) == npx
            # THIS! seems to be a very fast way to convert block data into a numpy array
            block_data[b, :] = band_data

        output_block = QgsRasterBlock(Qgis.ARGB32_Premultiplied, width, height)
        color_array = np.frombuffer(output_block.data(), dtype=QGIS2NUMPY_DATA_TYPES[output_block.dataType()])
        # fill with no-data color
        c = self._no_data_color.rgba()
        color_array[:] = c

        for iModel, model in enumerate(self._models):
            if iModel >= MAX_MODELS_SHOWED:
                break
            assert isinstance(model, AbstractMesmaModel)
            if not model.isVisible():
                continue
            is_match = model.matchWithRasterBlock(block_data)

            color_array[np.where(is_match)[0]] = model.color().rgb()
        output_block.setData(color_array.tobytes())
        return output_block

    def clone(self) -> QgsRasterRenderer:
        """ Overwritten from parent class. """
        r = ModelImageRenderer()
        models = []
        for m in self._models:
            assert isinstance(m, AbstractMesmaModel)
            m2 = copy.copy(m)

            models.append(m2)
        r.setModels(models)
        return r


class MesmaTreeNode(QObject):
    """ Class to describe a single tree node in the MesmaTreeView. """

    def __init__(self, parent_node, model, name=''):
        super(MesmaTreeNode, self).__init__()

        self._parent = None
        self._name = name
        self._children = []
        self._model = None
        self._toolTip = ''

        self.setParentNode(parent_node)
        if isinstance(model, AbstractMesmaModel):
            self._model = model

    def appendChildNodes(self, child_nodes: list):
        """ Add child node(s) to the end of this MesmaTreeNode.

        :param child_nodes: A list of MesmaTreeNodes.
        """
        self.insertChildNodes(self.childCount(), child_nodes)

    def insertChildNodes(self, index: int, child_nodes: list):
        """ Add child node(s) to this MesmaTreeNode at the given index.

        :param index: The index at which to insert the child nodes.
        :param child_nodes: A list of Tree Nodes.
        """
        assert index <= self.childCount()
        if isinstance(child_nodes, MesmaTreeNode):
            child_nodes = [child_nodes]
        assert isinstance(child_nodes, list)
        child_nodes = [l for l in child_nodes if l not in self._children]

        for i, node in enumerate(child_nodes):
            assert isinstance(node, MesmaTreeNode)
            self._children.insert(index + i, node)
            node.setParentNode(self)

    def clearChildNodes(self):
        """ Remove all child nodes from this MesmaTreeNode. """
        self._children = []

    def childNodes(self):
        """ Get the children of this MesmaTreeNode. """
        return self._children[:]

    def childCount(self):
        """ Get the number of children of this MesmaTreeNode. """
        return len(self._children)

    def visibleModels(self) -> list:
        """ Returns a list of visible models, i.e. each ModelInfo from this MesmaTreeNode that got checked. """
        result = []
        if self.childCount() == 0:
            if self.hasModel():
                if self._model.isVisible():
                    result.append(self._model)
        else:
            for child in self._children:
                result.extend(child.visibleModels())
        return result

    def model(self) -> AbstractMesmaModel:
        """ Get the Model of this MesmaTreeNode. """
        return self._model

    def hasModel(self) -> bool:
        """ Return True if this MesmaTreeNode has a model set. """
        return isinstance(self._model, AbstractMesmaModel)

    def parentNode(self):
        """ Get the parent MesmaTreeNode of this MesmaTreeNode. """
        return self._parent

    def setParentNode(self, parent_node):
        """ Set the parent MesmaTreeNode of this MesmaTreeNode. """
        if isinstance(parent_node, MesmaTreeNode):
            self._parent = parent_node
            parent_node.appendChildNodes([self])

    def checkState(self) -> Qt.CheckState:
        """ Get the check state of this MesmaTreeNode. """

        # check the state of the children
        n_unchecked = n_checked = 0
        for node in self._children:
            check_state = node.checkState()
            if check_state == Qt.PartiallyChecked:          # if a child is partially checked, return partially checked
                return Qt.PartiallyChecked
            if check_state == Qt.Checked:
                n_checked += 1
            else:
                n_unchecked += 1
        if n_checked > 0 and n_unchecked > 0:               # if some are checked and some are unchecked: partially
            return Qt.PartiallyChecked
        elif n_checked == 0 and n_unchecked == 0:           # there are no children:
            return Qt.Checked if self._model.isVisible() else Qt.Unchecked
        elif n_unchecked == 0:                              # all are checked
            return Qt.Checked
        else:                                               # all are unchecked
            return Qt.Unchecked

    def setCheckState(self, state: Qt.CheckState):
        """ Set the check state of this MesmaTreeNode (recursively). """
        if self.childCount() == 0:
            if self.hasModel():
                self.model().setVisible(state == Qt.Checked)
        else:
            for child in self._children:
                child.setCheckState(state)

    def icon(self):
        """ Get the icon of this MesmaTreeNode. """
        if self.hasModel():
            pm = QPixmap(QSize(64, 64))
            pm.fill(self._model.color())
            return QIcon(pm)
        else:
            return None

    def toolTip(self) -> str:
        """ Get the tooltip of this MesmaTreeNode. """
        return self._toolTip

    def setToolTip(self, tool_tip: str):
        """ Set the tooltip of this MesmaTreeNode. """
        self._toolTip = tool_tip

    def name(self) -> str:
        """ Get the name of this MesmaTreeNode. """
        return self._name


class MesmaTreeModel(QAbstractItemModel):
    """ Implementation of QAbstractItemModel for a MesmaTreeModel. """

    def __init__(self, model_summary: MesmaSummary, parent=None):
        super(MesmaTreeModel, self).__init__(parent)

        self._root_node = MesmaTreeNode(None, None)
        self._column_names = ['Name', 'Classes', '#px', '#EM']
        self._model_summary = model_summary
        self._model_summary.sigSourceChanged.connect(self._rebuild)
        if self.modelSummary().source() is not None:
            self._rebuild()

    def modelSummary(self):
        """ Get the model summary. """
        return self._model_summary

    def rootNode(self) -> MesmaTreeNode:
        """ Get the root node of this MesmaTreeModel. """
        return self._root_node

    def columnNames(self) -> list:
        """ Get the column names of this MesmaTreeModel. """
        return self._column_names

    def columnName(self, i) -> str:
        """" Get the column name at index i. """
        if isinstance(i, QModelIndex):
            i = i.column()
        return self._column_names[i]

    def _rebuild(self):
        """ Rebuild the Tree from scratch. """
        self.beginResetModel()
        self._root_node.clearChildNodes()

        first_node = MesmaTreeNode(parent_node=self._root_node, model=None, name='Classes')
        for membership in self._model_summary.classMemberships():
            MesmaTreeNode(parent_node=first_node, model=membership, name=membership.name())

        second_node = MesmaTreeNode(parent_node=self._root_node, model=None, name='Class-models')
        for class_model in self._model_summary.classModels():
            class_node = MesmaTreeNode(parent_node=second_node, model=class_model, name=class_model.name())
            mesma_models = self._model_summary.mesmaModelsByClassModel(class_model)
            for mesma_model in mesma_models:
                MesmaTreeNode(parent_node=class_node, model=mesma_model, name=mesma_model.name())

        self.endResetModel()

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole):
        """ Implementation of the QAbstractItemModel function headerData. """
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if len(self._column_names) > section:
                return self._column_names[section]
            else:
                return ''
        else:
            return None

    def parent(self, index):
        """ Get the index of the parent of the given MesmaTreeNode's index.

        :param index: The index of a MesmaTreeNode.
        """
        if not index.isValid():
            return QModelIndex()
        node = self.indexToNode(index)
        if not isinstance(node, MesmaTreeNode):
            return QModelIndex()

        parent_node = node.parentNode()
        if not isinstance(parent_node, MesmaTreeNode):
            return QModelIndex()

        return self.nodeToIndex(parent_node)

    def rowCount(self, parent_index: QModelIndex = QModelIndex()) -> int:
        """ Get the number of child nodes of the given parent.

         :param parent_index: The index of the parent MesmaTreeNode.
         """
        parent_node = self.indexToNode(parent_index)
        return parent_node.childCount() if isinstance(parent_node, MesmaTreeNode) else 0

    def columnCount(self, parent_index: QModelIndex = QModelIndex()) -> int:
        """ Get the number of column names of this MesmaTreeModel. Parameter unused. """
        return len(self._column_names)

    def index(self, row: int, column: int, parent_index: QModelIndex = QModelIndex()):
        """ Get the index of the MesmaTreeNode at the given row and column of the parent MesmaTreeNode.

        :param row: The row of the MesmaTreeNode.
        :param column: The column of the MesmaTreeNode.
        :param parent_index: The index of the parent MesmaTreeNode.
        """
        if parent_index is None:
            parent_node = self._root_node
        else:
            parent_node = self.indexToNode(parent_index)

        if row < 0 or row >= parent_node.childCount():
            return QModelIndex()
        if column < 0 or column >= self.columnCount():
            return QModelIndex()

        if isinstance(parent_node, MesmaTreeNode):
            return self.createIndex(row, column, parent_node.childNodes()[row])
        else:
            return QModelIndex()

    def indexToNode(self, index: QModelIndex) -> MesmaTreeNode:
        """ Get the MesmaTreeNode of an index.

        :param index: The index of the MesmaTreeNode.
        """
        if not index.isValid():
            return self._root_node
        else:
            return index.internalPointer()

    def nodeToIndex(self, node: MesmaTreeNode):
        """ Get the index of a Node.

        :param node: The MesmaTreeNode of which you need an index.
        """
        if node == self._root_node:
            return QModelIndex()
        else:
            parent_node = node.parentNode()
            assert isinstance(parent_node, MesmaTreeNode)
            if node not in parent_node.childNodes():
                return QModelIndex()
            return self.createIndex(parent_node.childNodes().index(node), 0, node)

    def rasterRenderer(self) -> QgsRasterRenderer:
        """ Get a ModelImageRenderer for this MesmaTreeModel. """
        r = ModelImageRenderer(None)
        models = self._root_node.visibleModels()
        r.setModels(models)
        return r

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        """ Implementation of the QAbstractItemModel function data. """

        node = self.indexToNode(index)
        if role == Qt.UserRole:
            return node

        column = index.column()

        column_name = self.columnName(column)

        if role == Qt.DisplayRole:
            if node.hasModel():
                mesma_model = node.model()
                if column_name == 'Name':
                    return mesma_model.name()
                elif column_name == '#EM':
                    return 'n.a.' if isinstance(mesma_model, ClassMembership) else mesma_model.numberOfClasses()
                elif column_name == 'Classes':
                    return self._model_summary.usedClassesString(mesma_model)
                elif column_name == '#px':
                    return mesma_model.pxCount()
            else:
                if column_name == 'Name':
                    return node.name()

        if role == Qt.DecorationRole and column == 0:
            return node.icon()
        if role == Qt.EditRole and column_name == 'Name':
            return node.name()
        if role == Qt.CheckStateRole and column == 0:
            return node.checkState()
        if role == Qt.ToolTipRole:
            return None

        return None

    def setData(self, index: QModelIndex, value: QVariant, role: int = Qt.EditRole):
        """ Implementation of the QAbstractItemModel function setData. """

        node = self.indexToNode(index)
        if role == Qt.UserRole:
            return node

        mesma_model = node.model()
        changed = False

        if index.column() == 0:
            if role == Qt.CheckStateRole:
                assert isinstance(value, int)
                value = Qt.CheckState(value)
                node.setCheckState(value)
                changed = True
            elif role == Qt.DisplayRole and node.hasModel() and isinstance(value, str):
                mesma_model.setName(value)
                changed = True
            elif role == Qt.DecorationRole and node.hasModel() and isinstance(value, QColor):
                mesma_model.setColor(value)
                changed = True

        if changed:
            self.dataChanged.emit(index, index, [role])
            if role == Qt.CheckStateRole:
                parent = node.parentNode()
                if isinstance(parent, MesmaTreeNode):
                    parent_index = self.nodeToIndex(parent)
                    self.dataChanged.emit(parent_index, parent_index, [role])

                idx0 = self.createIndex(0, 0, node)
                idx1 = self.createIndex(node.childCount() - 1, 0, parent)
                self.dataChanged.emit(idx0, idx1, [role])

        return changed

    def flags(self, index: QModelIndex):
        """ Implementation of the QAbstractItemModel function flags. """

        if not index.isValid():
            return Qt.NoItemFlags

        flags = Qt.ItemIsEnabled | Qt.ItemIsSelectable
        if index.column() == 0:
            flags = flags | Qt.ItemIsUserCheckable | Qt.ItemIsEditable
        return flags


class MesmaTreeView(QTreeView):
    """ Implementation of QTreeView for a MesmaTreeView. """

    def __init__(self, parent=None):
        super(MesmaTreeView, self).__init__(parent)

        self._model = None

    def setModel(self, model: QAbstractItemModel):
        """ Overwrite setModel from Parent Class. """
        super(MesmaTreeView, self).setModel(model)
        self._model = model.modelReset.connect(self._resetModel)

    def _resetModel(self):
        parent = QModelIndex()
        for r in range(self.model().rowCount(parent)):
            self.setFirstColumnSpanned(r, parent, True)

        # col 0 interactive
        self.header().setSectionResizeMode(0, QHeaderView.Interactive)
        width = self.header().sectionSize(0)
        self.header().setSectionResizeMode(0, QHeaderView.Interactive)
        self.header().resizeSection(0, width + 40)

    def contextMenuEvent(self, event):
        """ Create the QTreeView Mouse context menu """
        menu = QMenu(self)
        a = menu.addAction('Check Selected')
        a.triggered.connect(lambda: self._setCheckState(Qt.Checked))
        a = menu.addAction('Uncheck Selected')
        a.triggered.connect(lambda: self._setCheckState(Qt.Unchecked))
        a = menu.addAction('Set Color')
        a.triggered.connect(lambda: self._setColor())
        menu.popup(QCursor.pos())

    def _setCheckState(self, check_state):
        """ Check or uncheck the selected rows

        :param check_state: Qt.CheckState
        """

        filter_model = self.model()
        mesma_tree_model = filter_model.sourceModel()

        indices = self.selectionModel().selectedIndexes()
        if len(indices) == 0:
            return
        indices = [filter_model.mapToSource(idx) for idx in indices]
        indices = sorted(indices, key=lambda idx: idx.row())

        b = check_state == Qt.Checked

        for index in indices:
            mesma_model = mesma_tree_model.indexToNode(index).model()
            mesma_model.setVisible(b)
        mesma_tree_model.dataChanged.emit(indices[0], indices[1], [Qt.CheckStateRole])

    def _setColor(self):
        """ Set a new (pixel) color for the selected rows. """

        filter_model = self.model()
        mesma_tree_model = filter_model.sourceModel()

        indices = self.selectionModel().selectedIndexes()
        if len(indices) == 0:
            return
        source_indices = [filter_model.mapToSource(idx) for idx in indices]
        node = mesma_tree_model.indexToNode(source_indices[0])

        if isinstance(node, MesmaTreeNode) and node.hasModel():
            color = node.model().color()
        else:
            return

        if isinstance(color, QColor):
            color = QColorDialog.getColor(initial=color, parent=self, title='Select Color')

        if isinstance(color, QColor):
            b = mesma_tree_model.blockSignals(True)
            for idx in source_indices:
                mesma_tree_model.setData(idx, color, Qt.DecorationRole)
            mesma_tree_model.blockSignals(b)
            mesma_tree_model.dataChanged.emit(source_indices[0], source_indices[-1], [Qt.DecorationRole])


class SortFilterProxyModel(QSortFilterProxyModel):
    """A QSortFilterProxyModel to handle the MesmaTableModel and MesmaTreeModel. """

    def __init__(self, parent=None):
        super(SortFilterProxyModel, self).__init__(parent)
        self._mesma_model = None

    def setSourceModel(self, source_model: QAbstractItemModel):
        """ Implementation of setSourceModel function in parent class. """
        self._mesma_model = source_model
        super(SortFilterProxyModel, self).setSourceModel(source_model)

    def filterAcceptsRow(self, source_row: int, source_parent: QModelIndex):
        """ Implementation of filterAcceptsRow function in parent class. """
        reg = self.filterRegExp()
        assert isinstance(reg, QRegExp)
        if len(reg.pattern()) == 0:
            return True
        model = self.sourceModel()
        assert isinstance(model, QAbstractItemModel)
        for c in range(model.columnCount()):
            idx = model.index(source_row, c, source_parent)
            data = model.data(idx)
            if isinstance(data, str) and reg.exactMatch(data):
                return True
        return False

    def mapToSource(self, proxy_index: QModelIndex):
        """ Implementation of mapToSource function in parent class. """
        return super(SortFilterProxyModel, self).mapToSource(proxy_index)


# class MapLayerProxyModel(QgsMapLayerProxyModel):
#     """A QgsMapLayerProxyModel to handle the MesmaTableModel and MesmaTreeModel. """
#
#     def __init__(self, parent=None):
#         super(MapLayerProxyModel, self).__init__(parent)
#
#     def filterAcceptsRow(self, source_row: int, source_parent: QModelIndex):
#
#         b = super(MapLayerProxyModel, self).filterAcceptsRow(source_row, source_parent)
#         idx = self.sourceModel().index(source_row, 0, source_parent)
#         lyr = idx.internalPointer()
#
#         if not isinstance(lyr, QgsRasterLayer):
#             return False
#         else:
#             dt = lyr.dataProvider()
#
#         return b


class ModelVisualizationWidget(QMainWindow):
    """ QMainWindow to interactively visualize the MESMA models. """

    def __init__(self, parent = None, testing: bool = None):
        super(ModelVisualizationWidget, self).__init__(parent)
        loadUi(os.path.join(os.path.dirname(__file__), 'mesma_visualisation.ui'), self)

        # header
        excluded_providers = [p for p in QgsProviderRegistry.instance().providerList() if p not in ['gdal']]
        self.mapLayerComboBox.setExcludedProviders(excluded_providers)
        self.mapLayerComboBox.setFilters(QgsMapLayerProxyModel.RasterLayer)
        self.mapLayerComboBox.layerChanged.connect(self._layerChanged)

        self.loadImageAction.triggered.connect(self._browse)
        self.readEndmembersAction.triggered.connect(lambda: self._readModels())
        self.repaintAction.triggered.connect(self._repaint)

        self.loadImageButton.setDefaultAction(self.loadImageAction)
        self.readEndmembersButton.setDefaultAction(self.readEndmembersAction)
        self.repaintButton.setDefaultAction(self.repaintAction)

        # Model Summary
        self._model_summary = MesmaSummary()
        self._model_summary.sigLoadingProgress.connect(self._progress)
        self._model_summary.sigSourceWillChange.connect(lambda file:
                                                        self.progressLabel.setText('Loading "{}" ...'.format(file)))
        self._model_summary.sigSourceChanged.connect(lambda file:
                                                     self.progressLabel.setText('Loading "{}" done!'.format(file)))

        # Tree View
        self._tree_model = MesmaTreeModel(self._model_summary)
        self._tree_filter_model = SortFilterProxyModel(self)
        self._tree_filter_model.setSourceModel(self._tree_model)
        self.treeView.setModel(self._tree_filter_model)
        self.treeView.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        self._tree_filter_model.sort(1, order=Qt.AscendingOrder)

        # Widget Variables
        self._r = None
        self._lyr = None
        self._test = testing

    def _browse(self):

        filters = QgsProviderRegistry.instance().fileRasterFilters()
        paths, _ = QFileDialog.getOpenFileNames(filter=filters)

        if len(paths) > 0:
            self.openImage(paths)

    def openImage(self, paths):

        if len(paths) > 0:
            layers = []
            for path in paths:
                try:
                    lyr = QgsRasterLayer(path, os.path.basename(path), 'gdal')
                    assert isinstance(lyr, QgsRasterLayer)
                    assert lyr.isValid()
                    layers.append(lyr)
                except Exception as ex:
                    print(ex, file=sys.stderr)

            if len(layers) > 0:
                QgsProject.instance().addMapLayers(layers, True)
                self.mapLayerComboBox.setLayer(layers[0])

    def _layerChanged(self):
        """ Read the models of the new layer. """
        current_layer = self.mapLayerComboBox.currentLayer()
        if current_layer is None:
            return
        self._readModels(layer=current_layer)

    def _readModels(self, layer: QgsRasterLayer = None):
        """ Reads the endmember models from the MESMA model raster layer output.

        :param layer: QGIS raster layer pointing to the MESMA model
        """
        if layer is None:
            layer = self._endMemberRasterLayer()

            self.progressBar.setValue(0)

            if layer is None:
                self.progressLabel.setText('Models image not specified')
                return [], None

            if not isinstance(layer, QgsRasterLayer) or layer.providerType() != 'gdal':
                self.progressLabel.setText('Unable to read layer "{}" ({}) with gdal'.format(layer.name(), layer))
                return [], None

        path_source = layer.source()

        try:
            self._model_summary.readMesmaModelsImage(path=path_source, parent=self)
            # self.treeView.expandAll()
            self.treeView.expand(self._tree_filter_model.index(1, 0))
            self.treeView.expand(self._tree_filter_model.index(0, 0))

        except Exception as ex:
            print(str(ex), file=sys.stderr)

    def _progress(self, done: int, maximum: int):
        self.progressBar.setRange(0, maximum)
        self.progressBar.setValue(done)

    def _filterTextChanged(self):
        pattern = self.filterText.text()
        is_regex = self.filterAction.isChecked()

        if is_regex:
            self._table_filter_model.setFilterRegExp(pattern)
        else:
            self._table_filter_model.setFilterWildcard(pattern)

    def _repaint(self):
        lyr = self._endMemberRasterLayer()
        if isinstance(lyr, QgsRasterLayer):
            # r = self._rasterRenderer()
            r = self._tree_model.rasterRenderer()
            self._r = r  # keep a reference on this renderer and avoid python GC to kill objects with living C++ backend
            self._lyr = lyr
            r.setInput(lyr.dataProvider())
            lyr.setRenderer(r)
            lyr.triggerRepaint()

    def _endMemberRasterLayer(self) -> QgsRasterLayer:
        return self.mapLayerComboBox.currentLayer()

    def closeEvent(self, event: QCloseEvent):
        """ Overwrite close event: warn the user that all edits (colors etc.) will be lost. """

        if not self._model_summary.mesmaModels() or self._test:
            event.accept()

        else:
            box = QMessageBox(parent=self)
            box.setText("Are you sure you want to close this window? All color settings will be lost.")
            box.setIcon(QMessageBox.Warning)
            box.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            box.exec()
            if box.result() == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()


def _run():
    from qgis.core import QgsApplication
    app = QgsApplication([], True)
    app.initQgis()

    z = ModelVisualizationWidget()
    z.show()

    app.exec_()


if __name__ == '__main__':
    _run()
