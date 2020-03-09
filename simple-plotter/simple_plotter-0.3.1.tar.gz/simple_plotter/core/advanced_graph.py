"""
advanced_graph.py - graph class for simple-plotter based on kivy-garden/graph
Copyright (C) 2020  Thies Hecker

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

The color table in standard_colors method is taken from matplotlib v3,1,3:
https://github.com/matplotlib/matplotlib/blob/v3.1.3/lib/matplotlib/_cm.py

See the matplotlib license agreement below.

License agreement for matplotlib versions 1.3.0 and later
=========================================================

1. This LICENSE AGREEMENT is between the Matplotlib Development Team
("MDT"), and the Individual or Organization ("Licensee") accessing and
otherwise using matplotlib software in source or binary form and its
associated documentation.

2. Subject to the terms and conditions of this License Agreement, MDT
hereby grants Licensee a nonexclusive, royalty-free, world-wide license
to reproduce, analyze, test, perform and/or display publicly, prepare
derivative works, distribute, and otherwise use matplotlib
alone or in any derivative version, provided, however, that MDT's
License Agreement and MDT's notice of copyright, i.e., "Copyright (c)
2012- Matplotlib Development Team; All Rights Reserved" are retained in
matplotlib  alone or in any derivative version prepared by
Licensee.

3. In the event Licensee prepares a derivative work that is based on or
incorporates matplotlib or any part thereof, and wants to
make the derivative work available to others as provided herein, then
Licensee hereby agrees to include in any such work a brief summary of
the changes made to matplotlib .

4. MDT is making matplotlib available to Licensee on an "AS
IS" basis.  MDT MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
IMPLIED.  BY WAY OF EXAMPLE, BUT NOT LIMITATION, MDT MAKES NO AND
DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS
FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF MATPLOTLIB
WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

5. MDT SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF MATPLOTLIB
 FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR
LOSS AS A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING
MATPLOTLIB , OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF
THE POSSIBILITY THEREOF.

6. This License Agreement will automatically terminate upon a material
breach of its terms and conditions.

7. Nothing in this License Agreement shall be deemed to create any
relationship of agency, partnership, or joint venture between MDT and
Licensee.  This License Agreement does not grant permission to use MDT
trademarks or trade name in a trademark sense to endorse or promote
products or services of Licensee, or any third party.

8. By copying, installing or otherwise using matplotlib ,
Licensee agrees to be bound by the terms and conditions of this License
Agreement.

License agreement for matplotlib versions prior to 1.3.0
========================================================

1. This LICENSE AGREEMENT is between John D. Hunter ("JDH"), and the
Individual or Organization ("Licensee") accessing and otherwise using
matplotlib software in source or binary form and its associated
documentation.

2. Subject to the terms and conditions of this License Agreement, JDH
hereby grants Licensee a nonexclusive, royalty-free, world-wide license
to reproduce, analyze, test, perform and/or display publicly, prepare
derivative works, distribute, and otherwise use matplotlib
alone or in any derivative version, provided, however, that JDH's
License Agreement and JDH's notice of copyright, i.e., "Copyright (c)
2002-2011 John D. Hunter; All Rights Reserved" are retained in
matplotlib  alone or in any derivative version prepared by
Licensee.

3. In the event Licensee prepares a derivative work that is based on or
incorporates matplotlib  or any part thereof, and wants to
make the derivative work available to others as provided herein, then
Licensee hereby agrees to include in any such work a brief summary of
the changes made to matplotlib.

4. JDH is making matplotlib  available to Licensee on an "AS
IS" basis.  JDH MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
IMPLIED.  BY WAY OF EXAMPLE, BUT NOT LIMITATION, JDH MAKES NO AND
DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS
FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF MATPLOTLIB
WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

5. JDH SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF MATPLOTLIB
 FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR
LOSS AS A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING
MATPLOTLIB , OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF
THE POSSIBILITY THEREOF.

6. This License Agreement will automatically terminate upon a material
breach of its terms and conditions.

7. Nothing in this License Agreement shall be deemed to create any
relationship of agency, partnership, or joint venture between JDH and
Licensee.  This License Agreement does not grant permission to use JDH
trademarks or trade name in a trademark sense to endorse or promote
products or services of Licensee, or any third party.

8. By copying, installing or otherwise using matplotlib,
Licensee agrees to be bound by the terms and conditions of this License
Agreement.

"""

import math
import warnings
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy_garden.graph import Graph, LinePlot


