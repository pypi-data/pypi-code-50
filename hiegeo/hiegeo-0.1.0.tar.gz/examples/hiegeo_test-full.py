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
    `hiegeo_test-full.py`

:Purpose:
    A script to test the module `hiegeo.py`.

:Usage:
    From the shell type `./hiegeo_test-full.py`, or hit `<F5>` or `run` if you are
    using spyderlib.

:Parameters:
    Required input files:
        - One JSON file containing the main parameters.
        - One CSV file with the info about the intersections/contact points.
    See the attached documentation for more details.

:Version:
    See file `hiegeo.py`
    
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
# Plot SBs (simple version)
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
print('    - Plotted figure "SBs_Hierarchy3-2-1_simple.png/pdf"')

# ==============================================================
# Plot SBs (complete version, for Hierarchy 3,2 & 1)
# NOTE: The "complete version" only include more control on
#       the legend appearance, required to create the figures
#       included in the manuscript.
# ==============================================================
fig, ax  = pl.subplots(1,1, figsize=(8,5))

# This is only useful to avoid calling the "tight_layout" command, just to
# have all the figures for the different hierarchy having the same size...
ax.set_position([0.1,0.1,0.65,0.8])

pl.title("Stratigraphic boundaries, Hierarchy 3,2,1")
hiegeo.plot_sb_ax(ax, [1,2,3])

pl.xlabel("x [m]")
pl.ylabel("z [m]")

pl.xlim((x_min, x_max))
pl.ylim((z_min, z_max))


# Collect (in a dictionary) all the SBs defined in the script
# depending on their hierarchy
sbobs = {}
sbobs[3] = hiegeo.get_sbobj_by_hie(3, reverse=True)
sbobs[2] = hiegeo.get_sbobj_by_hie(2, reverse=True)
sbobs[1] = hiegeo.get_sbobj_by_hie(1, reverse=True)

# Create the legend for SBs of hierarchy 3
hand3 = []
for sbob in sbobs[3]:
    hand3.append(mlines.Line2D([], [], color=sbob.color,
                               label="{0.name} ({0.chronology})".format(sbob),
                               lw=3))
leg3 = pl.legend(handles=hand3, bbox_to_anchor=(1.04, 1), loc="upper left",
                 borderaxespad=0., title="Hierarchy 3")
pl.gca().add_artist(leg3)

# Create the legend for SBs of hierarchy 2    
hand2 = []
for sbob in sbobs[2]:
    hand2.append(mlines.Line2D([], [], color=sbob.color,
                               label="{0.name} ({0.chronology})".format(sbob), lw=2))

leg2 = pl.legend(handles=hand2, bbox_to_anchor=(1.04, 0.6), loc="upper left",
                 borderaxespad=0., title="Hierarchy 2")
pl.gca().add_artist(leg2)

# Create the legend for SBs of hierarchy 1    
hand1 = []
for sbob in sbobs[1]:
    hand1.append(mlines.Line2D([], [], color=sbob.color,
                               label="{0.name} ({0.chronology})".format(sbob), lw=1))

leg1 = pl.legend(handles=hand1, bbox_to_anchor=(1.04, 0.3), loc="upper left",
                 borderaxespad=0., title="Hierarchy 1")
pl.gca().add_artist(leg1)

pl.savefig("SBs_Hierarchy3-2-1.png", dpi=400)
pl.savefig("SBs_Hierarchy3-2-1.pdf")
pl.close()
print('    - Plotted figure "SBs_Hierarchy3-2-1.png/pdf"')


# ==============================================================
# Plot SBs (complete version, for Hierarchy 3 & 2)
# NOTE: The "complete version" only include more control on
#       the legend appearance, required to create the figures
#       included in the manuscript.
# ==============================================================
fig, ax  = pl.subplots(1,1, figsize=(8,5))

# This is only useful to avoid calling the "tight_layout" command, just to
# have all the figures for the different hierarchy having the same size...
ax.set_position([0.1,0.1,0.65,0.8])

pl.title("Stratigraphic boundaries, Hierarchy 3,2")
hiegeo.plot_sb_ax(ax, [2,3])

pl.xlabel("x [m]")
pl.ylabel("z [m]")

pl.xlim((x_min, x_max))
pl.ylim((z_min, z_max))


