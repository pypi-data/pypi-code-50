'''_583.py

PinionConvex
'''


from mastapy.gears.manufacturing.bevel import (
    _584, _579, _580, _582,
    _585, _586, _587
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.bevel.basic_machine_settings import _601
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_PINION_CONVEX = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'PinionConvex')


__docformat__ = 'restructuredtext en'
__all__ = ('PinionConvex',)


class PinionConvex(_1.APIBase):
    '''PinionConvex

    This is a mastapy class.
    '''

    TYPE = _PINION_CONVEX

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PinionConvex.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def pinion_cutter_parameters_convex(self) -> '_584.PinionFinishMachineSettings':
        '''PinionFinishMachineSettings: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_584.PinionFinishMachineSettings)(self.wrapped.PinionCutterParametersConvex) if self.wrapped.PinionCutterParametersConvex else None

    @property
    def pinion_cutter_parameters_convex_of_type_pinion_bevel_generating_modified_roll_machine_settings(self) -> '_579.PinionBevelGeneratingModifiedRollMachineSettings':
        '''PinionBevelGeneratingModifiedRollMachineSettings: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _579.PinionBevelGeneratingModifiedRollMachineSettings.TYPE not in self.wrapped.PinionCutterParametersConvex.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_convex to PinionBevelGeneratingModifiedRollMachineSettings. Expected: {}.'.format(self.wrapped.PinionCutterParametersConvex.__class__.__qualname__))

        return constructor.new(_579.PinionBevelGeneratingModifiedRollMachineSettings)(self.wrapped.PinionCutterParametersConvex) if self.wrapped.PinionCutterParametersConvex else None

    @property
    def pinion_cutter_parameters_convex_of_type_pinion_bevel_generating_tilt_machine_settings(self) -> '_580.PinionBevelGeneratingTiltMachineSettings':
        '''PinionBevelGeneratingTiltMachineSettings: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _580.PinionBevelGeneratingTiltMachineSettings.TYPE not in self.wrapped.PinionCutterParametersConvex.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_convex to PinionBevelGeneratingTiltMachineSettings. Expected: {}.'.format(self.wrapped.PinionCutterParametersConvex.__class__.__qualname__))

        return constructor.new(_580.PinionBevelGeneratingTiltMachineSettings)(self.wrapped.PinionCutterParametersConvex) if self.wrapped.PinionCutterParametersConvex else None

    @property
    def pinion_cutter_parameters_convex_of_type_pinion_conical_machine_settings_specified(self) -> '_582.PinionConicalMachineSettingsSpecified':
        '''PinionConicalMachineSettingsSpecified: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _582.PinionConicalMachineSettingsSpecified.TYPE not in self.wrapped.PinionCutterParametersConvex.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_convex to PinionConicalMachineSettingsSpecified. Expected: {}.'.format(self.wrapped.PinionCutterParametersConvex.__class__.__qualname__))

        return constructor.new(_582.PinionConicalMachineSettingsSpecified)(self.wrapped.PinionCutterParametersConvex) if self.wrapped.PinionCutterParametersConvex else None

    @property
    def pinion_cutter_parameters_convex_of_type_pinion_hypoid_formate_tilt_machine_settings(self) -> '_585.PinionHypoidFormateTiltMachineSettings':
        '''PinionHypoidFormateTiltMachineSettings: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _585.PinionHypoidFormateTiltMachineSettings.TYPE not in self.wrapped.PinionCutterParametersConvex.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_convex to PinionHypoidFormateTiltMachineSettings. Expected: {}.'.format(self.wrapped.PinionCutterParametersConvex.__class__.__qualname__))

        return constructor.new(_585.PinionHypoidFormateTiltMachineSettings)(self.wrapped.PinionCutterParametersConvex) if self.wrapped.PinionCutterParametersConvex else None

    @property
    def pinion_cutter_parameters_convex_of_type_pinion_hypoid_generating_tilt_machine_settings(self) -> '_586.PinionHypoidGeneratingTiltMachineSettings':
        '''PinionHypoidGeneratingTiltMachineSettings: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _586.PinionHypoidGeneratingTiltMachineSettings.TYPE not in self.wrapped.PinionCutterParametersConvex.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_convex to PinionHypoidGeneratingTiltMachineSettings. Expected: {}.'.format(self.wrapped.PinionCutterParametersConvex.__class__.__qualname__))

        return constructor.new(_586.PinionHypoidGeneratingTiltMachineSettings)(self.wrapped.PinionCutterParametersConvex) if self.wrapped.PinionCutterParametersConvex else None

    @property
    def pinion_cutter_parameters_convex_of_type_pinion_machine_settings_smt(self) -> '_587.PinionMachineSettingsSMT':
        '''PinionMachineSettingsSMT: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _587.PinionMachineSettingsSMT.TYPE not in self.wrapped.PinionCutterParametersConvex.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_convex to PinionMachineSettingsSMT. Expected: {}.'.format(self.wrapped.PinionCutterParametersConvex.__class__.__qualname__))

        return constructor.new(_587.PinionMachineSettingsSMT)(self.wrapped.PinionCutterParametersConvex) if self.wrapped.PinionCutterParametersConvex else None

    @property
    def pinion_convex_ib_configuration(self) -> '_601.BasicConicalGearMachineSettingsGenerated':
        '''BasicConicalGearMachineSettingsGenerated: 'PinionConvexIBConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_601.BasicConicalGearMachineSettingsGenerated)(self.wrapped.PinionConvexIBConfiguration) if self.wrapped.PinionConvexIBConfiguration else None
