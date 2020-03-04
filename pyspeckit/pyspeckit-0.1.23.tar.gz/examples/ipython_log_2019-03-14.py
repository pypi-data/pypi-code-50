########################################################
# Started Logging At: 2019-03-14 08:43:20
########################################################
########################################################
# # Started Logging At: 2019-03-14 08:43:20
########################################################
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
noise11 = np.random.randn(*cube11.shape)
noise22 = np.random.randn(*cube22.shape)
cube_oneone = pyspeckit.Cube(cube=cube11+noise11, xarr=xarr11)
cube_twotwo = pyspeckit.Cube(cube=cube22+noise22, xarr=xarr22)
stack = pyspeckit.CubeStack([cube_oneone,cube_twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-50,50]}
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,130,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,0,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,130,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,0,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,130,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,0,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,130,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,0,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,130,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,0,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,130,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,0,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,130,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,0,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,130,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,0,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,130,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,0,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,130,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,0,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,130,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,0,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,130,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,0,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,130,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,0,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,130,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,0,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,130,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,0,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,130,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,0,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,130,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,0,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,-25,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,-25,0],
              start_from_point=(3,3),
              multicore=1)
stack.mapplot(estimator=4, vmin=-5, vmax=5)
pl.figure(3)
stack.plot_spectrum(3,3)

pl.show()
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,-25,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,-25,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,-25,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,-25,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,-25,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,-25,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,-25,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,-25,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,-25,0],
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
noise11 = np.random.randn(*cube11.shape)
noise22 = np.random.randn(*cube22.shape)
cube_oneone = pyspeckit.Cube(cube=cube11+noise11, xarr=xarr11)
cube_twotwo = pyspeckit.Cube(cube=cube22+noise22, xarr=xarr22)
stack = pyspeckit.CubeStack([cube_oneone,cube_twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-50,50]}
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,-25,0],
              start_from_point=(3,3),
              multicore=1)
print(xarr11)
print(xarr11.to(u.km/u.s))
spec11
#[Out]# array([0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#        0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#        2.61811822e-13, 1.86728114e-10, 5.51169105e-08, 6.73793519e-06,
#[Out]#        3.41142988e-04, 7.15156030e-03, 6.19593663e-02, 2.21269114e-01,
#[Out]#        3.28068488e-01, 2.03663046e-01, 5.32234112e-02, 1.96365983e-02,
#[Out]#        1.02798076e-01, 3.11392313e-01, 4.04845334e-01, 3.09448272e-01,
#[Out]#        5.85282562e-01, 1.26126822e+00, 1.27021626e+00, 5.95330287e-01,
#[Out]#        3.08037931e-01, 4.04925031e-01, 3.16611437e-01, 1.05810595e-01,
#[Out]#        2.01898401e-02, 5.27953832e-02, 2.01104381e-01, 3.25845472e-01,
#[Out]#        2.23410839e-01, 6.43502362e-02, 7.73439728e-03, 3.88956425e-04,
#[Out]#        8.19876631e-06, 7.24253676e-08, 2.67917040e-10, 4.14739852e-13,
#[Out]#        0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#        0.00000000e+00, 0.00000000e+00])
spec22
#[Out]# array([0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#[Out]#        0.00000000e+00, 8.68622023e-14, 4.96815114e-11, 1.19314554e-08,
#[Out]#        1.19664978e-06, 5.00619829e-05, 8.72612866e-04, 6.32978480e-03,
#[Out]#        1.90880780e-02, 2.39307574e-02, 1.25823478e-02, 4.34982026e-03,
#[Out]#        9.81393661e-03, 2.29280115e-02, 2.27527678e-02, 9.36826960e-03,
#[Out]#        1.59970680e-03, 1.65630142e-04, 1.76737601e-03, 2.46844491e-02,
#[Out]#        1.43093706e-01, 3.43664743e-01, 3.46351803e-01, 1.46504619e-01,
#[Out]#        2.56760528e-02, 1.86681407e-03, 1.61455806e-04, 1.51840442e-03,
#[Out]#        9.07915396e-03, 2.25113091e-02, 2.31532583e-02, 1.00937152e-02,
#[Out]#        4.33567204e-03, 1.23355091e-02, 2.38326089e-02, 1.93211575e-02,
#[Out]#        6.51015777e-03, 9.11630969e-04, 5.31078864e-05, 1.28863808e-06,
#[Out]#        1.30385649e-08, 5.50756156e-11, 9.66496468e-14, 0.00000000e+00,
#[Out]#        0.00000000e+00, 0.00000000e+00])
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
    ntot=14.5+np.random.randn()
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
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-50,50]}
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,-25,0],
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
    ntot=14.5+np.random.randn()
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
noise11 = np.random.randn(*cube11.shape)/10.
noise22 = np.random.randn(*cube22.shape)/10.
cube_oneone = pyspeckit.Cube(cube=cube11+noise11, xarr=xarr11)
cube_twotwo = pyspeckit.Cube(cube=cube22+noise22, xarr=xarr22)
stack = pyspeckit.CubeStack([cube_oneone,cube_twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-50,50]}
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[20,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,-25,0],
              start_from_point=(3,3),
              multicore=1)
