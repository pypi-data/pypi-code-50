# Copyright 2018 Jetperch LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# https://stackoverflow.com/questions/11874767/real-time-plotting-in-while-loop-with-matplotlib
# https://wiki.qt.io/Gallery_of_Qt_CSS_Based_Styles

import os
import platform
import sys
from . import __version__
import joulescope
from PySide2 import QtCore, QtGui, QtWidgets
from joulescope_ui.error_window import Ui_ErrorWindow
from joulescope_ui.main_window import Ui_mainWindow
from joulescope_ui.widgets import widget_register
from joulescope.usb import DeviceNotify
from joulescope_ui.data_recorder_process import DataRecorderProcess as DataRecorder
from joulescope.data_recorder import construct_record_filename  # DataRecorder
from joulescope_ui.recording_viewer_device import RecordingViewerDevice
from joulescope_ui.preferences_ui import PreferencesDialog
from joulescope_ui.update_check import check as software_update_check
from joulescope_ui.logging_util import logging_preconfig, logging_config, LOG_PATH, logging_start
from joulescope_ui.range_tool import RangeToolInvoke
from joulescope_ui import help_ui
from joulescope_ui import firmware_manager
from joulescope_ui.plugin_manager import PluginManager
from joulescope_ui.exporter import Exporter
from joulescope_ui.command_processor import CommandProcessor
from joulescope_ui.preferences_def import preferences_def
from joulescope_ui.preferences_defaults import defaults as preference_defaults
from joulescope_ui import ui_util
import io
import ctypes
import collections
import gc
import pyperclip
import traceback
import time
import webbrowser
import logging
log = logging.getLogger(__name__)


STATUS_BAR_TIMEOUT = 5000  # milliseconds
USERS_GUIDE_URL = "https://download.joulescope.com/docs/JoulescopeUsersGuide/index.html"
FRAME_LIMIT_DELAY_MS = 30
FRAME_LIMIT_MAXIMUM_DELAY_MS = 2000


ABOUT = """\
<html>
Joulescope UI version {ui_version}<br/> 
Joulescope driver version {driver_version}<br/>
<a href="https://www.joulescope.com">https://www.joulescope.com</a>

<pre>
Copyright 2018-2019 Jetperch LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
</pre>
</html>
"""


SOFTWARE_UPDATE = """\
<html>
<p>
A software update is available:<br/>
Current version = {current_version}<br/>
Available version = {latest_version}<br/>
Channel = {channel}<br/>
</p>
<p><a href="{url}">Download</a> now.</p>
</html>
"""


STARTUP_ERROR_MESSAGE = """\
<html><body>
<h2>Unexpected Error</h2>
<p>The Joulescope UI encountered an error,<br/>
and it cannot start correctly.<p>
<p>Please report this error by contacting us:
<ul>
   <li><a href="https://www.joulescope.com/contact">Contact form</a></li>
   <li><a href="https://forum.joulescope.com/">Joulescope forum</a></li>
   <li><a href="https://github.com/jetperch/pyjoulescope_ui/issues">GitHub</a></li>
</ul>
</p>
<p>Please include the text below,<br/>
which has been automatically copied to your clipboard.</p>
<pre>
{msg_err}
</pre>
</body></html>
"""


TOOLTIP_NO_SOURCE = """\
No data source selected.
Connect a Joulescope or 
open a file."""


class ValueLabel(QtWidgets.QLabel):

    def __init__(self, parent=None, text=''):
        QtWidgets.QLabel.__init__(self, parent)
        self._text = text

    def set(self, value):
        self.setText('%s=%-8.2f' % (self._text, value))


def dict_update_recursive(tgt, src):
    """Merge src into tgt, overwriting as needed.

    :param tgt: The target dict.
    :param src: the source dict.
    """
    for key, value in src.items():
        if key in tgt and isinstance(tgt[key], dict) and isinstance(value, collections.Mapping):
            dict_update_recursive(tgt[key], value)
        else:
            tgt[key] = value


class DeviceDisable:

    def __str__(self):
        return "disable"

    def close(self):
        pass


def dock_widget_parse_str(s):
    if not isinstance(s, str):
        raise ValueError('dock_widget_parse_str value %s' % (s, ))
    parts = s.split(':')
    if len(parts) == 1:
        return parts[0], None
    elif len(parts) == 2:
        return parts
    else:
        raise ValueError('Unsupported value %s', s)


class MyDockWidget(QtWidgets.QDockWidget):

    def __init__(self, parent, widget_def, cmdp, instance_id):
        self.instance_id = int(instance_id)
        self.name = widget_def['name']
        QtWidgets.QDockWidget.__init__(self, self.name, parent)
        self.setObjectName(str(self))
        self._parent = parent
        self._cmdp = cmdp
        self.widget_def = widget_def

        self.inner_widget = widget_def['class'](self, cmdp, self.state_preference)
        self.inner_widget.setObjectName(str(self) + "__inner__")
        self.setWidget(self.inner_widget)
        self.dockLocationChanged.connect(self._on_dock_location_changed)

    def __str__(self):
        return f'{self.name}:{self.instance_id}'

    @property
    def state_preference(self):
        return f'Widgets/_state/{self}'

    def _on_dock_location_changed(self, area):
        self._parent._window_state_update()

    def resizeEvent(self, event):
        self._parent._window_state_update()

    def dock_widget_close(self):
        if not self.widget_def.get('singleton', False):
            self.widget_def['dock_widget'] = None
            self.widget_def = None
            self.inner_widget = None
            self._cmdp = None
            self._parent = None
            self.deleteLater()

    def closeEvent(self, event):
        if self.isVisible():
            log.info('MyDockWidget.closeEvent for %s', self)
            self._cmdp.invoke('!Widgets/remove', str(self))
            event.ignore()
        elif not self.widget_def.get('singleton', False):
            log.info('MyDockWidget.closeEvent for %s', self)
            QtWidgets.QDockWidget.closeEvent(self, event)
            self.dock_widget_close()
        else:
            log.info('MyDockWidget.closeEvent for %s', self)


