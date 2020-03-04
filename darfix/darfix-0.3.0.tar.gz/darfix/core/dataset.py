# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2017 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ###########################################################################*/


__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "16/12/2019"

import copy
import numpy
import logging
import cv2

import fabio

from silx.io import utils
from silx.io import fabioh5
from silx.io.url import DataUrl
from silx.gui import qt

_logger = logging.getLogger(__file__)

DEFAULT_METADATA = fabioh5.FabioReader.DEFAULT

COUNTER_METADATA = fabioh5.FabioReader.COUNTER

POSITIONER_METADATA = fabioh5.FabioReader.POSITIONER

_METADATA_TYPES = {'default': DEFAULT_METADATA,
                   'counter': COUNTER_METADATA,
                   'positioner': POSITIONER_METADATA}

_METADATA_TYPES_I = {}
"""used to retrieve the metadata name (str) for the silx.io.fabioh5 id"""
for key, value in _METADATA_TYPES.items():
    assert value not in _METADATA_TYPES_I
    _METADATA_TYPES_I[value] = key


class Dataset(qt.QObject):
    """Class to define a dataset from a series of raw data and dark data.

    :param raw_filename: first filename of raw data to iterate from.
    :param dark_filename: first filename of dark data to iterate from.
    :param Union[Generator,Iterator,List] filenames: Ordered list of filenames
        to process as a file series.
    :param Union[List,numpy.ndarray] data: list or numpy array of the dataset
        data.
    :param Union[List,numpy.ndarray] dark_data: list or numpy array of the
        dataset dark data.
    :param Union[Bool, None] load_data: If False, the data is not computed
        after the creation of the file_series. It waits until the load_data()
        method is called.
    """
    sigProgressChanged = qt.Signal(int)

    def __init__(self, raw_filename=None, dark_filename=None, filenames=None,
                 filter_data=False, load_data=True):
        qt.QObject.__init__(self)

        self._data = None
        self._reshaped_data = None
        self._filter_data = filter_data
        self.dark_frames = []
        self.metadata = []
        self.raw_filename = raw_filename
        self.dark_filename = dark_filename
        self.filenames = filenames
        self.__dims = AcquisitionDims()
        # Keys: dimensions names, values: dimensions values
        self._dimensions_values = {}

        # Initialize data
        self._file_series = fabio.open_series(first_filename=raw_filename,
                                              filenames=filenames)

        if load_data:
            self.load_data()

        if dark_filename is not None:

            with fabio.open_series(first_filename=dark_filename) as series:
                for dark_frame in series.frames():
                    # TODO: save only data, headers??
                    self.dark_frames.append(dark_frame.data)
        self.dark_frames = numpy.array(self.dark_frames)

    def load_data(self, percentage=1):
        """
        Function that saves the data of the frames into DataUrls and the metadata
        into fabio Readers.
        """
        data_urls = []
        self.metadata = []

        for iFrame in numpy.arange(start=0, stop=self._file_series.nframes):
            frame = self._file_series.getframe(iFrame).file_container
            data_urls.append(DataUrl(file_path=frame.filename,
                                     scheme='fabio').path())
            self.metadata.append(fabioh5.EdfFabioReader(fabio_image=frame))
            self.sigProgressChanged.emit(int(percentage * iFrame / self._file_series.nframes * 100))

        self.data_urls = numpy.array(data_urls)

    def compute_intensity_threshold(self, percentage=1, start=0):
        """
        Function that computes the data from the set of urls.
        If the filter_data flag is activated it filters the data following the next:
        -- First, it computes the intensity for each frame, by calculating the variance after
        passing a gaussian filter.
        -- Second, computes the histogram of the intensity.
        -- Finally, saves the data of the frames with an intensity bigger than a threshold.
        The threshold is set to be the second bin of the histogram.

        :param float percentage: value used to emit the progress of the computation
        :param int start: number from where the process should emit
        """
        # TODO: enter the number of bins per parameter??
        intensity = []
        for i, frame in enumerate(self.data):
            intensity += [cv2.GaussianBlur(frame, (3, 3), 20).var()]
            self.sigProgressChanged.emit(int(start + percentage * i / len(self.data) * 100))
        values, bins = numpy.histogram(intensity, int(self._data.shape[0]))
        self.threshold = numpy.array(intensity) >= bins[1]

    @property
    def data(self):
        """
        If data has not been computed, it reads the data from the urls.
        If flag for filter data is activated, computes the threshold.

        :returns: numpy.ndarray
        """
        if self._data is None:
            data = []
            for i, url in enumerate(self.data_urls):
                data += [utils.get_data(url)]
            self._data = numpy.array(data)
            if self._filter_data:
                self.compute_intensity_threshold()

        return self._data

    def get_data(self, percentage=1, start=0):
        """
        If data has not been computed, it reads the data from the urls.
        If flag for filter data is activated, computes the threshold.

        :returns: numpy.ndarray
        """
        if self._data is None:
            data = []
            if self._filter_data:
                percentage /= 2
            for i, url in enumerate(self.data_urls):
                data += [utils.get_data(url)]
                self.sigProgressChanged.emit(int(start + ((percentage * i) / len(self.data_urls) * 100)))
            self._data = numpy.array(data)
            if self._filter_data:
                self.compute_intensity_threshold(percentage / 2, start=start + (percentage * 100))

        return self._data

    @data.setter
    def data(self, data):
        """
        Sets data and reshapes the data in case reshaping has  been done before.
        """
        self._data = data
        if self._reshaped_data is not None:
            self.reshape_data()

    @property
    def hi_data(self):
        """
        :returns: The high intensity data if filter flag is activated, else data.
        """
        return self.data[self.threshold] if self._filter_data else self.data

    @hi_data.setter
    def hi_data(self, data):
        """
        Sets high intensity data, if filter data flag is active, else sets data.

        :param array_like data: data to set.
        """
        if self._filter_data:
            self.data[self.threshold] = data
        else:
            self.data = data

    @property
    def li_data(self):
        """
        :returns: The low intensity data. The filter flag has to be activated.
        """
        if self._filter_data:
            return self.data[~self.threshold]
        else:
            return None

    @li_data.setter
    def li_data(self, li_data):
        """
        Sets low intensity data. Expects filter data flag o be active.
        """
        assert self._filter_data, "Empty frames only exist when the flag filter_data \
                                  is activated"
        self.data[~self.threshold] = li_data

    def reshape_data(self):
        """
        Function that reshapes the data to fit the dimensions.
        """
        if self.__dims.ndim > 1:
            try:
                shape = list(self.__dims.shape)
                shape.append(self.data.shape[-2])
                shape.append(self.data.shape[-1])
                self._reshaped_data = self.data.reshape(shape)
            except Exception:
                raise ValueError("Failed to reshape data into dimensions {} \
                                  Try using another tolerance value.".format(' '.join(self.__dims.get_names())))
        else:
            raise ValueError("Not enough dimensions where found")

    @property
    def reshaped_data(self):
        return self._reshaped_data

    def set_reshaped_data(self, data, axis, index):
        """
        Function to substitue data in a certain dimension.

        :param ndarray data: data to be inserted.
        :param int axis: axis of the data.
        :param int index: index of the data.
        """
        self.data = self.data.astype(numpy.float32, copy=False)
        if self._filter_data:
            threshold = numpy.take(self.threshold.view().reshape(self.__dims.shape), index, axis=axis)
            numpy.swapaxes(self._reshaped_data, 0, axis)[index, :][threshold] = data
        else:
            numpy.swapaxes(self._reshaped_data, 0, axis)[index, :] = data

    def get_reshaped_data(self, axis, index):
        """
        Returns reshaped data.
        If axis is given returns data at a certain index along the axis.
        If not returns all the reshaped data.

        :param int axis: axis of the data.
        :param int index: index of the data.
        """
        if self._filter_data:
            threshold = numpy.take(self.threshold.reshape(self.__dims.shape), index, axis=axis)
            return numpy.take(self._reshaped_data, index, axis=axis)[threshold]
        return numpy.take(self._reshaped_data, index, axis=axis)

    @property
    def nframes(self):
        if self.data is None:
            return 0
        else:
            return self.data.shape[0]

    @property
    def dims(self):
        return self.__dims

    @dims.setter
    def dims(self, _dims):
        assert isinstance(_dims, AcquisitionDims), "Dimensions dictionary has " \
            "to be of class `AcquisitionDims`"
        self.__dims = _dims

    def clear_dims(self):
        self.__dims = AcquisitionDims()

    def add_dim(self, axis, dim):
        """
        Adds a dimension to the dimension's dictionary.

        :param int axis: axis of the dimension.
        :param :class:`Dimension` dim: dimension to be added.
        """
        self.__dims.add_dim(axis, dim)

    def remove_dim(self, axis):
        """
        Removes a dimension from the dimension's dictionary.

        :param int axis: axis of the dimension.
        """
        self.__dims.remove_dim(axis)

    def find_dimensions(self, kind, tolerance=1e-9):
        """
        Goes over all the headers from a given kind and finds the dimensions
        that move (have more than one value) along the data.

        Note: Before, only the dimensions that could fit where shown, now it
        shows all the dimensions and let the user choose the valid ones.

        :param int kind: Type of metadata to find the dimensions.
        :param float tolerance: Tolerance that will be used to compute the
        unique values.
        """
        self.__dims.clear()
        self._dimensions_values = {}

        keys = numpy.array(list(self.metadata[0].get_keys(kind)))
        values = numpy.array([[data.get_value(kind=kind, name=key)[0] for data
                             in self.metadata] for key in keys])
        # Unique values for each key.
        unique_values = [numpy.unique(value, return_counts=True) for value in values]
        dimensions = []
        dataset_size = len(self.metadata)
        # For every key that has more than one different value, creates a new Dimension.
        for i, value in enumerate(unique_values):
            if value[1][0] != dataset_size:
                dimension = Dimension(kind, keys[i], tolerance=tolerance)
                dimension.setUniqueValues(numpy.unique(value[0]))
                # Value that tells when does the change of value occur. It is used to know the order
                # of the reshaping.
                dimension.changing_value = numpy.unique(values[i, :int(dataset_size / value[1][0])],
                                                        return_counts=True)[1][0]
                dimensions.append(dimension)

        for dimension in sorted(dimensions, key=lambda x: x.changing_value):
            self.__dims.add_dim(axis=self.__dims.ndim, dim=dimension)
            _logger.info("Dimension {} of size {} has been added for reshaping"
                         .format(dimension.name, dimension.size))

    def get_dimensions_values(self):
        """
        Returns all the metadata values of the dimensions.
        The values are assumed to be numbers.

        :returns: array_like
        """
        if not self._dimensions_values:
            data = self.metadata
            for dimension in self.__dims:
                values = numpy.empty((len(data)))
                for row, metadata_frame in enumerate(data):
                    values[row] = (metadata_frame.get_value(kind=dimension[1].kind,
                                   name=dimension[1].name)[0])
                self._dimensions_values[dimension[1].name] = values
        return self._dimensions_values

    def __deepcopy__(self, memo):
        """
        Create copy of the dataset. The data numpy array is also copied using
        deep copy. The rest of the attributes are the same.
        """
        dataset = type(self)(self.raw_filename, self.dark_filename, self.filenames,
                             filter_data=self._filter_data, load_data=False)
        dataset.data_urls = self.data_urls
        dataset.metadata = self.metadata
        dataset.data = copy.deepcopy(self.data, memo)
        if self._filter_data:
            dataset.threshold = copy.deepcopy(self.threshold, memo)
        dataset.dark_frames = copy.deepcopy(self.dark_frames, memo)
        dataset.dims = copy.deepcopy(self.__dims, memo)
        if self._reshaped_data is not None:
            dataset.reshape_data()
        return dataset