stack.mapplot(estimator=4, vmin=-5, vmax=5)
pl.figure(3)
stack.plot_spectrum(3,3)

pl.show()
sp = stack.get_spectrum(3,3)
sp.plotter()
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
    tkin=np.random.rand()*10+20
    ntot=14.5+np.random.randn()
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
    print(spec11.max(), spec22.max())
noise11 = np.random.randn(*cube11.shape)/10.
noise22 = np.random.randn(*cube22.shape)/10.
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
    tkin=np.random.rand()*10+20
    ntot=15.5+np.random.randn()
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
    print(spec11.max(), spec22.max())
noise11 = np.random.randn(*cube11.shape)/10.
noise22 = np.random.randn(*cube22.shape)/10.
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
    tkin=np.random.rand()*10+20
    ntot=15.5+np.random.randn()
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
    #print(spec11.max(), spec22.max())
noise11 = np.random.randn(*cube11.shape)/10.
noise22 = np.random.randn(*cube22.shape)/10.
cube_oneone = pyspeckit.Cube(cube=cube11+noise11, xarr=xarr11)
cube_twotwo = pyspeckit.Cube(cube=cube22+noise22, xarr=xarr22)
stack = pyspeckit.CubeStack([cube_oneone,cube_twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-50,50]}
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[25,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[2.73,2.73,10,1,-25,0],
              start_from_point=(3,3),
              multicore=1)
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[25,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[4,3,10,1,-25,0],
              start_from_point=(3,3),
              multicore=1)
stack.mapplot(estimator=4, vmin=-5, vmax=5)
pl.figure(3)
stack.plot_spectrum(3,3)

pl.show()
pl.close(5)
stack.mapplot(estimator=4, vmin=-5, vmax=5)
pl.figure(3)
stack.plot_spectrum(3,3)

pl.show()
sp = stack.get_spectrum(3,3)
sp.plotter()
stack.plot_spectrum(3,3)
pl.close('all')
stack.mapplot(estimator=4, vmin=-5, vmax=5)
pl.figure(3)
stack.plot_spectrum(3,3)

pl.show()
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis

nspecpix = 50
nspacepix = 5

