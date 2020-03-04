########################################################
# Started Logging At: 2019-03-13 18:45:04
########################################################

########################################################
# # Started Logging At: 2019-03-13 18:45:04
########################################################
get_ipython().magic('run fit_nh3_cube.py')
########################################################
# Started Logging At: 2019-03-13 19:00:35
########################################################

########################################################
# # Started Logging At: 2019-03-13 19:00:35
########################################################
get_ipython().magic('debug')
########################################################
# Started Logging At: 2019-03-13 19:01:15
########################################################

########################################################
# # Started Logging At: 2019-03-13 19:01:15
########################################################
get_ipython().magic('run fit_nh3_cube.py')
get_ipython().magic('run fit_nh3_test2.py')
pl.clf()
import pylab as pl
pl.clf()
get_ipython().magic('run fit_nh3_test2.py')
stack.plot_spectrum(50,50)
oneone.plot_spectrum(50,50)
twotwo.plot_spectrum(50,50)
stack.plot_special_kwargs = {'fignum':3, 'vrange':[55,135]}
get_ipython().magic('run fit_nh3_test2.py')
get_ipython().magic('run fit_nh3_test2.py')
stack.mapplot()
stack.mapplot()
########################################################
# Started Logging At: 2019-03-13 19:06:04
########################################################

########################################################
# # Started Logging At: 2019-03-13 19:06:04
########################################################
########################################################
# Started Logging At: 2019-03-13 19:06:56
########################################################

########################################################
# # Started Logging At: 2019-03-13 19:06:56
########################################################
stack.mapplot()
########################################################
# Started Logging At: 2019-03-13 19:09:36
########################################################
########################################################
# # Started Logging At: 2019-03-13 19:09:36
########################################################
get_ipython().magic('matplotlib notebook')
get_ipython().magic('run fit_nh3_test2.py')
stack.mapplot()
pl.show()
import pylab as pl
pl.show()
pl.figure(3)
pl.show()
stack.plot_spectrum(50,50)
stack.plot_spectrum(50,50)
pl.show()
pl.figure(3)
stack.plot_spectrum(50,50)
pl.show()
pl.figure(3)
stack.plot_spectrum(50,50)
pl.show()
import pylab as pl
pl.show()
stack.mapplot()
import pylab as pl
pl.show()
pl.figure(3)
pl.show()
pl.figure(3)
pl.show()
pl.figure(3)
pl.show()
pl.figure(3)
pl.show()
pl.figure(3)
pl.plot([0])
pl.show()
pl.figure(3)
pl.plot([0])
pl.show()
pl.close(3)
pl.figure(3)
pl.plot([0])
pl.show()
pl.close(3)
pl.figure(3)
pl.plot([0])
pl.show()
stack.mapplot()
pl.show()
oneone
#[Out]# <Cube object over spectral range 23.681 : 23.709 GHz and flux range = [nan, nan] Jy / beam with shape (57, 241, 961) at -0x7fffffffeed4a462>
oneone.cube
#[Out]# array([[[nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         ...,
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan]],
#[Out]# 
#[Out]#        [[nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         ...,
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan]],
#[Out]# 
#[Out]#        [[nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         ...,
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan]],
#[Out]# 
#[Out]#        ...,
#[Out]# 
#[Out]#        [[nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         ...,
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan]],
#[Out]# 
#[Out]#        [[nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         ...,
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan]],
#[Out]# 
#[Out]#        [[nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         ...,
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan],
#[Out]#         [nan, nan, nan, ..., nan, nan, nan]]], dtype=float32)
from spectral_cube import SpectralCube
oneone = SpectralCube.read('/Users/adam/work/gc/gc_amm22.res.gal.fits')
oneone
#[Out]# SpectralCube with shape=(57, 241, 961) and unit=Jy / beam:
#[Out]#  n_x:    961  type_x: GLON-SIN  unit_x: deg    range:     0.834354 deg:  359.767671 deg
#[Out]#  n_y:    241  type_y: GLAT-SIN  unit_y: deg    range:    -0.164100 deg:    0.102567 deg
#[Out]#  n_s:     57  type_s: VOPT      unit_s: m / s  range:  -185643.362 m / s:  168216.172 m / s
oneone[:,50:60,50:60].spectral_slab(-50*u.km/u.s, 50*u.km/u.s)
from astropy import units as u
oneone[:,50:60,50:60].spectral_slab(-50*u.km/u.s, 50*u.km/u.s)
#[Out]# SpectralCube with shape=(17, 10, 10) and unit=Jy / beam:
#[Out]#  n_x:     10  type_x: GLON-SIN  unit_x: deg    range:     0.768796 deg:    0.778797 deg
#[Out]#  n_y:     10  type_y: GLAT-SIN  unit_y: deg    range:    -0.108545 deg:   -0.098545 deg
#[Out]#  n_s:     17  type_s: VOPT      unit_s: m / s  range:   -52946.037 m / s:   48156.687 m / s
oneone.world_spines
#[Out]# <bound method SpatialCoordMixinClass.world_spines of SpectralCube with shape=(57, 241, 961) and unit=Jy / beam:
#[Out]#  n_x:    961  type_x: GLON-SIN  unit_x: deg    range:     0.834354 deg:  359.767671 deg
#[Out]#  n_y:    241  type_y: GLAT-SIN  unit_y: deg    range:    -0.164100 deg:    0.102567 deg
#[Out]#  n_s:     57  type_s: VOPT      unit_s: m / s  range:  -185643.362 m / s:  168216.172 m / s>
oneone.world_spines()
oneone.spatial_coordinate_map()
oneone.spatial_coordinate_map
#[Out]# [<Quantity [[-0.16410012, -0.16410013, -0.16410013, ..., -0.16410009,
#[Out]#              -0.16410008, -0.16410008],
#[Out]#             [-0.162989  , -0.16298901, -0.16298902, ..., -0.16298898,
#[Out]#              -0.16298897, -0.16298896],
#[Out]#             [-0.16187789, -0.1618779 , -0.1618779 , ..., -0.16187786,
#[Out]#              -0.16187786, -0.16187785],
#[Out]#             ...,
#[Out]#             [ 0.10034457,  0.10034457,  0.10034456, ...,  0.1003446 ,
#[Out]#               0.10034461,  0.10034461],
#[Out]#             [ 0.10145569,  0.10145568,  0.10145567, ...,  0.10145571,
#[Out]#               0.10145572,  0.10145573],
#[Out]#             [ 0.1025668 ,  0.10256679,  0.10256679, ...,  0.10256683,
#[Out]#               0.10256683,  0.10256684]] deg>,
#[Out]#  <Quantity [[  0.83435566,   0.8332445 ,   0.83213333, ..., 359.7698915 ,
#[Out]#              359.76878033, 359.76766917],
#[Out]#             [  0.83435563,   0.83324447,   0.8321333 , ..., 359.76989153,
#[Out]#              359.76878036, 359.7676692 ],
#[Out]#             [  0.8343556 ,   0.83324444,   0.83213327, ..., 359.76989156,
#[Out]#              359.76878039, 359.76766923],
#[Out]#             ...,
#[Out]#             [  0.8343543 ,   0.83324314,   0.83213198, ..., 359.76989287,
#[Out]#              359.76878171, 359.76767055],
#[Out]#             [  0.83435432,   0.83324315,   0.83213199, ..., 359.76989285,
#[Out]#              359.76878169, 359.76767053],
#[Out]#             [  0.83435433,   0.83324317,   0.83213201, ..., 359.76989283,
#[Out]#              359.76878167, 359.76767051]] deg>]
from spectral_cube import SpectralCube
oneone = SpectralCube.read('/Users/adam/work/gc/gc_amm11.res.gal.fits')
twotwo = SpectralCube.read('/Users/adam/work/gc/gc_amm22.res.gal.fits')
oneone[:,140:150,460:470].max(axis=0).quicklook()
from spectral_cube import SpectralCube
oneone = SpectralCube.read('/Users/adam/work/gc/gc_amm11.res.gal.fits')
twotwo = SpectralCube.read('/Users/adam/work/gc/gc_amm22.res.gal.fits')
oneone[:,140:150,460:470].write('/Users/adam/repos/pyspeckit-example-files/gcnh3_11.fits')
twotwo[:,140:150,460:470].write('/Users/adam/repos/pyspeckit-example-files/gcnh3_22.fits')
get_ipython().magic('pwd ')
#[Out]# '/Users/adam/repos/pyspeckit/examples'
########################################################
# Started Logging At: 2019-03-13 20:06:53
########################################################
########################################################
# # Started Logging At: 2019-03-13 20:06:54
########################################################
get_ipython().magic('matplotlib notebook')
import pylab as pl
import pyspeckit