class AcquisitionDims(object):
    """
    Define the view of the data which has to be made
    """
    def __init__(self):
        self.__dims = {}

    def add_dim(self, axis, dim):
        assert isinstance(dim, Dimension)
        self.__dims[axis] = dim

    def remove_dim(self, axis):
        if axis in self.__dims:
            del self.__dims[axis]

    def clear(self):
        self.__dims = {}

    @property
    def ndim(self):
        return len(self.__dims)

    def get(self, axis):
        """
        Get Dimension at certain axis.

        :param int axis: axis of the dimension.
        :return: the requested dimension if exists.
        """
        assert type(axis) is int
        if axis in self.__dims:
            return self.__dims[axis]
        else:
            return None

    def get_names(self):
        """
        Get list with all the names of the dimensions.

        :return: array_like of strings
        """
        dims = []
        for dim in self.__dims.values():
            dims += [dim.name]

        return dims

    @property
    def shape(self):
        """
        :return: shape of the currently defined dims
        """
        shape = []
        for iDim in range(self.ndim):
            if iDim not in self.__dims:
                shape.append(1)
            else:
                shape.append(self.__dims[iDim].size or -1)
        return tuple(shape)

    def set_size(self, axis, size):
        """
        Recreated new dimension with new size and same name and kind.

        :param int axis: axis of the dimension
        :param int size: new size for the dimension
        """
        if axis not in self.__dims:
            _logger.error('axis %s is not defined yet, cannot define a size '
                          'for it' % axis)
        else:
            self.__dims[axis] = Dimension(name=self.__dims[axis].name,
                                          kind=self.__dims[axis].kind,
                                          size=size)

    def __iter__(self):
        for iAxis, dim in self.__dims.items():
            yield (iAxis, dim)


