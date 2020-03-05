'''_88.py

SoundPressureEnclosure
'''


from mastapy.materials import _89
from mastapy._internal import constructor, conversion
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_SOUND_PRESSURE_ENCLOSURE = python_net_import('SMT.MastaAPI.Materials', 'SoundPressureEnclosure')


__docformat__ = 'restructuredtext en'
__all__ = ('SoundPressureEnclosure',)


class SoundPressureEnclosure(_1.APIBase):
    '''SoundPressureEnclosure

    This is a mastapy class.
    '''

    TYPE = _SOUND_PRESSURE_ENCLOSURE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SoundPressureEnclosure.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def enclosure_type(self) -> '_89.SoundPressureEnclosureType':
        '''SoundPressureEnclosureType: 'EnclosureType' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.EnclosureType)
        return constructor.new(_89.SoundPressureEnclosureType)(value) if value else None

    @enclosure_type.setter
    def enclosure_type(self, value: '_89.SoundPressureEnclosureType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.EnclosureType = value

    @property
    def surface_area(self) -> 'float':
        '''float: 'SurfaceArea' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SurfaceArea

    @property
    def measurement_radius(self) -> 'float':
        '''float: 'MeasurementRadius' is the original name of this property.'''

        return self.wrapped.MeasurementRadius

    @measurement_radius.setter
    def measurement_radius(self, value: 'float'):
        self.wrapped.MeasurementRadius = float(value) if value else 0.0
