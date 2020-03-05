'''_2020.py

WormGear
'''


from mastapy.gears.gear_designs.worm import _459
from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _1999
from mastapy._internal.python_net import python_net_import

_WORM_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'WormGear')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGear',)


class WormGear(_1999.Gear):
    '''WormGear

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR
    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGear.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def worm_gear_design(self) -> '_459.WormGearDesign':
        '''WormGearDesign: 'WormGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_459.WormGearDesign)(self.wrapped.WormGearDesign) if self.wrapped.WormGearDesign else None
