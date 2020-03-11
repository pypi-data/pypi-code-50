import pygrading.general_test as gg
from pygrading.html import *
import pygrading.docker as pk

web = pk.Network("net_create_test")

web.create()

web.remove()

vol = pk.Volume("test_volume")

vol.create()

print(vol.mount_point)

vol.remove()

