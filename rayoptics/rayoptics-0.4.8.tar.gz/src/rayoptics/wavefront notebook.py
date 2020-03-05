#!/usr/bin/env python
# coding: utf-8

# In[1]:


#%matplotlib inline
get_ipython().run_line_magic('matplotlib', 'inline')
#get_ipython().run_line_magic('matplotlib', 'widget')


# In[2]:


# initialization
from rayoptics.environment import *

from rayoptics.optical import analyses
from rayoptics.mpl.axisarrayfigure import Wavefront


# In[3]:


root_pth = Path(rayoptics.__file__).resolve().parent


# # Create a new model

# In[81]:


opm = OpticalModel()
sm = opm.seq_model
osp = opm.optical_spec
pm = opm.parax_model


# ## Define first order aperture and field for system

# In[82]:


pupil_diameter = 50.
pupil_radius = pupil_diameter/2
osp.pupil = PupilSpec(osp, key=['object', 'pupil'], value=pupil_diameter)

# single field on-axis
osp.field_of_view = FieldSpec(osp, key=['object', 'angle'], flds=[0.0])

# wavelength for analysis: 550nm
osp.spectral_region = WvlSpec([(550.0, 1.0)], ref_wl=0)


# ### object at infinity, i.e. collimated input

# In[83]:


sm.gaps[0].thi = 1e+11


# In[84]:


opm.add_mirror(lbl='M1', profile=Conic, r=-500., cc=-1., t=-250.)


# In[85]:


opm.update_model()


# # List first order data

# In[86]:


osp.parax_data.fod.list_first_order_data()


# # Draw a lens picture

# In[87]:


layout_plt = plt.figure(FigureClass=LensLayoutFigure, opt_model=opm).plot()


# In[88]:


fld, wvl, foc = osp.lookup_fld_wvl_focus(0)


# In[89]:


wavefront_plt = plt.figure(FigureClass=WavefrontFigure, opt_model=opm, num_rays=5).plot()

wavefront_plt.axis_data_array[0][0][0][2]
# In[90]:


wave_plt2 = plt.figure(FigureClass=Wavefront, opt_model=opm, num_rays=5).plot()


# In[91]:


grid, upd_grid = grid_pkg = analyses.trace_wavefront(opm, fld, wvl, foc, num_rays=5)


# In[92]:


opd = analyses.focus_wavefront(opm, grid_pkg, fld, wvl, foc)


# In[93]:


g = np.rollaxis(np.array(opd), 2)
max_data_value = max(np.max(g[2]), -np.min(g[2]))
#max_value = max_data_value
max_value = 2.5


# In[94]:


fig, ax = plt.subplots()
#im = ax.imshow(Z, interpolation='bilinear', cmap=cm.RdYlGn,
#               origin='lower', extent=[-3, 3, -3, 3],
#               vmax=abs(Z).max(), vmin=-abs(Z).max())
im = ax.imshow(g[2], cmap="RdBu_r", vmin=-max_value, vmax=max_value, extent=[-1., 1., -1., 1.], origin='lower')
fig.colorbar(im, ax=ax)
ax.set_aspect('equal')
plt.show()


# In[95]:


opd[2][1]


# In[96]:


upd_grid[2][1]


# In[97]:


opd_grid = analyses.eval_wavefront(opm, fld, wvl, foc, num_rays=5)


# In[98]:


opd_grid[2][1]


# In[99]:


vars(wavefront_plt)


# In[100]:


sm.ifcs[1].profile.cc


# In[ ]:




