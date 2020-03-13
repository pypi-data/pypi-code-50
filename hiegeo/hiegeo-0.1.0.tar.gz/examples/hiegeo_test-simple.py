#!/usr/bin/env python3
"""
:License:
    This file is part of hiegeo.

    hiegeo is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    hiegeo is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with hiegeo.  If not, see <https://www.gnu.org/licenses/>.

:This file:
    `hiegeo_test-simple.py`

:Purpose:
    A script to test the basic capabilities of the module `hiegeo.py`.

:Usage:
    From the shell type `./hiegeo_test-simple.py`, or hit `<F5>` or `run` if you are
    using spyderlib.

:Parameters:
    Required input files:
        - One JSON file containing the main parameters.
        - One CSV file with the info about the intersections/contact points.
    See the attached documentation for more details.

:Version:
    See file ``hiegeo.py``
    
:Authors:
    Alessandro Comunian <alessandro.comunian@unimi.it>

:License:
    This file is part of the Python module `hiegeo`.

    `hiegeo` is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    `hiegeo` is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with `hiegeo`.  If not, see <https://www.gnu.org/licenses/>.

.. note::

    1) Conventions:
        See file `hiegeo.py`

    2) The input files are provided as CSV, but other input format
       could be used thanks to the many Python libraries avaiable (for
       example, you could use `DBF` and the library "geopandas" or
       other data base format).

"""
import numpy as np
import matplotlib.pylab as pl
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import pandas as pd
import warnings
import json

import anytree as at

import hiegeo

# Print a header
hiegeo.print_start()

# ==============================================================
# Read the input parameters
# ==============================================================
with open("hiegeo_test.json", "r") as infile:
    par = json.load(infile)

# Set the name of the input file
file_in = par["data_file"]

# Read the data containing the points
# (See documentation and examples for the appropriate format)
print('    Reading input file: "{0}"'.format(file_in))
data = pd.read_csv(file_in)

# Print info about data
hiegeo.print_data_info(data)

#
# Set here the discretization grid defined in the parameter file.
#
# NOTE: In the data-set, the SB starting and ending *x* coordinates
#     should be ideally defined starting from the same value for all
#     the SBs. Alternatively, one can sligtly reduce the size of the
#     grid (in this case, a warning message will be printed).
#
x_min = par["grid"]["x_min"]
x_max = par["grid"]["x_max"]
dx = par["grid"]["dx"]
nx = int((x_max-x_min)/dx)+1

z_min = par["grid"]["z_min"]
z_max = par["grid"]["z_max"]
dz = par["grid"]["dz"]
nz = int((z_max-z_min)/dz)+1

# Prinf info about the discretization grid
print("")
print("    Discretization grid info:")
print("        x in [{0}, {1}]".format(x_min, x_max))
print("        z in [{0}, {1}]".format(z_min, z_max))
print("        grid size: ({0}x{1})".format(nx, nz))

# Create the discretization grid
x = np.linspace(x_min, x_max, nx)
z = np.linspace(z_min, z_max, nz)
xmesh, zmesh = np.meshgrid(x ,z)

# Check if data are contained in the discretization grid.
hiegeo.check_data_ingrid(data, x, z)

# Compute and store the number of points
len_data = len(data)

# Drop duplicates
# (just to be sure; if the database is well conceived there should
# not be duplicates)
data.drop_duplicates(subset=("sb_name", "x", "z", "chronology", "hierarchy"),
                     inplace=True)


# ==============================================================
# Creation of the SBs objects
# ==============================================================
print("")
print("    *********************************")
print("    * Handling SBs related stuff... *")
print("    *********************************")
print("")

print("    => Creating SBs objects... ")
# Create a list of SBs objects
sbs = hiegeo.create_sb_from_data(data, x, color=par["colors"])


# ==============================================================
# SBs various plots
# ==============================================================
print("\n\n    => Plotting SBs... ")

# ==============================================================
# Plot SBs
# ==============================================================
fig = pl.figure(figsize=(8,5))
ax = pl.subplot(111)

ax.set_title("Stratigraphic boundaries, Hierarchy 3,2,1")
hiegeo.plot_sb_ax(ax, [1,2,3])

ax.set_xlabel("x [m]")
ax.set_ylabel("z [m]")

