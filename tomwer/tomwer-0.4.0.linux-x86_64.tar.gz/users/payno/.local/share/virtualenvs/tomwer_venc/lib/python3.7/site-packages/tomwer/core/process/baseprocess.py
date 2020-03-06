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
"""
Basic class each orange widget processing an action should inheritate from
her corresponding class in core.
And all of those classes from core should implement this interface to deal
with the interpreter parser.
Allowing to convert an orane workflow to a TOWER workflow ( same action but no
GUI )
"""


__author__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "02/06/2017"


import threading
import h5py
import numpy
from datetime import datetime
from typing import Union
from silx.io.dictdump import dicttoh5
from collections import namedtuple
from silx.io.dictdump import h5todict
import logging

_logger = logging.getLogger(__name__)


_input_desc = namedtuple(
        "_input_desc", ['name', 'type', 'handler', 'doc']
)

_output_desc = namedtuple(
        "_output_desc", ['name', 'type', 'doc']
)

_process_desc = namedtuple(
    "_process_desc", ["process_order", "configuration", "results"]
)


class BaseProcess(object):
    """Class from which all tomwer process should inherit

    :param logger: the logger used by the class
    """

    endless_process = False
    """used to know if the process requires user action to stop the process"""

    inputs = []
    """list of requested inputs"""

    outputs = []
    """list of generated outputs"""

    _output_values = {}

    def __init__(self):
        self._scheme_title = None  # title of the associated scheme
        self._return_dict = False
        """should the return type of the handler should be TomoBase instance
        objects or dict"""
        # TODO: add processing order

    def setProperties(self, properties):
        raise NotImplementedError('BaseProcess is an abstract class')

    @staticmethod
    def properties_help():
        """

        :return: display the list of all managed keys and possible values
        :rtype: str
        """
        # TODO: use argsparse instead of this dict ?
        raise NotImplementedError('BaseProcess is an abstract class')

    def get_output_value(self, key):
        """

        :param str key: 
        :return: 
        """
        assert type(key) is str
        if key in self._output_values:
            return self._output_values[key]
        else:
            return None

    def clear_output_values(self):
        self._output_values.clear()

    def register_output(self, key, value):
        """

        :param str key: name of the output
        :param value: value of the output
        """
        self._output_values[key] = value

    def key_exist(self, key):
        for _output in self.outputs:
            if _output.name == key:
                return True
        return False

    def input_handler(self, name):
        """

        :param str name: name of input (can be see as link type)
        :return: handler name (str) or None if name not defined
        """
        for _input in self.inputs:
            if _input.name == name:
                return _input.handler
        return None

    def _set_return_dict(self, return_dict):
        """

        :param bool return_dict: if True, force the process to return a dict
                                 instead of a `.TomoBase` object
        """
        self._return_dict = return_dict

    @staticmethod
    def program_name():
        """Name of the program used for this processing"""
        raise NotImplementedError('Base class')

    @staticmethod
    def program_version():
        """version of the program used for this processing"""
        raise NotImplementedError('Base class')

    @staticmethod
    def definition():
        """definition of the process"""
        raise NotImplementedError('Base class')

    def get_configuration(self) -> Union[None,dict]:
        """

        :return: configuration of the process
        :rtype: dict
        """
        if len(self._settings) > 0:
            return self._settings
        else:
            return None

    def set_configuration(self, configuration: dict) -> None:
        self._settings = configuration

    def register_process(self, process_file: str,
                         configuration: Union[dict,None],
                         results: Union[dict,None], process_index: int,
                         overwrite: bool=True) -> None:
        """
        Store the current process in the linked h5 file if any,
        output data stored will be the one defined by the data_keys

        :param process_file: where to store the processing information
        :type: str
        :param process: process to record
        :type: BaseProcess
        :param configuration: configuration of the process
        :type: Union[dict,None]
        :param results: result of the processing
        :type: Union[dict,None]
        :param process_index: index of the process
        :type: int
        :param overwrite: if True then overwrite the process if already exists
        """
        assert process_file is not None
        try:
            self._register_process(process_file=process_file,
                                   process=self,
                                   configuration=configuration,
                                   results=results,
                                   process_index=process_index,
                                   overwrite=overwrite)
        except IOError as e:
            _logger.error(e)

    def _register_process(self, process_file: str, process,
                          configuration: Union[dict,None],
                         results: Union[dict,None], process_index: int,
                         overwrite: bool=True) -> None:
        """
        Store the current process in the linked h5 file if any,
        output data stored will be the one defined by the data_keys

        :param process_file: where to store the processing information
        :type: str
        :param process: process to record
        :type: BaseProcess
        :param configuration: configuration of the process
        :type: Union[dict,None]
        :param results: result of the processing
        :type: Union[dict,None]
        :param process_index: index of the process
        :type: int
        :param overwrite: if True then overwrite the process if already exists
        """
        assert process_file is not None, 'The process file should be defined'
        assert isinstance(process, BaseProcess)
        process_name = 'tomwer_process_' + str(process_index)
        # if the files does not exists, write scan properties
        with h5py.File(process_file, mode='a') as h5f:
            nx_process = h5f.require_group(process_name)
            nx_process.attrs['NX_class'] = "NXprocess"
            if overwrite:
                for key in ('program', 'version', 'date', 'processing_order',
                            'class_instance'):
                    if key in nx_process:
                        del nx_process[key]

            # write process information
            nx_process['program'] = process.program_name()
            nx_process['version'] = process.program_version()
            nx_process['date'] = datetime.now().replace(microsecond=0).isoformat()
            nx_process['processing_order'] = numpy.int32(process_index)
            _class = process.__class__
            nx_process['class_instance'] = '.'.join((_class.__module__,
                                                     _class.__name__))

        # dump result
        if results is not None:
            dicttoh5(results,
                     h5file=process_file,
                     h5path='/'.join((process_name, 'results')),
                     overwrite_data=True,
                     mode='a')

        # dump configuration
        if configuration is not None:
            dicttoh5(configuration,
                     h5file=process_file,
                     h5path='/'.join((process_name, 'configuration')),
                     overwrite_data=True,
                     mode='a')

    @staticmethod
    def get_processes_frm_type(process_file: str, process_type) -> list:
        """

        :param str process_file: file to read
        :param process_type: process type we are looking for
        :return: list of _process_desc(processing_order, configuration, results)
        :rtype: list
        """
        processes = []
        with h5py.File(process_file, mode='r') as h5f:
            for process in h5f.keys():
                nx_process = h5f[process]
                if nx_process['program'][()] == process_type.program_name():
                    p_order = nx_process["processing_order"][()]
                    config = h5todict(process_file, '/'.join((nx_process.name, 'configuration')))
                    results = h5todict(process_file, '/'.join((nx_process.name, 'results')))
                    processes.append(_process_desc(process_order=p_order,
                                                   configuration=config,
                                                   results=results))
        return processes


class SingleProcess(BaseProcess):
    """
    Interface for Single process (which can be applied on a single scan)
    """
    # TODO: refactor, scan should be inputs
    def process(self, scan=None):
        """
        Process should return an int. Default are zero for success and one for
        failure. It can also return an error value

        :param scan:
        :return:
        :rtype: int
        """
        raise NotImplementedError('Base class')


class EndlessProcess(BaseProcess):
    """
    Interface for Single process (which can be applied on a single scan)
    """
    endless_process = True

    process_finished_event = threading.Event()
    '''event when the process is finished'''

    def start(self):
        raise NotImplementedError('Base class')

    def stop(self):
        raise NotImplementedError('Base class')
