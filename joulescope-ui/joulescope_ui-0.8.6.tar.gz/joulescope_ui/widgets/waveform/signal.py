# Copyright 2019 Jetperch LLC
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

from PySide2 import QtCore
from .signal_statistics import SignalStatistics, SignalMarkerStatistics, si_format, html_format
from .signal_viewbox import SignalViewBox
from joulescope.stream_buffer import single_stat_to_api
from .yaxis import YAxis
import pyqtgraph as pg
import numpy as np
import logging


AUTO_RANGE_FRACT = 0.45  # autorange when current range smaller than existing range by this fractional amount.


INTEGRATION_UNITS = {
    'A': 'C',
    'W': 'J'
}


def _wheel_to_y_gain(delta):
    return 0.7 ** (delta / 120.0)


class Signal(QtCore.QObject):

    def __init__(self, parent, cmdp, name, display_name=None, units=None, y_limit=None, y_log_min=None, y_range=None, **kwargs):
        QtCore.QObject.__init__(self, parent=parent)
        self._cmdp = cmdp
        self.text_item = None
        self.name = name
        self.log = logging.getLogger(__name__ + '.' + name)
        self.units = units
        self.config = {
            'name': name,
            'y-axis': {
                'limit': y_limit,
                'log_min': y_log_min,
                'range': 'auto' if y_range is None else y_range
            },
        }
        self._markers_single = {}
        self._markers_dual = {}
        self._is_min_max_active = False  # when zoomed out enough to display min/max
        self._y_pan = None
        self.vb = SignalViewBox(name=self.name)
        if y_limit is not None:
            y_min, y_max = y_limit
            self.vb.setLimits(yMin=y_min, yMax=y_max)
            self.vb.setYRange(y_min, y_max)
        self.y_axis = YAxis(name, cmdp, log_enable=y_log_min is not None)
        self.y_axis.linkToView(self.vb)
        self.y_axis.setGrid(128)
        self._y_range_now = [None, None]

        self._most_recent_data = None
        if display_name is None:
            display_name = name
        if display_name is not None:
            self.y_axis.setLabel(text=display_name, units=units)
            self.text_item = SignalStatistics(field=self.name, units=units, cmdp=cmdp)

        self.curve_mean = pg.PlotDataItem()
        self.curve_max = pg.PlotDataItem()
        self.curve_min = pg.PlotDataItem()
        self.curve_range = None
        self.vb.addItem(self.curve_max)
        self.vb.addItem(self.curve_min)
        self.vb.addItem(self.curve_mean)

        self.curve_max.hide()
        self.curve_min.hide()

        self.y_axis.sigConfigEvent.connect(self.y_axis_config_update)
        self.y_axis.sigWheelZoomYEvent.connect(self.on_wheelZoomY)
        self.y_axis.sigPanYEvent.connect(self.on_panY)
        self.y_axis.range_set(self.config['y-axis']['range'])
        self.vb.sigYRangeChanged.connect(self._on_y_range_changed)

        cmdp.subscribe('Widgets/Waveform/grid_y', self._on_grid_y, update_now=True)
        cmdp.subscribe('Widgets/Waveform/show_min_max', self._on_show_min_max, update_now=True)
        cmdp.subscribe('Widgets/Waveform/trace_width', self._on_colors, update_now=True)
        cmdp.subscribe('Widgets/Waveform/mean_color', self._on_colors, update_now=True)
        cmdp.subscribe('Widgets/Waveform/min_max_trace_color', self._on_colors, update_now=True)
        cmdp.subscribe('Widgets/Waveform/min_max_fill_color', self._on_colors, update_now=True)

    def set_xlimits(self, x_min, x_max):
        self.vb.setLimits(xMin=x_min, xMax=x_max)

    def addToLayout(self, layout, row):
        layout.addItem(self.y_axis, row=row, col=0)
        layout.addItem(self.vb, row=row, col=1)
        if self.text_item:
            layout.addItem(self.text_item, row=row, col=2)
            layout.ci.layout.setRowStretchFactor(row, 150)
        else:
            layout.ci.layout.setRowStretchFactor(row, 10)

    def removeFromLayout(self, layout):
        rows = layout.ci.layout.rowCount()
        for row in range(rows):
            if layout.getItem(row, 1) == self.vb:
                layout.removeItem(self.y_axis)
                layout.removeItem(self.vb)
                if self.text_item:
                    layout.removeItem(self.text_item)
                return row

    def y_axis_config_update(self, cfg):
        update_range = cfg.get('range') == 'auto' and self.config.get('y-axis', {}).get('range') == 'manual'
        self.config['y-axis'].update(**cfg)
        # range, handled elsewhere
        if self.config['y-axis']['scale'] == 'logarithmic':
            self.y_axis.setLogMode(True)
            self.curve_mean.setLogMode(xMode=False, yMode=True)
            self.curve_min.setLogMode(xMode=False, yMode=True)
            self.curve_max.setLogMode(xMode=False, yMode=True)
            y_min = np.log10(self.config['y-axis']['log_min'])
            y_max = np.log10(self.config['y-axis']['limit'][1])
            self.vb.setLimits(yMin=y_min, yMax=y_max)
            self.vb.setYRange(y_min, y_max)
        else:
            self.y_axis.setLogMode(False)
            self.curve_mean.setLogMode(xMode=False, yMode=False)
            self.curve_min.setLogMode(xMode=False, yMode=False)
            self.curve_max.setLogMode(xMode=False, yMode=False)
            y_min, y_max = self.config['y-axis']['limit']
            self.vb.setLimits(yMin=y_min, yMax=y_max)
        if update_range:
            self.yaxis_autorange(*self._y_range_now)
        self._cmdp.publish('Widgets/Waveform/#requests/refresh', None)

    @QtCore.Slot(float, float)
    def on_wheelZoomY(self, y, delta):
        gain = _wheel_to_y_gain(delta)
        ra, rb = self.vb.viewRange()[1]
        if ra <= y <= rb:  # valid y, keep y in same screen location
            d1 = rb - ra
            d2 = d1 * gain
            f = (y - ra) / d1
            pa = y - f * d2
            pb = pa + d2
            self.vb.setRange(yRange=[pa, pb])
        else:
            self.log.warning('on_wheelZoomY(%s, %s) out of range', y, delta)

    @QtCore.Slot(object, float)
    def on_panY(self, command, y):
        self.log.info('on_panY(%s, %s)', command, y)
        if command == 'finish':
            if self._y_pan is not None:
                pass
            self._y_pan = None
        elif command == 'start':
            self._y_pan = [y] + self.vb.viewRange()[1]

        if self._y_pan is None:
            return

        y_start, ya, yb = self._y_pan
        delta = y_start - y
        ra = ya + delta
        rb = yb + delta
        self.vb.setRange(yRange=[ra, rb])

    def yaxis_autorange(self, v_min, v_max):
        if v_min is None or v_max is None:
            return
        self._y_range_now = [v_min, v_max]
        if self.config['y-axis'].get('range', 'auto') == 'manual':
            return
        _, (vb_min, vb_max) = self.vb.viewRange()
        if not np.isfinite(v_min):
            v_min = vb_min
        if not np.isfinite(v_max):
            v_max = vb_max
        if self.config['y-axis'].get('scale', 'linear') == 'logarithmic':
            v_min = np.log10(max(v_min, self.config['y-axis']['log_min']))
            v_max = np.log10(max(v_max, self.config['y-axis']['log_min']))
        vb_range = vb_max - vb_min
        v_range = v_max - v_min

        update_range = (v_max > vb_max) or (v_min < vb_min)
        if vb_range > 0:
            update_range |= (v_range / vb_range) < AUTO_RANGE_FRACT
        if update_range:
            self.vb.setYRange(v_min, v_max)

    def data_clear(self):
        self._most_recent_data = None
        self.curve_mean.clear()
        self.curve_mean.update()
        self.curve_mean.hide()
        self._min_max_disable()

    def _min_max_show(self):
        if not self._is_min_max_active:
            self._min_max_hide()
            return
        c = self._cmdp['Widgets/Waveform/show_min_max']
        if c == 'lines':
            self.curve_max.show()
            self.curve_min.show()
            if self.curve_range is not None:
                curve_range, self.curve_range = self.curve_range, None
                self.vb.removeItem(curve_range)
                del curve_range
        elif c == 'fill':
            self.curve_max.hide()
            self.curve_min.hide()
            if self.curve_range is None:
                brush = pg.mkBrush(color=self._cmdp['Widgets/Waveform/min_max_fill_color'])
                self.curve_range = pg.FillBetweenItem(self.curve_min, self.curve_max, brush=brush)
                self.vb.addItem(self.curve_range)
            else:
                self.curve_range.show()
        else:
            if c != 'off':
                self.log.warning('unsupported show_min_max mode: %s, presume "off"', c)
            self._min_max_hide()

    def _min_max_hide(self):
        self.curve_max.update()
        self.curve_max.hide()
        self.curve_min.update()
        self.curve_min.hide()
        if self.curve_range is not None:
            self.curve_range.hide()

    def _min_max_enable(self):
        self._is_min_max_active = True
        self._min_max_show()

    def _min_max_disable(self):
        self._is_min_max_active = False
        self._min_max_hide()

    def _log_bound(self, y):
        if self.config['y-axis'].get('scale', 'linear') == 'logarithmic':
            y_log_min = self.config['y-axis']['log_min']
            y = np.copy(y)
            y[y < y_log_min] = y_log_min
            # y = np.log10(y)
            return y
        else:
            return y

    def update(self, x, value):
        """Update the signal data.

        :param x: The length N array of x-axis time in seconds.
        :param value: The y-axis data which can be:
            * length N array
            * length Nx4 array of [mean, var, min, max].  Note that
              var, min, max may be NaN when not available.
        """
        if self.text_item:
            self.text_item.data_clear()
        if x is None or value is None or len(x) <= 1:
            self.data_clear()
            return

        # get the mean value regardless of shape
        z_mean = value['µ']['value']
        z_var = value['σ2']['value']
        z_min = value['min']['value']
        z_max = value['max']['value']
        self._most_recent_data = [x, z_mean, z_var, z_min, z_max]

        # get the valid mean values regardless of shape
        z_valid = np.isfinite(z_mean)
        x = x[z_valid]
        z_mean_valid = z_mean[z_valid]
        if not len(z_mean_valid):
            if len(z_mean):
                self.log.info('no valid data: %d -> %d', len(z_mean), len(z_mean_valid))
            if self.text_item:
                self.text_item.data_clear()
            return

        x_range = x[-1] - x[0]
        z_mean = z_mean_valid
        z_min = z_min[z_valid]
        if np.isfinite(z_min[0]):
            z_var = z_var[z_valid]
            z_max = z_max[z_valid]

        # compute statistics over the visible window
        z = z_mean
        self.curve_mean.setData(x, self._log_bound(z))
        self.curve_mean.show()
        if not np.isfinite(z_min[0]):
            self._min_max_disable()
            v_mean = np.mean(z)
            v_var = np.var(z)
            v_max = np.max(z)
            v_min = np.min(z)
        else:
            self._min_max_enable()
            v_mean = np.mean(z_mean)
            v_min = np.min(z_min)
            v_max = np.max(z_max)
            mean_delta = z_mean - v_mean
            # combine variances across the combined samples
            v_var = np.sum(np.square(mean_delta, out=mean_delta) + z_var) / len(z_mean)
            self.curve_min.setData(x, self._log_bound(z_min))
            self.curve_max.setData(x, self._log_bound(z_max))

        if self._cmdp['Widgets/Waveform/show_min_max'] == 'off':
            # use min/max of the mean trace for y-axis autoranging (not actual min/max)
            v_min = np.min(z_mean)
            v_max = np.max(z_mean)

        if not np.isfinite(v_min) or not np.isfinite(v_max) or np.abs(v_min) > 1000 or np.abs(v_max) > 1000:
            self.log.warning('signal.update(%r, %r)' % (v_min, v_max))
        if self.text_item is not None:
            labels = single_stat_to_api(v_mean, v_var, v_min, v_max, self.units)
            integration_units = INTEGRATION_UNITS.get(self.units)
            if integration_units is not None:
                labels['∫'] = {'value': v_mean * x_range, 'units': integration_units}
            labels['Δt'] = {'value': x_range, 'units': 's'}
            self.text_item.data_update(labels)

        self.yaxis_autorange(v_min, v_max)

    def update_markers_single_all(self, markers):
        current_markers = self._markers_single.copy()
        for name, pos in markers:
            current_markers.pop(name, None)
            self.update_markers_single_one(name, pos)
        if len(current_markers):
            for marker_name in list(current_markers.keys()):
                m = self._markers_single.pop(marker_name)
                self.vb.scene().removeItem(m)

    def update_markers_single_one(self, marker_name, marker_pos):
        if marker_name not in self._markers_single:
            m = SignalMarkerStatistics(self.name, self._cmdp)
            self.vb.addItem(m)
            m.setVisible(True)
            m.move(self.vb, marker_pos)
            self._markers_single[marker_name] = m
        m = self._markers_single[marker_name]
        if marker_pos is None:
            stats = None
        else:
            stats = self.statistics_at(marker_pos)
        m.data_update(self.vb, marker_pos, stats)

    def update_markers_dual_one(self, marker_name, marker_pos, statistics):
        if marker_name not in self._markers_dual:
            m = SignalMarkerStatistics(self.name, self._cmdp)
            self.vb.addItem(m)
            m.setVisible(True)
            m.move(self.vb, marker_pos)
            self._markers_dual[marker_name] = m
        m = self._markers_dual[marker_name]
        m.data_update(self.vb, marker_pos, statistics)

    def update_markers_dual_all(self, values):
        # list of (marker_name, marker_pos, statistics)
        current_markers = self._markers_dual.copy()
        for name, pos, statistic in values:
            current_markers.pop(name, None)
            self.update_markers_dual_one(name, pos, statistic)
        if len(current_markers):
            for marker_name in list(current_markers.keys()):
                m = self._markers_dual.pop(marker_name)
                self.vb.scene().removeItem(m)

    def marker_move(self, marker_name, marker_pos):
        for m in [self._markers_single.get(marker_name), self._markers_dual.get(marker_name)]:
            if m is not None:
                m.move(self.vb, marker_pos)
                m.computing()

    def statistics_at(self, x):
        """Get the statistics at the provided x value.

        :param x: The x-axis value in seconds.
        :return: The dict mapping parameter name to float value.
        """
        if self._most_recent_data is None:
            return {}
        z_x, z_mean, z_var, z_min, z_max = self._most_recent_data
        if not z_x[0] <= x <= z_x[-1]:
            return {}
        idx = np.argmax(z_x >= x)
        y_mean = float(z_mean[idx])
        if not np.isfinite(y_mean):
            return {}
        if z_min is not None and np.isfinite(z_min[idx]):
            y_var = float(z_var[idx])
            y_min = float(z_min[idx])
            y_max = float(z_max[idx])
            labels = single_stat_to_api(y_mean, y_var, y_min, y_max, self.units)
        else:
            labels = {'µ': {'value': y_mean, 'units': self.units}}
        return labels

    def _on_show_min_max(self, topic, value):
        self._min_max_show()
        self.vb.update()

    def _on_grid_y(self, topic, value):
        self.y_axis.setGrid(128 if bool(value) else 0)

    def _on_colors(self, topic, value):
        trace_width = int(self._cmdp['Widgets/Waveform/trace_width'])
        mean_color = tuple(self._cmdp['Widgets/Waveform/mean_color'])
        min_max_trace_color = tuple(self._cmdp['Widgets/Waveform/min_max_trace_color'])
        self._pen_min_max = pg.mkPen(color=min_max_trace_color, width=trace_width)
        self._pen_mean = pg.mkPen(color=mean_color, width=trace_width)
        self.curve_min.setPen(self._pen_min_max)
        self.curve_max.setPen(self._pen_min_max)
        self.curve_mean.setPen(self._pen_mean)
        if self.curve_range is not None:
            brush_color = tuple(self._cmdp['Widgets/Waveform/min_max_fill_color'])
            brush = pg.mkBrush(color=brush_color)
            self.curve_range.setBrush(brush)
        self.vb.update()

    @QtCore.Slot(object, object)
    def _on_y_range_changed(self, vb, y_range):
        self.log.info('_on_y_range_changed(%s, %s)', self.name, y_range)
        for m in self._markers_single.values():
            m.move(self.vb)
        for m in self._markers_dual.values():
            m.move(self.vb)
