'''_377.py

ZerolBevelGearRating
'''


from mastapy.gears.gear_designs.zerol_bevel import _442
from mastapy._internal import constructor
from mastapy.gears.rating.bevel import _434
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.ZerolBevel', 'ZerolBevelGearRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearRating',)


class ZerolBevelGearRating(_434.BevelGearRating):
    '''ZerolBevelGearRating

    This is a mastapy class.
    '''

    TYPE = _ZEROL_BEVEL_GEAR_RATING
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearRating.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def zerol_bevel_gear(self) -> '_442.ZerolBevelGearDesign':
        '''ZerolBevelGearDesign: 'ZerolBevelGear' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_442.ZerolBevelGearDesign)(self.wrapped.ZerolBevelGear) if self.wrapped.ZerolBevelGear else None
