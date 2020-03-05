'''_715.py

Wheel
'''


from mastapy.gears.manufacturing.bevel.cutters import _719
from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel.basic_machine_settings import _725, _726, _727
from mastapy._internal.cast_exception import CastException
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_WHEEL = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'Wheel')


__docformat__ = 'restructuredtext en'
__all__ = ('Wheel',)


class Wheel(_1.APIBase):
    '''Wheel

    This is a mastapy class.
    '''

    TYPE = _WHEEL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Wheel.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def wheel_finish_cutter(self) -> '_719.WheelFinishCutter':
        '''WheelFinishCutter: 'WheelFinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_719.WheelFinishCutter)(self.wrapped.WheelFinishCutter) if self.wrapped.WheelFinishCutter else None

    @property
    def basic_conical_gear_machine_settings(self) -> '_725.BasicConicalGearMachineSettings':
        '''BasicConicalGearMachineSettings: 'BasicConicalGearMachineSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_725.BasicConicalGearMachineSettings)(self.wrapped.BasicConicalGearMachineSettings) if self.wrapped.BasicConicalGearMachineSettings else None

    @property
    def basic_conical_gear_machine_settings_of_type_basic_conical_gear_machine_settings_formate(self) -> '_726.BasicConicalGearMachineSettingsFormate':
        '''BasicConicalGearMachineSettingsFormate: 'BasicConicalGearMachineSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _726.BasicConicalGearMachineSettingsFormate.TYPE not in self.wrapped.BasicConicalGearMachineSettings.__class__.__mro__:
            raise CastException('Failed to cast basic_conical_gear_machine_settings to BasicConicalGearMachineSettingsFormate. Expected: {}.'.format(self.wrapped.BasicConicalGearMachineSettings.__class__.__qualname__))

        return constructor.new(_726.BasicConicalGearMachineSettingsFormate)(self.wrapped.BasicConicalGearMachineSettings) if self.wrapped.BasicConicalGearMachineSettings else None

    @property
    def basic_conical_gear_machine_settings_of_type_basic_conical_gear_machine_settings_generated(self) -> '_727.BasicConicalGearMachineSettingsGenerated':
        '''BasicConicalGearMachineSettingsGenerated: 'BasicConicalGearMachineSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _727.BasicConicalGearMachineSettingsGenerated.TYPE not in self.wrapped.BasicConicalGearMachineSettings.__class__.__mro__:
            raise CastException('Failed to cast basic_conical_gear_machine_settings to BasicConicalGearMachineSettingsGenerated. Expected: {}.'.format(self.wrapped.BasicConicalGearMachineSettings.__class__.__qualname__))

        return constructor.new(_727.BasicConicalGearMachineSettingsGenerated)(self.wrapped.BasicConicalGearMachineSettings) if self.wrapped.BasicConicalGearMachineSettings else None