ax.set_xlim((x_min, x_max))
ax.set_ylim((z_min, z_max))

pl.legend(bbox_to_anchor=(1.04,1), loc="upper left")
pl.tight_layout()

pl.savefig("SBs_Hierarchy3-2-1_simple.png", dpi=400)
pl.savefig("SBs_Hierarchy3-2-1_simple.pdf")
pl.close()
print('    - Plotted figure "SBs_Hierarchy3-2-1_simple.png/png"')

# ==============================================================
# SU related
# (now deal with the SUs)
# ==============================================================
print("")
print("    *********************************")
print("    * Handling SUs related stuff... *")
print("    *********************************")
print("")

# Collect all the defined SBs, following different criteria (see the
# documentation of the function `get_sbobj_by_hie` for more info.)
sbobs_ge = {}
sbobs_ge[1] = hiegeo.get_sbobj_by_hie(1, mode="ge",  reverse=False)
sbobs_ge[2] = hiegeo.get_sbobj_by_hie(2, mode="ge", reverse=False)
sbobs_ge[3] = hiegeo.get_sbobj_by_hie(3, mode="ge", reverse=False)

sbobs_eq = {}
sbobs_eq[1] = hiegeo.get_sbobj_by_hie(1, mode="eq",  reverse=False)
sbobs_eq[2] = hiegeo.get_sbobj_by_hie(2, mode="eq", reverse=False)
sbobs_eq[3] = hiegeo.get_sbobj_by_hie(3, mode="eq", reverse=False)

# Create a dictionary of SUs for the different hierarchy
SUs = {1: [], 2: [], 3: []}

# This is the matrix for the GSLIB/VTK output
out = np.zeros((nz, nx))

# This is the current hierarchy to be handled
curr_hie = 3
for i, sbob in enumerate(sbobs_eq[curr_hie][:-1]):
    print("    Creating SU with bottom {0}".format(sbobs_eq[curr_hie][i].name))
    SUs[curr_hie].append( hiegeo.SUnit(name="SU{0}".format(i),
                                      bot=sbobs_eq[curr_hie][i],
                                      sbs=sbobs_ge[curr_hie][i:]))
    mnn = np.tile(~np.isnan(SUs[curr_hie][i].z_bot), (nz, 1))
    with warnings.catch_warnings():
        # This happens because where a SU is not defined all values are NaN.
        # Ignoring this warning should not be harmful.
        warnings.simplefilter("ignore")
        mask_bot =  (zmesh >= SUs[curr_hie][i].z_bot)
        mask_top =  (zmesh <  SUs[curr_hie][i].z_top)
        out[mask_top & mask_bot] = i+1    


# ==============================================================
# Plot SUs (simple version)
# ==============================================================

hie_alpha = np.linspace(0,1,data["hierarchy"].max()+1)

hiemins = [1,2,3]

for hiemin in hiemins:
    #
    # Plot hierarchies
    #
    file_png = "SUs_min-hierarchy{0}.png".format(hiemin)
    file_pdf = "SUs_min-hierarchy{0}.pdf".format(hiemin)    
    fig = pl.figure(figsize=(8,5))
    ax = pl.subplot(111)
    ax.set_position([0.1,0.1,0.65,0.8])
    
    ax.set_title("Stratigraphic units, min hierarchy: {0}".format(hiemin))

    ax.set_xlabel("x [m]")
    ax.set_ylabel("z [m]")
    ax.set_xlim((x_min, x_max))
    ax.set_ylim((z_min, z_max))
    
    hiegeo.plot_su_ax(ax, hiemin, hie_alpha)

    # Put a legend to the right of the current axis
    ax.legend(bbox_to_anchor=(1.04,1), loc="upper left")

    pl.savefig(file_png, dpi=400)
    pl.savefig(file_pdf)    
    pl.close()
 
# ==============================================================
# Plot the hierarchical representation
# ==============================================================
print("")
print("    *******************************")
print("    * Hierarchical representation *")
print("    *******************************")
print("")
for root_sb in reversed(sbs[3]):
    for pre, _, node in at.RenderTree(root_sb):
        treestr = "        {0}{1}".format(pre, node.name)
        print(treestr.ljust(8))

print("")   
