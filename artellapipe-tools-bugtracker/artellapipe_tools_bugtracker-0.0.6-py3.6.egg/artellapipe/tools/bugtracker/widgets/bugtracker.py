#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool that allows to detect errors and trace calls and easily them to TDs
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os
import sys
import getpass
import logging
import platform
import datetime
import traceback
import subprocess
import webbrowser
import collections
try:
    from urllib import quote
except ImportError:
    from urllib2 import quote

from Qt.QtCore import *
from Qt.QtWidgets import *

import tpDcc as tp
from tpDcc.libs.python import osplatform
from tpDcc.libs.qt.widgets import splitters, stack
from tpDcc.libs.qt.core import base, qtutils

import artellapipe
from artellapipe.core import tool

LOGGER = logging.getLogger()


class ArtellaBugTracker(artellapipe.ToolWidget):

    BUG_TYPES = ['Bug', 'Request']
    ATTACHER_TYPE = tool.ToolAttacher.Dialog
    CPU_INFO = None
    GPU_INFO = None

    def __init__(self, project, config, settings, parent, tool=None, traceback=None):

        self._tool = tool
        self._trace = traceback
        self._bug_data = dict()

        super(ArtellaBugTracker, self).__init__(project=project, config=config, settings=settings, parent=parent)

    def ui(self):
        super(ArtellaBugTracker, self).ui()

        top_layout = QGridLayout()
        type_lbl = QLabel('Type')
        self._types_combo = QComboBox()
        self._types_combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        tool_lbl = QLabel('Tool: ')
        self._tools_combo = QComboBox()
        self._tools_combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        department_lbl = QLabel('Department: ')
        self._departments_combo = QComboBox()
        self._departments_combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        top_layout.setColumnStretch(1, 1)
        top_layout.addWidget(type_lbl, 0, 0)
        top_layout.addWidget(self._types_combo, 0, 1)
        top_layout.addWidget(tool_lbl, 1, 0)
        top_layout.addWidget(self._tools_combo, 1, 1)
        top_layout.addWidget(department_lbl, 2, 0)
        top_layout.addWidget(self._departments_combo, 2, 1)

        self._stack = stack.SlidingStackedWidget()
        self._stack.set_vertical_mode()

        self._bug_widget = BugWidget(main=self, project=self._project, traceback=self._trace)
        self._request_widget = RequestWidget(main=self, project=self._project)
        self._stack.addWidget(self._bug_widget)
        self._stack.addWidget(self._request_widget)

        self.main_layout.addLayout(top_layout)
        self.main_layout.addWidget(self._stack)

        self._fill_combos()

    @property
    def tool(self):
        return self._tool

    def has_tool(self):
        if self._tool and hasattr(self._tool, 'config'):
            return True

        return False

    def get_current_data(self):
        data = {
            'department': self._departments_combo.currentText(),
            'tool': {
                'name': self._tools_combo.currentData().get('name'),
                'version': self._tools_combo.currentData().get('version'),
                'config': self._tools_combo.currentData().get('config'),
                'data': self._tools_combo.currentData(),
            }
        }

        return data

    def _fill_combos(self):

        self._tools_combo.clear()
        self._departments_combo.clear()
        self._types_combo.clear()

        # Types
        for t in self.BUG_TYPES:
            self._types_combo.addItem(t)

        # Tools
        valid_tool = False
        tool_info = None
        if self._tool is not None:
            if not hasattr(self._tool, 'config'):
                LOGGER.warning('Given Tool is not a valid one. Specify manually the tool in the Bug Tracker ...')
            else:
                tool_name = self._tool.config.data.get('name', None)
                if tool_name:
                    tool_info = artellapipe.ToolsMgr().get_tool_data_from_tool(self._tool, as_dict=True)
                    if tool_info:
                        valid_tool = True
                    else:
                        LOGGER.warning(
                            'Impossible to retrieve tool information. Specify manually the tool in the Bug Tracker ...')
                else:
                    LOGGER.warning('Impossible to retrieve tool name. Specify manually the tool in the Bug Tracker ...')

        if valid_tool and tool_info:
            all_tools = tool_info
        else:
            all_tools = dict()
            for package_name in ['artellapipe', artellapipe.project.get_clean_name()]:
                package_tools = tp.ToolsMgr().get_package_tools(package_name) or list()
                all_tools.update(package_tools)

        for tool_id, tool_info in all_tools.items():
            tool_name = tool_info.get('name', None)
            if not tool_name:
                continue
            tool_icon_name = tool_info.get('icon', None)
            tool_version = tool_info.get('version', None)
            if tool_version:
                tool_name = '{} - {}'.format(tool_name, tool_version)
            if tool_icon_name:
                tool_icon = tp.ResourcesMgr().icon(tool_icon_name)
                self._tools_combo.addItem(tool_icon, tool_name, userData=tool_info)
            else:
                self._tools_combo.addItem(tool_name, userData=tool_info)

        # Departments
        all_departents = self._project.departments
        for department in all_departents:
            self._departments_combo.addItem(department)

    def setup_signals(self):
        self._types_combo.currentIndexChanged.connect(self._on_type_index_changed)
        self._stack.animFinished.connect(self._on_stack_anim_finished)

    def _on_type_index_changed(self, index):
        self._types_combo.setEnabled(False)
        self._stack.slide_in_index(index)

    def _on_stack_anim_finished(self):
        self._types_combo.setEnabled(True)