class Dimension(object):
    """
    Define a dimension used during the dataset

    :param Union[int,str] kind: metadata type in fabioh5 mapping
    :param str name: name of the dimension (should fit the fabioh5 mapping
                     for now)
    :param Union[int,None] size: length of the dimension.
    """
    def __init__(self, kind, name, size=None, tolerance=1e-09):
        if type(kind) is str:
            assert kind in _METADATA_TYPES
            self.__kind = _METADATA_TYPES[kind]
        else:
            self.__kind = kind
        self.__name = name
        self._size = size
        self._tolerance = tolerance
        self.__unique_values = []

    @property
    def kind(self):
        return self.__kind

    def _setKind(self, kind):
        self.__kind = kind

    @property
    def name(self):
        return self.__name

    def _setName(self, name):
        self.__name = name

    @property
    def size(self):
        return self._size

    def _setSize(self, size):
        self._size = size

    @property
    def tolerance(self):
        return self._tolerance

    def _setTolerance(self, tolerance):
        assert isinstance(tolerance, float), "Tolerance has to be float number"
        self._tolerance = tolerance

    @property
    def unique_values(self):
        return self.__unique_values

    def _find_unique_values(self, values):
        """
        Function that compares the values passed as parameter and returns only the unique
        ones given the dimension's tolerance.

        :param array_like values: list of values to compare.
        """
        unique_values = []
        import math
        if not numpy.all(numpy.isreal(values)):
            return values
        for val in values:
            if not unique_values:
                unique_values.append(val)
            else:
                unique = True
                for unique_value in unique_values:
                    if math.isclose(unique_value, val, rel_tol=self.tolerance):
                        unique = False
                        break
                if unique:
                    unique_values.append(val)
        return unique_values

    def setUniqueValues(self, values):
        """
        Sets the unique values of the dimension. If the size of the dimension is fixed,
        it automatically sets the first size values, else it finds the unique values.

        :param array_like values: list of values.
        """
        if self.size:
            self.__unique_values = values[:self.size]
        else:
            self.__unique_values = self._find_unique_values(values)
        self._setSize(len(self.__unique_values))

    def __str__(self):
        return " ".join((str(self.kind), str(self.name), 'size:', str(self.size)))

    def to_dict(self):
        """Translate the current Dimension to a dictionary"""
        return {
            'name': self.name,
            'kind': self.kind,
            'size': self.size,
            'tolerance': self.tolerance
        }

    @staticmethod
    def from_dict(_dict):
        """

        :param dict _dict: dict defining the dimension. Should contains the
                           following keys: name, kind, size.
                           Unique values are not stored into it because it
                           depends on the metadata and should be obtained from a
                           fit / set_dims
        :return: Dimension corresponding to the dict given
        :rtype: :class:`Dimension`
        """
        assert type(_dict) is dict
        missing_keys = []
        for _key in ('name', 'kind', 'size', 'tolerance'):
            if _key not in _dict:
                missing_keys.append(missing_keys)
        if len(missing_keys) > 0:
            raise ValueError('There is some missing keys (%s), unable to create'
                             'a valid Dim')
        else:
            return Dimension(name=_dict['name'],
                             kind=_dict['kind'],
                             size=_dict['size'],
                             tolerance=_dict['tolerance'])