# Collect (in a dictionary) all the SBs defined in the script
# depending on their hierarchy
sbobs = {}
sbobs[3] = hiegeo.get_sbobj_by_hie(3, reverse=True)
sbobs[2] = hiegeo.get_sbobj_by_hie(2, reverse=True)

# Create the legend for SBs of hierarchy 3
hand3 = []
for sbob in sbobs[3]:
    hand3.append(mlines.Line2D([], [], color=sbob.color,
                               label="{0.name} ({0.chronology})".format(sbob),
                               lw=3))
leg3 = pl.legend(handles=hand3, bbox_to_anchor=(1.04, 1), loc="upper left",
                 borderaxespad=0., title="Hierarchy 3")
pl.gca().add_artist(leg3)

# Create the legend for SBs of hierarchy 2    
hand2 = []
for sbob in sbobs[2]:
    hand2.append(mlines.Line2D([], [], color=sbob.color,
                               label="{0.name} ({0.chronology})".format(sbob), lw=2))

leg2 = pl.legend(handles=hand2, bbox_to_anchor=(1.04, 0.6), loc="upper left",
                 borderaxespad=0., title="Hierarchy 2")
pl.gca().add_artist(leg2)

pl.savefig("SBs_Hierarchy3-2.png", dpi=400)
pl.savefig("SBs_Hierarchy3-2.pdf")
pl.close()
print('    - Plotted figure "SBs_Hierarchy3-2.png/pdf"')


# ==============================================================
# Plot SBs (complete version, for Hierarchy 3)
# NOTE: The "complete version" only include more control on
#       the legend appearance, required to create the figures
#       included in the manuscript.
# ==============================================================
fig, ax  = pl.subplots(1,1, figsize=(8,5))

# This is only useful to avoid calling the "tight_layout" command, just to
# have all the figures for the different hierarchy having the same size...
ax.set_position([0.1,0.1,0.65,0.8])

pl.title("Stratigraphic boundaries, Hierarchy 3")
hiegeo.plot_sb_ax(ax, [3])

pl.xlabel("x [m]")
pl.ylabel("z [m]")

pl.xlim((x_min, x_max))
pl.ylim((z_min, z_max))


# Collect (in a dictionary) all the SBs defined in the script
# depending on their hierarchy
sbobs = {}
sbobs[3] = hiegeo.get_sbobj_by_hie(3, reverse=True)

# Create the legend for SBs of hierarchy 3
hand3 = []
for sbob in sbobs[3]:
    hand3.append(mlines.Line2D([], [], color=sbob.color,
                               label="{0.name} ({0.chronology})".format(sbob),
                               lw=3))
leg3 = pl.legend(handles=hand3, bbox_to_anchor=(1.04, 1), loc="upper left",
                 borderaxespad=0., title="Hierarchy 3")
pl.gca().add_artist(leg3)

pl.savefig("SBs_Hierarchy3.png", dpi=400)
pl.savefig("SBs_Hierarchy3.pdf")
pl.close()
print('    - Plotted figure "SBs_Hierarchy3.png/pdf"')


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
# Plot SUs (complete version, for Hierarchy 3)
# ==============================================================
fig, ax  = pl.subplots(1,1, figsize=(8,5)) 
ax.set_position([0.1,0.1,0.65,0.8])
 
hand3 = []
curr_hie = 3
for i, sbob in enumerate(sbobs_eq[curr_hie][:-1]):
    pl.fill_between(SUs[curr_hie][i].bot.xd, SUs[curr_hie][i].z_bot,
                    SUs[curr_hie][i].z_top, where=SUs[curr_hie][i].domain,
                    label=SUs[curr_hie][i].name, facecolor=sbob.color,
                        edgecolor="black", lw=0.5)
    hand3.append(mpatches.Patch(color=sbob.color,
                                label="{0.name}".format(SUs[curr_hie][i]), lw=3))    

leg3 = pl.legend(handles=hand3, bbox_to_anchor=(1.04, 1), loc="upper left",
                 borderaxespad=0., title="Hierarchy 3")
ax = pl.gca().add_artist(leg3)

pl.title("Stratigraphic units, Hierarchy 3")
pl.xlim((x_min, x_max))
pl.ylim((z_min, z_max))
pl.xlabel("x [m]")
pl.ylabel("z [m]")

