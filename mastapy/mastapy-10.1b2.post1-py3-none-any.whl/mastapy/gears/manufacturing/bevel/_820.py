'''_820.py

ConicalPinionManufacturingConfig
'''


from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel import (
    _817, _813, _838, _833,
    _834, _836, _839, _840,
    _841, _842, _808
)
from mastapy.gears.manufacturing.bevel.cutters import _845, _846
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_CONICAL_PINION_MANUFACTURING_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalPinionManufacturingConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalPinionManufacturingConfig',)


class ConicalPinionManufacturingConfig(_808.ConicalGearManufacturingConfig):
    '''ConicalPinionManufacturingConfig

    This is a mastapy class.
    '''

    TYPE = _CONICAL_PINION_MANUFACTURING_CONFIG
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalPinionManufacturingConfig.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def pinion_finish_manufacturing_machine(self) -> 'str':
        '''str: 'PinionFinishManufacturingMachine' is the original name of this property.'''

        return self.wrapped.PinionFinishManufacturingMachine.SelectedItemName

    @pinion_finish_manufacturing_machine.setter
    def pinion_finish_manufacturing_machine(self, value: 'str'):
        self.wrapped.PinionFinishManufacturingMachine.SetSelectedItem(str(value) if value else None)

    @property
    def pinion_rough_manufacturing_machine(self) -> 'str':
        '''str: 'PinionRoughManufacturingMachine' is the original name of this property.'''

        return self.wrapped.PinionRoughManufacturingMachine.SelectedItemName

    @pinion_rough_manufacturing_machine.setter
    def pinion_rough_manufacturing_machine(self, value: 'str'):
        self.wrapped.PinionRoughManufacturingMachine.SetSelectedItem(str(value) if value else None)

    @property
    def mesh_config(self) -> '_817.ConicalMeshManufacturingConfig':
        '''ConicalMeshManufacturingConfig: 'MeshConfig' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_817.ConicalMeshManufacturingConfig)(self.wrapped.MeshConfig) if self.wrapped.MeshConfig else None

    @property
    def pinion_concave_ob_configuration(self) -> '_813.ConicalMeshFlankManufacturingConfig':
        '''ConicalMeshFlankManufacturingConfig: 'PinionConcaveOBConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_813.ConicalMeshFlankManufacturingConfig)(self.wrapped.PinionConcaveOBConfiguration) if self.wrapped.PinionConcaveOBConfiguration else None

    @property
    def pinion_convex_ib_configuration(self) -> '_813.ConicalMeshFlankManufacturingConfig':
        '''ConicalMeshFlankManufacturingConfig: 'PinionConvexIBConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_813.ConicalMeshFlankManufacturingConfig)(self.wrapped.PinionConvexIBConfiguration) if self.wrapped.PinionConvexIBConfiguration else None

    @property
    def pinion_finish_cutter(self) -> '_845.PinionFinishCutter':
        '''PinionFinishCutter: 'PinionFinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_845.PinionFinishCutter)(self.wrapped.PinionFinishCutter) if self.wrapped.PinionFinishCutter else None

    @property
    def pinion_rough_cutter(self) -> '_846.PinionRoughCutter':
        '''PinionRoughCutter: 'PinionRoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_846.PinionRoughCutter)(self.wrapped.PinionRoughCutter) if self.wrapped.PinionRoughCutter else None

    @property
    def pinion_cutter_parameters_concave(self) -> '_838.PinionFinishMachineSettings':
        '''PinionFinishMachineSettings: 'PinionCutterParametersConcave' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_838.PinionFinishMachineSettings)(self.wrapped.PinionCutterParametersConcave) if self.wrapped.PinionCutterParametersConcave else None

    @property
    def pinion_cutter_parameters_concave_of_type_pinion_bevel_generating_modified_roll_machine_settings(self) -> '_833.PinionBevelGeneratingModifiedRollMachineSettings':
        '''PinionBevelGeneratingModifiedRollMachineSettings: 'PinionCutterParametersConcave' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _833.PinionBevelGeneratingModifiedRollMachineSettings.TYPE not in self.wrapped.PinionCutterParametersConcave.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_concave to PinionBevelGeneratingModifiedRollMachineSettings. Expected: {}.'.format(self.wrapped.PinionCutterParametersConcave.__class__.__qualname__))

        return constructor.new(_833.PinionBevelGeneratingModifiedRollMachineSettings)(self.wrapped.PinionCutterParametersConcave) if self.wrapped.PinionCutterParametersConcave else None

    @property
    def pinion_cutter_parameters_concave_of_type_pinion_bevel_generating_tilt_machine_settings(self) -> '_834.PinionBevelGeneratingTiltMachineSettings':
        '''PinionBevelGeneratingTiltMachineSettings: 'PinionCutterParametersConcave' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _834.PinionBevelGeneratingTiltMachineSettings.TYPE not in self.wrapped.PinionCutterParametersConcave.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_concave to PinionBevelGeneratingTiltMachineSettings. Expected: {}.'.format(self.wrapped.PinionCutterParametersConcave.__class__.__qualname__))

        return constructor.new(_834.PinionBevelGeneratingTiltMachineSettings)(self.wrapped.PinionCutterParametersConcave) if self.wrapped.PinionCutterParametersConcave else None

    @property
    def pinion_cutter_parameters_concave_of_type_pinion_conical_machine_settings_specified(self) -> '_836.PinionConicalMachineSettingsSpecified':
        '''PinionConicalMachineSettingsSpecified: 'PinionCutterParametersConcave' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _836.PinionConicalMachineSettingsSpecified.TYPE not in self.wrapped.PinionCutterParametersConcave.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_concave to PinionConicalMachineSettingsSpecified. Expected: {}.'.format(self.wrapped.PinionCutterParametersConcave.__class__.__qualname__))

        return constructor.new(_836.PinionConicalMachineSettingsSpecified)(self.wrapped.PinionCutterParametersConcave) if self.wrapped.PinionCutterParametersConcave else None

    @property
    def pinion_cutter_parameters_concave_of_type_pinion_hypoid_formate_tilt_machine_settings(self) -> '_839.PinionHypoidFormateTiltMachineSettings':
        '''PinionHypoidFormateTiltMachineSettings: 'PinionCutterParametersConcave' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _839.PinionHypoidFormateTiltMachineSettings.TYPE not in self.wrapped.PinionCutterParametersConcave.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_concave to PinionHypoidFormateTiltMachineSettings. Expected: {}.'.format(self.wrapped.PinionCutterParametersConcave.__class__.__qualname__))

        return constructor.new(_839.PinionHypoidFormateTiltMachineSettings)(self.wrapped.PinionCutterParametersConcave) if self.wrapped.PinionCutterParametersConcave else None

    @property
    def pinion_cutter_parameters_concave_of_type_pinion_hypoid_generating_tilt_machine_settings(self) -> '_840.PinionHypoidGeneratingTiltMachineSettings':
        '''PinionHypoidGeneratingTiltMachineSettings: 'PinionCutterParametersConcave' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _840.PinionHypoidGeneratingTiltMachineSettings.TYPE not in self.wrapped.PinionCutterParametersConcave.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_concave to PinionHypoidGeneratingTiltMachineSettings. Expected: {}.'.format(self.wrapped.PinionCutterParametersConcave.__class__.__qualname__))

        return constructor.new(_840.PinionHypoidGeneratingTiltMachineSettings)(self.wrapped.PinionCutterParametersConcave) if self.wrapped.PinionCutterParametersConcave else None

    @property
    def pinion_cutter_parameters_concave_of_type_pinion_machine_settings_smt(self) -> '_841.PinionMachineSettingsSMT':
        '''PinionMachineSettingsSMT: 'PinionCutterParametersConcave' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _841.PinionMachineSettingsSMT.TYPE not in self.wrapped.PinionCutterParametersConcave.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_concave to PinionMachineSettingsSMT. Expected: {}.'.format(self.wrapped.PinionCutterParametersConcave.__class__.__qualname__))

        return constructor.new(_841.PinionMachineSettingsSMT)(self.wrapped.PinionCutterParametersConcave) if self.wrapped.PinionCutterParametersConcave else None

    @property
    def pinion_cutter_parameters_convex(self) -> '_838.PinionFinishMachineSettings':
        '''PinionFinishMachineSettings: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_838.PinionFinishMachineSettings)(self.wrapped.PinionCutterParametersConvex) if self.wrapped.PinionCutterParametersConvex else None

    @property
    def pinion_cutter_parameters_convex_of_type_pinion_bevel_generating_modified_roll_machine_settings(self) -> '_833.PinionBevelGeneratingModifiedRollMachineSettings':
        '''PinionBevelGeneratingModifiedRollMachineSettings: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _833.PinionBevelGeneratingModifiedRollMachineSettings.TYPE not in self.wrapped.PinionCutterParametersConvex.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_convex to PinionBevelGeneratingModifiedRollMachineSettings. Expected: {}.'.format(self.wrapped.PinionCutterParametersConvex.__class__.__qualname__))

        return constructor.new(_833.PinionBevelGeneratingModifiedRollMachineSettings)(self.wrapped.PinionCutterParametersConvex) if self.wrapped.PinionCutterParametersConvex else None

    @property
    def pinion_cutter_parameters_convex_of_type_pinion_bevel_generating_tilt_machine_settings(self) -> '_834.PinionBevelGeneratingTiltMachineSettings':
        '''PinionBevelGeneratingTiltMachineSettings: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _834.PinionBevelGeneratingTiltMachineSettings.TYPE not in self.wrapped.PinionCutterParametersConvex.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_convex to PinionBevelGeneratingTiltMachineSettings. Expected: {}.'.format(self.wrapped.PinionCutterParametersConvex.__class__.__qualname__))

        return constructor.new(_834.PinionBevelGeneratingTiltMachineSettings)(self.wrapped.PinionCutterParametersConvex) if self.wrapped.PinionCutterParametersConvex else None

    @property
    def pinion_cutter_parameters_convex_of_type_pinion_conical_machine_settings_specified(self) -> '_836.PinionConicalMachineSettingsSpecified':
        '''PinionConicalMachineSettingsSpecified: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _836.PinionConicalMachineSettingsSpecified.TYPE not in self.wrapped.PinionCutterParametersConvex.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_convex to PinionConicalMachineSettingsSpecified. Expected: {}.'.format(self.wrapped.PinionCutterParametersConvex.__class__.__qualname__))

        return constructor.new(_836.PinionConicalMachineSettingsSpecified)(self.wrapped.PinionCutterParametersConvex) if self.wrapped.PinionCutterParametersConvex else None

    @property
    def pinion_cutter_parameters_convex_of_type_pinion_hypoid_formate_tilt_machine_settings(self) -> '_839.PinionHypoidFormateTiltMachineSettings':
        '''PinionHypoidFormateTiltMachineSettings: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _839.PinionHypoidFormateTiltMachineSettings.TYPE not in self.wrapped.PinionCutterParametersConvex.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_convex to PinionHypoidFormateTiltMachineSettings. Expected: {}.'.format(self.wrapped.PinionCutterParametersConvex.__class__.__qualname__))

        return constructor.new(_839.PinionHypoidFormateTiltMachineSettings)(self.wrapped.PinionCutterParametersConvex) if self.wrapped.PinionCutterParametersConvex else None

    @property
    def pinion_cutter_parameters_convex_of_type_pinion_hypoid_generating_tilt_machine_settings(self) -> '_840.PinionHypoidGeneratingTiltMachineSettings':
        '''PinionHypoidGeneratingTiltMachineSettings: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _840.PinionHypoidGeneratingTiltMachineSettings.TYPE not in self.wrapped.PinionCutterParametersConvex.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_convex to PinionHypoidGeneratingTiltMachineSettings. Expected: {}.'.format(self.wrapped.PinionCutterParametersConvex.__class__.__qualname__))

        return constructor.new(_840.PinionHypoidGeneratingTiltMachineSettings)(self.wrapped.PinionCutterParametersConvex) if self.wrapped.PinionCutterParametersConvex else None

    @property
    def pinion_cutter_parameters_convex_of_type_pinion_machine_settings_smt(self) -> '_841.PinionMachineSettingsSMT':
        '''PinionMachineSettingsSMT: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _841.PinionMachineSettingsSMT.TYPE not in self.wrapped.PinionCutterParametersConvex.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_convex to PinionMachineSettingsSMT. Expected: {}.'.format(self.wrapped.PinionCutterParametersConvex.__class__.__qualname__))

        return constructor.new(_841.PinionMachineSettingsSMT)(self.wrapped.PinionCutterParametersConvex) if self.wrapped.PinionCutterParametersConvex else None

    @property
    def pinion_rough_machine_setting(self) -> '_842.PinionRoughMachineSetting':
        '''PinionRoughMachineSetting: 'PinionRoughMachineSetting' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_842.PinionRoughMachineSetting)(self.wrapped.PinionRoughMachineSetting) if self.wrapped.PinionRoughMachineSetting else None