class AnnotatedLinePlot(BoxLayout):

    def __init__(self, title=None, show_legend=True, **kwargs):
        """Extends the kivy-graden/graph by some additional features, like a title, legend, automatic colors

        Args:

            title(str): Title to place above the plot
            show_legend(bool): If true legend will be shown below the graph
            **kwargs: Keyword arguments for kivy_garden.graph.Graph class
        """

        # we will put everything in a vertical layout: Title, graph, legend
        super().__init__(padding=10, orientation='vertical')

        self.xmin = xmin = kwargs.pop('xmin', None)
        self.xmax = xmax = kwargs.pop('xmax', None)
        self.ymin = ymin = kwargs.pop('ymin', None)
        self.ymax = ymax = kwargs.pop('ymax', None)
        self.xlog = xlog = kwargs.pop('xlog', False)
        self.ylog = ylog = kwargs.pop('ylog', False)
        self.x_ticks_major_user = x_ticks_major = kwargs.pop('x_ticks_major', None)
        self.y_ticks_major_user = y_ticks_major = kwargs.pop('y_ticks_major', None)

        self.xy_datasets = []

        # Graph does not accept None for several values e.g. xmin, xmax, ymin,... - so we will define some initial
        # values which work for lin. and log. scale. These will be recalculated with first plot being added...
        if not xmin:
            xmin = 1.
        if not ymax:
            xmax = 10.

        if not ymin:
            ymin = 1.
        if not ymax:
            ymax = 10.

        if not x_ticks_major:
            x_ticks_major = 1.
        if not y_ticks_major:
            y_ticks_major = 1.

        self.graph = Graph(x_ticks_major=x_ticks_major, y_ticks_major=y_ticks_major, xlog=xlog, ylog=ylog, xmin=xmin,
                           xmax=xmax, ymin=ymin, ymax=ymax, **kwargs)

        self.show_legend = show_legend
        self.legend_row_height = 40     # in px

        if title:
            self.title = title
            self.lblTitle = Label(text=self.title, size_hint_y=0.1)
            self.add_widget(self.lblTitle)

        self.add_widget(self.graph)

    def plot(self, x_values, y_values, color=None, label=None):
        """Adds a plot to the graph

        Args:
            x_values(list): List of x-values
            y_values(list): List of y-values
            color(tuple): RGBA color value (0...1.) for the curves color- e.g. (0.5, 1., 1., 1.)
            label(str): Legend label for the curve

        Note:
            If color is None the color will automatically be assigned based on the predefined standard colors.
        """

        if len(x_values) != len(y_values):
            raise ValueError('x- and y-value lists must have the same length! '
                             'But x has {} and y has {} elements'.format(len(x_values), len(y_values)))

        # TODO: This loop will discard all data points, whose x- and/or y-values are <= 0 in case logarithmic
        # scaling is set for the corresponding axis - this will cause some issues, if data is replotted in linear scale
        # i.e. earlier discarded data points will show up
        xy_data = []
        for i, x_val in enumerate(x_values):
            if self.xlog and x_val <= 0:
                warnings.warn('X-axis is set to logarithmic scale, but data point {} x-value is {} '
                              '- data point will be ignored.'.format(i, x_val))
            elif self.ylog and y_values[i] <= 0:
                warnings.warn('Y-axis is set to logarithmic scale, but data point {} y-value is {} '
                              '- data point will be ignored.'.format(i, y_values[i]))
            else:
                xy_data.append((x_val, y_values[i]))

        self.xy_datasets.append(xy_data)

        if color is None:
            if len(self.xy_datasets) <= len(self.standard_colors):
                color_idx = len(self.xy_datasets)-1
            else:   # if more date sets than standard colors repeat colors
                color_q = (len(self.xy_datasets)-1)/len(self.standard_colors)
                color_idx = int((color_q - int(color_q)) * len(self.standard_colors))
            color = self.standard_colors[color_idx]

        plot = LinePlot(color=color, line_width=2)

        plot.points = xy_data
        self.graph.add_plot(plot)

        if label and self.show_legend:
            # add the legende layout, if this is the first plot
            if len(self.xy_datasets) == 1:
                self.layout_legend = GridLayout(padding=10, cols=2, size_hint_y=0.1)
                # row_default_height=self.legend_row_height, row_force_default=True)
                # self.lblLegend = Label(text='Legend text goes here...', size_hint_y=0.1)
                # self.layout_legend.add_widget(self.lblLegend)
                self.add_widget(self.layout_legend)

            lblLegendColor = Label(text='---', color=color, bold=True) #, halign='right', size_hint_x=0.5)
            lblLegendEntry = Label(text=label) #, halign='left', size_hint_x=0.5)

            self.layout_legend.add_widget(lblLegendColor)
            self.layout_legend.add_widget(lblLegendEntry)

            # resize the plot canvas for the legend entries
            print('Widget height:', self.to_window(*self.size))
            self.layout_legend.size_hint_y = len(self.xy_datasets) * 0.1
            print(self.layout_legend.size_hint_y)
            # self.do_layout()

        self.recalculate_axis_limits()

    def recalculate_axis_limits(self):
        """Recalculates the axis limits and updates the graph"""

        xmin, xmax, x_ticks_major, x_ticks_minor = self.recalculate_x_axis()
        ymin, ymax, y_ticks_major, y_ticks_minor = self.recalculate_y_axis()

        if self.x_ticks_major_user:
            x_ticks_major = self.x_ticks_major_user
        if self.y_ticks_major_user:
            y_ticks_major = self.y_ticks_major_user

        self.graph.xmin = float(xmin)
        self.graph.xmax = float(xmax)
        self.graph.x_ticks_major = x_ticks_major
        self.graph.x_ticks_minor = x_ticks_minor

        self.graph.ymin = float(ymin)
        self.graph.ymax = float(ymax)
        self.graph.y_ticks_major = y_ticks_major
        self.graph.y_ticks_minor = y_ticks_minor

    def recalculate_y_axis(self):
        """Recalculates y-axis limits

        Returns:
            tuple: tuple consisting of:

                * float: y-axis min. value
                * float: y-axis max. value
                * float: tick major spacing
                * int: number minor ticks
        """
        # check if plot limits need to be adjusted
        limit_min = self.ymin if self.ymin is not None else self.y_data_limits[0]
        limit_max = self.ymax if self.ymax is not None else self.y_data_limits[1]

        y_range = limit_max - limit_min
        mag_y = int(round(math.log10(y_range)))-1
        print('Y-range: {}, magnitude: {}'.format(y_range, mag_y))

        if self.ylog:
            if limit_max <= 0:
                raise ValueError('All y-values are <= 0 and log-scale is selected. No values can be displayed!')
            # axis limits
            mag_y_max = int(round(math.log10(limit_max)))
            smooth_ymax = 10 ** mag_y_max
            if limit_min <= 0:
                mag_y_min = mag_y_max - 3  # display three decades
            else:
                mag_y_min = math.floor(math.log10(limit_min))
            smooth_ymin = 0.9 * (10 ** mag_y_min)
            # ticks
            smooth_ticks = 1  # one tick for each decade
            ticks_minor = 10
        else:
            # axis limits
            if self.ymin is None:
                # calculate nearest smooth value
                smooth_ymin = math.floor(self.y_data_limits[0] / 10 ** mag_y) * (10 ** mag_y)
            else:
                smooth_ymin = self.ymin
            if self.ymax is None:
                smooth_ymax = math.ceil(self.y_data_limits[1] / 10 ** mag_y) * (10 ** mag_y)
            else:
                smooth_ymax = self.ymax

            #ticks
            new_ticks = (smooth_ymax - smooth_ymin) / 10
            smooth_ticks = math.ceil(new_ticks / 10 ** (mag_y)) * 10 ** (mag_y)
            ticks_minor = 10

        print('new ymin/max:', smooth_ymin, smooth_ymax)
        print('New major tick step:', smooth_ticks)

        return smooth_ymin, smooth_ymax, smooth_ticks, ticks_minor

    def recalculate_x_axis(self):
        """Recalculates the x-axis limits and ticks

        Returns:
            tuple: tuple consisting of:

                * float: y-axis min. value
                * float: y-axis max. value
                * float: tick major spacing
                * int: number minor ticks
        """

        #TODO: there is a special, when ylog is set and x-y value pairs are removed due to negative y-values.
        # in this case the x-axis limits need to be recalculated to rounded values

        limit_min = self.xmin if self.xmin is not None else self.x_data_limits[0]
        limit_max = self.xmax if self.xmax is not None else self.x_data_limits[1]

        x_range = limit_max - limit_min
        mag_x = int(round(math.log10(x_range))) - 1

        if self.xlog:
            # axis limits
            if limit_max <= 0:
                raise ValueError('At least max. x-value needs to be > 0, if log scale for x-Axis is selected')
            else:
                mag_x_max = math.ceil(math.log10(limit_max))

            smooth_xmax = 10 ** mag_x_max
            if limit_min <= 0:
                mag_x_min = mag_x_max - 3  # display three decades
            else:
                mag_x_min = math.floor(math.log10(limit_min))
            smooth_xmin = 0.9 * (10 ** mag_x_min)     # it seems graden graph needs one additional tick to display
            # the min. tick label...

            # ticks
            smooth_ticks = 1  # one tick for each decade
            ticks_minor = 10  # 10 minor ticks per decade
        else:
            smooth_xmin = limit_min
            smooth_xmax = limit_max

            # ticks
            new_ticks = (smooth_xmax - smooth_xmin) / 10
            smooth_ticks = math.ceil(new_ticks / 10 ** (mag_x)) * 10 ** (mag_x)
            ticks_minor = 10

        print('new xmin/max:', smooth_xmin, smooth_xmax)
        print('New major tick step:', smooth_ticks)

        return smooth_xmin, smooth_xmax, smooth_ticks, ticks_minor

    @property
    def x_data_limits(self):
        """tuple: Returns data limits (xmin and xmax) in terms of x-coordinates"""
        data_limits = self.get_data_limits()
        xmin = data_limits[0]
        xmax = data_limits[1]

        return xmin, xmax

    @property
    def y_data_limits(self):
        """tuple: Returns data limits (ymin and ymax) in terms of y-coordinates"""
        data_limits = self.get_data_limits()
        ymin = data_limits[2]
        ymax = data_limits[3]

        return ymin, ymax

    def get_data_limits(self):
        """Calculate x- and y-data limits

        Returns:

            tuple: tuple consisting of:

                * float: min. x-value
                * float: max. x-value
                * float: min. y-value
                * float: max. y-value
        """

        if len(self.xy_datasets) > 0:
            xmin = self.xy_datasets[0][0][0]
            xmax = self.xy_datasets[0][0][0]
            ymax = self.xy_datasets[0][0][1]
            ymin = self.xy_datasets[0][0][1]
            for data_set in self.xy_datasets:
                for point in data_set:
                    if point[0] > xmax:
                        xmax = point[0]
                    if point[0] < xmin:
                        xmin = point[0]
                    if point[1] < ymin:
                        ymin = point[1]
                    if point[1] > ymax:
                        ymax = point[1]
                    if point[1] < ymin:
                        ymin = point[1]

        else:
            xmin = None
            xmax = None
            ymax = None
            ymin = None

        return xmin, xmax, ymin, ymax

    # @staticmethod
    # def generate_random_color():
    #     """Generates a random color"""
    #     return [random(), random(), random(), 1]

    @property
    def standard_colors(self):
        """list: Returns a list of 18 standard color RGBA values

        The color map table is taken from matplotlib source code:
        https://github.com/matplotlib/matplotlib/blob/master/lib/matplotlib/_cm.py
        """

        _tab20_data = (
            (0.12156862745098039, 0.4666666666666667, 0.7058823529411765),  # 1f77b4
            (0.6823529411764706, 0.7803921568627451, 0.9098039215686274),  # aec7e8
            (1.0, 0.4980392156862745, 0.054901960784313725),  # ff7f0e
            (1.0, 0.7333333333333333, 0.47058823529411764),  # ffbb78
            (0.17254901960784313, 0.6274509803921569, 0.17254901960784313),  # 2ca02c
            (0.596078431372549, 0.8745098039215686, 0.5411764705882353),  # 98df8a
            (0.8392156862745098, 0.15294117647058825, 0.1568627450980392),  # d62728
            (1.0, 0.596078431372549, 0.5882352941176471),  # ff9896
            (0.5803921568627451, 0.403921568627451, 0.7411764705882353),  # 9467bd
            (0.7725490196078432, 0.6901960784313725, 0.8352941176470589),  # c5b0d5
            (0.5490196078431373, 0.33725490196078434, 0.29411764705882354),  # 8c564b
            (0.7686274509803922, 0.611764705882353, 0.5803921568627451),  # c49c94
            (0.8901960784313725, 0.4666666666666667, 0.7607843137254902),  # e377c2
            (0.9686274509803922, 0.7137254901960784, 0.8235294117647058),  # f7b6d2
            (0.4980392156862745, 0.4980392156862745, 0.4980392156862745),  # 7f7f7f
            (0.7803921568627451, 0.7803921568627451, 0.7803921568627451),  # c7c7c7
            (0.7372549019607844, 0.7411764705882353, 0.13333333333333333),  # bcbd22
            (0.8588235294117647, 0.8588235294117647, 0.5529411764705883),  # dbdb8d
            (0.09019607843137255, 0.7450980392156863, 0.8117647058823529),  # 17becf
            (0.6196078431372549, 0.8549019607843137, 0.8980392156862745),  # 9edae5
        )

        rgba_values = []
        for rgb_value in _tab20_data:
            rgba_values.append((rgb_value[0], rgb_value[1], rgb_value[2], 1))

        return rgba_values