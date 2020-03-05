'''_378.py

ZerolBevelGearSetRating
'''


from typing import List

from mastapy.gears.gear_designs.zerol_bevel import _355
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.zerol_bevel import _376, _377
from mastapy.gears.rating.bevel import _399
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.ZerolBevel', 'ZerolBevelGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetRating',)


class ZerolBevelGearSetRating(_399.BevelGearSetRating):
    '''ZerolBevelGearSetRating

    This is a mastapy class.
    '''

    TYPE = _ZEROL_BEVEL_GEAR_SET_RATING
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def zerol_bevel_gear_set(self) -> '_355.ZerolBevelGearSetDesign':
        '''ZerolBevelGearSetDesign: 'ZerolBevelGearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_355.ZerolBevelGearSetDesign)(self.wrapped.ZerolBevelGearSet) if self.wrapped.ZerolBevelGearSet else None

    @property
    def zerol_bevel_mesh_ratings(self) -> 'List[_376.ZerolBevelGearMeshRating]':
        '''List[ZerolBevelGearMeshRating]: 'ZerolBevelMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelMeshRatings, constructor.new(_376.ZerolBevelGearMeshRating))
        return value

    @property
    def zerol_bevel_gear_ratings(self) -> 'List[_377.ZerolBevelGearRating]':
        '''List[ZerolBevelGearRating]: 'ZerolBevelGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearRatings, constructor.new(_377.ZerolBevelGearRating))
        return value
