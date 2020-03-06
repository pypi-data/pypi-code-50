from shapely.geometry import Point
from shapely.geometry import Polygon
import numpy as np
import matplotlib.pyplot as plt

from geometry import *
from sectiongen import *

# line = create_line(0, 300)
# print(line)
# print(line.coords[1])
# print('line.bounds =', line.bounds)
# print('line =', line)
# p1 = Point(40, 40)
# print(line.distance(p1))
# plt.plot(p1.x, p1.y, 'r.', ms=20)
# plt.plot(*line.xy, 'k-')


# x = [0, 0, 250, 250]
# y = [0, 500, 500, 0]
# polygon = Polygon([(xi, yi) for xi, yi in zip(x, y)])
# plt.plot(*polygon.exterior.xy)
# #
# ints = polygon_line_intersections(polygon, line)
# print('intersections', ints)
# print('intersections', np.array(ints.xy))
# plt.plot(*ints.xy)

# #
# x = np.array([150, 150])
# y = np.array([200, 400])
# ab = evaluate_points(x, y, 0, 300)
# print(ab)

# plt.plot(x, y, '.')
# plt.plot([0, 300], [300, 300])

# plt.show()

# find_compr_tension_zones(polygon, line)

# na = LineString([(-1000, -60), (1000, -60)])
# point = Point(350/2, -30)
# offset = project_point_to_line(na, point)
# print(offset)


'''
TODO Create alternative constructor for polygons and circles in the same class
     `Section`.
'''

from conctools import Section
import numpy as np
import matplotlib.pyplot as plt

import sectiongen

# --- Example 4.10 ---
xs, ys = sectiongen.rebar_coordinates(300-45-25/2, 10)
x, y = sectiongen.rebar_coordinates(300, 500)
fck = 25
fyk = 550
ds = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
for xss, yss in zip(xs, ys):
    print(f'{xss:.0f}, {yss:.0f}')
# section = ps.Section(vertices=[x, y], rebars=[xs, ys])
section = Section(vertices=[x, y], rebars=[xs, ys, ds], fck=fck, fyk=fyk,
                  gamma_c=1.45, gamma_s=1.2, alpha_cc=1)
# section.plot()
N, M, metadata = section.capacity_diagram(n_locations=200)
# N, M = section.capacity_diagram(neutral_axis_locations=[-24.1])

fig, ax = plt.subplots()

ax.plot(N, M, '.-')
# print(metadata['neutral_axis'])
# --- Annotatate with neutral axis location ---
plot_annotations = False
if plot_annotations:
    neutral_axis_y = metadata['neutral_axis']
    for x, y, na_y in zip(M, N, neutral_axis_y):
        # text = f'({x:.0f}, {y:.0f})'
        text = f'({na_y:.0f})'
        print(text)
        ax.annotate(s=text, xy=(x, y))

ax.invert_yaxis()
# ax.set_xticks(np.arange(min(N), max(N)+1000, step=1000), minor=False)
# ax.set_yticks(np.arange(min(M), max(M), step=100), minor=False)
# ax.xaxis.grid(True, which='major')
# ax.yaxis.grid(True, which='major')
# ax.grid(b=True, which='both', color='#999999', linestyle='-', alpha=0.2)
ax.grid()

# Plot manually computed points
manual_points = {'A': (2250, 0), 'B': (-2123, 595), 'E': (-7125, 0)}

N_manual, M_manual = list(zip(*manual_points.values()))

plt.plot(N_manual, M_manual, 'x', color='limegreen', markersize=20)

plt.show()
