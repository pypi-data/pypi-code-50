'''_416.py

StraightBevelGearMeshRating
'''


from typing import List

from mastapy.gears.gear_designs.straight_bevel import _443
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.straight_bevel import _417
from mastapy.gears.rating.bevel import _407
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.StraightBevel', 'StraightBevelGearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearMeshRating',)


class StraightBevelGearMeshRating(_407.BevelGearMeshRating):
    '''StraightBevelGearMeshRating

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_RATING
    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def straight_bevel_gear_mesh(self) -> '_443.StraightBevelGearMeshDesign':
        '''StraightBevelGearMeshDesign: 'StraightBevelGearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_443.StraightBevelGearMeshDesign)(self.wrapped.StraightBevelGearMesh) if self.wrapped.StraightBevelGearMesh else None

    @property
    def straight_bevel_gear_ratings(self) -> 'List[_417.StraightBevelGearRating]':
        '''List[StraightBevelGearRating]: 'StraightBevelGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearRatings, constructor.new(_417.StraightBevelGearRating))
        return value