twotwo = pyspeckit.Cube('gcnh3_11.fits')
oneone = pyspeckit.Cube('gcnh3_22.fits')
oneone.xarr.velocity_convention = 'radio'
twotwo.xarr.velocity_convention = 'radio'
stack = pyspeckit.CubeStack([oneone,twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-30,135]}
stack.mapplot()
pl.show()
pl.figure(3)
pl.show()
pl.figure(3)
stack.plot_spectrum(50,50)
pl.show()
pl.figure(3)
stack.plot_spectrum(5,5)
pl.show()
stack.mapplot(estimator=np.nanmax)
pl.show()
stack.mapplot(estimator=np.nanmax, figure=pl.figure(1))
pl.show()
########################################################
# Started Logging At: 2019-03-13 20:08:03
########################################################
########################################################
# # Started Logging At: 2019-03-13 20:08:03
########################################################
get_ipython().magic('matplotlib notebook')
import pylab as pl
import pyspeckit

twotwo = pyspeckit.Cube('gcnh3_11.fits')
oneone = pyspeckit.Cube('gcnh3_22.fits')
oneone.xarr.velocity_convention = 'radio'
twotwo.xarr.velocity_convention = 'radio'
stack = pyspeckit.CubeStack([oneone,twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-30,135]}
stack.mapplot(estimator=np.nanmax, figure=pl.figure(1))
pl.show()
stack.mapplot(estimator=np.nanmax, figure=pl.figure(1))
pl.show()
stack.mapplot(estimator=np.nanmax)
pl.show()
pl.figure(3)
stack.plot_spectrum(5,5)
pl.show()
stack.mapplot(estimator=np.nanmax)
pl.figure(3)
stack.plot_spectrum(5,5)

pl.show()
########################################################
# Started Logging At: 2019-03-13 20:12:03
########################################################
########################################################
# # Started Logging At: 2019-03-13 20:12:03
########################################################
get_ipython().magic('matplotlib notebook')
import pylab as pl
import pyspeckit

twotwo = pyspeckit.Cube('gcnh3_11.fits')
oneone = pyspeckit.Cube('gcnh3_22.fits')
oneone.xarr.velocity_convention = 'radio'
twotwo.xarr.velocity_convention = 'radio'
stack = pyspeckit.CubeStack([oneone,twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-30,135]}
stack.mapplot(estimator=np.nanmax)
pl.figure(3)
stack.plot_spectrum(5,5)

pl.show()
pl.figure(3)
stack.plot_spectrum(5,5)
pl.show()
########################################################
# Started Logging At: 2019-03-13 20:26:59
########################################################
########################################################
# # Started Logging At: 2019-03-13 20:27:00
########################################################
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=guesses,
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=guesses,
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
stack.mapplot(estimator=np.nanmax)
pl.figure(3)
stack.plot_spectrum(5,5)

pl.show()
import pyspeckit