class MainWindow(QtWidgets.QMainWindow):
    on_deviceNotifySignal = QtCore.Signal(object, object)
    _deviceOpenRequestSignal = QtCore.Signal(object)
    _deviceScanRequestSignal = QtCore.Signal()
    on_stopSignal = QtCore.Signal(int, str)
    on_statisticSignal = QtCore.Signal(object)
    on_softwareUpdateSignal = QtCore.Signal(str, str, str)
    on_deviceEventSignal = QtCore.Signal(int, str)  # event, message

    on_progressValue = QtCore.Signal(int)
    on_progressMessage = QtCore.Signal(str)

    def __init__(self, app, device_name, cmdp, multiprocessing_logging_queue):
        self._app = app
        self._device_scan_name = 'joulescope' if device_name is None else str(device_name)
        self._multiprocessing_logging_queue = multiprocessing_logging_queue
        self._devices = []
        self._device = None
        self._streaming_status = None
        self._fps_counter = 0
        self._fps_time = None
        self._fps_limit_timer = QtCore.QTimer()
        self._fps_limit_timer.setSingleShot(True)
        self._fps_limit_timer.timeout.connect(self.on_fpsTimer)

        self._profile_actions = []
        self._profile_action_group = None

        self._parameters = {}
        self._data_view = None  # created when device is opened
        self._recording = None  # created to record stream to JLS file
        self._accumulators = {
            'time': 0.0,
            'fields': {
                'charge': [0.0, 0.0],  # accumulated value, last stats value
                'energy': [0.0, 0.0],  # accumulated value, last stats value
            },
        }
        self._is_scanning = False
        self._progress_dialog = None

        self._cmdp = cmdp
        self._plugins = PluginManager(self._cmdp)
        self._cmdp.publish('Plugins/#registered', self._plugins)

        super(MainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        # Central widget to keep top at top
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setMaximumWidth(1)
        self.setCentralWidget(self.central_widget)

        self.on_deviceNotifySignal.connect(self.device_notify)
        self._deviceOpenRequestSignal.connect(self.on_deviceOpen, type=QtCore.Qt.QueuedConnection)
        self._deviceScanRequestSignal.connect(self.on_deviceScan, type=QtCore.Qt.QueuedConnection)

        self._widget_defs = widget_register(self._cmdp)
        self._widgets = []

        # must be after other preferences so applied last
        self._cmdp.define('_window', brief='UI window configuration', dtype='obj', default=None)

        preference_defaults(self._cmdp.preferences)
        self._view_menu()

        self._cmdp.subscribe('Device/#state/source', self._device_state_source)
        self._cmdp.subscribe('Device/#state/sample_drop_color', self._device_state_color)
        self._cmdp.subscribe('Device/#state/name', self._on_device_state_name)
        self._cmdp.subscribe('Device/#state/play', self._on_device_state_play)
        self._cmdp.subscribe('Device/#state/record', self._on_device_state_record)
        self._cmdp.subscribe('Widgets/Waveform/#requests/data_next', self._on_waveform_requests_data_next)
        self._cmdp.subscribe('!preferences/profile/add', self._on_preferences_profile_add)
        self._cmdp.subscribe('!preferences/profile/remove', self._on_preferences_profile_remove)
        self._cmdp.subscribe('!preferences/profile/set', self._on_preferences_profile_set)
        self._cmdp.subscribe('Widgets/active', self._on_widgets_active)
        self._cmdp.subscribe('_window', self._on_window_state)
        self._cmdp.subscribe('General/developer', self._on_general_developer)

        # Main implements the DataView bindings
        self._cmdp.subscribe('DataView/#service/x_change_request', self._on_dataview_service_x_change_request)
        self._cmdp.subscribe('DataView/#service/range_statistics', self._on_dataview_service_range_statistics)

        self._cmdp.register('!RangeTool/run', self._cmd_range_tool_run,
                            brief='Run a range tool over a data region.',
                            detail='The value is a dict with the keys:\n' +
                                   'name: The name string for the tool.\n' +
                                   'x_start: The starting position, in view x-axis coordinates\n' +
                                   'x_stop: The stopping position, in view x-axis coordinates')

        self._cmdp.register('!Widgets/add', self._widgets_add_cmd,
                            brief='Add a main window widget',
                            detail='The value is the widget name.',
                            record_undo=True)
        self._cmdp.register('!Widgets/remove', self._widgets_remove_cmd,
                            brief='Remove a main window widget',
                            detail='The value is the widget or widget name string.',
                            record_undo=True)

        # Device selection
        self.device_action_group = QtWidgets.QActionGroup(self)
        self._device_disable = DeviceDisable()
        self._device_add(self._device_disable)

        # Other menu items
        self.ui.actionOpen.triggered.connect(self.on_recording_open)
        self.ui.actionPreferences.triggered.connect(self.on_preferences)
        self.ui.actionExit.triggered.connect(self.close)

        # status update timer
        self.status_update_timer = QtCore.QTimer(self)
        self.status_update_timer.setInterval(500)  # milliseconds
        self.status_update_timer.timeout.connect(self.on_statusUpdateTimer)
        self.status_update_timer.start()

        # Status bar
        self._source_indicator = QtWidgets.QLabel(self.ui.statusbar)
        self.ui.statusbar.addPermanentWidget(self._source_indicator)

        # device scan timer - because bad things happen, see rescan_interval config
        self.rescan_timer = QtCore.QTimer(self)
        self.rescan_timer.timeout.connect(self.on_rescanTimer)

        self.on_stopSignal.connect(self._on_stop, type=QtCore.Qt.QueuedConnection)
        self.on_statisticSignal.connect(self._on_statistic, type=QtCore.Qt.QueuedConnection)
        self.on_deviceEventSignal.connect(self._on_device_event, type=QtCore.Qt.QueuedConnection)

        # Software update
        self.on_softwareUpdateSignal.connect(self._on_software_update, type=QtCore.Qt.QueuedConnection)

        # help
        self.ui.actionGettingStarted.triggered.connect(self._help_getting_started)
        self.ui.actionUsersGuide.triggered.connect(self._help_users_guide)
        self.ui.actionViewLogs.triggered.connect(self._view_logs)
        self.ui.actionCredits.triggered.connect(self._help_credits)
        self.ui.actionAbout.triggered.connect(self._help_about)

        # tools
        self.ui.actionClearEnergy.triggered.connect(self._accumulators_zero_total)
        with self._plugins as p:
            p.range_tool_register('Export data', Exporter)
        self._plugins.builtin_register()
        self._device_close()

        # Add global keyboard shortcuts for the application
        # Attempted app.installEventFilter(self) with def eventFilter
        # but need to handle gets ShortcutOverride, KeyPress, KeyRelease, multiple times
        self._shortcut_undo = QtWidgets.QShortcut(QtGui.QKeySequence.Undo, self)
        self._shortcut_undo.activated.connect(lambda: self._cmdp.invoke('!undo'))
        self._shortcut_redo = QtWidgets.QShortcut(QtGui.QKeySequence.Redo, self)
        self._shortcut_redo.activated.connect(lambda: self._cmdp.invoke('!redo'))

        if not self._cmdp.restore_success:
            self.status('Could not restore preferences - using defaults', timeout=0)

    def _path(self):
        """Get the data_path.

        :return: The data path, which is guaranteed to be valid.
        :raise ValueError: If no valid path can be found.

        Side-effect: will update 'General/data_path' parameters if the
        configured path is not available.
        """
        config_path = self._cmdp['General/data_path']
        paths = [config_path,
                 self._cmdp.preferences.definition_get('General/data_path')['default'],
                 os.getcwd()]
        for path in paths:
            try:
                if not os.path.isdir(path):
                    os.makedirs(path, exist_ok=True)
                if config_path != path:
                    self._cmdp['General/data_path'] = path
                return path
            except:
                log.info('Invalid path: %s', path)
        raise ValueError('No path found')

    def _profile_view_menu_factory(self, profile):

        def menu_fn(checked):
            if checked:
                self._cmdp.invoke('!preferences/profile/set', profile)

        return menu_fn

    def _on_preferences_profile_set(self, topic, value):
        self._view_menu()

    def _on_preferences_profile_add(self, topic, value):
        self._view_menu()

    def _on_preferences_profile_remove(self, topic, value):
        self._view_menu()

    def _on_general_developer(self, topic, value):
        self._view_menu()

    def _view_menu(self):
        self._profile_action_group = None
        self._profile_actions = []
        menu = self.ui.menuView
        menu.clear()

        developer = self._cmdp['General/developer']
        self._profile_action_group = QtWidgets.QActionGroup(menu)
        self._profile_action_group.setExclusive(True)
        for profile in sorted(self._cmdp.preferences.profiles):
            if profile == 'defaults':
                continue
            action = menu.addAction(profile)
            action.setCheckable(True)
            self._profile_action_group.addAction(action)
            if profile == self._cmdp.preferences.profile:
                action.setChecked(True)
            action.triggered.connect(self._profile_view_menu_factory(profile))
            self._profile_actions.append(action)

        self._profile_menu_separator = menu.addSeparator()
        for widget_def in self._widget_defs.values():
            widget_def['action'] = None  # clear any existing action reference
            widget_def.setdefault('dock_widget', None)
            if not developer and 'developer' in widget_def.get('permissions', []):
                continue
            self._widget_view_menu_factory(menu, widget_def)

    def _widget_view_menu_factory(self, menu, widget_def):
        name = widget_def['name']
        action = menu.addAction(name)
        widget_def['action'] = action

        def menu_fn(checked):
            if checked or not widget_def.get('singleton', False):
                self._cmdp.invoke('!Widgets/add', name)
            elif widget_def.get('singleton', False):
                self._cmdp.invoke('!Widgets/remove', name)

        if widget_def.get('singleton', False):
            action.setCheckable(True)
            dock_widget = widget_def.get('dock_widget')
            if dock_widget is not None and dock_widget.isVisible():
                action.setChecked(True)
            action.toggled.connect(menu_fn)
        else:
            action.triggered.connect(menu_fn)

    @property
    def _is_streaming(self):
        return self._streaming_status is not None

    @property
    def _is_streaming_device(self):
        return hasattr(self._device, 'start')

    def run(self, filename=None):
        if filename is not None:
            self._recording_open(filename)
            self._cmdp.publish('!preferences/profile/set', 'Oscilloscope')
        else:
            self._on_widgets_active('Widgets/active', self._cmdp['Widgets/active'])
            self._on_window_state('_window', self._cmdp['_window'])
        self._software_update_check()
        log.debug('Qt show()')
        self.show()
        log.debug('Qt show() success')
        self._device_scan()

    @QtCore.Slot()
    def on_statusUpdateTimer(self):
        if self._has_active_device and hasattr(self._device, 'status'):
            try:
                s = self._device.status()
                if s['driver']['return_code']['value']:
                    self._device_recover()
                    return
                self._status_fn(s)
            except:
                log.exception("statusUpdateTimer failed - assume device error")
                self._device_recover()
                return

    @QtCore.Slot()
    def on_rescanTimer(self):
        log.debug('rescanTimer')
        self._device_scan()

    def _on_waveform_requests_data_next(self, topic, data):
        self._fps_counter += 1
        if self._is_streaming and self._data_view is not None:
            self._fps_limit_timer.stop()
            # help to limit the frame rate for smoother animation
            # consider adding adaptive filter to handle processing glitches
            self._fps_limit_timer.start(FRAME_LIMIT_DELAY_MS)

    @QtCore.Slot()
    def on_fpsTimer(self):
        if self._is_streaming and self._data_view is not None:
            self._data_view.refresh()
            self._fps_limit_timer.start(FRAME_LIMIT_MAXIMUM_DELAY_MS)

    @QtCore.Slot(object)
    def _on_statistic(self, statistics):
        self._accumulators['time'] += statistics['time']['delta']['value']
        statistics['time']['accumulator'] = {'value': self._accumulators['time'], 'units': 's'}
        for field in ['charge', 'energy']:
            d = statistics['accumulators'][field]
            x = d['value']
            z = self._accumulators['fields'][field]
            z[0] += x - z[1]
            z[1] = x
            d['value'] = z[0]
        self._cmdp.publish('Device/#state/statistics', statistics)

    def _on_dataview_service_x_change_request(self, topic, value):
        # DataView/#service/x_change_request
        if value is None:
            return
        x_min, x_max, x_count = value
        log.info('_on_dataview_service_x_change_request(%s, %s, %s)', x_min, x_max, x_count)
        if self._data_view is not None:
            self._data_view.on_x_change('resize', {'pixels': x_count})
            self._data_view.on_x_change('span_absolute', {'range': [x_min, x_max]})

    @QtCore.Slot(object, object)
    def device_notify(self, inserted, info):
        log.info('Device notify')
        self._device_scan()

    def disable_floating(self):
        for widget in self._widgets:
            widget[0].setFloating(False)

    def _software_update_check(self):
        if self._cmdp['General/update_check']:
            channel = self._cmdp['General/update_channel']
            software_update_check(self.on_softwareUpdateSignal.emit, channel)

    def _on_software_update(self, current_version, latest_version, url):
        channel = self._cmdp['General/update_channel']
        log.info('_on_software_update(current_version=%r, latest_version=%r, channel=%s, url=%r)',
                 current_version, latest_version, channel, url)
        txt = SOFTWARE_UPDATE.format(current_version=current_version,
                                     latest_version=latest_version,
                                     channel=channel,
                                     url=url)
        QtWidgets.QMessageBox.about(self, 'Joulescope Software Update Available', txt)

    def _help_about(self):
        log.info('_help_about')
        txt = ABOUT.format(ui_version=__version__, driver_version=joulescope.VERSION)
        QtWidgets.QMessageBox.about(self, 'Joulescope', txt)

    def _help_credits(self):
        log.info('_help_credits')
        html = help_ui.load_credits()
        dialog = help_ui.ScrollMessageBox(html, self)
        dialog.setWindowTitle('Joulescope Credits')
        dialog.exec_()

    def _help_getting_started(self):
        log.info('_help_getting_started')
        html = help_ui.load_getting_started()
        dialog = help_ui.ScrollMessageBox(html, self)
        dialog.setWindowTitle('Getting Started with Your Joulescope')
        dialog.exec_()

    def _help_users_guide(self):
        log.info('_help_users_guide')
        webbrowser.open_new_tab(USERS_GUIDE_URL)

    def _view_logs(self):
        log.info('_view_logs(%s)', LOG_PATH)
        ui_util.show_in_folder(LOG_PATH)

    def _accumulators_zero_total(self):
        log.info('_accumulators_zero_total')
        self._accumulators['time'] = 0.0
        for z in self._accumulators['fields'].values():
            z[0] = 0.0  # accumulated value

    def _accumulators_zero_last(self):
        log.info('_accumulators_zero_last')
        for z in self._accumulators['fields'].values():
            z[1] = 0.0  # last update value

    def _device_state_source(self, topic, data):
        self._source_indicator.setText(f'  {data}  ')
        self._source_indicator.setToolTip(self._cmdp['Device/#state/name'])

    def _device_state_color(self, topic, data):
        if data is None or data == '':
            style = ""
        else:
            style = f"QLabel {{ background-color : {data} }}"
        self._source_indicator.setStyleSheet(style)

    @property
    def _has_active_device(self):
        return self._device not in [None, self._device_disable]

    def _device_open_failed(self, msg):
        self.status(msg)
        self._device_recover()
        return None

    @QtCore.Slot(int, str)
    def _on_device_event(self, event, msg):
        # Must connect with Qt.QueuedConnection since likely called from the
        # device's python data thread.
        level = logging.WARNING if event > 0 else logging.INFO
        log.log(level, '_on_device_event(%r, %r)', event, msg)

    def _on_device_state_name(self, topic, data):
        self.setWindowTitle(f'Joulescope: {data}')

    def _device_open(self, device):
        if self._device == device:
            log.info('device_open reopen %s', str(device))
            return
        self._device_close()
        log.info('device_open %s', str(device))
        self._accumulators_zero_last()
        self._device = device
        if self._has_active_device:
            if hasattr(self._device, 'parameter_set'):
                self._device.parameter_set('buffer_duration', self._cmdp['Device/setting/buffer_duration'])
                self._device.parameter_set('sampling_frequency', self._cmdp['Device/setting/sampling_frequency'])
            try:
                self._device.open(self.on_deviceEventSignal.emit)
            except:
                log.exception('while opening device')
                return self._device_open_failed('Could not open device')
            try:
                self._firmware_update_on_open()
            except:
                log.exception('firmware update failed')
                self._device_close()
                return
            try:
                self._cmdp.publish('Device/#state/name', str(self._device))
                if not self._device.ui_action.isChecked():
                    self._device.ui_action.setChecked(True)
                if hasattr(self._device, 'view_factory'):
                    data_view = self._device.view_factory()
                    data_view.on_update_fn = self._data_view_update_fn
                    data_view.open()
                    data_view.refresh()
                    self._cmdp.publish('Device/#state/x_limits', data_view.limits)
                    self._data_view = data_view
                if hasattr(self._device, 'statistics_callback'):
                    self._device.statistics_callback = self.on_statisticSignal.emit
                self._cmdp.subscribe('Device/setting/', self._on_device_parameter, update_now=True)
                self._cmdp.subscribe('Device/extio/', self._on_device_parameter, update_now=True)
                if self._is_streaming_device:
                    if self._cmdp['Device/autostream']:
                        self._cmdp.publish('Device/#state/source', 'USB')
                        self._cmdp.publish('Device/#state/play', True)
                    else:
                        self._cmdp.publish('Device/#state/source', 'Buffer')
            except:
                log.exception('while initializing after open device')
                return self._device_open_failed('Could not initialize device')

    def _data_view_update_fn(self, data):
        self._cmdp.publish('DataView/#data', data)

    def _on_device_parameter(self, topic, value):
        if not hasattr(self._device, 'parameter_set'):
            return
        topic = topic.split('/')[-1]
        while topic.startswith('_'):
            topic = topic[1:]
        try:
            self._device.parameter_set(topic, value)
        except Exception:
            log.exception('during parameter_set')
            self.status('Parameter set %s failed, value=%s' % (topic, value))
            self._device_recover()

    def _device_close(self):
        log.debug('_device_close: start')
        self._cmdp.unsubscribe('Device/setting/', self._on_device_parameter)
        self._cmdp.unsubscribe('Device/extio/', self._on_device_parameter)
        device = self._device
        is_active_device = self._has_active_device
        self._device = self._device_disable
        log.info('device_close %s', str(device))
        if self._data_view is not None:
            self._data_view.close()
            self._data_view = None
        if device:
            on_close = self._cmdp['Device/on_close']
            try:
                if hasattr(device, 'status'):
                    if on_close == 'sensor_off':
                        device.parameter_set('sensor_power', 'off')
                    elif on_close == 'current_off':
                        device.parameter_set('i_range', 'off')
                    elif on_close == 'current_auto':
                        device.parameter_set('i_range', 'auto')
                    else:  # keep
                        pass
            except:
                log.warning('could not set Device.on_close behavior %s', on_close)
            device.close()

        if is_active_device and hasattr(device, 'ui_action') and device.ui_action.isChecked():
            device.ui_action.setChecked(False)
        if hasattr(device, 'ui_on_close'):
            device.ui_on_close()

        self._device_disable.ui_action.setChecked(True)
        self._accumulators_zero_last()
        self._cmdp.publish('Device/#state/name', '')
        self._cmdp.publish('Device/#state/source', 'None')
        self._cmdp.publish('Device/#state/sample_drop_color', '')
        self._cmdp.publish('Device/#state/play', False)
        self._cmdp.publish('Device/#state/record', False)
        gc.collect()  # safe time to force garbage collection
        gc.collect()
        log.debug('_device_close: done')

    def _device_recover(self):
        log.info('_device_recover: start')
        devices, self._devices = self._devices, []
        for device in devices:
            self._device_remove(device)
        self._deviceScanRequestSignal.emit()
        log.info('_device_recover: done')

    def _device_reopen(self):
        d = self._device
        self._device_close()
        self._deviceOpenRequestSignal.emit(d)

    @QtCore.Slot(object)
    def on_deviceOpen(self, d):
        self._device_open(d)

    def _device_add(self, device):
        """Add device to the user interface"""
        log.info('_device_change add %s', device)
        action = QtWidgets.QAction(str(device), self)
        action.setCheckable(True)
        action.setChecked(False)
        action.triggered.connect(lambda x: self._device_open(device))
        self.device_action_group.addAction(action)
        self.ui.menuDevice.addAction(action)
        device.ui_action = action

    def _device_remove(self, device):
        """Remove the device from the user interface"""
        log.info('_device_change remove')
        self.device_action_group.removeAction(device.ui_action)
        self.ui.menuDevice.removeAction(device.ui_action)
        if self._device == device:
            self._device_close()
        device.ui_action.triggered.disconnect()

    def _bootloader_scan(self):
        try:
            bootloaders = joulescope.scan('bootloader')
        except:
            return
        if not len(bootloaders):
            return

        log.info('Found %d Joulescope bootloaders', len(bootloaders))
        data = firmware_manager.load()

        if data is None:
            # no firmware, just attempt to kick into existing application
            for b in list(bootloaders):
                try:
                    b.open()
                except:
                    log.exception('while attempting to open bootloader')
                    continue
                try:
                    b.go()
                except:
                    log.exception('while attempting to run the application')
            return False

        for b in list(bootloaders):
            self.status('Programming firmware')
            try:
                b.open()
            except:
                log.exception('while attempting to open bootloader')
                continue
            try:
                self._firmware_update(b)
            except:
                log.exception('while attempting to run the application')

    def _device_scan(self):
        """Scan for new physical Joulescope devices."""
        if self._is_scanning:
            log.info('_device_scan already in progress')
            return
        log.info('_device_scan start')
        try:
            self._is_scanning = True
            self._bootloader_scan()
            physical_devices = [d for d in self._devices if hasattr(d, 'usb_device')]
            virtual_devices = [d for d in self._devices if not hasattr(d, 'usb_device')]
            devices, added, removed = joulescope.scan_for_changes(name=self._device_scan_name, devices=physical_devices)
            if self._device in removed:
                self._device_close()
            for d in removed:
                self._device_remove(d)
            for d in added:
                self._device_add(d)
            self._devices = virtual_devices + devices
            log.info('current device = %s, %s', self._device, self._device is self._device_disable)
            if self._device is self._device_disable and len(devices):
                log.info('device_scan activate first device %s', devices[0])
                devices[0].ui_action.trigger()
        finally:
            self._is_scanning = False
        log.info('_device_scan done')

    @QtCore.Slot()
    def on_deviceScan(self):
        self._device_scan()

    def _progress_dialog_construct(self):
        dialog = QtWidgets.QProgressDialog()
        dialog.setCancelButton(None)
        dialog.setWindowTitle('Joulescope')
        dialog.setLabelText('Firmware update in progress\nDo not unplug or turn off power')
        dialog.setRange(0, 1000)
        width = QtGui.QFontMetrics(dialog.font()).width('Do not unplug or turn off power') + 100
        dialog.resize(width, dialog.height())
        self._progress_dialog = dialog
        return dialog

    def _progress_dialog_finalize(self):
        self.on_progressValue.disconnect()
        self.on_progressMessage.disconnect()
        self._progress_dialog = None

    def _firmware_update_on_open(self):
        if not hasattr(self._device, 'parameters'):
            return
        firmware_update_cfg = self._cmdp['Device/firmware_update']
        if firmware_update_cfg in ['off', 'never'] or not bool(firmware_update_cfg):
            log.info('Skip firmware update: %s', firmware_update_cfg)
            return
        info = self._device.info()
        ver = None
        ver_required = firmware_manager.version_required()
        if info is not None and firmware_update_cfg != 'always':
            ver = info.get('ctl', {}).get('fw', {}).get('ver', '0.0.0')
            try:
                ver = tuple([int(x) for x in ver.split('.')])
            except ValueError:
                log.warning('Unsupported version %s', ver)
                return
            if ver >= ver_required:
                log.info('controller firmware is up to date: %s >= %s', ver, ver_required)
                return
        log.info('firmware update required: %s < %s', ver, ver_required)
        self.status('Firmware update required')
        self._device, d = None, self._device
        self._firmware_update(d)
        d.open()
        self._device = d

    def _firmware_update(self, device):
        data = firmware_manager.load()
        if data is None:
            self.status('Firmware update required, but could not find firmware image')
            return False

        dialog = self._progress_dialog_construct()
        progress = {
            'stage': '',
            'device': None,
        }

        self.on_progressValue.connect(dialog.setValue)
        self.on_progressMessage.connect(self.status)

        def progress_cbk(value):
            self.on_progressValue.emit(int(value * 1000))
            self.on_progressMessage.emit('Firmware upgrade [%.1f%%] %s' % (value * 100, progress['stage']))

        def stage_cbk(s):
            progress['stage'] = s

        def done_cbk(d):
            progress['device'] = d
            if d is None:
                self.on_progressMessage.emit('Firmware upgrade failed - unplug and retry')
            dialog.accept()

        self._is_scanning, is_scanning = True, self._is_scanning
        try:
            t = firmware_manager.upgrade(device, data, progress_cbk=progress_cbk, stage_cbk=stage_cbk, done_cbk=done_cbk)
            dialog.exec()
            t.join()
        finally:
            self._progress_dialog_finalize()
            self._is_scanning = is_scanning
            # self.status_update_timer.start()

    @QtCore.Slot(int, str)
    def _on_stop(self, event, message):
        log.debug('_on_stop(%d, %s)', event, message)
        self._cmdp.publish('Device/#state/play', False)

    def _device_stream_start(self):
        log.debug('_device_stream_start')
        if not self._has_active_device:
            log.warning('_device_stream_start when no device')
            return
        if not hasattr(self._device, 'start'):
            log.info('device does not support start')
            return
        self._accumulators_zero_last()
        self._streaming_status = {}
        self._cmdp.publish('Device/#state/sampling_frequency', self._device.sampling_frequency)
        try:
            self._device.start(stop_fn=self.on_stopSignal.emit)
        except Exception:
            log.exception('_device_stream_start')
            self.status('Could not start device streaming')
        self._cmdp.publish('Device/#state/source', 'USB')

    def _device_stream_stop(self):
        log.debug('_device_stream_stop')
        self._streaming_status = None
        if not self._has_active_device:
            log.info('_device_stream_stop when no device')
            return
        if hasattr(self._device, 'stop'):
            self._device.stop()  # always safe to call
        self._cmdp.publish('Device/#state/source', 'Buffer')
        self._cmdp.publish('Device/#state/sample_drop_color', '')

    def _on_device_state_play(self, topic, checked):
        log.info('_on_device_state_play(%s, %s)', topic, checked)
        if not self._is_streaming_device:
            return
        elif checked and not self._is_streaming:
            self._device_stream_start()
        elif not checked and self._is_streaming:
            self._device_stream_stop()

    def _device_can_record(self):
        return self._has_active_device and hasattr(self._device, 'stream_process_register')

    def _device_stream_record_start(self, filename):
        self._device_stream_record_close()
        if self._device_can_record():
            self._recording = DataRecorder(filename,
                                           calibration=self._device.calibration,
                                           multiprocessing_logging_queue=self._multiprocessing_logging_queue)
            self._device.stream_process_register(self._recording)
        else:
            log.warning('start recording failed for %s', filename)

    def _device_stream_record_close(self):
        if self._recording is not None:
            if self._has_active_device and hasattr(self._device, 'stream_process_unregister'):
                self._device.stream_process_unregister(self._recording)
            self._recording.close()
            self._recording = None

    def _device_stream_record_stop(self):
        self._device_stream_record_close()

    def _on_device_state_record(self, topic, enable):
        if enable:
            if self._device_can_record():
                self._device_stream_record_close()
                fname = construct_record_filename()
                path = os.path.join(self._path(), fname)
                filename, selected_filter = QtWidgets.QFileDialog.getSaveFileName(
                    self, 'Save Joulescope Recording', path, 'Joulescope Data (*.jls)')
                filename = str(filename)
                if not len(filename):
                    self.status('Invalid filename, do not record')
                    self._device_stream_record_stop()
                    self._cmdp.publish('Device/#state/record', False)
                else:
                    self._device_stream_record_start(filename)
            else:
                self.status('Selected device cannot record')
        elif not enable:
            self._device_stream_record_stop()

    def _save(self):
        if self._device is None:
            self.status('Device not open, cannot save buffer')
            return
        # Save the current buffer
        filename, selected_filter = QtWidgets.QFileDialog.getSaveFileName(
            self, 'Save Joulescope buffer', self._path(), 'Joulescope Data (*.jls)')
        filename = str(filename)
        if not len(filename):
            self.status('Invalid filename, do not open')
            return
        # todo

    def on_recording_open(self):
        filename, selected_filter = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open Joulescope Recording', self._path(), 'Joulescope Data (*.jls)')
        filename = str(filename)
        if not len(filename) or not os.path.isfile(filename):
            self.status('Invalid filename, do not open')
            return
        self._recording_open(filename)

    def _recording_open(self, filename):
        if filename is None:
            return
        self._device_close()
        log.info('open recording %s', filename)
        device = RecordingViewerDevice(filename)
        device.ui_on_close = lambda: self._device_remove(device)
        self._device_add(device)
        self._device_open(device)

        self._cmdp.publish('Device/#state/name', os.path.basename(filename))
        self._cmdp.publish('Device/#state/source', 'File')
        self._cmdp.publish('Device/#state/sample_drop_color', '')

    def _instance_id_next(self):
        """Get the next dock widget instance id.

        :return: The integer instance id which must be unique across all
            widgets that currently exist, even after restarting the
            application.
        """
        # Only used when creating a new widget, so performance is not critical.
        instance_ids = [w.instance_id for w in self._widgets]
        for widget_def in self._widget_defs.values():
            w = widget_def.get('dock_widget')
            if w is not None:
                instance_ids.append(w.instance_id)
        instance_id = 1
        while instance_id in instance_ids:
            instance_id += 1
        log.debug('_instance_id_next => %d', instance_id)
        return instance_id

    def _widget_str(self, widget_str):
        name, instance_id = dock_widget_parse_str(widget_str)
        if instance_id is None:
            instance_id = self._instance_id_next()
        return f'{name}:{instance_id}'

    @property
    def _widgets_active(self):
        return [str(widget) for widget in self._widgets]  # if widget.isVisible()

    def _widgets_add_cmd(self, topic, value):
        widget_str = self._widget_str(value)
        if widget_str in self._widgets_active:
            return None
        widgets_active = self._widgets_active + [widget_str]
        self._cmdp.publish('Widgets/active', widgets_active)
        return (topic, widget_str), [('!Widgets/remove', widget_str)]

    def _widgets_find_first(self, widget_str):
        widgets_active = self._widgets_active
        name, instance_id = dock_widget_parse_str(widget_str)
        if instance_id is not None:
            if widget_str not in widgets_active:
                raise ValueError('widget not found: %s', name)
            return widget_str
        for widget in widgets_active:
            if name == dock_widget_parse_str(widget)[0]:
                return widget
        raise ValueError('widget not found: %s', name)

    def _widgets_remove_cmd(self, topic, value):
        widget_str = self._widgets_find_first(value)
        widgets_active = self._widgets_active
        if widget_str not in self._widgets_active:
            return None
        widgets_active.remove(widget_str)
        self._cmdp.publish('Widgets/active', widgets_active)
        return (topic, widget_str), [('!Widgets/add', widget_str)]

    def _widgets_add(self, widget_str):
        name, instance_id = dock_widget_parse_str(self._widget_str(widget_str))
        if instance_id is None:
            raise ValueError('instance_id not specified')
        if name not in self._widget_defs:
            log.warning('_widgets_add(%s) not found', name)
            return
        widget_def = self._widget_defs[name]
        if widget_def.get('singleton', False):
            log.info('add singleton widget %s', name)
            if widget_def['dock_widget'] is None:
                dock_widget = MyDockWidget(self, widget_def, self._cmdp, instance_id)
                widget_def['dock_widget'] = dock_widget
            else:
                dock_widget = widget_def['dock_widget']
            action = widget_def.get('action')
            if action is not None:
                signal_block_state = action.blockSignals(True)
                action.setChecked(True)
                action.blockSignals(signal_block_state)
        else:
            log.info('add widget %s', name)
            dock_widget = MyDockWidget(self, widget_def, self._cmdp, instance_id)
        size_policy = widget_def.get('sizePolicy', ['expanding', 'expanding'])
        dock_widget.setSizePolicy(ui_util.str_to_size_policy(size_policy[0]),
                                  ui_util.str_to_size_policy(size_policy[1]))
        location = widget_def.get('location', QtCore.Qt.RightDockWidgetArea)
        self.addDockWidget(location, dock_widget)
        dock_widget.setVisible(True)
        self._widgets.append(dock_widget)
        return dock_widget

    def _widgets_get(self, widget_str):
        name, instance_id = dock_widget_parse_str(widget_str)
        v = f'{name}:{instance_id}'
        widgets = [w for w in self._widgets if str(w) == v]
        if len(widgets) == 0:
            log.warning('_widget_get(%s) not found', widget_str)
            raise ValueError(f'widget {widget_str} not found')
        return widgets[-1]  # most recently added, in case of multiple

    def _widgets_remove(self, widget_str):
        dock_widget = self._widgets_get(widget_str)
        dock_widget.setVisible(False)
        self._widgets.remove(dock_widget)
        self.removeDockWidget(dock_widget)

        widget_def = self._widget_defs[dock_widget.name]
        name = widget_def['name']
        if widget_def.get('singleton', False):
            log.info('remove singleton widget %s', str(dock_widget))
            action = widget_def.get('action')
            if action is not None:
                signal_block_state = action.blockSignals(True)
                action.setChecked(False)
                action.blockSignals(signal_block_state)
        else:
            log.info('remove widget %s', name)
            p = dock_widget.state_preference
            dock_widget.close()
            self._cmdp.invoke('!preferences/preference/clear', (p, None))
        return dock_widget

    def _on_widgets_active(self, topic, value):
        # must be safe to call repeatedly
        log.debug('_on_widgets_active: %s', value)
        widgets_previous = self._widgets_active
        widgets_next = value
        for widget in widgets_previous:
            if widget not in widgets_next:
                self._widgets_remove(widget)
        for widget in widgets_next:
            if widget not in widgets_previous:
                self._widgets_add(widget)
        self._window_state_update()

    def _window_state(self):
        return {
            'geometry': self.saveGeometry().data(),
            'state': self.saveState().data(),
            'maximized': self.isMaximized(),
            'pos': list(self.pos().toTuple()),
            'size': list(self.size().toTuple()),
        }

    def _window_state_update(self):
        s = self._window_state()
        s['__ignore__'] = True
        self._cmdp.publish('_window', s)

    def _on_window_state(self, topic, value):
        log.debug('_on_window_state')
        # WARNING: mutate value so that future invocations (undo, restore) take effect
        window_state = value
        if window_state is not None:
            if not hasattr(window_state, 'pop'):
                return
            if window_state.pop('__ignore__', False):
                return

        if window_state is not None:
            self.restoreGeometry(window_state['geometry'])
            self.restoreState(window_state['state'])

        # force visible, since restoreState can hide
        for widget in self._widgets:
            widget.setVisible(True)

        # force invisible, since restoreState can show
        active_widgets = self._widgets_active
        for widget in self.findChildren(QtGui.QDockWidget):
            if str(widget) not in active_widgets:
                widget.setVisible(False)

        window_location = self._cmdp['General/window_location']
        window_size = self._cmdp['General/window_size']
        if window_size == 'minimum':
            self.adjustSize()
        if window_location == 'center':
            if window_size.endswith('%'):
                f = float(window_size[:-1]) * 0.01
                self._window_center_and_resize(f, f)
            else:
                self._window_center_and_resize(None, None)

    def _window_center_and_resize(self, width_fract, height_fract):
        # https://wiki.qt.io/Center_and_Resize_MainWindow
        try:
            screen = self.window().windowHandle().screen()
        except AttributeError:
            return
        geometry = screen.availableGeometry()
        available_size = geometry.size()
        width, height = available_size.width(), available_size.height()
        log.info('Available dimensions [%d, %d]', width, height)
        sz = self.size()
        w, h = sz.width(), sz.height()
        if width_fract is not None:
            w = int(width * width_fract)
        if height_fract is not None:
            h = int(height * height_fract)
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight,
                QtCore.Qt.AlignCenter,
                QtCore.QSize(w, h),
                geometry
            )
        )

    def closeEvent(self, event):
        log.info('closeEvent()')
        try:
            self._cmdp.preferences.save()
        except:
            log.exception('closeEvent could not save preferences')
        try:
            self._device_close()
        except:
            log.exception('closeEvent could not close device')
        return super(MainWindow, self).closeEvent(event)

    def _source_indicator_status_update(self, status):
        if not self._is_streaming or status is None or 'buffer' not in status:
            return
        buffer = status['buffer']
        n_sample_id = buffer.get('sample_id')
        n_sample_missing_count = buffer.get('sample_missing_count')
        if n_sample_id is None or n_sample_missing_count is None:
            return

        try:
            n_sample_id = n_sample_id['value']
            n_sample_missing_count = n_sample_missing_count['value']
            if len(self._streaming_status):  # skip first time
                d_sample_id = n_sample_id - self._streaming_status['sample_id']
                d_sample_missing_count = n_sample_missing_count - self._streaming_status['sample_missing_count']
                if (0 == d_sample_id) or ((d_sample_missing_count / d_sample_id) > 0.001):
                    color = 'red'
                    log.warning('status RED: d_sample_id=%d, d_sample_missing_count=%d',
                                d_sample_id, d_sample_missing_count)
                elif d_sample_missing_count:
                    color = 'yellow'
                    log.warning('status YELLOW: d_sample_id=%d, d_sample_missing_count=%d',
                                d_sample_id, d_sample_missing_count)
                else:
                    color = 'LightGreen'
            else:
                color = ''
            self._streaming_status['sample_id'] = n_sample_id
            self._streaming_status['sample_missing_count'] = n_sample_missing_count
            self._cmdp.publish('Device/#state/sample_drop_color', color)
            self._cmdp.publish('Device/#state/source', 'USB')
        except:
            log.exception('_source_indicator_status_update')

    def _fps_compute(self):
        fps_time = time.time()
        if self._fps_time is None:
            fps = 0.0
        else:
            fps = self._fps_counter / (fps_time - self._fps_time)
        self._fps_counter = 0
        self._fps_time = fps_time
        return fps

    def _status_fn(self, status):
        status['ui'] = {
            'display_rate': {
                'value': self._fps_compute(),
                'units': 'fps',
            },
        }
        self._cmdp.publish('Device/#state/status', status)
        self._source_indicator_status_update(status)

    @QtCore.Slot(str)
    def status(self, msg, timeout=STATUS_BAR_TIMEOUT, level=None):
        """Display a status message.

        :param msg: The message to display.
        :param timeout: The optional timeout in milliseconds.  0 
            does not time out.
        :param level: The logging level for the message.  None (default)
            is equivalent to log.INFO.
        """
        level = logging.INFO if level is None else level
        log.log(level, msg)
        self.ui.statusbar.showMessage(msg, timeout)

    def on_preferences(self):
        log.info('on_preferences')
        reopen_params = [
            'Device/setting/buffer_duration',
            'Device/setting/reduction_frequency',
            'Device/setting/sampling_frequency']
        value_before = [self._cmdp.preferences.get(x) for x in reopen_params]
        d = PreferencesDialog(self, self._cmdp)
        if not d.exec_():
            return
        try:
            self._cmdp.preferences.save()
        except Exception:
            self.status('Could not save preferences', level=logging.ERROR)
        value_after = [self._cmdp.preferences.get(x) for x in reopen_params]
        if self._is_streaming_device and value_before != value_after:
            self._device_reopen()

    def _on_dataview_service_range_statistics(self, topic, value):
        # topic: DataView/#service/range_statistics
        # value: x_start, x_stop, reply_topic : all others passed back
        ranges = value['ranges']
        reply_topic = value['reply_topic']
        source_id = value.get('source_id', None)
        if not hasattr(self._data_view, 'statistics_get_multiple'):
            msg = 'Dual markers not supported by selected device'
            self.status(msg)
            error_rsp = {'request': value, 'response': None}
            self._cmdp.publish(reply_topic, error_rsp)
            return

        def _on_done(data):
            rsp = {'request': value, 'response': data}
            self._cmdp.publish(reply_topic, rsp)

        self._data_view.statistics_get_multiple(ranges, units='seconds', callback=_on_done, source_id=source_id)

    def _cmd_range_tool_run(self, topic, value):
        # note: no undo available
        self._path()  # has side effect of validating path
        range_tool = self._plugins.range_tools.get(value['name'])
        if range_tool is None:
            self.status(f'Range tool {value["name"]} not found')
            return None
        x_start, x_stop = value['x_start'], value['x_stop']
        if not hasattr(self._data_view, 'statistics_get'):
            self.status('Range tool not supported by selected device')
            return None
        if hasattr(self._device, 'voltage_range'):
            voltage_range = self._device.voltage_range
        elif hasattr(self._device, 'stream_buffer'):
            voltage_range = self._device.stream_buffer.voltage_range
        else:
            voltage_range = None
            log.warning('cannot get voltage_range')
        self._cmdp.publish('Plugins/#state/voltage_range', voltage_range)
        invoke = RangeToolInvoke(self, range_tool, cmdp=self._cmdp)
        invoke.sigFinished.connect(self.on_rangeToolFinished)
        s = self._data_view.statistics_get(x_start, x_stop, units='seconds')
        invoke.run(self._data_view, s, x_start, x_stop)
        return None

    @QtCore.Slot(object, str)
    def on_rangeToolFinished(self, range_tool, msg):
        if msg:
            log.warning(msg)
            self.status(msg)
        else:
            self.status(range_tool.name + ' done')

    def dropEvent(self, event):
        log.debug('dropEvent')
        return super().dropEvent(event)

    def resizeEvent(self, event):
        rv = super().resizeEvent(event)
        self._window_state_update()
        return rv

    def moveEvent(self, event):
        rv = super().moveEvent(event)
        self._window_state_update()
        return rv


