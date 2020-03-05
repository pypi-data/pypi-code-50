'''_114.py

ImportedFE
'''


from typing import Callable, List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable, list_with_selected_item, enum_with_selected_value
from mastapy.utility.units_and_measurements import _1387
from mastapy.system_model.imported_fes import (
    _1851, _1882, _1906, _1845,
    _1847, _1907, _1902, _1881,
    _1843, _1867, _1869, _1888,
    _1887, _1884, _1885, _1886
)
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.part_model import _1926, _1922, _1934
from mastapy.nodal_analysis import _88, _91
from mastapy.nodal_analysis.component_mode_synthesis import _220
from mastapy.system_model import _1746
from mastapy.math_utility import _1216
from mastapy.materials import _226
from mastapy.system_model.part_model.shaft_model import _1952
from mastapy.math_utility.measured_vectors import _1254
from mastapy.utility.units_and_measurements.measurements import (
    _1306, _1373, _1325, _1282
)
from mastapy import _352

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_IMPORTED_FE = python_net_import('SMT.MastaAPI.SystemModel.ImportedFEs', 'ImportedFE')


__docformat__ = 'restructuredtext en'
__all__ = ('ImportedFE',)


class ImportedFE(_91.FEStiffness):
    '''ImportedFE

    This is a mastapy class.
    '''

    TYPE = _IMPORTED_FE
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ImportedFE.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def external_fe_forces_are_from_gravity_only(self) -> 'bool':
        '''bool: 'ExternalFEForcesAreFromGravityOnly' is the original name of this property.'''

        return self.wrapped.ExternalFEForcesAreFromGravityOnly

    @external_fe_forces_are_from_gravity_only.setter
    def external_fe_forces_are_from_gravity_only(self, value: 'bool'):
        self.wrapped.ExternalFEForcesAreFromGravityOnly = bool(value) if value else False

    @property
    def housing_is_grounded(self) -> 'bool':
        '''bool: 'HousingIsGrounded' is the original name of this property.'''

        return self.wrapped.HousingIsGrounded

    @housing_is_grounded.setter
    def housing_is_grounded(self, value: 'bool'):
        self.wrapped.HousingIsGrounded = bool(value) if value else False

    @property
    def check_fe_has_internal_modes_before_nvh_analysis(self) -> 'bool':
        '''bool: 'CheckFEHasInternalModesBeforeNVHAnalysis' is the original name of this property.'''

        return self.wrapped.CheckFEHasInternalModesBeforeNVHAnalysis

    @check_fe_has_internal_modes_before_nvh_analysis.setter
    def check_fe_has_internal_modes_before_nvh_analysis(self, value: 'bool'):
        self.wrapped.CheckFEHasInternalModesBeforeNVHAnalysis = bool(value) if value else False

    @property
    def expected_number_of_rigid_body_modes(self) -> 'overridable.Overridable_int':
        '''overridable.Overridable_int: 'ExpectedNumberOfRigidBodyModes' is the original name of this property.'''

        return constructor.new(overridable.Overridable_int)(self.wrapped.ExpectedNumberOfRigidBodyModes) if self.wrapped.ExpectedNumberOfRigidBodyModes else None

    @expected_number_of_rigid_body_modes.setter
    def expected_number_of_rigid_body_modes(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.TYPE
        enclosed_type = overridable.Overridable_int.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0)
        self.wrapped.ExpectedNumberOfRigidBodyModes = value

    @property
    def actual_number_of_rigid_body_modes(self) -> 'int':
        '''int: 'ActualNumberOfRigidBodyModes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ActualNumberOfRigidBodyModes

    @property
    def is_housing(self) -> 'bool':
        '''bool: 'IsHousing' is the original name of this property.'''

        return self.wrapped.IsHousing

    @is_housing.setter
    def is_housing(self, value: 'bool'):
        self.wrapped.IsHousing = bool(value) if value else False

    @property
    def distance_display_unit(self) -> 'list_with_selected_item.ListWithSelectedItem_Unit':
        '''list_with_selected_item.ListWithSelectedItem_Unit: 'DistanceDisplayUnit' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_Unit)(self.wrapped.DistanceDisplayUnit) if self.wrapped.DistanceDisplayUnit else None

    @distance_display_unit.setter
    def distance_display_unit(self, value: 'list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.TYPE
        enclosed_type = list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value else None)
        self.wrapped.DistanceDisplayUnit = value

    @property
    def force_display_unit(self) -> 'list_with_selected_item.ListWithSelectedItem_Unit':
        '''list_with_selected_item.ListWithSelectedItem_Unit: 'ForceDisplayUnit' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_Unit)(self.wrapped.ForceDisplayUnit) if self.wrapped.ForceDisplayUnit else None

    @force_display_unit.setter
    def force_display_unit(self, value: 'list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.TYPE
        enclosed_type = list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value else None)
        self.wrapped.ForceDisplayUnit = value

    @property
    def non_condensation_node_size(self) -> 'int':
        '''int: 'NonCondensationNodeSize' is the original name of this property.'''

        return self.wrapped.NonCondensationNodeSize

    @non_condensation_node_size.setter
    def non_condensation_node_size(self, value: 'int'):
        self.wrapped.NonCondensationNodeSize = int(value) if value else 0

    @property
    def auto_connect_external_nodes(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'AutoConnectExternalNodes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AutoConnectExternalNodes

    @property
    def default_node_creation_options(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'DefaultNodeCreationOptions' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DefaultNodeCreationOptions

    @property
    def angular_alignment_tolerance(self) -> 'float':
        '''float: 'AngularAlignmentTolerance' is the original name of this property.'''

        return self.wrapped.AngularAlignmentTolerance

    @angular_alignment_tolerance.setter
    def angular_alignment_tolerance(self, value: 'float'):
        self.wrapped.AngularAlignmentTolerance = float(value) if value else 0.0

    @property
    def bearing_node_alignment(self) -> '_1851.BearingNodeAlignmentOption':
        '''BearingNodeAlignmentOption: 'BearingNodeAlignment' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.BearingNodeAlignment)
        return constructor.new(_1851.BearingNodeAlignmentOption)(value) if value else None

    @bearing_node_alignment.setter
    def bearing_node_alignment(self, value: '_1851.BearingNodeAlignmentOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.BearingNodeAlignment = value

    @property
    def comment(self) -> 'str':
        '''str: 'Comment' is the original name of this property.'''

        return self.wrapped.Comment

    @comment.setter
    def comment(self, value: 'str'):
        self.wrapped.Comment = str(value) if value else None

    @property
    def polar_inertia(self) -> 'float':
        '''float: 'PolarInertia' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PolarInertia

    @property
    def torque_transmission_relative_tolerance(self) -> 'float':
        '''float: 'TorqueTransmissionRelativeTolerance' is the original name of this property.'''

        return self.wrapped.TorqueTransmissionRelativeTolerance

    @torque_transmission_relative_tolerance.setter
    def torque_transmission_relative_tolerance(self, value: 'float'):
        self.wrapped.TorqueTransmissionRelativeTolerance = float(value) if value else 0.0

    @property
    def type_(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ImportedFEType':
        '''enum_with_selected_value.EnumWithSelectedValue_ImportedFEType: 'Type' is the original name of this property.'''

        return constructor.new(enum_with_selected_value.EnumWithSelectedValue_ImportedFEType)(self.wrapped.Type) if self.wrapped.Type else None

    @type_.setter
    def type_(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ImportedFEType.implicit_type()'):
        wrapper_type = enum_with_selected_value.EnumWithSelectedValue_ImportedFEType.TYPE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ImportedFEType.implicit_type()
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.Type = value

    @property
    def full_fe_model_mesh_path(self) -> 'str':
        '''str: 'FullFEModelMeshPath' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.FullFEModelMeshPath

    @property
    def full_fe_model_vectors_path(self) -> 'str':
        '''str: 'FullFEModelVectorsPath' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.FullFEModelVectorsPath

    @property
    def material(self) -> 'str':
        '''str: 'Material' is the original name of this property.'''

        return self.wrapped.Material.SelectedItemName

    @material.setter
    def material(self, value: 'str'):
        self.wrapped.Material.SetSelectedItem(str(value) if value else None)

    @property
    def thermal_expansion_option(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ThermalExpansionOption':
        '''enum_with_selected_value.EnumWithSelectedValue_ThermalExpansionOption: 'ThermalExpansionOption' is the original name of this property.'''

        return constructor.new(enum_with_selected_value.EnumWithSelectedValue_ThermalExpansionOption)(self.wrapped.ThermalExpansionOption) if self.wrapped.ThermalExpansionOption else None

    @thermal_expansion_option.setter
    def thermal_expansion_option(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ThermalExpansionOption.implicit_type()'):
        wrapper_type = enum_with_selected_value.EnumWithSelectedValue_ThermalExpansionOption.TYPE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ThermalExpansionOption.implicit_type()
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.ThermalExpansionOption = value

    @property
    def thermal_expansion_status(self) -> 'str':
        '''str: 'ThermalExpansionStatus' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ThermalExpansionStatus

    @property
    def add_geometry(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'AddGeometry' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AddGeometry

    @property
    def import_node_positions(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'ImportNodePositions' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ImportNodePositions

    @property
    def create_fe_volume_mesh(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'CreateFEVolumeMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.CreateFEVolumeMesh

    @property
    def update_gear_teeth_mesh(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'UpdateGearTeethMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.UpdateGearTeethMesh

    @property
    def import_reduced_stiffness(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'ImportReducedStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ImportReducedStiffness

    @property
    def open_existing_smtfe_file(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'OpenExistingSMTFEFile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OpenExistingSMTFEFile

    @property
    def re_import_external_fe_mesh(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'ReImportExternalFEMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ReImportExternalFEMesh

    @property
    def perform_reduction(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'PerformReduction' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PerformReduction

    @property
    def number_of_condensation_nodes_in_reduced_model(self) -> 'int':
        '''int: 'NumberOfCondensationNodesInReducedModel' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfCondensationNodesInReducedModel

    @property
    def number_of_condensation_nodes(self) -> 'int':
        '''int: 'NumberOfCondensationNodes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfCondensationNodes

    @property
    def perform_thermal_analysis(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'PerformThermalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PerformThermalAnalysis

    @property
    def datum(self) -> 'list_with_selected_item.ListWithSelectedItem_Datum':
        '''list_with_selected_item.ListWithSelectedItem_Datum: 'Datum' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_Datum)(self.wrapped.Datum) if self.wrapped.Datum else None

    @datum.setter
    def datum(self, value: 'list_with_selected_item.ListWithSelectedItem_Datum.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Datum.TYPE
        enclosed_type = list_with_selected_item.ListWithSelectedItem_Datum.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value else None)
        self.wrapped.Datum = value

    @property
    def copy_datum_to_manual(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'CopyDatumToManual' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.CopyDatumToManual

    @property
    def alignment_method(self) -> '_1845.AlignmentMethod':
        '''AlignmentMethod: 'AlignmentMethod' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.AlignmentMethod)
        return constructor.new(_1845.AlignmentMethod)(value) if value else None

    @alignment_method.setter
    def alignment_method(self, value: '_1845.AlignmentMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.AlignmentMethod = value

    @property
    def component_to_align_to(self) -> 'list_with_selected_item.ListWithSelectedItem_Component':
        '''list_with_selected_item.ListWithSelectedItem_Component: 'ComponentToAlignTo' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_Component)(self.wrapped.ComponentToAlignTo) if self.wrapped.ComponentToAlignTo else None

    @component_to_align_to.setter
    def component_to_align_to(self, value: 'list_with_selected_item.ListWithSelectedItem_Component.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Component.TYPE
        enclosed_type = list_with_selected_item.ListWithSelectedItem_Component.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value else None)
        self.wrapped.ComponentToAlignTo = value

    @property
    def delete_all_links(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'DeleteAllLinks' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DeleteAllLinks

    @property
    def full_fe_model_mesh_size(self) -> 'str':
        '''str: 'FullFEModelMeshSize' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.FullFEModelMeshSize

    @property
    def full_fe_model_vectors_size(self) -> 'str':
        '''str: 'FullFEModelVectorsSize' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.FullFEModelVectorsSize

    @property
    def embed_fe_model_mesh_in_masta_file(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'EmbedFEModelMeshInMASTAFile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.EmbedFEModelMeshInMASTAFile

    @property
    def embed_fe_model_vectors_in_masta_file(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'EmbedFEModelVectorsInMASTAFile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.EmbedFEModelVectorsInMASTAFile

    @property
    def store_full_fe_model_mesh_in_external_file(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'StoreFullFEModelMeshInExternalFile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.StoreFullFEModelMeshInExternalFile

    @property
    def store_full_fe_model_vectors_in_external_file(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'StoreFullFEModelVectorsInExternalFile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.StoreFullFEModelVectorsInExternalFile

    @property
    def unload_external_mesh_file(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'UnloadExternalMeshFile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.UnloadExternalMeshFile

    @property
    def load_external_mesh_file(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'LoadExternalMeshFile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LoadExternalMeshFile

    @property
    def unload_external_vectors_file(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'UnloadExternalVectorsFile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.UnloadExternalVectorsFile

    @property
    def load_external_vectors_file(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'LoadExternalVectorsFile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LoadExternalVectorsFile

    @property
    def remove_full_fe_mesh(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'RemoveFullFEMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RemoveFullFEMesh

    @property
    def number_of_angles(self) -> 'int':
        '''int: 'NumberOfAngles' is the original name of this property.'''

        return self.wrapped.NumberOfAngles

    @number_of_angles.setter
    def number_of_angles(self, value: 'int'):
        self.wrapped.NumberOfAngles = int(value) if value else 0

    @property
    def angle_span(self) -> 'float':
        '''float: 'AngleSpan' is the original name of this property.'''

        return self.wrapped.AngleSpan

    @angle_span.setter
    def angle_span(self, value: 'float'):
        self.wrapped.AngleSpan = float(value) if value else 0.0

    @property
    def condensation_node_size(self) -> 'float':
        '''float: 'CondensationNodeSize' is the original name of this property.'''

        return self.wrapped.CondensationNodeSize

    @condensation_node_size.setter
    def condensation_node_size(self, value: 'float'):
        self.wrapped.CondensationNodeSize = float(value) if value else 0.0

    @property
    def bearing_races_in_fe(self) -> 'bool':
        '''bool: 'BearingRacesInFE' is the original name of this property.'''

        return self.wrapped.BearingRacesInFE

    @bearing_races_in_fe.setter
    def bearing_races_in_fe(self, value: 'bool'):
        self.wrapped.BearingRacesInFE = bool(value) if value else False

    @property
    def is_mesh_loaded(self) -> 'bool':
        '''bool: 'IsMeshLoaded' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.IsMeshLoaded

    @property
    def are_vectors_loaded(self) -> 'bool':
        '''bool: 'AreVectorsLoaded' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AreVectorsLoaded

    @property
    def fe_meshing_options(self) -> '_88.FEMeshingOptions':
        '''FEMeshingOptions: 'FEMeshingOptions' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_88.FEMeshingOptions)(self.wrapped.FEMeshingOptions) if self.wrapped.FEMeshingOptions else None

    @property
    def cms_model(self) -> '_220.FullFEModel':
        '''FullFEModel: 'CMSModel' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_220.FullFEModel)(self.wrapped.CMSModel) if self.wrapped.CMSModel else None

    @property
    def alignment_to_component(self) -> '_1746.RelativeComponentAlignment[_1922.Component]':
        '''RelativeComponentAlignment[Component]: 'AlignmentToComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1746.RelativeComponentAlignment)[_1922.Component](self.wrapped.AlignmentToComponent) if self.wrapped.AlignmentToComponent else None

    @property
    def alignment_using_axial_node_positions(self) -> '_1847.AlignmentUsingAxialNodePositions':
        '''AlignmentUsingAxialNodePositions: 'AlignmentUsingAxialNodePositions' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1847.AlignmentUsingAxialNodePositions)(self.wrapped.AlignmentUsingAxialNodePositions) if self.wrapped.AlignmentUsingAxialNodePositions else None

    @property
    def coordinate_system(self) -> '_1216.CoordinateSystem3D':
        '''CoordinateSystem3D: 'CoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1216.CoordinateSystem3D)(self.wrapped.CoordinateSystem) if self.wrapped.CoordinateSystem else None

    @property
    def export(self) -> '_1907.UsedForExportingAnImportedFEsSetupOrSubstructuringStepToAnFEFile':
        '''UsedForExportingAnImportedFEsSetupOrSubstructuringStepToAnFEFile: 'Export' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1907.UsedForExportingAnImportedFEsSetupOrSubstructuringStepToAnFEFile)(self.wrapped.Export) if self.wrapped.Export else None

    @property
    def acoustic_radiation_efficiency(self) -> '_226.AcousticRadiationEfficiency':
        '''AcousticRadiationEfficiency: 'AcousticRadiationEfficiency' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_226.AcousticRadiationEfficiency)(self.wrapped.AcousticRadiationEfficiency) if self.wrapped.AcousticRadiationEfficiency else None

    @property
    def shafts_that_can_be_replaced(self) -> 'List[_1902.ReplacedShaftSelectionHelper]':
        '''List[ReplacedShaftSelectionHelper]: 'ShaftsThatCanBeReplaced' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftsThatCanBeReplaced, constructor.new(_1902.ReplacedShaftSelectionHelper))
        return value

    @property
    def nodes(self) -> 'List[_1881.ImportedFEStiffnessNode]':
        '''List[ImportedFEStiffnessNode]: 'Nodes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Nodes, constructor.new(_1881.ImportedFEStiffnessNode))
        return value

    @property
    def replaced_shafts(self) -> 'List[_1952.Shaft]':
        '''List[Shaft]: 'ReplacedShafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ReplacedShafts, constructor.new(_1952.Shaft))
        return value

    @property
    def links(self) -> 'List[_1843.ImportedFELink]':
        '''List[ImportedFELink]: 'Links' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Links, constructor.new(_1843.ImportedFELink))
        return value

    @property
    def thermal_expansion_forces(self) -> 'List[_1254.VectorWithLinearAndAngularComponents[_1306.ForcePerUnitTemperature, _1373.TorquePerUnitTemperature]]':
        '''List[VectorWithLinearAndAngularComponents[ForcePerUnitTemperature, TorquePerUnitTemperature]]: 'ThermalExpansionForces' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ThermalExpansionForces, constructor.new(_1254.VectorWithLinearAndAngularComponents)[_1306.ForcePerUnitTemperature, _1373.TorquePerUnitTemperature])
        return value

    @property
    def thermal_expansion_displacements(self) -> 'List[_1254.VectorWithLinearAndAngularComponents[_1325.LengthPerUnitTemperature, _1282.AnglePerUnitTemperature]]':
        '''List[VectorWithLinearAndAngularComponents[LengthPerUnitTemperature, AnglePerUnitTemperature]]: 'ThermalExpansionDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ThermalExpansionDisplacements, constructor.new(_1254.VectorWithLinearAndAngularComponents)[_1325.LengthPerUnitTemperature, _1282.AnglePerUnitTemperature])
        return value

    @property
    def geometries(self) -> 'List[_1867.FEStiffnessGeometry]':
        '''List[FEStiffnessGeometry]: 'Geometries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Geometries, constructor.new(_1867.FEStiffnessGeometry))
        return value

    @property
    def gear_meshing_options(self) -> 'List[_1869.GearMeshingOptions]':
        '''List[GearMeshingOptions]: 'GearMeshingOptions' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearMeshingOptions, constructor.new(_1869.GearMeshingOptions))
        return value

    @property
    def independent_masta_created_condensation_nodes(self) -> 'List[_1888.IndependentMastaCreatedCondensationNode]':
        '''List[IndependentMastaCreatedCondensationNode]: 'IndependentMastaCreatedCondensationNodes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.IndependentMastaCreatedCondensationNodes, constructor.new(_1888.IndependentMastaCreatedCondensationNode))
        return value

    @property
    def imported_fe_component(self) -> '_1934.ImportedFEComponent':
        '''ImportedFEComponent: 'ImportedFEComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1934.ImportedFEComponent)(self.wrapped.ImportedFEComponent) if self.wrapped.ImportedFEComponent else None

    def store_full_fe_mesh_in_external_file(self, external_fe_path: 'str'):
        ''' 'StoreFullFeMeshInExternalFile' is the original name of this method.

        Args:
            external_fe_path (str)
        '''

        external_fe_path = str(external_fe_path)
        self.wrapped.StoreFullFeMeshInExternalFile(external_fe_path if external_fe_path else None)

    def load_existing_masta_fe_file(self, file_name: 'str'):
        ''' 'LoadExistingMastaFEFile' is the original name of this method.

        Args:
            file_name (str)
        '''

        file_name = str(file_name)
        self.wrapped.LoadExistingMastaFEFile(file_name if file_name else None)

    def load_existing_masta_fe_file_with_progress(self, file_name: 'str', progress: '_352.TaskProgress'):
        ''' 'LoadExistingMastaFEFile' is the original name of this method.

        Args:
            file_name (str)
            progress (mastapy.TaskProgress)
        '''

        file_name = str(file_name)
        self.wrapped.LoadExistingMastaFEFile(file_name if file_name else None, progress.wrapped if progress else None)

    def create_imported_fe_with_selection_static_analysis(self) -> '_1887.ImportedFEWithSelectionStaticAnalysis':
        ''' 'CreateImportedFEWithSelectionStaticAnalysis' is the original name of this method.

        Returns:
            mastapy.system_model.imported_fes.ImportedFEWithSelectionStaticAnalysis
        '''

        method_result = self.wrapped.CreateImportedFEWithSelectionStaticAnalysis()
        return constructor.new(_1887.ImportedFEWithSelectionStaticAnalysis)(method_result) if method_result else None

    def create_imported_fe_with_selection_components(self) -> '_1884.ImportedFEWithSelectionComponents':
        ''' 'CreateImportedFEWithSelectionComponents' is the original name of this method.

        Returns:
            mastapy.system_model.imported_fes.ImportedFEWithSelectionComponents
        '''

        method_result = self.wrapped.CreateImportedFEWithSelectionComponents()
        return constructor.new(_1884.ImportedFEWithSelectionComponents)(method_result) if method_result else None

    def create_imported_fe_with_selection_for_harmonic_analysis(self) -> '_1885.ImportedFEWithSelectionForHarmonicAnalysis':
        ''' 'CreateImportedFEWithSelectionForHarmonicAnalysis' is the original name of this method.

        Returns:
            mastapy.system_model.imported_fes.ImportedFEWithSelectionForHarmonicAnalysis
        '''

        method_result = self.wrapped.CreateImportedFEWithSelectionForHarmonicAnalysis()
        return constructor.new(_1885.ImportedFEWithSelectionForHarmonicAnalysis)(method_result) if method_result else None

    def create_imported_fe_with_selection_modal_analysis(self) -> '_1886.ImportedFEWithSelectionModalAnalysis':
        ''' 'CreateImportedFEWithSelectionModalAnalysis' is the original name of this method.

        Returns:
            mastapy.system_model.imported_fes.ImportedFEWithSelectionModalAnalysis
        '''

        method_result = self.wrapped.CreateImportedFEWithSelectionModalAnalysis()
        return constructor.new(_1886.ImportedFEWithSelectionModalAnalysis)(method_result) if method_result else None

    def links_for(self, node: '_1881.ImportedFEStiffnessNode') -> 'List[_1843.ImportedFELink]':
        ''' 'LinksFor' is the original name of this method.

        Args:
            node (mastapy.system_model.imported_fes.ImportedFEStiffnessNode)

        Returns:
            List[mastapy.system_model.imported_fes.ImportedFELink]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.LinksFor(node.wrapped if node else None), constructor.new(_1843.ImportedFELink))
