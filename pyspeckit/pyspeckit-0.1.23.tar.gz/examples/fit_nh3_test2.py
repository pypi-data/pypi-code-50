import pyspeckit

twotwo = pyspeckit.Cube('gcnh3_11.fits')
oneone = pyspeckit.Cube('gcnh3_22.fits')
oneone.xarr.velocity_convention = 'radio'
twotwo.xarr.velocity_convention = 'radio'
stack = pyspeckit.CubeStack([oneone,twotwo])

stack.plot_special = pyspeckit.wrappers.fitnh3.plotter_override
stack.plot_special_kwargs = {'fignum':3, 'vrange':[-30,135]}