twotwo = pyspeckit.Cube('gcnh3_11.fits')
oneone = pyspeckit.Cube('gcnh3_22.fits')
oneone.xarr.velocity_convention = 'radio'
twotwo.xarr.velocity_convention = 'radio'
stack = pyspeckit.CubeStack([oneone,twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-30,135]}
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=guesses,
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[10, 10, 13, 10, 50, 0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[10, 10, 13, 10, 50, 0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
stack.mapplot(estimator=np.nanmax)
pl.figure(3)
stack.plot_spectrum(5,5)

pl.show()
import pylab as pl
stack.mapplot(estimator=np.nanmax)
pl.figure(3)
stack.plot_spectrum(5,5)

pl.show()
get_ipython().magic('matplotlib notebook')
import pylab as pl
import pyspeckit

twotwo = pyspeckit.Cube('gcnh3_11.fits')
oneone = pyspeckit.Cube('gcnh3_22.fits')
oneone.xarr.velocity_convention = 'radio'
twotwo.xarr.velocity_convention = 'radio'
stack = pyspeckit.CubeStack([oneone,twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-30,135]}
stack.mapplot(estimator=np.nanmax)
pl.figure(3)
stack.plot_spectrum(5,5)

pl.show()
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[10, 10, 13, 10, 30, 0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
sp = stack.get_spectrum(5,5)
########################################################
# Started Logging At: 2019-03-13 20:30:29
########################################################
########################################################
# # Started Logging At: 2019-03-13 20:30:29
########################################################
stack.mapplot(estimator=np.nanmax)
pl.figure(3)
stack.plot_spectrum(5,5)

pl.show()
sp = stack.get_spectrum(5,5)
get_ipython().magic('matplotlib notebook')
import pylab as pl
import pyspeckit

twotwo = pyspeckit.Cube('gcnh3_11.fits')
oneone = pyspeckit.Cube('gcnh3_22.fits')
oneone.xarr.velocity_convention = 'radio'
twotwo.xarr.velocity_convention = 'radio'
stack = pyspeckit.CubeStack([oneone,twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-30,135]}
sp = stack.get_spectrum(5,5)
sp.plotter()
sp.specfit(fittype='cold_ammonia', guesses=[10,10,13,10,50,0.5])
sp.specfit(fittype='cold_ammonia', guesses=[10,15,13,10,50,0.5])
sp.specfit(fittype='cold_ammonia', guesses=[10,7,13,10,50,0.5])
sp.plotter()
import pyspeckit

twotwo = pyspeckit.Cube('gcnh3_11.fits').to(u.K)
oneone = pyspeckit.Cube('gcnh3_22.fits').to(u.K)
oneone.xarr.velocity_convention = 'radio'
twotwo.xarr.velocity_convention = 'radio'
stack = pyspeckit.CubeStack([oneone,twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-30,135]}
import pyspeckit
from spectral_cube import SpectralCube

cube_oneone = SpectralCube.read('gcnh3_11.fits').to(u.K)
twotwo = pyspeckit.Cube('gcnh3_11.fits')
oneone = pyspeckit.Cube('gcnh3_22.fits')
oneone.xarr.velocity_convention = 'radio'
twotwo.xarr.velocity_convention = 'radio'
stack = pyspeckit.CubeStack([oneone,twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-30,135]}
import pyspeckit
from spectral_cube import SpectralCube
from astropy import units as u
cube_oneone = SpectralCube.read('gcnh3_11.fits').to(u.K)
twotwo = pyspeckit.Cube(cube_oneone)
oneone = pyspeckit.Cube('gcnh3_22.fits')
oneone.xarr.velocity_convention = 'radio'
twotwo.xarr.velocity_convention = 'radio'
stack = pyspeckit.CubeStack([oneone,twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-30,135]}
import pyspeckit
from spectral_cube import SpectralCube
from astropy import units as u
cube_oneone = SpectralCube.read('gcnh3_11.fits').to(u.K)
cube_twotwo = SpectralCube.read('gcnh3_22.fits').to(u.K)
oneone = pyspeckit.Cube.from_hdu(cube_oneone.hdu)
twotwo = pyspeckit.Cube.from_hdu(cube_twotwo.hdu)
oneone.xarr.velocity_convention = 'radio'
twotwo.xarr.velocity_convention = 'radio'
stack = pyspeckit.CubeStack([oneone,twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-30,135]}
import pyspeckit
from spectral_cube import SpectralCube
from astropy import units as u
cube_oneone = SpectralCube.read('gcnh3_11.fits').to(u.K)
cube_twotwo = SpectralCube.read('gcnh3_22.fits').to(u.K)
oneone = pyspeckit.Cube(cube=cube_oneone)
twotwo = pyspeckit.Cube(cube=cube_twotwo)
oneone.xarr.velocity_convention = 'radio'
twotwo.xarr.velocity_convention = 'radio'
stack = pyspeckit.CubeStack([oneone,twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-30,135]}
sp = stack.get_spectrum(5,5)
sp.specfit(fittype='cold_ammonia', guesses=[10,7,13,10,50,0.5])
sp.plotter()
sp.specfit(fittype='cold_ammonia', guesses=[40,7,13,10,50,0.5])
sp.specfit(fittype='cold_ammonia', guesses=[40,7,14.2,6,30,0.5])
sp.specfit(fittype='cold_ammonia', guesses=[40,7,14.2,6,30,0.5])
sp.plotter()
sp.specfit(fittype='cold_ammonia', guesses=[40,15,14.2,6,30,0.5])
sp.specfit(fittype='cold_ammonia', guesses=[40,15,14.2,6,30,0.5])
sp.plotter()
sp.specfit(fittype='cold_ammonia', guesses=[40,13,14.2,5.8,30,0.5])
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[40,13,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[40,13,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[40,13,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[40,13,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[40,13,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[40,13,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[40,13,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[40,13,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[40,13,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[40,13,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[40,13,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[40,13,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
sp.specfit(fittype='cold_ammonia', guesses=[29.8,13,14.2,5.8,30,0.5])
sp.specfit(fittype='cold_ammonia', guesses=[29.8,13,14.2,5.8,30,0.5])
sp.plotter()
sp.specfit(fittype='cold_ammonia', guesses=[29.8,13,14.2,5.8,30,0.5])
sp.specfit(fittype='cold_ammonia', guesses=[29.8,13,14.2,5.8,30,0.5])
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.5],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=3,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,t,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,T,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,T,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,T,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,T,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,T,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,T,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,T,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,T,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,T,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,T,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,T,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,T,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,T,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,T,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,T,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,T,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,0,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,10,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,10,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,10,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,10,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,10,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,10,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,F,F,T,T],
            minpars=[2.73,2.73,10,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,T,F,T,T],
            minpars=[2.73,2.73,10,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,T,F,T,T],
            minpars=[2.73,2.73,10,0,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,T,T,T,T],
            minpars=[2.73,2.73,10,1,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.3],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,T,T,T,T],
            minpars=[2.73,2.73,10,1,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
stack.mapplot(estimator=np.nanmax)
pl.figure(3)
stack.plot_spectrum(5,5)

pl.show()
stack.mapplot(estimator=5)
pl.figure(3)
stack.plot_spectrum(5,5)

pl.show()
stack.parcube
#[Out]# array([[[0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          2.98614101e+01, 2.98145281e+01, 4.76055814e+01, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 2.98646419e+01, 2.98632494e+01,
#[Out]#          2.98606217e+01, 2.98167627e+01, 4.70387372e+01, 6.26421921e+01,
#[Out]#          0.00000000e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 2.98616590e+01, 2.98622741e+01,
#[Out]#          2.98604150e+01, 2.98244868e+01, 4.45146712e+01, 6.53194796e+01,
#[Out]#          4.03846273e+01, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 2.98606806e+01, 2.98594804e+01, 2.98577150e+01,
#[Out]#          2.98568947e+01, 2.98635849e+01, 3.99602017e+01, 3.58027177e+01,
#[Out]#          2.99626257e+01, 2.98567881e+01],
#[Out]#         [0.00000000e+00, 2.98119278e+01, 2.98117313e+01, 2.98113666e+01,
#[Out]#          2.98110647e+01, 2.98064579e+01, 2.99346014e+01, 2.99386427e+01,
#[Out]#          2.98473427e+01, 2.98238132e+01],
#[Out]#         [0.00000000e+00, 4.52902274e+01, 2.69230564e+01, 2.59767970e+01,
#[Out]#          2.40875752e+01, 2.98840363e+01, 3.86050109e+01, 4.13314093e+01,
#[Out]#          4.87608800e+01, 3.96110153e+07],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 2.74244337e+01, 2.55487855e+01,
#[Out]#          2.16224293e+01, 2.99158849e+01, 3.70227317e+01, 5.05517179e+01,
#[Out]#          1.36478886e+02, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 2.32111362e+01, 2.99626057e+01,
#[Out]#          2.98492642e+01, 2.98498584e+01, 3.99901026e+01, 5.26713334e+01,
#[Out]#          7.10156620e+01, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          2.98281313e+01, 2.98138432e+01, 4.32337534e+01, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00]],
#[Out]# 
#[Out]#        [[0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          1.80852935e+03, 1.80652935e+03, 2.57219988e+02, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 2.00552935e+03, 1.80852935e+03,
#[Out]#          1.41452935e+03, 1.41252935e+03, 2.52377274e+02, 2.17800470e+02,
#[Out]#          0.00000000e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 1.61152935e+03, 1.21752935e+03,
#[Out]#          1.01852935e+03, 1.01852935e+03, 2.01485354e+02, 1.92963780e+02,
#[Out]#          3.35293463e+01, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 2.00552935e+03, 1.61152935e+03, 1.21752935e+03,
#[Out]#          8.21529346e+02, 6.24529346e+02, 1.19348301e+02, 3.35293463e+01,
#[Out]#          4.27529346e+02, 8.19529346e+02],
#[Out]#         [0.00000000e+00, 2.00552935e+03, 1.60952935e+03, 1.21552935e+03,
#[Out]#          8.21529346e+02, 4.25529346e+02, 4.27529346e+02, 4.27529346e+02,
#[Out]#          8.21529346e+02, 1.21352935e+03],
#[Out]#         [0.00000000e+00, 5.82199881e+01, 6.27086933e+01, 3.05166616e+01,
#[Out]#          3.79953807e+00, 2.30529346e+02, 3.72862266e+01, 6.10760975e+00,
#[Out]#          4.48535394e+00, 3.05632726e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 2.42619944e+01, 1.23657259e+01,
#[Out]#          3.07672492e+00, 2.30529346e+02, 3.22137341e+00, 6.09053952e+00,
#[Out]#          4.68745574e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 3.08108672e+00, 2.30529346e+02,
#[Out]#          6.24529346e+02, 6.24529346e+02, 3.36650391e+00, 3.60632742e+00,
#[Out]#          3.84311769e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          1.01652935e+03, 1.41252935e+03, 3.30942079e+00, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00]],
#[Out]# 
#[Out]#        [[0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          1.43430118e+01, 1.43430156e+01, 1.45233142e+01, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 1.43431005e+01, 1.43430129e+01,
#[Out]#          1.43427533e+01, 1.43427581e+01, 1.44689577e+01, 1.44082021e+01,
#[Out]#          0.00000000e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 1.43429019e+01, 1.43425558e+01,
#[Out]#          1.43422625e+01, 1.43422651e+01, 1.43963758e+01, 1.43184835e+01,
#[Out]#          1.43068133e+01, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 1.43430990e+01, 1.43429010e+01, 1.43425532e+01,
#[Out]#          1.43417914e+01, 1.43409185e+01, 1.43181480e+01, 1.43077954e+01,
#[Out]#          1.43405348e+01, 1.43421408e+01],
#[Out]#         [0.00000000e+00, 1.43431025e+01, 1.43429049e+01, 1.43425589e+01,
#[Out]#          1.43417941e+01, 1.43388120e+01, 1.43399799e+01, 1.43399805e+01,
#[Out]#          1.43419645e+01, 1.43426472e+01],
#[Out]#         [0.00000000e+00, 1.45072971e+01, 1.44309206e+01, 1.44026491e+01,
#[Out]#          1.49187712e+01, 1.43374712e+01, 1.42436353e+01, 1.42929554e+01,
#[Out]#          1.42742409e+01, 1.48656052e+01],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 1.43437845e+01, 1.43394851e+01,
#[Out]#          1.53285370e+01, 1.43374740e+01, 1.51322586e+01, 1.43906309e+01,
#[Out]#          1.43502646e+01, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 1.52758208e+01, 1.43380121e+01,
#[Out]#          1.43414759e+01, 1.43414777e+01, 1.50423603e+01, 1.48717642e+01,
#[Out]#          1.46119575e+01, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          1.43424432e+01, 1.43427940e+01, 1.51006903e+01, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00]],
#[Out]# 
#[Out]#        [[0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          5.71925609e+00, 5.72477792e+00, 3.00233958e+00, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 5.71854271e+00, 5.71934440e+00,
#[Out]#          5.72171099e+00, 5.72684444e+00, 3.08322161e+00, 2.92159510e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 5.72081861e+00, 5.72427485e+00,
#[Out]#          5.72742468e+00, 5.73178982e+00, 3.31942587e+00, 2.96473391e+00,
#[Out]#          3.98914239e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 5.71948342e+00, 5.72141733e+00, 5.72534280e+00,
#[Out]#          5.73510853e+00, 5.74664165e+00, 3.88066209e+00, 4.96775791e+00,
#[Out]#          5.73733278e+00, 5.73375109e+00],
#[Out]#         [0.00000000e+00, 5.72561198e+00, 5.72757758e+00, 5.73189465e+00,
#[Out]#          5.74383694e+00, 5.80091176e+00, 5.75360948e+00, 5.75254655e+00,
#[Out]#          5.73340834e+00, 5.73080541e+00],
#[Out]#         [0.00000000e+00, 3.18137296e+00, 6.43939046e+00, 6.33739301e+00,
#[Out]#          6.20827911e+00, 5.81864856e+00, 6.56136647e+00, 6.18415028e+00,
#[Out]#          4.44743813e+00, 1.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 5.35735276e+00, 5.48978089e+00,
#[Out]#          4.20605232e+00, 5.81584184e+00, 2.91725749e+00, 2.83618693e+00,
#[Out]#          2.47296523e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 2.77616859e+00, 5.77395272e+00,
#[Out]#          5.74190325e+00, 5.74499093e+00, 2.73343573e+00, 2.53275679e+00,
#[Out]#          2.11036311e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          5.73401174e+00, 5.73006807e+00, 2.45544164e+00, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00]],
#[Out]# 
#[Out]#        [[0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          3.18450441e+01, 3.18364226e+01, 3.24101140e+01, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 3.18447073e+01, 3.18451069e+01,
#[Out]#          3.18460892e+01, 3.18384905e+01, 3.25508404e+01, 3.24323981e+01,
#[Out]#          0.00000000e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 3.18450575e+01, 3.18459085e+01,
#[Out]#          3.18461731e+01, 3.18404047e+01, 3.27257688e+01, 3.25616515e+01,
#[Out]#          3.22734439e+01, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 3.18435568e+01, 3.18444477e+01, 3.18449642e+01,
#[Out]#          3.18435785e+01, 3.18402600e+01, 3.28666534e+01, 3.22639110e+01,
#[Out]#          3.18359258e+01, 3.18306942e+01],
#[Out]#         [0.00000000e+00, 3.18340456e+01, 3.18353191e+01, 3.18361886e+01,
#[Out]#          3.18339821e+01, 3.18065298e+01, 3.18387349e+01, 3.18384098e+01,
#[Out]#          3.18399351e+01, 3.18331898e+01],
#[Out]#         [0.00000000e+00, 3.23103640e+01, 2.91157102e+01, 2.88266645e+01,
#[Out]#          2.94867851e+01, 3.17893850e+01, 2.71172970e+01, 3.13137639e+01,
#[Out]#          3.23571979e+01, 2.44158424e+01],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 2.60990973e+01, 2.68321302e+01,
#[Out]#          2.55560099e+01, 3.17873007e+01, 2.34202680e+01, 2.32383558e+01,
#[Out]#          2.22364193e+01, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 2.42402538e+01, 3.17945891e+01,
#[Out]#          3.18323326e+01, 3.18306632e+01, 2.27833428e+01, 2.24799673e+01,
#[Out]#          2.23533099e+01, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          3.18304346e+01, 3.18333516e+01, 2.21782811e+01, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00]],
#[Out]# 
#[Out]#        [[0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          3.00000000e-01, 3.00000000e-01, 3.00000000e-01, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 3.00000000e-01, 3.00000000e-01,
#[Out]#          3.00000000e-01, 3.00000000e-01, 3.00000000e-01, 3.00000000e-01,
#[Out]#          0.00000000e+00, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 3.00000000e-01, 3.00000000e-01,
#[Out]#          3.00000000e-01, 3.00000000e-01, 3.00000000e-01, 3.00000000e-01,
#[Out]#          3.00000000e-01, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 3.00000000e-01, 3.00000000e-01, 3.00000000e-01,
#[Out]#          3.00000000e-01, 3.00000000e-01, 3.00000000e-01, 3.00000000e-01,
#[Out]#          3.00000000e-01, 3.00000000e-01],
#[Out]#         [0.00000000e+00, 3.00000000e-01, 3.00000000e-01, 3.00000000e-01,
#[Out]#          3.00000000e-01, 3.00000000e-01, 3.00000000e-01, 3.00000000e-01,
#[Out]#          3.00000000e-01, 3.00000000e-01],
#[Out]#         [0.00000000e+00, 3.00000000e-01, 3.00000000e-01, 3.00000000e-01,
#[Out]#          3.00000000e-01, 3.00000000e-01, 3.00000000e-01, 3.00000000e-01,
#[Out]#          3.00000000e-01, 3.00000000e-01],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 3.00000000e-01, 3.00000000e-01,
#[Out]#          3.00000000e-01, 3.00000000e-01, 3.00000000e-01, 3.00000000e-01,
#[Out]#          3.00000000e-01, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 3.00000000e-01, 3.00000000e-01,
#[Out]#          3.00000000e-01, 3.00000000e-01, 3.00000000e-01, 3.00000000e-01,
#[Out]#          3.00000000e-01, 0.00000000e+00],
#[Out]#         [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#          3.00000000e-01, 3.00000000e-01, 3.00000000e-01, 0.00000000e+00,
#[Out]#          0.00000000e+00, 0.00000000e+00]]])
stack.mapplot(estimator=5)
#pl.figure(3)
#stack.plot_spectrum(5,5)

pl.show()
stack.mapplot(estimator=4)
#pl.figure(3)
#stack.plot_spectrum(5,5)

pl.show()
stack.mapplot(estimator=4, vmin=25, vmax=35)
#pl.figure(3)
#stack.plot_spectrum(5,5)

pl.show()
stack.mapplot(estimator=4, vmin=20, vmax=35)
#pl.figure(3)
#stack.plot_spectrum(5,5)

pl.show()
stack.mapplot(estimator=4, vmin=20, vmax=35)
pl.figure(3)
stack.plot_spectrum(7,7)

pl.show()
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[29.8,28,14.2,5.8,30,0.1],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,T,T,T,T],
            minpars=[2.73,2.73,10,1,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
np.random.ran()
np.random.rand()
#[Out]# 0.7714901188973015
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis
xarr11 = spaxis((np.linspace(-50, 50, 100)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.GHz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-50, 50, 100)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.GHz,
                 velocity_convention='radio')

cube11 = np.zeros([100,10,10])
cube22 = np.zeros([100,10,10])
for ii,jj in np.indices([10,10]):
    tkin=np.random.rand()*10+15
    ntot=14+np.random.randn()
    width=1.5+np.random.rand()
    xoff_v=np.random.randn()*5
    spec11 = ammonia.cold_ammonia(xarr11,
                                  tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v
                                  )
    spec22 = ammonia.cold_ammonia(xarr22, tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v)
    cube11[:,ii,jj] = spec11
    cube22[:,ii,jj] = spec22
cube_oneone = pyspeckit.SpectralCube(cube=cube11, xarr=xarr11)
cube_twotwo = pyspeckit.SpectralCube(cube=cube11, xarr=xarr11)
stack = pyspeckit.CubeStack([cube_oneone,cube_twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-30,135]}
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis
xarr11 = spaxis((np.linspace(-50, 50, 100)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.GHz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-50, 50, 100)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.GHz,
                 velocity_convention='radio')

cube11 = np.zeros([100,10,10])
cube22 = np.zeros([100,10,10])
for ii,jj in np.indices(10,10):
    tkin=np.random.rand()*10+15
    ntot=14+np.random.randn()
    width=1.5+np.random.rand()
    xoff_v=np.random.randn()*5
    spec11 = ammonia.cold_ammonia(xarr11,
                                  tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v
                                  )
    spec22 = ammonia.cold_ammonia(xarr22, tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v)
    cube11[:,ii,jj] = spec11
    cube22[:,ii,jj] = spec22
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis
xarr11 = spaxis((np.linspace(-50, 50, 100)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.GHz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-50, 50, 100)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.GHz,
                 velocity_convention='radio')

cube11 = np.zeros([100,10,10])
cube22 = np.zeros([100,10,10])
for ii,jj in zip(*np.indices([10,10])):
    tkin=np.random.rand()*10+15
    ntot=14+np.random.randn()
    width=1.5+np.random.rand()
    xoff_v=np.random.randn()*5
    spec11 = ammonia.cold_ammonia(xarr11,
                                  tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v
                                  )
    spec22 = ammonia.cold_ammonia(xarr22, tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v)
    cube11[:,ii,jj] = spec11
    cube22[:,ii,jj] = spec22
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis
xarr11 = spaxis((np.linspace(-50, 50, 100)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.GHz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-50, 50, 100)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.GHz,
                 velocity_convention='radio')

cube11 = np.zeros([100,10,10])
cube22 = np.zeros([100,10,10])
for ii,jj in zip(range(10), range(10)):
    tkin=np.random.rand()*10+15
    ntot=14+np.random.randn()
    width=1.5+np.random.rand()
    xoff_v=np.random.randn()*5
    spec11 = ammonia.cold_ammonia(xarr11,
                                  tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v
                                  )
    spec22 = ammonia.cold_ammonia(xarr22, tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v)
    cube11[:,ii,jj] = spec11
    cube22[:,ii,jj] = spec22
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis
xarr11 = spaxis((np.linspace(-50, 50, 100)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.GHz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-50, 50, 100)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.GHz,
                 velocity_convention='radio')

cube11 = np.zeros([100,10,10])
cube22 = np.zeros([100,10,10])
for ii,jj in zip(range(10), range(10)):
    tkin=np.random.rand()*10+15
    ntot=14+np.random.randn()
    width=1.5+np.random.rand()
    xoff_v=np.random.randn()*5
    spec11 = ammonia.cold_ammonia(xarr11,
                                  tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v,
                                  tex=tkin
                                  )
    spec22 = ammonia.cold_ammonia(xarr22, tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v, tex=tkin)
    cube11[:,ii,jj] = spec11
    cube22[:,ii,jj] = spec22
cube_oneone = pyspeckit.SpectralCube(cube=cube11, xarr=xarr11)
cube_twotwo = pyspeckit.SpectralCube(cube=cube11, xarr=xarr11)
stack = pyspeckit.CubeStack([cube_oneone,cube_twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-30,135]}
cube_oneone = pyspeckit.Cube(cube=cube11, xarr=xarr11)
cube_twotwo = pyspeckit.Cube(cube=cube11, xarr=xarr11)
stack = pyspeckit.CubeStack([cube_oneone,cube_twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-30,135]}
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[20,15,14.2,2.8,0,0.1],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,T,T,T,T],
            minpars=[2.73,2.73,10,1,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
pl.plot(spec11)
#[Out]# [<matplotlib.lines.Line2D at 0x1a20b16a58>]
pl.plot(spec11)
pl.show()
pl.close('all')
pl.plot(spec11)
pl.show()
pl.close('all')
pl.plot(xarr11, spec11)
pl.show()
xarr11
#[Out]# SpectroscopicAxis([23698447316.47632,...,23690543683.523685], unit=Unit("GHz"), refX=<Quantity 2.36944955e+10 GHz>, refX_unit=Unit("GHz"), frame=None, redshift=None, xtype=None, velocity convention='radio')
xarr11.to(u.km/u.s)
#[Out]# SpectroscopicAxis([-49.99999999998171,...,50.00000000003354], unit=Unit("km / s"), refX=<Quantity 2.36944955e+10 GHz>, refX_unit=Unit("GHz"), frame=None, redshift=None, xtype=None, velocity convention='radio')
ammonia.cold_ammonia(xarr11, tkin=20, ntot=14, width=3, xoff_v=0, tex=19)
#[Out]# array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
log.setLevel('DEBUG')
from astropy import log
log.setLevel('DEBUG')
ammonia.cold_ammonia(xarr11, tkin=20, ntot=14, width=3, xoff_v=0, tex=19)
#[Out]# array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
ammonia.cold_ammonia(xarr11, tkin=24, ntot=14, width=3, xoff_v=0, tex=19)
#[Out]# array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis
xarr11 = spaxis((np.linspace(-50, 50, 100)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.GHz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-50, 50, 100)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.GHz,
                 velocity_convention='radio')

cube11 = np.zeros([100,10,10])
cube22 = np.zeros([100,10,10])
for ii,jj in zip(range(10), range(10)):
    tkin=np.random.rand()*10+15
    ntot=14+np.random.randn()
    width=1.5+np.random.rand()
    xoff_v=np.random.randn()*5
    tex = tkin * 0.8
    spec11 = ammonia.cold_ammonia(xarr11,
                                  tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v,
                                  tex=tex
                                  )
    spec22 = ammonia.cold_ammonia(xarr22, tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v, tex=tex)
    cube11[:,ii,jj] = spec11
    cube22[:,ii,jj] = spec22
from astropy import log
log.setLevel('INFO')
from astropy import log
log.setLevel('INFO')
ammonia.cold_ammonia(xarr11, tkin=24, ntot=14, width=3, xoff_v=0, tex=19)
#[Out]# array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
#[Out]#        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
nh3con.freq_dict['oneone']
#[Out]# 23694495500.0
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis
xarr11 = spaxis((np.linspace(-50, 50, 100)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.Hz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-50, 50, 100)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.Hz,
                 velocity_convention='radio')

cube11 = np.zeros([100,10,10])
cube22 = np.zeros([100,10,10])
for ii,jj in zip(range(10), range(10)):
    tkin=np.random.rand()*10+15
    ntot=14+np.random.randn()
    width=1.5+np.random.rand()
    xoff_v=np.random.randn()*5
    tex = tkin * 0.8
    spec11 = ammonia.cold_ammonia(xarr11,
                                  tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v,
                                  tex=tex
                                  )
    spec22 = ammonia.cold_ammonia(xarr22, tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v, tex=tex)
    cube11[:,ii,jj] = spec11
    cube22[:,ii,jj] = spec22
from astropy import log
log.setLevel('INFO')
ammonia.cold_ammonia(xarr11, tkin=24, ntot=14, width=3, xoff_v=0, tex=19)
#[Out]# array([0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#        0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 5.40728266e-15,
#[Out]#        6.12825377e-14, 7.20971042e-13, 7.51432079e-12, 6.99558221e-11,
#[Out]#        5.81488403e-10, 4.31572929e-09, 2.85996183e-08, 1.69222873e-07,
#[Out]#        8.94027344e-07, 4.21731049e-06, 1.77628817e-05, 6.68011820e-05,
#[Out]#        2.24309108e-04, 6.72511025e-04, 1.80026560e-03, 4.30278125e-03,
#[Out]#        9.18172350e-03, 1.74923227e-02, 2.97517524e-02, 4.51784345e-02,
#[Out]#        6.12550457e-02, 7.41675020e-02, 8.02164037e-02, 7.75473866e-02,
#[Out]#        6.71518904e-02, 5.25059984e-02, 3.81530082e-02, 2.81748891e-02,
#[Out]#        2.53026836e-02, 3.06779364e-02, 4.37946859e-02, 6.23963316e-02,
#[Out]#        8.27437638e-02, 1.00902434e-01, 1.15029944e-01, 1.27467021e-01,
#[Out]#        1.44776893e-01, 1.74609468e-01, 2.20339772e-01, 2.76621219e-01,
#[Out]#        3.29408830e-01, 3.61600512e-01, 3.61537493e-01, 3.29232684e-01,
#[Out]#        2.76370567e-01, 2.20076195e-01, 1.74406389e-01, 1.44697027e-01,
#[Out]#        1.27535794e-01, 1.15222040e-01, 1.01154547e-01, 8.29884854e-02,
#[Out]#        6.25958774e-02, 4.39538343e-02, 3.08307811e-02, 2.54832138e-02,
#[Out]#        2.83877153e-02, 3.83596607e-02, 5.26370247e-02, 6.71429398e-02,
#[Out]#        7.73800760e-02, 7.99358398e-02, 7.38615108e-02, 6.10085760e-02,
#[Out]#        4.50350202e-02, 2.97053205e-02, 1.75069218e-02, 9.21870775e-03,
#[Out]#        4.33736025e-03, 1.82344791e-03, 6.84998499e-04, 2.29945843e-04,
#[Out]#        6.89775462e-05, 1.84900997e-05, 4.42915653e-06, 9.48096716e-07,
#[Out]#        1.81356335e-07, 3.09998194e-08, 4.73509955e-09, 6.46307983e-10,
#[Out]#        7.88292580e-11, 8.59218196e-12, 8.36327352e-13, 7.20971865e-14,
#[Out]#        5.40728906e-15, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#        0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00])
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis
xarr11 = spaxis((np.linspace(-50, 50, 100)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.Hz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-50, 50, 100)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.Hz,
                 velocity_convention='radio')

cube11 = np.zeros([100,10,10])
cube22 = np.zeros([100,10,10])
for ii,jj in zip(range(10), range(10)):
    tkin=np.random.rand()*10+15
    ntot=14+np.random.randn()
    width=1.5+np.random.rand()
    xoff_v=np.random.randn()*5
    tex = tkin * 0.8
    spec11 = ammonia.cold_ammonia(xarr11,
                                  tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v,
                                  tex=tex
                                  )
    spec22 = ammonia.cold_ammonia(xarr22, tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v, tex=tex)
    cube11[:,ii,jj] = spec11
    cube22[:,ii,jj] = spec22
from astropy import log
log.setLevel('INFO')
ammonia.cold_ammonia(xarr11, tkin=24, ntot=14, width=3, xoff_v=0, tex=19)
#[Out]# array([0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#        0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 5.40728266e-15,
#[Out]#        6.12825377e-14, 7.20971042e-13, 7.51432079e-12, 6.99558221e-11,
#[Out]#        5.81488403e-10, 4.31572929e-09, 2.85996183e-08, 1.69222873e-07,
#[Out]#        8.94027344e-07, 4.21731049e-06, 1.77628817e-05, 6.68011820e-05,
#[Out]#        2.24309108e-04, 6.72511025e-04, 1.80026560e-03, 4.30278125e-03,
#[Out]#        9.18172350e-03, 1.74923227e-02, 2.97517524e-02, 4.51784345e-02,
#[Out]#        6.12550457e-02, 7.41675020e-02, 8.02164037e-02, 7.75473866e-02,
#[Out]#        6.71518904e-02, 5.25059984e-02, 3.81530082e-02, 2.81748891e-02,
#[Out]#        2.53026836e-02, 3.06779364e-02, 4.37946859e-02, 6.23963316e-02,
#[Out]#        8.27437638e-02, 1.00902434e-01, 1.15029944e-01, 1.27467021e-01,
#[Out]#        1.44776893e-01, 1.74609468e-01, 2.20339772e-01, 2.76621219e-01,
#[Out]#        3.29408830e-01, 3.61600512e-01, 3.61537493e-01, 3.29232684e-01,
#[Out]#        2.76370567e-01, 2.20076195e-01, 1.74406389e-01, 1.44697027e-01,
#[Out]#        1.27535794e-01, 1.15222040e-01, 1.01154547e-01, 8.29884854e-02,
#[Out]#        6.25958774e-02, 4.39538343e-02, 3.08307811e-02, 2.54832138e-02,
#[Out]#        2.83877153e-02, 3.83596607e-02, 5.26370247e-02, 6.71429398e-02,
#[Out]#        7.73800760e-02, 7.99358398e-02, 7.38615108e-02, 6.10085760e-02,
#[Out]#        4.50350202e-02, 2.97053205e-02, 1.75069218e-02, 9.21870775e-03,
#[Out]#        4.33736025e-03, 1.82344791e-03, 6.84998499e-04, 2.29945843e-04,
#[Out]#        6.89775462e-05, 1.84900997e-05, 4.42915653e-06, 9.48096716e-07,
#[Out]#        1.81356335e-07, 3.09998194e-08, 4.73509955e-09, 6.46307983e-10,
#[Out]#        7.88292580e-11, 8.59218196e-12, 8.36327352e-13, 7.20971865e-14,
#[Out]#        5.40728906e-15, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#        0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00])
pl.close('all')
pl.plot(xarr11, spec11)
pl.show()
cube_oneone = pyspeckit.Cube(cube=cube11, xarr=xarr11)
cube_twotwo = pyspeckit.Cube(cube=cube11, xarr=xarr11)
stack = pyspeckit.CubeStack([cube_oneone,cube_twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-30,135]}
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[20,15,14.2,2.8,0,0.1],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,T,T,T,T],
            minpars=[2.73,2.73,10,1,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
get_ipython().magic('matplotlib notebook')
import pylab as pl
import pyspeckit
from spectral_cube import SpectralCube
from astropy import units as u
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis

nspecpix = 50
nspacepix = 5

xarr11 = spaxis((np.linspace(-50, 50, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.Hz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-50, 50, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.Hz,
                 velocity_convention='radio')

cube11 = np.zeros([nspecpix,nspacepix,nspacepix])
cube22 = np.zeros([nspecpix,nspacepix,nspacepix])
for ii,jj in zip(range(nspacepix), range(nspacepix)):
    tkin=np.random.rand()*10+15
    ntot=14+np.random.randn()
    width=1.5+np.random.rand()
    xoff_v=np.random.randn()*5
    tex = tkin * 0.8
    spec11 = ammonia.cold_ammonia(xarr11,
                                  tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v,
                                  tex=tex
                                  )
    spec22 = ammonia.cold_ammonia(xarr22, tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v, tex=tex)
    cube11[:,ii,jj] = spec11
    cube22[:,ii,jj] = spec22
cube_oneone = pyspeckit.Cube(cube=cube11, xarr=xarr11)
cube_twotwo = pyspeckit.Cube(cube=cube11, xarr=xarr11)
stack = pyspeckit.CubeStack([cube_oneone,cube_twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-30,135]}
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[20,15,14.2,2.8,0,0.1],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,T,T,T,T],
            minpars=[2.73,2.73,10,1,0,0],
            use_nearest_as_guess=True, start_from_point=(5,5),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[20,15,14.2,2.8,0,0.1],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,T,T,T,T],
            minpars=[2.73,2.73,10,1,0,0],
            use_nearest_as_guess=True, start_from_point=(3,3),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[20,15,14.2,2.8,0,0.1],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T], signal_cut=2,
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,T,T,T,T],
            minpars=[2.73,2.73,10,1,0,0],
            start_from_point=(3,3),
            multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[20,15,14.2,2.8,0,0.1],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T],
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,T,T,T,T],
            minpars=[2.73,2.73,10,1,0,0],
            start_from_point=(3,3),
            multicore=1)
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis

nspecpix = 50
nspacepix = 5

xarr11 = spaxis((np.linspace(-50, 50, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.Hz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-50, 50, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.Hz,
                 velocity_convention='radio')

cube11 = np.zeros([nspecpix,nspacepix,nspacepix])
cube22 = np.zeros([nspecpix,nspacepix,nspacepix])
for ii,jj in zip(range(nspacepix), range(nspacepix)):
    tkin=np.random.rand()*10+15
    ntot=14+np.random.randn()
    width=1.5+np.random.rand()
    xoff_v=np.random.randn()*5
    tex = tkin * 0.8
    spec11 = ammonia.cold_ammonia(xarr11,
                                  tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v,
                                  tex=tex
                                  )
    spec22 = ammonia.cold_ammonia(xarr22, tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v, tex=tex)
    cube11[:,ii,jj] = spec11
    cube22[:,ii,jj] = spec22
noise11 = np.random.randn(cube11.shape)
noise22 = np.random.randn(cube22.shape)
cube_oneone = pyspeckit.Cube(cube=cube11+noise11, xarr=xarr11)
cube_twotwo = pyspeckit.Cube(cube=cube22+noise22, xarr=xarr22)
stack = pyspeckit.CubeStack([cube_oneone,cube_twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-30,135]}
import pyspeckit
from spectral_cube import SpectralCube
from astropy import units as u
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis

nspecpix = 50
nspacepix = 5

xarr11 = spaxis((np.linspace(-50, 50, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.Hz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-50, 50, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.Hz,
                 velocity_convention='radio')

cube11 = np.zeros([nspecpix,nspacepix,nspacepix])
cube22 = np.zeros([nspecpix,nspacepix,nspacepix])
for ii,jj in zip(range(nspacepix), range(nspacepix)):
    tkin=np.random.rand()*10+15
    ntot=14+np.random.randn()
    width=1.5+np.random.rand()
    xoff_v=np.random.randn()*5
    tex = tkin * 0.8
    spec11 = ammonia.cold_ammonia(xarr11,
                                  tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v,
                                  tex=tex
                                  )
    spec22 = ammonia.cold_ammonia(xarr22, tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v, tex=tex)
    cube11[:,ii,jj] = spec11
    cube22[:,ii,jj] = spec22
noise11 = np.random.randn(cube11.shape)
noise22 = np.random.randn(cube22.shape)
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis

nspecpix = 50
nspacepix = 5

xarr11 = spaxis((np.linspace(-50, 50, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.Hz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-50, 50, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.Hz,
                 velocity_convention='radio')

cube11 = np.zeros([nspecpix,nspacepix,nspacepix])
cube22 = np.zeros([nspecpix,nspacepix,nspacepix])
for ii,jj in zip(range(nspacepix), range(nspacepix)):
    tkin=np.random.rand()*10+15
    ntot=14+np.random.randn()
    width=1.5+np.random.rand()
    xoff_v=np.random.randn()*5
    tex = tkin * 0.8
    spec11 = ammonia.cold_ammonia(xarr11,
                                  tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v,
                                  tex=tex
                                  )
    spec22 = ammonia.cold_ammonia(xarr22, tkin=tkin, ntot=ntot, width=width, xoff_v=xoff_v, tex=tex)
    cube11[:,ii,jj] = spec11
    cube22[:,ii,jj] = spec22
noise11 = np.random.randn(*cube11.shape)
noise22 = np.random.randn(*cube22.shape)
cube_oneone = pyspeckit.Cube(cube=cube11+noise11, xarr=xarr11)
cube_twotwo = pyspeckit.Cube(cube=cube22+noise22, xarr=xarr22)
stack = pyspeckit.CubeStack([cube_oneone,cube_twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-30,135]}
F=False
T=True
stack.fiteach(fittype='cold_ammonia', multifit=None, guesses=[20,15,14.2,2.8,0,0.1],
            integral=False, verbose_level=3, fixed=[F,F,F,F,F,T],
            limitedmax=[F,F,F,F,T,T],
            maxpars=[0,0,0,0,130,1],
            limitedmin=[T,T,T,T,T,T],
            minpars=[2.73,2.73,10,1,0,0],
            start_from_point=(3,3),
            multicore=1)
stack.mapplot(estimator=4, vmin=20, vmax=35)
pl.figure(3)
stack.plot_spectrum(7,7)

pl.show()
stack.mapplot(estimator=4, vmin=20, vmax=35)
pl.figure(3)
stack.plot_spectrum(3,3)

pl.show()
stack.mapplot(estimator=4, vmin=-5, vmax=5)
pl.figure(3)
stack.plot_spectrum(3,3)

pl.show()
cube_oneone = pyspeckit.Cube(cube=cube11+noise11, xarr=xarr11)
cube_twotwo = pyspeckit.Cube(cube=cube22+noise22, xarr=xarr22)
stack = pyspeckit.CubeStack([cube_oneone,cube_twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-50,50]}
stack.mapplot(estimator=4, vmin=-5, vmax=5)
pl.figure(3)
stack.plot_spectrum(3,3)

pl.show()
stack.mapplot(estimator=4, vmin=-5, vmax=5)
pl.figure(3)
stack.plot_spectrum(3,3)

pl.show()