class BugWidget(base.BaseWidget, object):
    def __init__(self, main, project, traceback=None, parent=None):

        self._project = project
        self._main = main

        super(BugWidget, self).__init__(parent=parent)

        self.set_trace(trace=traceback)

    def ui(self):
        super(BugWidget, self).ui()

        bug_data_frame = QFrame()
        bug_data_frame.setFrameStyle(QFrame.Raised | QFrame.StyledPanel)
        self._bug_data_layout = QGridLayout()
        bug_data_frame.setLayout(self._bug_data_layout)

        self._trace_text = QTextEdit()
        self._trace_text.setMinimumHeight(100)
        self._trace_text.setReadOnly(True)
        self._trace_text.setEnabled(False)

        self._title_line = QLineEdit()
        self._title_line.setPlaceholderText('Short title for the bug ...')
        self._steps_area = QTextEdit()
        txt_msg = 'Explain with details how to reproduce the error ...'
        steps_lbl = QLabel(txt_msg)
        if qtutils.is_pyside2():
            self._steps_area.setPlaceholderText(txt_msg)
        self._steps_area.setMinimumHeight(350)

        self._send_btn = QPushButton('Send Bug')
        self._send_btn.setIcon(tp.ResourcesMgr().icon('bug'))
        self._send_btn.setEnabled(False)

        self.main_layout.addWidget(splitters.Splitter('Bug Data'))
        self.main_layout.addWidget(bug_data_frame)
        self.main_layout.addWidget(splitters.Splitter('Error Trace'))
        self.main_layout.addWidget(self._trace_text)
        self.main_layout.addLayout(splitters.SplitterLayout())
        self.main_layout.addWidget(self._title_line)
        if qtutils.is_pyside():
            self.main_layout.addWidget(steps_lbl)
        self.main_layout.addWidget(self._steps_area)
        self.main_layout.addLayout(splitters.SplitterLayout())
        self.main_layout.addWidget(self._send_btn)

        self._fill_bug_data()

    def setup_signals(self):
        self._title_line.textChanged.connect(self._update_ui)
        self._steps_area.textChanged.connect(self._update_ui)
        self._send_btn.clicked.connect(self._on_send_bug)

    def set_trace(self, trace):
        """
        Sets the traceback text
        :param trace: str
        """

        self._trace_text.setPlainText(str(trace))
        self._update_ui()

    def _update_ui(self):
        """
        Internal function that updates Artella Bug Tracker UI
        """

        self._send_btn.setEnabled(self._steps_area.toPlainText() != '' and self._title_line.text() != '')

    def _get_cpu_info(self):
        cpu_info = dict()
        try:
            import cpuinfo
            cpuinfo_py = os.path.join(os.path.dirname(os.path.abspath(cpuinfo.__file__)), 'cpuinfo.py')
            out = subprocess.check_output('python {}'.format(cpuinfo_py), creationflags=0x08000000)
            cpu_data = str(out).split('\n')
            for inf in cpu_data:
                inf = inf.rstrip()
                inf_split = inf.split(':')
                if len(inf_split) != 2:
                    continue
                cpu_info[inf_split[0]] = inf_split[1].lstrip()
        except Exception as exc:
            LOGGER.warning('Impossible to retrieve CPU info: {} | {}'.format(exc, traceback.format_exc()))
            return dict()

        return cpu_info

    def _get_gpu_info(self):
        gpu_info = {
            'gpus': {}
        }
        try:
            import GPUtil
            GPUtil.showUtilization()
            gpus_list = GPUtil.getGPUs()
            for gpu in gpus_list:
                gpu_info['gpus'][gpu.uuid] = {
                    'name': gpu.name,
                    'driver': gpu.driver,
                    'memoryTotal': gpu.memoryTotal,
                    'memoryUsed': gpu.memoryUsed,
                    'memoryUtil': gpu.memoryUtil,
                    'load': gpu.load
                }
        except Exception as exc:
            LOGGER.warning('Impossible to retrieve GPU info: {} | {}'.format(exc, traceback.format_exc()))
            return dict()

        return gpu_info

    def _get_disk_usage(self):
        try:
            _ntuple_diskusage = collections.namedtuple('usage', 'total used free')

            def bytes2human(n):
                symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
                prefix = dict()
                for i, s in enumerate(symbols):
                    prefix[s] = 1 << (i + 1) * 10
                for s in reversed(symbols):
                    if n >= prefix[s]:
                        value = float(n) / prefix[s]
                        return '%.1f%s' % (value, s)
                return "%sB" % n

            def get_usage_and_free_percentages(total, used, free):
                return str(round((used / total) * 100, 2)), str(round((free / total) * 100, 2))

            if hasattr(os, 'statvfs'):  # POSIX
                def disk_usage(path):
                    st = os.statvfs(path)
                    free = st.f_bavail * st.f_frsize
                    total = st.f_blocks * st.f_frsize
                    used = (st.f_blocks - st.f_bfree) * st.f_frsize
                    return _ntuple_diskusage(total, used, free)
            elif os.name == 'nt':  # Windows
                import ctypes

                def disk_usage(path):
                    _, total, free = ctypes.c_ulonglong(), ctypes.c_ulonglong(), ctypes.c_ulonglong()
                    if sys.version_info >= (3,) or isinstance(path, unicode):
                        fun = ctypes.windll.kernel32.GetDiskFreeSpaceExW
                    else:
                        fun = ctypes.windll.kernel32.GetDiskFreeSpaceExA
                    ret = fun(path, ctypes.byref(_), ctypes.byref(total), ctypes.byref(free))
                    if ret == 0:
                        raise ctypes.WinError()
                    used = total.value - free.value
                    return _ntuple_diskusage(total.value, used, free.value)
            else:
                raise NotImplementedError("platform not supported")

            disk_usage_dict = {
                'drives': {}
            }
            paths_to_get_disk_usage_of = [
                os.path.dirname(sys.executable),
                self._project.get_project_path()
            ]
            for p in paths_to_get_disk_usage_of:
                path_drive = os.path.splitdrive(p)[0]
                usage = disk_usage(p)
                if not usage:
                    continue

                usage_percentage, free_percentage = get_usage_and_free_percentages(
                    usage.total, usage.used, usage.free
                )

                disk_usage_dict['drives'][path_drive] = {
                    'total': bytes2human(usage.total),
                    'used': bytes2human(usage.used),
                    'free': bytes2human(usage.free),
                    'usage_percentage': usage_percentage,
                    'free_percentage': free_percentage
                }

            return disk_usage_dict

        except Exception as exc:
            LOGGER.warning('Impossible to retrieve Disk Usage info: {} | {}'.format(exc, traceback.format_exc()))
            return None

    def _get_base_bug_data(self):
        bug_data = {
            'user': getpass.getuser(),
            'time': str(datetime.datetime.now()),
            'pythonVersion': sys.version,
            'friendlyPythonVersion': "{0}.{1}.{2}.{3}.{4}".format(*sys.version_info),
            'node': platform.node(),
            'OSRelease': platform.release(),
            'OSVersion': platform.platform(),
            'processor': platform.processor(),
            'machineType': platform.machine(),
            'env': os.environ,
            'syspaths': sys.path,
            'executable': sys.executable,
            'dcc_name': tp.Dcc.get_name(),
            'dcc_version': tp.Dcc.get_version()
        }

        return bug_data

    def _get_bug_data(self):

        bug_data = self._get_base_bug_data()

        if not ArtellaBugTracker.CPU_INFO:
            ArtellaBugTracker.CPU_INFO = self._get_cpu_info()
        if ArtellaBugTracker.CPU_INFO:
            bug_data.update(ArtellaBugTracker.CPU_INFO)

        if not ArtellaBugTracker.GPU_INFO:
            ArtellaBugTracker.GPU_INFO = self._get_gpu_info()
        if ArtellaBugTracker.GPU_INFO:
            bug_data.update(ArtellaBugTracker.GPU_INFO)

        disk_usage = self._get_disk_usage()
        if disk_usage:
            bug_data.update(disk_usage)

        return bug_data

    def _fill_bug_data(self):
        qtutils.clear_layout(self._bug_data_layout)

        def _add_info(title, data, row, column):
            title_lbl = QLabel('{}: '.format(title))
            title_lbl.setStyleSheet('font-weight: bold')
            title_lbl.setAlignment(Qt.AlignRight)
            data_text = str(bug_data.get(data, '-not found-'))
            data_lbl = QLabel(data_text)
            data_lbl.setToolTip(data_text)
            data_lbl.setStatusTip(data_text)
            data_lbl.setStyleSheet('background-color: rgba(45, 85, 45, 50);')
            self._bug_data_layout.setColumnStretch(column + 1, 1)
            self._bug_data_layout.addWidget(title_lbl, row, column)
            self._bug_data_layout.addWidget(data_lbl, row, column + 1)

        def _add_drives_info(row, column):
            drives = bug_data.get('drives')
            if not drives:
                return
            i = 0
            for drive_letter, drive_info in drives.items():
                title_lbl = QLabel('Hard Drive Usage ({})'.format(drive_letter))
                title_lbl.setStyleSheet('font-weight: bold')
                title_lbl.setAlignment(Qt.AlignRight)
                data_text = '{} of {} ({}%)'.format(
                    drive_info['used'], drive_info['total'], drive_info['usage_percentage'])
                data_lbl = QLabel(data_text)
                data_lbl.setToolTip(data_text)
                data_lbl.setStatusTip(data_text)
                data_lbl.setStyleSheet('background-color: rgba(45, 85, 45, 50);')
                self._bug_data_layout.setColumnStretch(column + i + 1, 1)
                self._bug_data_layout.addWidget(title_lbl, row + i, column)
                self._bug_data_layout.addWidget(data_lbl, row + i, column + 1)
                i += 1

        def _add_gpu_info(row, column):

            def _add_info(gpu_id, title, data, index, row, column):
                title_lbl = QLabel('{}: '.format(title))
                title_lbl.setStyleSheet('font-weight: bold')
                title_lbl.setAlignment(Qt.AlignRight)
                data_text = str(gpus[gpu_id].get(data, '-not found-'))
                data_lbl = QLabel(data_text)
                data_lbl.setToolTip(data_text)
                data_lbl.setStatusTip(data_text)
                data_lbl.setStyleSheet('background-color: rgba(45, 85, 45, 50);')
                self._bug_data_layout.setColumnStretch(column + index + 1, 1)
                self._bug_data_layout.addWidget(title_lbl, row + index, column)
                self._bug_data_layout.addWidget(data_lbl, row + index, column + 1)

            gpus = bug_data.get('gpus')
            if not gpus:
                return
            row_index = 0
            for i, gpu_id in enumerate(gpus.keys()):
                _add_info(gpu_id, 'GPU Name ({})'.format(i), 'name', row_index, row, column)
                row_index += 1
                _add_info(gpu_id, 'GPU Driver ({})'.format(i), 'driver', row_index, row, column)
                row_index += 1
                title_lbl = QLabel('GPU Usage ({})'.format(i))
                title_lbl.setStyleSheet('font-weight: bold')
                title_lbl.setAlignment(Qt.AlignRight)
                data_text = '{} of {} ({}%)'.format(
                    str(round((gpus[gpu_id]['memoryUsed'] / 1000), 2)) + 'GB',
                    str(round((gpus[gpu_id]['memoryTotal'] / 1000), 2)) + 'GB',
                    str(round(float(gpus[gpu_id]['memoryUtil']) * 100, 2)))
                data_lbl = QLabel(data_text)
                data_lbl.setToolTip(data_text)
                data_lbl.setStatusTip(data_text)
                data_lbl.setStyleSheet('background-color: rgba(45, 85, 45, 50);')
                self._bug_data_layout.setColumnStretch(column + row_index + 1, 1)
                self._bug_data_layout.addWidget(title_lbl, row + row_index, column)
                self._bug_data_layout.addWidget(data_lbl, row + row_index, column + 1)

        bug_data = self._get_bug_data()

        _add_info('User', 'user', 0, 0)
        _add_info('Time', 'time', 1, 0)
        _add_info('Computer Type', 'machineType', 2, 0)
        _add_info('Platform OS', 'OSVersion', 3, 0)
        _add_info('Platform Version', 'OSRelease', 4, 0)
        _add_info('Python Version', 'friendlyPythonVersion', 5, 0)
        _add_drives_info(6, 0)

        _add_info('DCC Name', 'dcc_name', 0, 2)
        _add_info('DCC Version', 'dcc_version', 1, 2)
        _add_info('CPU Cores', 'Count', 2, 2)
        _add_info('CPU Bits', 'Bits', 3, 2)
        _add_info('CPU Vendor', 'Brand', 4, 2)
        _add_gpu_info(5, 2)

        self._bug_data = bug_data

    def _send_email_bug(self):

        if not self._project:
            LOGGER.warning('Impossible to send bug because there is project defined')
            return
        project_name = self._project.name.title()
        if not self._project.emails:
            LOGGER.warning(
                'Impossible to send bug because there is no emails defined in the project: {}'.format(project_name))
            return

        project_name = self._project.name.title()

        current_data = self._main.get_current_data()
        if not current_data:
            LOGGER.warning('No data available to send ...')
            return False

        tool_name = current_data.get('tool', {}).get('name', None)
        tool_version = current_data.get('tool', {}).get('version', 'unknown')
        department = current_data.get('department', None)
        steps = self._steps_area.toPlainText()
        user = str(osplatform.get_user())
        title = self._title_line.text()
        current_time = str(datetime.datetime.now())
        node = platform.node()
        os_release = platform.release()
        os_version = platform.platform()
        os_processor = platform.processor()
        os_machine = platform.machine()
        executable = sys.executable
        dcc_name = tp.Dcc.get_name()
        dcc_version = tp.Dcc.get_version()

        msg = self._trace_text.toPlainText()
        msg += '\n----------------------------\n'
        msg += 'User: {}\n'.format(user)
        msg += 'Time: {}\n'.format(current_time)
        msg += 'Tool: {}\n'.format(tool_name)
        msg += 'Version: {}\n'.format(tool_version)
        msg += 'Project: {}\n'.format(project_name)
        msg += 'DCC Name: {}\n'.format(dcc_name)
        msg += 'DCC Version: {}\n'.format(dcc_version)
        msg += 'Department: {}\n'.format(department)
        msg += 'Computer Name: {}\n'.format(node)
        msg += 'Platform Release: {}\n'.format(os_release)
        msg += 'Platform Version: {}\n'.format(os_version)
        msg += 'Processor: {}\n'.format(os_processor)
        msg += 'Machine: {}\n'.format(os_machine)
        msg += 'Python Executable: {}\n'.format(executable)
        msg += 'Steps: \n{}\n'.format(steps)

        if tool_name:
            subject = '[{}][Bug][{}]({}) - {}'.format(project_name, tool_name, user, title)
        else:
            subject = '[{}][Bug]({}) - {}'.format(project_name, user, title)

        webbrowser.open(
            "mailto:{}?subject={}&body={}".format(';'.join(self._project.emails), subject, quote(str(msg))))

    def _get_bug_data_for_sentry(self):
        os_data = self._get_base_bug_data()
        cpu_data = ArtellaBugTracker.CPU_INFO if ArtellaBugTracker.CPU_INFO else dict()
        gpu_data = ArtellaBugTracker.GPU_INFO if ArtellaBugTracker.GPU_INFO else dict()
        disk_data = self._get_disk_usage()
        disk_data = disk_data if disk_data else dict()

        return os_data, cpu_data, gpu_data, disk_data

    def _send_sentry_bug(self):

        if not self._project:
            LOGGER.warning('Impossible to send bug because there is project defined')
            return False

        if not self._main:
            LOGGER.warning('No main widget defined')
            return False

        current_data = self._main.get_current_data()
        if not current_data:
            LOGGER.warning('No data available to send ...')
            return False

        tool_name = current_data.get('tool', {}).get('name', None)
        tool_version = current_data.get('tool', {}).get('version', 'unknown')
        if not tool_name:
            LOGGER.warning('Impossible to send bug because tool name ({}) is not valid ({})'.format(tool_name))
            return False

        import sentry_sdk
        from sentry_sdk import push_scope, capture_message

        bugtracker_sentry_id = self._main.config.data.get('sentry_id')

        sentry_id = None
        if self._main.has_tool():
            sentry_id = self._main.tool.config.data.get('sentry_id', None)
        else:
            tool_config = current_data.get('tool', {}).get('config', None)
            if tool_config and hasattr(tool_config, 'data'):
                sentry_id = tool_config.data.get('sentry_id', None)

        if not sentry_id:
            LOGGER.warning('No Sentry ID found for tool: "{}". Bug will be reported as a generic one ...')
            sentry_id = bugtracker_sentry_id

        if not sentry_id:
            LOGGER.warning("Sentry ID is not available! Sending request using email ...")
            return self._send_email_request()

        sentry_sdk.init(sentry_id)

        project_name = self._project.name.title()

        department = current_data.get('department', None)
        steps = self._steps_area.toPlainText()
        user = str(osplatform.get_user())
        title = self._title_line.text()
        dcc_name = tp.Dcc.get_name()
        dcc_version = tp.Dcc.get_version()

        if not tool_name or not department:
            LOGGER.warning(
                'Impossible to send request because tool name ({}) or department are not valid ({})'.format(
                    tool_name, department))
            return False

        msg = '[{}][Bug][{}]({}) - {}'.format(project_name, tool_name, user, title)

        with push_scope() as scope:
            scope.user = {'username': user}
            scope.level = 'error'
            scope.set_tag('type', 'bug')
            scope.set_tag('project', project_name)
            scope.set_tag('department', department)
            scope.set_tag('dcc', dcc_name)
            scope.set_tag('dcc_version', dcc_version)
            scope.set_tag('version', tool_version)
            scope.set_tag('tool', tool_name)
            scope.set_extra('project', project_name)
            scope.set_extra('department', department)
            scope.set_extra('tool', tool_name)
            scope.set_extra('version', tool_version)
            scope.set_extra('steps', steps)
            scope.set_extra('trace', self._trace_text.toPlainText())
            scope.set_extra('dcc_data', {'name': dcc_name, 'version': dcc_version})

            os_data, cpu_data, gpu_data, disk_data = self._get_bug_data_for_sentry()
            if os_data:
                scope.set_extra('os_data', os_data)
            if cpu_data:
                scope.set_extra('cpu_data', cpu_data)
            if gpu_data:
                scope.set_extra('gpu_data', gpu_data.get('gpus', dict()))
            if disk_data:
                scope.set_extra('disk_data', disk_data.get('drives', dict()))

            capture_message(msg)

        sentry_sdk.init(bugtracker_sentry_id)

        return True

    def _on_send_bug(self):
        """
        Internal callback function that is called when the user press Send Bug button
        """

        try:
            import sentry_sdk
        except ImportError as exc:
            self._send_email_bug()
            LOGGER.info('Bug send through email successfully!')
            self._main.close_tool_attacher()
            return

        self._send_sentry_bug()
        LOGGER.info('Bug send successfully!')

        self._main.close_tool_attacher()


