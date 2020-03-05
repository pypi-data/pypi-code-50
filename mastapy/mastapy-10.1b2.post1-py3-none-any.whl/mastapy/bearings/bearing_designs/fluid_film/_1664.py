'''_1664.py

PlainGreaseFilledJournalBearing
'''


from mastapy.bearings.bearing_designs.fluid_film import (
    _1720, _1722, _1716, _1717,
    _1719, _1721
)
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLAIN_GREASE_FILLED_JOURNAL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm', 'PlainGreaseFilledJournalBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('PlainGreaseFilledJournalBearing',)


class PlainGreaseFilledJournalBearing(_1721.PlainJournalBearing):
    '''PlainGreaseFilledJournalBearing

    This is a mastapy class.
    '''

    TYPE = _PLAIN_GREASE_FILLED_JOURNAL_BEARING
    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlainGreaseFilledJournalBearing.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def housing_type(self) -> '_1720.PlainGreaseFilledJournalBearingHousingType':
        '''PlainGreaseFilledJournalBearingHousingType: 'HousingType' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.HousingType)
        return constructor.new(_1720.PlainGreaseFilledJournalBearingHousingType)(value) if value else None

    @housing_type.setter
    def housing_type(self, value: '_1720.PlainGreaseFilledJournalBearingHousingType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.HousingType = value

    @property
    def housing_detail(self) -> '_1722.PlainJournalHousing':
        '''PlainJournalHousing: 'HousingDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1722.PlainJournalHousing)(self.wrapped.HousingDetail) if self.wrapped.HousingDetail else None

    @property
    def housing_detail_of_type_cylindrical_housing_journal_bearing(self) -> '_1716.CylindricalHousingJournalBearing':
        '''CylindricalHousingJournalBearing: 'HousingDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HousingDetail.__class__.__qualname__ != 'CylindricalHousingJournalBearing':
            raise CastException('Failed to cast housing_detail to CylindricalHousingJournalBearing. Expected: {}.'.format(self.wrapped.HousingDetail.__class__.__qualname__))

        return constructor.new(_1716.CylindricalHousingJournalBearing)(self.wrapped.HousingDetail) if self.wrapped.HousingDetail else None

    @property
    def housing_detail_of_type_machinery_encased_journal_bearing(self) -> '_1717.MachineryEncasedJournalBearing':
        '''MachineryEncasedJournalBearing: 'HousingDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HousingDetail.__class__.__qualname__ != 'MachineryEncasedJournalBearing':
            raise CastException('Failed to cast housing_detail to MachineryEncasedJournalBearing. Expected: {}.'.format(self.wrapped.HousingDetail.__class__.__qualname__))

        return constructor.new(_1717.MachineryEncasedJournalBearing)(self.wrapped.HousingDetail) if self.wrapped.HousingDetail else None

    @property
    def housing_detail_of_type_pedestal_journal_bearing(self) -> '_1719.PedestalJournalBearing':
        '''PedestalJournalBearing: 'HousingDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HousingDetail.__class__.__qualname__ != 'PedestalJournalBearing':
            raise CastException('Failed to cast housing_detail to PedestalJournalBearing. Expected: {}.'.format(self.wrapped.HousingDetail.__class__.__qualname__))

        return constructor.new(_1719.PedestalJournalBearing)(self.wrapped.HousingDetail) if self.wrapped.HousingDetail else None
