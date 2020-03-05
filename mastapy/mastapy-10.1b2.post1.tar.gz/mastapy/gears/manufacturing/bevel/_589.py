'''_589.py

Wheel
'''


from mastapy.gears.manufacturing.bevel.cutters import _593
from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel.basic_machine_settings import _599, _600, _601
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
    def wheel_finish_cutter(self) -> '_593.WheelFinishCutter':
        '''WheelFinishCutter: 'WheelFinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_593.WheelFinishCutter)(self.wrapped.WheelFinishCutter) if self.wrapped.WheelFinishCutter else None

    @property
    def basic_conical_gear_machine_settings(self) -> '_599.BasicConicalGearMachineSettings':
        '''BasicConicalGearMachineSettings: 'BasicConicalGearMachineSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_599.BasicConicalGearMachineSettings)(self.wrapped.BasicConicalGearMachineSettings) if self.wrapped.BasicConicalGearMachineSettings else None

    @property
    def basic_conical_gear_machine_settings_of_type_basic_conical_gear_machine_settings_formate(self) -> '_600.BasicConicalGearMachineSettingsFormate':
        '''BasicConicalGearMachineSettingsFormate: 'BasicConicalGearMachineSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _600.BasicConicalGearMachineSettingsFormate.TYPE not in self.wrapped.BasicConicalGearMachineSettings.__class__.__mro__:
            raise CastException('Failed to cast basic_conical_gear_machine_settings to BasicConicalGearMachineSettingsFormate. Expected: {}.'.format(self.wrapped.BasicConicalGearMachineSettings.__class__.__qualname__))

        return constructor.new(_600.BasicConicalGearMachineSettingsFormate)(self.wrapped.BasicConicalGearMachineSettings) if self.wrapped.BasicConicalGearMachineSettings else None

    @property
    def basic_conical_gear_machine_settings_of_type_basic_conical_gear_machine_settings_generated(self) -> '_601.BasicConicalGearMachineSettingsGenerated':
        '''BasicConicalGearMachineSettingsGenerated: 'BasicConicalGearMachineSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _601.BasicConicalGearMachineSettingsGenerated.TYPE not in self.wrapped.BasicConicalGearMachineSettings.__class__.__mro__:
            raise CastException('Failed to cast basic_conical_gear_machine_settings to BasicConicalGearMachineSettingsGenerated. Expected: {}.'.format(self.wrapped.BasicConicalGearMachineSettings.__class__.__qualname__))

        return constructor.new(_601.BasicConicalGearMachineSettingsGenerated)(self.wrapped.BasicConicalGearMachineSettings) if self.wrapped.BasicConicalGearMachineSettings else None