class RequestWidget(base.BaseWidget, object):
    def __init__(self, main, project, parent=None):

        self._project = project
        self._main = main

        super(RequestWidget, self).__init__(parent=parent)

    def ui(self):
        super(RequestWidget, self).ui()

        self._title_line = QLineEdit()
        self._title_line.setPlaceholderText('Short title for the request ...')
        self._request_area = QTextEdit()
        txt_msg = 'Explain with details your request ...'
        request_lbl = QLabel(txt_msg)
        if qtutils.is_pyside2():
            self._request_area.setPlaceholderText(txt_msg)
        self._request_area.setMinimumHeight(100)

        self._send_btn = QPushButton('Send Request')
        self._send_btn.setIcon(tp.ResourcesMgr().icon('message'))
        self._send_btn.setEnabled(False)

        self.main_layout.addWidget(self._title_line)
        if qtutils.is_pyside():
            self.main_layout.addWidget(request_lbl)
        self.main_layout.addWidget(self._request_area)
        self.main_layout.addLayout(splitters.SplitterLayout())
        self.main_layout.addWidget(self._send_btn)

    def setup_signals(self):
        self._title_line.textChanged.connect(self._update_ui)
        self._request_area.textChanged.connect(self._update_ui)
        self._send_btn.clicked.connect(self._on_send_request)

    def _update_ui(self):
        """
        Internal function that updates Artella Bug Tracker UI
        """

        self._send_btn.setEnabled(self._request_area.toPlainText() != '' and self._title_line.text() != '')

    def _send_sentry_request(self):
        if not self._project:
            LOGGER.warning('Impossible to send bug because there is project defined')
            return False

        if not self._main:
            LOGGER.warning('No main widget defined')
            return False

        current_data = self._main.get_current_data()
        if not current_data:
            LOGGER.warning('No data available to send ...')
            return False

        tool_name = current_data.get('tool', {}).get('name', None)
        tool_version = current_data.get('tool', {}).get('version', 'unknown')
        if not tool_name:
            LOGGER.warning('Impossible to send request because tool name ({}) is not valid ({})'.format(tool_name))
            return False

        import sentry_sdk
        from sentry_sdk import push_scope, capture_message

        bugtracker_sentry_id = self._main.config.data.get('sentry_id')

        sentry_id = None
        if self._main.has_tool():
            sentry_id = self._main.tool.config.data.get('sentry_id', None)
        else:
            tool_data = artellapipe.ToolsMgr().get_tool_data_from_name(tool_name)
            if not tool_data:
                LOGGER.warning('No data found for tool: "{}"'.format(tool_name))
                return False
            tool_config = tool_data.get('config', None)
            if tool_config and hasattr(tool_config, 'data'):
                sentry_id = tool_config.data.get('sentry_id', None)

        if not sentry_id:
            LOGGER.warning('No Sentry ID found for tool: "{}". Bug will be reported as a generic one ...')
            sentry_id = bugtracker_sentry_id

        if not sentry_id:
            LOGGER.warning("Sentry ID is not available! Sending request using email ...")
            return self._send_email_request()

        sentry_sdk.init(sentry_id)

        project_name = self._project.name.title()

        department = current_data.get('department', None)
        request = self._request_area.toPlainText()
        user = str(osplatform.get_user())
        title = self._title_line.text()
        dcc_name = tp.Dcc.get_name()
        dcc_version = tp.Dcc.get_version()

        if not tool_name or not department:
            LOGGER.warning(
                'Impossible to send request because tool name ({}) or department are not valid ({})'.format(
                    tool_name, department))
            return False

        msg = '[{}][Request][{}]({}) - {}'.format(project_name, tool_name, user, title)

        with push_scope() as scope:
            scope.user = {'username': user}
            scope.level = 'info'
            scope.set_tag('type', 'request')
            scope.set_tag('project', project_name)
            scope.set_tag('dcc', dcc_name)
            scope.set_tag('dcc_version', dcc_version)
            scope.set_tag('version', tool_version)
            scope.set_tag('tool', tool_name)
            scope.set_tag('department', department)
            scope.set_tag('tool', tool_name)
            scope.set_extra('project', project_name)
            scope.set_extra('department', department)
            scope.set_extra('tool', tool_name)
            scope.set_extra('version', tool_version)
            scope.set_extra('request', request)
            scope.set_extra('dcc_data', {'name': tp.Dcc.get_name(), 'version': tp.Dcc.get_version()})
            capture_message(msg)

        sentry_sdk.init(bugtracker_sentry_id)

        return True

    def _send_email_request(self):
        if not self._project:
            LOGGER.warning('Impossible to send bug because there is project defined')
            return
        project_name = self._project.name.title()
        if not self._project.emails:
            LOGGER.warning(
                'Impossible to send bug because there is no emails defined in the project: {}'.format(project_name))
            return

        project_name = self._project.name.title()

        current_data = self._main.get_current_data()
        if not current_data:
            LOGGER.warning('No data available to send ...')
            return False

        tool_name = current_data.get('tool', {}).get('name', None)
        tool_version = current_data.get('tool', {}).get('version', 'unknown')
        department = current_data.get('department', None)
        request = self._request_area.toPlainText()
        user = str(osplatform.get_user())
        title = self._title_line.text()
        current_time = str(datetime.datetime.now())
        node = platform.node()
        os_release = platform.release()
        os_version = platform.platform()
        os_processor = platform.processor()
        os_machine = platform.machine()
        executable = sys.executable
        dcc_name = tp.Dcc.get_name()
        dcc_version = tp.Dcc.get_version()

        msg = ''
        msg += 'User: {}\n'.format(user)
        msg += 'Time: {}\n'.format(current_time)
        msg += 'Tool: {}\n'.format(tool_name)
        msg += 'Version: {}\n'.format(tool_version)
        msg += 'Project: {}\n'.format(project_name)
        msg += 'DCC Name: {}\n'.format(dcc_name)
        msg += 'DCC Version: {}\n'.format(dcc_version)
        msg += 'Department: {}\n'.format(department)
        msg += 'Computer Name: {}\n'.format(node)
        msg += 'Platform Release: {}\n'.format(os_release)
        msg += 'Platform Version: {}\n'.format(os_version)
        msg += 'Processor: {}\n'.format(os_processor)
        msg += 'Machine: {}\n'.format(os_machine)
        msg += 'Python Executable: {}\n'.format(executable)
        msg += 'Request: \n{}\n'.format(request)

        if tool_name:
            subject = '[{}][Request][{}]({}) - {}'.format(project_name, tool_name, user, title)
        else:
            subject = '[{}][Request]({}) - {}'.format(project_name, user, title)

        webbrowser.open(
            "mailto:{}?subject={}&body={}".format(';'.join(self._project.emails), subject, quote(str(msg))))

    def _on_send_request(self):
        """
        Internal callback function that is called when the user press Send Request button
        """

        try:
            import sentry_sdk
        except ImportError as exc:
            self._send_email_request()
            LOGGER.info('Request send through email successfully!')
            self._main.close_tool_attacher()
            return

        self._send_sentry_request()
        LOGGER.info('Request send successfully!')
        self._main.close_tool_attacher()