pl.savefig("SUs_Hierarchy3.png", dpi=400)
pl.savefig("SUs_Hierarchy3.pdf")
print('    - Plotted figure "SUs_Hierarchy3.png/pdf"')
pl.close()

curr_hie = 2
out_max = np.max(out)
for i, sbob in enumerate(sbobs_eq[curr_hie]):
    print("    Creating SU with bottom {0}".format(sbobs_eq[curr_hie][i].name))
    # Check who is the parent of the current SU
    SUs_cand = SUs[curr_hie+1]
    SUparent = next(su for su in SUs_cand if su.bot.name ==
                    sbobs_eq[curr_hie][i].parent.name)
    curr_name = SUparent.name + "-1"
    SUparent.name = SUparent.name + "-0"
    
    SUs[curr_hie].append( hiegeo.SUnit(name=curr_name,
       bot=sbobs_eq[curr_hie][i], sbs=sbobs_ge[curr_hie][i:]))
    
    with warnings.catch_warnings():
        # This happens because where a SU is not defined all values are NaN.
        # Ignoring this warning should not be harmful.
        warnings.simplefilter("ignore")
        out[(zmesh >= SUs[curr_hie][i].z_bot) &
            (zmesh < SUs[curr_hie][i].z_top)] = out_max + i + 1

# ==============================================================
# Plot SUs (complete version, for Hierarchy 3, 2)
# ==============================================================
fig, ax  = pl.subplots(1,1, figsize=(8,5)) 
ax.set_position([0.1,0.1,0.65,0.8])
hand3 = []

curr_hie = 3
for i, sbob in enumerate(sbobs_eq[curr_hie][:-1]):
    pl.fill_between(SUs[curr_hie][i].bot.xd, SUs[curr_hie][i].z_bot,
                    SUs[curr_hie][i].z_top, where=SUs[curr_hie][i].domain,
                    label=SUs[curr_hie][i].name, facecolor=sbob.color,
                        edgecolor="black", lw=0.5)
    hand3.append(mpatches.Patch(color=sbob.color,
                                label="{0.name}".format(SUs[curr_hie][i]), lw=3))    

leg3 = pl.legend(handles=hand3, bbox_to_anchor=(1.04, 1), loc="upper left",
                 borderaxespad=0., title="Hierarchy 3")
ax = pl.gca().add_artist(leg3)

hand2 = []
# Colors for S0-1, S1-1, 
col = ["#e46668", "#fdc995", "#c7e5f0", "#72a7ce"]
curr_hie = 2
for i, sbob in enumerate(sbobs_eq[curr_hie]):
    pl.fill_between(SUs[curr_hie][i].bot.xd, SUs[curr_hie][i].z_bot,
                    SUs[curr_hie][i].z_top, where=SUs[curr_hie][i].domain,
                    label=SUs[curr_hie][i].name, facecolor=col[i],
                        edgecolor="black", lw=0.5)
    hand2.append(mpatches.Patch(color=col[i],
                                label="{0.name}".format(SUs[curr_hie][i]), lw=3))        

leg2 = pl.legend(handles=hand2, bbox_to_anchor=(1.04, 0.65), loc="upper left",
                 borderaxespad=0., title="Hierarchy 2")
ax = pl.gca().add_artist(leg2)

pl.title("Stratigraphic units, Hierarchy 3, 2")
pl.xlim((x_min, x_max))
pl.ylim((z_min, z_max))
pl.xlabel("x [m]")
pl.ylabel("z [m]")

pl.savefig("SUs_Hierarchy3-2.png", dpi=400)
pl.savefig("SUs_Hierarchy3-2.pdf")
print('    - Plotted figure "SUs_Hierarchy3-2.png/pdf"')
pl.close()


curr_hie = 1
out_max = np.max(out)
for i, sbob in enumerate(sbobs_eq[curr_hie]):
    print("    Creating SU with bottom {0}".format(sbobs_eq[curr_hie][i].name))
    SUs_cand = SUs[curr_hie+1]
    SUparent = next(su for su in SUs_cand if su.bot.name ==
                    sbobs_eq[curr_hie][i].parent.name)
    curr_name = SUparent.name + "-1"#.format(i+1)
    SUparent.name = SUparent.name + "-0"

    SUs[curr_hie].append( hiegeo.SUnit(name=curr_name,
       bot=sbobs_eq[curr_hie][i], sbs=sbobs_ge[curr_hie][i:]))
    with warnings.catch_warnings():
        # This happens because where a SU is not defined all values are NaN.
        # Ignoring this warning should not be harmful.
        warnings.simplefilter("ignore")
        out[(zmesh >= SUs[curr_hie][i].z_bot) &
            (zmesh < SUs[curr_hie][i].z_top)] = out_max + i + 1


