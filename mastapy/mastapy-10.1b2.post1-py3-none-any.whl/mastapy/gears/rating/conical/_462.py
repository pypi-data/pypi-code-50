'''_462.py

ConicalGearRating
'''


from mastapy.gears.rating import _338, _340
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Conical', 'ConicalGearRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearRating',)


class ConicalGearRating(_340.GearRating):
    '''ConicalGearRating

    This is a mastapy class.
    '''

    TYPE = _CONICAL_GEAR_RATING
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalGearRating.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def concave_flank_rating(self) -> '_338.GearFlankRating':
        '''GearFlankRating: 'ConcaveFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_338.GearFlankRating)(self.wrapped.ConcaveFlankRating) if self.wrapped.ConcaveFlankRating else None

    @property
    def convex_flank_rating(self) -> '_338.GearFlankRating':
        '''GearFlankRating: 'ConvexFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_338.GearFlankRating)(self.wrapped.ConvexFlankRating) if self.wrapped.ConvexFlankRating else None