class ErrorWindow(QtWidgets.QMainWindow):

    def __init__(self, msg):
        super(ErrorWindow, self).__init__()
        self.ui = Ui_ErrorWindow()
        self.ui.setupUi(self)
        self.ui.label.setText(msg)
        self.ui.label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.ui.label.setOpenExternalLinks(True)
        self.show()


def load_fonts():
    font_list = ['']
    iterator = QtCore.QDirIterator(':/joulescope/fonts/', QtCore.QDirIterator.Subdirectories)
    while iterator.hasNext():
        resource_path = iterator.next()
        if resource_path.endswith('.ttf'):
            rv = QtGui.QFontDatabase.addApplicationFont(resource_path)
            if rv == -1:
                log.warning(f'Could not load font {resource_path}')
            else:
                font_list.append(f'    {resource_path} => {rv}')
    log.debug('Loaded fonts:%s', '\n'.join(font_list))


def run(device_name=None, log_level=None, file_log_level=None, filename=None):
    """Run the Joulescope UI application.

    :param device_name: The optional Joulescope device name.  None (default)
        searches for normal Joulescope devices.
    :param log_level: The logging level for the stdout console stream log.
        The allowed levels are in :data:`joulescope_ui.logging_util.LEVELS`.
        None (default) disables console logging.
    :param file_log_level: The logging level for the file log.
        The allowed levels are in :data:`joulescope_ui.logging_util.LEVELS`.
        None (default) uses the configuration value.
    :param filename: The optional filename to display immediately.

    :return: 0 on success or error code on failure.
    """
    app = None
    try:
        logging_preconfig()  # capture log messages until logging_config
        cmdp = CommandProcessor()
        cmdp = preferences_def(cmdp)
        if file_log_level is None:
            file_log_level = cmdp.preferences['General/log_level']
        logging_config(file_log_level=file_log_level,
                       stream_log_level=log_level)
        logging.getLogger('joulescope').setLevel(logging.WARNING)
        starting_profile = cmdp.preferences['General/starting_profile']
        if starting_profile not in ['previous', 'app defaults']:
            cmdp.preferences.profile = starting_profile

        log.info('Arguments: %s', (sys.argv, ))
        log.info('Start Qt')
        try:
            log.info('Configure high DPI scaling')
            # http://doc.qt.io/qt-5/highdpi.html
            # https://vicrucann.github.io/tutorials/osg-qt-high-dpi/
            if sys.platform.startswith('win'):
                ctypes.windll.user32.SetProcessDPIAware()
            QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        except:
            log.exception('while configuring high DPI scaling')
        app = QtWidgets.QApplication(sys.argv)
        load_fonts()
        # app.setFont(QtGui.QFont('Lato', 10))
        multiprocessing_logging_queue, logging_stop = logging_start()

    except Exception:
        log.exception('during initialization')
        with io.StringIO() as f:
            traceback.print_exc(file=f)
            t = f.getvalue()
        if app is None:
            app = QtWidgets.QApplication(sys.argv)
        msg_err = '\n'.join([
            "--------------------",
            f"Exception on Joulescope UI {__version__} startup. ",
            'Python=' + sys.version,
            'Platform=' + platform.platform(),
            t])
        pyperclip.copy(msg_err)
        msg = STARTUP_ERROR_MESSAGE.format(msg_err=msg_err)
        ui = ErrorWindow(msg)
        return app.exec_()

    try:
        ui = MainWindow(app, device_name, cmdp, multiprocessing_logging_queue)
    except:
        log.exception('MainWindow initializer failed')
        raise
    ui.run(filename)
    device_notify = DeviceNotify(ui.on_deviceNotifySignal.emit)
    rc = app.exec_()
    del ui
    device_notify.close()
    logging_stop()
    return rc