# ==============================================================
# Plot SUs (complete version, for Hierarchy 3, 2 & 1)
# ==============================================================
fig, ax  = pl.subplots(1,1, figsize=(8,5)) 
ax.set_position([0.1,0.1,0.65,0.8])
hand3 = []

curr_hie = 3
for i, sbob in enumerate(sbobs_eq[curr_hie][:-1]):
    pl.fill_between(SUs[curr_hie][i].bot.xd, SUs[curr_hie][i].z_bot,
                    SUs[curr_hie][i].z_top, where=SUs[curr_hie][i].domain,
                    label=SUs[curr_hie][i].name, facecolor=sbob.color,
                        edgecolor="black", lw=0.5)
    hand3.append(mpatches.Patch(color=sbob.color,
                                label="{0.name}".format(SUs[curr_hie][i]), lw=3))    

leg3 = pl.legend(handles=hand3, bbox_to_anchor=(1.04, 1), loc="upper left",
                 borderaxespad=0., title="Hierarchy 3")
ax = pl.gca().add_artist(leg3)

hand2 = []
col = ["#e46668", "#fdc995", "#c7e5f0", "#72a7ce"]
curr_hie = 2
for i, sbob in enumerate(sbobs_eq[curr_hie]):
    pl.fill_between(SUs[curr_hie][i].bot.xd, SUs[curr_hie][i].z_bot,
                    SUs[curr_hie][i].z_top, where=SUs[curr_hie][i].domain,
                    label=SUs[curr_hie][i].name, facecolor=col[i],
                        edgecolor="black", lw=0.5)
    hand2.append(mpatches.Patch(color=col[i],
                                label="{0.name}".format(SUs[curr_hie][i]), lw=3))        

leg2 = pl.legend(handles=hand2, bbox_to_anchor=(1.04, 0.65), loc="upper left",
                 borderaxespad=0., title="Hierarchy 2")
ax = pl.gca().add_artist(leg2)


hand1 = []
curr_hie = 1
col = ["#fee4ca", "#e3f2f7"]
for i, sbob in enumerate(sbobs_eq[curr_hie]):
    pl.fill_between(SUs[curr_hie][i].bot.xd, SUs[curr_hie][i].z_bot,
                    SUs[curr_hie][i].z_top, where=SUs[curr_hie][i].domain,
                    label=SUs[curr_hie][i].name, facecolor=col[i],
                        edgecolor="black", lw=0.5)
    hand1.append(mpatches.Patch(color=col[i],
                                label="{0.name}".format(SUs[curr_hie][i]), lw=3))

leg1 = pl.legend(handles=hand1, bbox_to_anchor=(1.04, 0.35), loc="upper left",
                 borderaxespad=0., title="Hierarchy 1")
# Add the legend manually to the current Axes.
ax = pl.gca().add_artist(leg1)

pl.title("Stratigraphic units, Hierarchy 3, 2, 1")
pl.xlim((x_min, x_max))
pl.ylim((z_min, z_max))
pl.xlabel("x [m]")
pl.ylabel("z [m]")

pl.savefig("SUs_Hierarchy3-2-1.png", dpi=400)
pl.savefig("SUs_Hierarchy3-2-1.pdf")
print('    - Plotted figure "SUs_Hierarchy3-2-1.png/pdf"')
pl.close()


# ==============================================================
# Save SUs as a GSLIB file
# ==============================================================

# Save output as GSLIB file
out_df = pd.DataFrame({"code": out.ravel(order="C")})
file_out = "SUs.gslib"

# Save the mask as a GSLIB file
with open(file_out, "w") as out_obj:
    out_obj.write("{0} 1 {1} {2} 1.0 {3} {4} 0.0 {5}\n1\ncode\n".format(nx, nz,
                  dx, dz, x_min, z_min))
    out_df.to_csv(out_obj, index=False, index_label=False, header=False,
                 float_format="%d", sep="\t")



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
