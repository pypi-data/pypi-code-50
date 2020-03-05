'''_169.py

MeshSingleFlankRating
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears import _122
from mastapy.materials.efficiency import _99
from mastapy.gears.rating import _167
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_MESH_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'MeshSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('MeshSingleFlankRating',)


class MeshSingleFlankRating(_1.APIBase):
    '''MeshSingleFlankRating

    This is a mastapy class.
    '''

    TYPE = _MESH_SINGLE_FLANK_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MeshSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def power(self) -> 'float':
        '''float: 'Power' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Power

    @property
    def rating_standard_name(self) -> 'str':
        '''str: 'RatingStandardName' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RatingStandardName

    @property
    def coefficient_of_friction_calculation_method(self) -> '_122.CoefficientOfFrictionCalculationMethod':
        '''CoefficientOfFrictionCalculationMethod: 'CoefficientOfFrictionCalculationMethod' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.CoefficientOfFrictionCalculationMethod)
        return constructor.new(_122.CoefficientOfFrictionCalculationMethod)(value) if value else None

    @coefficient_of_friction_calculation_method.setter
    def coefficient_of_friction_calculation_method(self, value: '_122.CoefficientOfFrictionCalculationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.CoefficientOfFrictionCalculationMethod = value

    @property
    def efficiency_rating_method(self) -> '_99.EfficiencyRatingMethod':
        '''EfficiencyRatingMethod: 'EfficiencyRatingMethod' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.EfficiencyRatingMethod)
        return constructor.new(_99.EfficiencyRatingMethod)(value) if value else None

    @efficiency_rating_method.setter
    def efficiency_rating_method(self, value: '_99.EfficiencyRatingMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.EfficiencyRatingMethod = value

    @property
    def name(self) -> 'str':
        '''str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Name

    @property
    def gear_single_flank_ratings(self) -> 'List[_167.GearSingleFlankRating]':
        '''List[GearSingleFlankRating]: 'GearSingleFlankRatings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearSingleFlankRatings, constructor.new(_167.GearSingleFlankRating))
        return value
