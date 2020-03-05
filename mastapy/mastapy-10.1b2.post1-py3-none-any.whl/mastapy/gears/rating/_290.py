'''_290.py

GearRating
'''


from mastapy.gears.rating import _285, _283
from mastapy._internal import constructor
from mastapy.materials import _227
from mastapy._internal.python_net import python_net_import

_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'GearRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GearRating',)


class GearRating(_283.AbstractGearRating):
    '''GearRating

    This is a mastapy class.
    '''

    TYPE = _GEAR_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearRating.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def static_safety_factor(self) -> '_285.BendingAndContactReportingObject':
        '''BendingAndContactReportingObject: 'StaticSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_285.BendingAndContactReportingObject)(self.wrapped.StaticSafetyFactor) if self.wrapped.StaticSafetyFactor else None

    @property
    def bending_safety_factor_results(self) -> '_227.SafetyFactorItem':
        '''SafetyFactorItem: 'BendingSafetyFactorResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_227.SafetyFactorItem)(self.wrapped.BendingSafetyFactorResults) if self.wrapped.BendingSafetyFactorResults else None

    @property
    def contact_safety_factor_results(self) -> '_227.SafetyFactorItem':
        '''SafetyFactorItem: 'ContactSafetyFactorResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_227.SafetyFactorItem)(self.wrapped.ContactSafetyFactorResults) if self.wrapped.ContactSafetyFactorResults else None