xarr11 = spaxis((np.linspace(-25, 25, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.Hz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-25, 25, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.Hz,
                 velocity_convention='radio')

cube11 = np.zeros([nspecpix,nspacepix,nspacepix])
cube22 = np.zeros([nspecpix,nspacepix,nspacepix])
for ii,jj in zip(range(nspacepix), range(nspacepix)):
    tkin=np.random.rand()*10+20
    ntot=14.1+np.random.randn()
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
    #print(spec11.max(), spec22.max())
noise11 = np.random.randn(*cube11.shape)/10.
noise22 = np.random.randn(*cube22.shape)/10.
cube_oneone = pyspeckit.Cube(cube=cube11+noise11, xarr=xarr11)
cube_twotwo = pyspeckit.Cube(cube=cube22+noise22, xarr=xarr22)
stack = pyspeckit.CubeStack([cube_oneone,cube_twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-50,50]}
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[25,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[4,3,10,1,-25,0],
              start_from_point=(3,3),
              multicore=1)
pl.close('all')
stack.mapplot(estimator=4, vmin=-5, vmax=5)
pl.figure(3)
stack.plot_spectrum(3,3)

pl.show()
stack.plot_spectrum(3,3)
pl.close('all')
stack.plot_spectrum(3,3)
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis

nspecpix = 50
nspacepix = 5

xarr11 = spaxis((np.linspace(-25, 25, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.Hz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-25, 25, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.Hz,
                 velocity_convention='radio')

cube11 = np.zeros([nspecpix,nspacepix,nspacepix])
cube22 = np.zeros([nspecpix,nspacepix,nspacepix])
for ii,jj in zip(range(nspacepix), range(nspacepix)):
    tkin=np.random.rand()*10+20
    ntot=14.1+np.random.randn()
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
    print(spec11.max(), spec22.max())
noise11 = np.random.randn(*cube11.shape)/10.
noise22 = np.random.randn(*cube22.shape)/10.
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis

nspecpix = 50
nspacepix = 5

xarr11 = spaxis((np.linspace(-25, 25, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.Hz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-25, 25, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.Hz,
                 velocity_convention='radio')

cube11 = np.zeros([nspecpix,nspacepix,nspacepix])
cube22 = np.zeros([nspecpix,nspacepix,nspacepix])
for ii,jj in zip(range(nspacepix), range(nspacepix)):
    tkin=np.random.rand()*10+20
    ntot=14.1+np.random.randn()/10
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
    print(spec11.max(), spec22.max())
noise11 = np.random.randn(*cube11.shape)/10.
noise22 = np.random.randn(*cube22.shape)/10.
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis

nspecpix = 50
nspacepix = 5

xarr11 = spaxis((np.linspace(-25, 25, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.Hz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-25, 25, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.Hz,
                 velocity_convention='radio')

cube11 = np.zeros([nspecpix,nspacepix,nspacepix])
cube22 = np.zeros([nspecpix,nspacepix,nspacepix])
for ii,jj in zip(range(nspacepix), range(nspacepix)):
    tkin=np.random.rand()*10+20
    ntot=14.3+np.random.randn()/10
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
    print(spec11.max(), spec22.max())
noise11 = np.random.randn(*cube11.shape)/10.
noise22 = np.random.randn(*cube22.shape)/10.
cube_oneone = pyspeckit.Cube(cube=cube11+noise11, xarr=xarr11)
cube_twotwo = pyspeckit.Cube(cube=cube22+noise22, xarr=xarr22)
stack = pyspeckit.CubeStack([cube_oneone,cube_twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-50,50]}
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[25,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[4,3,10,1,-25,0],
              start_from_point=(3,3),
              multicore=1)
pl.close('all')
stack.mapplot(estimator=4, vmin=-5, vmax=5)
pl.figure(3)
stack.plot_spectrum(3,3)

pl.show()
import itertools
itertools.product(range(3),range(3))
#[Out]# <itertools.product at 0x1a28493798>
import itertools
list(itertools.product(range(3),range(3)))
#[Out]# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis
import itertools

nspecpix = 50
nspacepix = 5

xarr11 = spaxis((np.linspace(-25, 25, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.Hz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-25, 25, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.Hz,
                 velocity_convention='radio')

cube11 = np.zeros([nspecpix,nspacepix,nspacepix])
cube22 = np.zeros([nspecpix,nspacepix,nspacepix])
for ii,jj in itertools.product(range(nspacepix), range(nspacepix)):
    tkin=np.random.rand()*10+20
    ntot=14.3+np.random.randn()/10
    while ntot < 14.2:
        ntot += 0.1
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
    print(spec11.max(), spec22.max())
noise11 = np.random.randn(*cube11.shape)/10.
noise22 = np.random.randn(*cube22.shape)/10.
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis
import itertools

nspecpix = 50
nspacepix = 5

xarr11 = spaxis((np.linspace(-25, 25, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.Hz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-25, 25, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.Hz,
                 velocity_convention='radio')

cube11 = np.zeros([nspecpix,nspacepix,nspacepix])
cube22 = np.zeros([nspecpix,nspacepix,nspacepix])
for ii,jj in itertools.product(range(nspacepix), range(nspacepix)):
    tkin=np.random.rand()*10+20
    ntot=14.4+np.random.randn()/10
    while ntot < 14.2:
        ntot += 0.1
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
    print(spec11.max(), spec22.max())
noise11 = np.random.randn(*cube11.shape)/10.
noise22 = np.random.randn(*cube22.shape)/10.
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis
import itertools

nspecpix = 50
nspacepix = 5

xarr11 = spaxis((np.linspace(-25, 25, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.Hz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-25, 25, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.Hz,
                 velocity_convention='radio')

cube11 = np.zeros([nspecpix,nspacepix,nspacepix])
cube22 = np.zeros([nspecpix,nspacepix,nspacepix])
for ii,jj in itertools.product(range(nspacepix), range(nspacepix)):
    tkin=np.random.rand()*10+20
    ntot=14.5+np.random.randn()/10
    while ntot < 14.2:
        ntot += 0.1
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
    print(spec11.max(), spec22.max())
noise11 = np.random.randn(*cube11.shape)/10.
noise22 = np.random.randn(*cube22.shape)/10.
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis
import itertools

nspecpix = 50
nspacepix = 5

xarr11 = spaxis((np.linspace(-25, 25, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.Hz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-25, 25, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.Hz,
                 velocity_convention='radio')

cube11 = np.zeros([nspecpix,nspacepix,nspacepix])
cube22 = np.zeros([nspecpix,nspacepix,nspacepix])
for ii,jj in itertools.product(range(nspacepix), range(nspacepix)):
    tkin=np.random.rand()*10+20
    ntot=14.5+np.random.randn()/10
    while ntot < 14.2:
        ntot += 0.1
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
    #print(spec11.max(), spec22.max())
noise11 = np.random.randn(*cube11.shape)/10.
noise22 = np.random.randn(*cube22.shape)/10.
cube_oneone = pyspeckit.Cube(cube=cube11+noise11, xarr=xarr11)
cube_twotwo = pyspeckit.Cube(cube=cube22+noise22, xarr=xarr22)
stack = pyspeckit.CubeStack([cube_oneone,cube_twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-50,50]}
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[25,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[4,3,10,1,-25,0],
              start_from_point=(3,3),
              multicore=1)
pl.close('all')
stack.mapplot(estimator=4, vmin=-5, vmax=5)
pl.figure(3)
stack.plot_spectrum(3,3)

pl.show()
########################################################
# Started Logging At: 2019-03-14 10:23:11
########################################################
########################################################
# # Started Logging At: 2019-03-14 10:23:11
########################################################
get_ipython().magic('matplotlib notebook')
import pylab as pl
import pyspeckit
from spectral_cube import SpectralCube
from astropy import units as u
import pyspeckit.spectrum.models.ammonia as ammonia
import pyspeckit.spectrum.models.ammonia_constants as nh3con
from pyspeckit.spectrum.units import SpectroscopicAxis as spaxis
import itertools

nspecpix = 50
nspacepix = 5

xarr11 = spaxis((np.linspace(-25, 25, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['oneone']*u.Hz,
                 velocity_convention='radio')
xarr22 = spaxis((np.linspace(-25, 25, nspecpix)*u.km/u.s),
                 refX=nh3con.freq_dict['twotwo']*u.Hz,
                 velocity_convention='radio')

cube11 = np.zeros([nspecpix,nspacepix,nspacepix])
cube22 = np.zeros([nspecpix,nspacepix,nspacepix])
for ii,jj in itertools.product(range(nspacepix), range(nspacepix)):
    tkin=np.random.rand()*10+20
    ntot=14.5+np.random.randn()/10
    while ntot < 14.2:
        ntot += 0.1
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
    #print(spec11.max(), spec22.max())
noise11 = np.random.randn(*cube11.shape)/10.
noise22 = np.random.randn(*cube22.shape)/10.
cube_oneone = pyspeckit.Cube(cube=cube11+noise11, xarr=xarr11)
cube_twotwo = pyspeckit.Cube(cube=cube22+noise22, xarr=xarr22)
stack = pyspeckit.CubeStack([cube_oneone,cube_twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-50,50]}
F=False
T=True
stack.fiteach(fittype='cold_ammonia',
              guesses=[25,15,14.2,2.8,0,0.1],
              integral=False,
              verbose_level=0,
              fixed=[F,F,F,F,F,T],
              limitedmax=[F,F,F,F,T,T],
              maxpars=[0,0,0,0,25,1],
              limitedmin=[T,T,T,T,T,T],
              minpars=[4,3,10,1,-25,0],
              start_from_point=(3,3),
              multicore=1)
pl.close('all')
stack.mapplot(estimator=4, vmin=-5, vmax=5)
pl.figure(3)
stack.plot_spectrum(3,3)

pl.show()
