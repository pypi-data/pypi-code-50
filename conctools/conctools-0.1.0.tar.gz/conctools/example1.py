
'''
'''

from conctools import Section
import pandas as pd
import matplotlib.pyplot as plt


# --- Example 4.10 ---
x = [0, 0, 350, 350]
y = [0, -450, -450, 0]
fck = 25
fyk = 500
xs = [60, 290, 60, 290]
ys = [-60, -60, -390, -390]
ds = [32, 32, 25, 25]
na_locs = [-60, -158, -241, -390, -450, -99999]
# na_locs_with_full_tension = [9999, 1000, 450, 0, -60, -158, -241, -390, -450, -9999]
# na_locs_with_full_tension = [0, -60, -158, -241, -390, -450, -9999]

# section = ps.Section(vertices=[x, y], rebars=[xs, ys])
section = Section(vertices=[x, y], rebars=[xs, ys, ds], fck=fck, fyk=fyk,
                  gamma_c=1.5, alpha_cc=0.85)
# section.plot()
# N, M = section.capacity_diagram(neutral_axis_locations=na_locs_with_full_tension)
# N, M, metadata = section.capacity_diagram(neutral_axis_locations=na_locs)
N, M, metadata = section.capacity_diagram(n_locations=300)

df = pd.DataFrame(metadata)
# df.to_csv('example4_10_extended.csv')
print(df.head().to_string())

# section.plot()

fig, ax = plt.subplots()

ax.plot(M, N, '.-')

# --- Annotatate with neutral axis location ---
plot_neutral_axis_annotations = True
if plot_neutral_axis_annotations:
    for x, y, y_na in zip(M, N, metadata['neutral_axis']):
        # text = f'({x:.0f}, {y:.0f})'
        text = f'({y_na:.0f})'
        # print(text)
        ax.annotate(s=text, xy=(x, y))

# --- Annotatate with neutral axis location ---
plot_annotations = False
if plot_annotations:
    for x, y in zip(M, N):
        text = f'({x:.0f}, {y:.0f})'
    #    print(text)
        ax.annotate(s=text, xy=(x, y))

ax.invert_yaxis()
ax.grid()
ax.set_title('sdad')
plt.show()
