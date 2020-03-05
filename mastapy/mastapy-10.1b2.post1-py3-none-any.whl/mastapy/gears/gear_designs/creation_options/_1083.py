'''_1083.py

SpiralBevelGearSetCreationOptions
'''


from mastapy.gears.gear_designs.creation_options import _1081
from mastapy.gears.gear_designs.spiral_bevel import _378
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_CREATION_OPTIONS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.CreationOptions', 'SpiralBevelGearSetCreationOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetCreationOptions',)


class SpiralBevelGearSetCreationOptions(_1081.GearSetCreationOptions['_378.SpiralBevelGearSetDesign']):
    '''SpiralBevelGearSetCreationOptions

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_SET_CREATION_OPTIONS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetCreationOptions.TYPE'):
        super().__init__(instance_to_wrap)
