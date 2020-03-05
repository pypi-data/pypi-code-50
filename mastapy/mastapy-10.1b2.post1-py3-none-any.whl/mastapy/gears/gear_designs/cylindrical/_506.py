'''_506.py

CylindricalGearDesign
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy.geometry.twod import _288
from mastapy.gears import _308, _290
from mastapy._internal.python_net import python_net_import
from mastapy.gears.gear_designs.cylindrical import (
    _1007, _1006, _1008, _1009,
    _1020, _648, _402, _1021,
    _737, _738, _753, _981,
    _500
)
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1034
from mastapy.gears.manufacturing.cylindrical import _615
from mastapy.gears.materials import (
    _599, _590, _591, _593,
    _597, _600, _606, _608
)
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
    _1064, _1067, _1059, _1061,
    _1057, _1058, _1060, _1062,
    _1065, _1066, _1063
)
from mastapy.gears.gear_designs.agma_gleason_conical import _1085
from mastapy.gears.gear_designs import _636

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_CYLINDRICAL_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearDesign',)


class CylindricalGearDesign(_636.GearDesign):
    '''CylindricalGearDesign

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_DESIGN
    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearDesign.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def transverse_chamfer_angle(self) -> 'float':
        '''float: 'TransverseChamferAngle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TransverseChamferAngle

    @property
    def chamfer_angle_in_normal_plane(self) -> 'float':
        '''float: 'ChamferAngleInNormalPlane' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ChamferAngleInNormalPlane

    @property
    def web_status(self) -> 'str':
        '''str: 'WebStatus' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.WebStatus

    @property
    def effective_web_thickness(self) -> 'float':
        '''float: 'EffectiveWebThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.EffectiveWebThickness

    @property
    def web_centre_offset(self) -> 'float':
        '''float: 'WebCentreOffset' is the original name of this property.'''

        return self.wrapped.WebCentreOffset

    @web_centre_offset.setter
    def web_centre_offset(self, value: 'float'):
        self.wrapped.WebCentreOffset = float(value) if value else 0.0

    @property
    def specified_web_thickness(self) -> 'float':
        '''float: 'SpecifiedWebThickness' is the original name of this property.'''

        return self.wrapped.SpecifiedWebThickness

    @specified_web_thickness.setter
    def specified_web_thickness(self, value: 'float'):
        self.wrapped.SpecifiedWebThickness = float(value) if value else 0.0

    @property
    def rim_thickness(self) -> 'float':
        '''float: 'RimThickness' is the original name of this property.'''

        return self.wrapped.RimThickness

    @rim_thickness.setter
    def rim_thickness(self, value: 'float'):
        self.wrapped.RimThickness = float(value) if value else 0.0

    @property
    def rim_thickness_normal_module_ratio(self) -> 'float':
        '''float: 'RimThicknessNormalModuleRatio' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RimThicknessNormalModuleRatio

    @property
    def minimum_required_rim_thickness_by_standard_iso8140042005(self) -> 'float':
        '''float: 'MinimumRequiredRimThicknessByStandardISO8140042005' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MinimumRequiredRimThicknessByStandardISO8140042005

    @property
    def rim_diameter(self) -> 'float':
        '''float: 'RimDiameter' is the original name of this property.'''

        return self.wrapped.RimDiameter

    @rim_diameter.setter
    def rim_diameter(self, value: 'float'):
        self.wrapped.RimDiameter = float(value) if value else 0.0

    @property
    def absolute_rim_diameter(self) -> 'float':
        '''float: 'AbsoluteRimDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AbsoluteRimDiameter

    @property
    def lead(self) -> 'float':
        '''float: 'Lead' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Lead

    @property
    def tip_diameter(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'TipDiameter' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.TipDiameter) if self.wrapped.TipDiameter else None

    @tip_diameter.setter
    def tip_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.TipDiameter = value

    @property
    def signed_tip_diameter(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'SignedTipDiameter' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.SignedTipDiameter) if self.wrapped.SignedTipDiameter else None

    @signed_tip_diameter.setter
    def signed_tip_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.SignedTipDiameter = value

    @property
    def tip_alteration_coefficient(self) -> 'float':
        '''float: 'TipAlterationCoefficient' is the original name of this property.'''

        return self.wrapped.TipAlterationCoefficient

    @tip_alteration_coefficient.setter
    def tip_alteration_coefficient(self, value: 'float'):
        self.wrapped.TipAlterationCoefficient = float(value) if value else 0.0

    @property
    def root_diameter(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'RootDiameter' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.RootDiameter) if self.wrapped.RootDiameter else None

    @root_diameter.setter
    def root_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.RootDiameter = value

    @property
    def signed_root_diameter(self) -> 'float':
        '''float: 'SignedRootDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SignedRootDiameter

    @property
    def tip_thickness(self) -> 'float':
        '''float: 'TipThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TipThickness

    @property
    def normal_thickness_at_tip_form_diameter_at_upper_backlash_allowance(self) -> 'float':
        '''float: 'NormalThicknessAtTipFormDiameterAtUpperBacklashAllowance' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NormalThicknessAtTipFormDiameterAtUpperBacklashAllowance

    @property
    def normal_thickness_at_tip_form_diameter_at_lower_backlash_allowance(self) -> 'float':
        '''float: 'NormalThicknessAtTipFormDiameterAtLowerBacklashAllowance' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NormalThicknessAtTipFormDiameterAtLowerBacklashAllowance

    @property
    def normal_thickness_at_tip_form_diameter_at_lower_backlash_allowance_over_normal_module(self) -> 'float':
        '''float: 'NormalThicknessAtTipFormDiameterAtLowerBacklashAllowanceOverNormalModule' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NormalThicknessAtTipFormDiameterAtLowerBacklashAllowanceOverNormalModule

    @property
    def tip_thickness_at_upper_backlash_allowance(self) -> 'float':
        '''float: 'TipThicknessAtUpperBacklashAllowance' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TipThicknessAtUpperBacklashAllowance

    @property
    def tip_thickness_at_lower_backlash_allowance(self) -> 'float':
        '''float: 'TipThicknessAtLowerBacklashAllowance' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TipThicknessAtLowerBacklashAllowance

    @property
    def tip_thickness_at_lower_backlash_allowance_over_normal_module(self) -> 'float':
        '''float: 'TipThicknessAtLowerBacklashAllowanceOverNormalModule' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TipThicknessAtLowerBacklashAllowanceOverNormalModule

    @property
    def internal_external(self) -> '_288.InternalExternalType':
        '''InternalExternalType: 'InternalExternal' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.InternalExternal)
        return constructor.new(_288.InternalExternalType)(value) if value else None

    @internal_external.setter
    def internal_external(self, value: '_288.InternalExternalType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.InternalExternal = value

    @property
    def material_name(self) -> 'str':
        '''str: 'MaterialName' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MaterialName

    @property
    def helix_angle_at_tip_form_diameter(self) -> 'float':
        '''float: 'HelixAngleAtTipFormDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.HelixAngleAtTipFormDiameter

    @property
    def addendum(self) -> 'float':
        '''float: 'Addendum' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Addendum

    @property
    def dedendum(self) -> 'float':
        '''float: 'Dedendum' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Dedendum

    @property
    def tooth_thickness_half_angle_at_reference_circle(self) -> 'float':
        '''float: 'ToothThicknessHalfAngleAtReferenceCircle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ToothThicknessHalfAngleAtReferenceCircle

    @property
    def thermal_contact_coefficient(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'ThermalContactCoefficient' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.ThermalContactCoefficient) if self.wrapped.ThermalContactCoefficient else None

    @thermal_contact_coefficient.setter
    def thermal_contact_coefficient(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.ThermalContactCoefficient = value

    @property
    def normal_space_width_at_root_form_diameter(self) -> 'float':
        '''float: 'NormalSpaceWidthAtRootFormDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NormalSpaceWidthAtRootFormDiameter

    @property
    def mass(self) -> 'float':
        '''float: 'Mass' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Mass

    @property
    def reference_diameter(self) -> 'float':
        '''float: 'ReferenceDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ReferenceDiameter

    @property
    def transverse_pressure_angle(self) -> 'float':
        '''float: 'TransversePressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TransversePressureAngle

    @property
    def normal_pressure_angle(self) -> 'float':
        '''float: 'NormalPressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NormalPressureAngle

    @property
    def gear_hand(self) -> 'str':
        '''str: 'GearHand' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.GearHand

    @property
    def hand(self) -> '_308.Hand':
        '''Hand: 'Hand' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.Hand)
        return constructor.new(_308.Hand)(value) if value else None

    @hand.setter
    def hand(self, value: '_308.Hand'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Hand = value

    @property
    def face_width(self) -> 'float':
        '''float: 'FaceWidth' is the original name of this property.'''

        return self.wrapped.FaceWidth

    @face_width.setter
    def face_width(self, value: 'float'):
        self.wrapped.FaceWidth = float(value) if value else 0.0

    @property
    def helix_angle(self) -> 'float':
        '''float: 'HelixAngle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.HelixAngle

    @property
    def number_of_teeth_unsigned(self) -> 'float':
        '''float: 'NumberOfTeethUnsigned' is the original name of this property.'''

        return self.wrapped.NumberOfTeethUnsigned

    @number_of_teeth_unsigned.setter
    def number_of_teeth_unsigned(self, value: 'float'):
        self.wrapped.NumberOfTeethUnsigned = float(value) if value else 0.0

    @property
    def normal_module(self) -> 'float':
        '''float: 'NormalModule' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NormalModule

    @property
    def number_of_teeth_maintaining_ratio_calculating_normal_module(self) -> 'int':
        '''int: 'NumberOfTeethMaintainingRatioCalculatingNormalModule' is the original name of this property.'''

        return self.wrapped.NumberOfTeethMaintainingRatioCalculatingNormalModule

    @number_of_teeth_maintaining_ratio_calculating_normal_module.setter
    def number_of_teeth_maintaining_ratio_calculating_normal_module(self, value: 'int'):
        self.wrapped.NumberOfTeethMaintainingRatioCalculatingNormalModule = int(value) if value else 0

    @property
    def number_of_teeth_with_normal_module_adjustment(self) -> 'int':
        '''int: 'NumberOfTeethWithNormalModuleAdjustment' is the original name of this property.'''

        return self.wrapped.NumberOfTeethWithNormalModuleAdjustment

    @number_of_teeth_with_normal_module_adjustment.setter
    def number_of_teeth_with_normal_module_adjustment(self, value: 'int'):
        self.wrapped.NumberOfTeethWithNormalModuleAdjustment = int(value) if value else 0

    @property
    def normal_base_pitch(self) -> 'float':
        '''float: 'NormalBasePitch' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NormalBasePitch

    @property
    def transverse_base_pitch(self) -> 'float':
        '''float: 'TransverseBasePitch' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TransverseBasePitch

    @property
    def base_diameter(self) -> 'float':
        '''float: 'BaseDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.BaseDiameter

    @property
    def absolute_base_diameter(self) -> 'float':
        '''float: 'AbsoluteBaseDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AbsoluteBaseDiameter

    @property
    def tip_form_diameter(self) -> 'float':
        '''float: 'TipFormDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TipFormDiameter

    @property
    def absolute_tip_form_diameter(self) -> 'float':
        '''float: 'AbsoluteTipFormDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AbsoluteTipFormDiameter

    @property
    def root_form_diameter(self) -> 'float':
        '''float: 'RootFormDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RootFormDiameter

    @property
    def absolute_form_diameter(self) -> 'float':
        '''float: 'AbsoluteFormDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AbsoluteFormDiameter

    @property
    def lowest_sap_diameter(self) -> 'float':
        '''float: 'LowestSAPDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LowestSAPDiameter

    @property
    def form_to_sap_diameter_absolute_clearance_as_normal_module_ratio(self) -> 'float':
        '''float: 'FormToSAPDiameterAbsoluteClearanceAsNormalModuleRatio' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.FormToSAPDiameterAbsoluteClearanceAsNormalModuleRatio

    @property
    def absolute_form_to_sap_diameter_clearance(self) -> 'float':
        '''float: 'AbsoluteFormToSAPDiameterClearance' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AbsoluteFormToSAPDiameterClearance

    @property
    def base_to_form_diameter_clearance_as_normal_module_ratio(self) -> 'float':
        '''float: 'BaseToFormDiameterClearanceAsNormalModuleRatio' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.BaseToFormDiameterClearanceAsNormalModuleRatio

    @property
    def base_to_form_diameter_clearance(self) -> 'float':
        '''float: 'BaseToFormDiameterClearance' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.BaseToFormDiameterClearance

    @property
    def mean_normal_thickness_at_half_depth(self) -> 'float':
        '''float: 'MeanNormalThicknessAtHalfDepth' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MeanNormalThicknessAtHalfDepth

    @property
    def mean_normal_thickness_at_tip_form_diameter(self) -> 'float':
        '''float: 'MeanNormalThicknessAtTipFormDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MeanNormalThicknessAtTipFormDiameter

    @property
    def mean_normal_thickness_at_root_form_diameter(self) -> 'float':
        '''float: 'MeanNormalThicknessAtRootFormDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MeanNormalThicknessAtRootFormDiameter

    @property
    def normal_tooth_thickness_at_the_base_circle(self) -> 'float':
        '''float: 'NormalToothThicknessAtTheBaseCircle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NormalToothThicknessAtTheBaseCircle

    @property
    def transverse_tooth_thickness_at_the_base_circle(self) -> 'float':
        '''float: 'TransverseToothThicknessAtTheBaseCircle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TransverseToothThicknessAtTheBaseCircle

    @property
    def use_default_design_material(self) -> 'bool':
        '''bool: 'UseDefaultDesignMaterial' is the original name of this property.'''

        return self.wrapped.UseDefaultDesignMaterial

    @use_default_design_material.setter
    def use_default_design_material(self, value: 'bool'):
        self.wrapped.UseDefaultDesignMaterial = bool(value) if value else False

    @property
    def material_iso(self) -> 'str':
        '''str: 'MaterialISO' is the original name of this property.'''

        return self.wrapped.MaterialISO.SelectedItemName

    @material_iso.setter
    def material_iso(self, value: 'str'):
        self.wrapped.MaterialISO.SetSelectedItem(str(value) if value else None)

    @property
    def material_agma(self) -> 'str':
        '''str: 'MaterialAGMA' is the original name of this property.'''

        return self.wrapped.MaterialAGMA.SelectedItemName

    @material_agma.setter
    def material_agma(self, value: 'str'):
        self.wrapped.MaterialAGMA.SetSelectedItem(str(value) if value else None)

    @property
    def tooth_depth(self) -> 'float':
        '''float: 'ToothDepth' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ToothDepth

    @property
    def root_heat_transfer_coefficient(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'RootHeatTransferCoefficient' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.RootHeatTransferCoefficient) if self.wrapped.RootHeatTransferCoefficient else None

    @root_heat_transfer_coefficient.setter
    def root_heat_transfer_coefficient(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.RootHeatTransferCoefficient = value

    @property
    def flank_heat_transfer_coefficient(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'FlankHeatTransferCoefficient' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.FlankHeatTransferCoefficient) if self.wrapped.FlankHeatTransferCoefficient else None

    @flank_heat_transfer_coefficient.setter
    def flank_heat_transfer_coefficient(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.FlankHeatTransferCoefficient = value

    @property
    def permissible_linear_wear(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'PermissibleLinearWear' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.PermissibleLinearWear) if self.wrapped.PermissibleLinearWear else None

    @permissible_linear_wear.setter
    def permissible_linear_wear(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.PermissibleLinearWear = value

    @property
    def initial_clocking_angle(self) -> 'float':
        '''float: 'InitialClockingAngle' is the original name of this property.'''

        return self.wrapped.InitialClockingAngle

    @initial_clocking_angle.setter
    def initial_clocking_angle(self, value: 'float'):
        self.wrapped.InitialClockingAngle = float(value) if value else 0.0

    @property
    def mean_generating_circle_diameter(self) -> 'float':
        '''float: 'MeanGeneratingCircleDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MeanGeneratingCircleDiameter

    @property
    def effective_tip_radius(self) -> 'float':
        '''float: 'EffectiveTipRadius' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.EffectiveTipRadius

    @property
    def tip_form_roll_distance(self) -> 'float':
        '''float: 'TipFormRollDistance' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TipFormRollDistance

    @property
    def tip_form_roll_angle(self) -> 'float':
        '''float: 'TipFormRollAngle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TipFormRollAngle

    @property
    def form_radius(self) -> 'float':
        '''float: 'FormRadius' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.FormRadius

    @property
    def root_form_roll_distance(self) -> 'float':
        '''float: 'RootFormRollDistance' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RootFormRollDistance

    @property
    def root_form_roll_angle(self) -> 'float':
        '''float: 'RootFormRollAngle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RootFormRollAngle

    @property
    def has_chamfer(self) -> 'bool':
        '''bool: 'HasChamfer' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.HasChamfer

    @property
    def factor_for_the_increase_of_the_yield_point_under_compression(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'FactorForTheIncreaseOfTheYieldPointUnderCompression' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.FactorForTheIncreaseOfTheYieldPointUnderCompression) if self.wrapped.FactorForTheIncreaseOfTheYieldPointUnderCompression else None

    @factor_for_the_increase_of_the_yield_point_under_compression.setter
    def factor_for_the_increase_of_the_yield_point_under_compression(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.FactorForTheIncreaseOfTheYieldPointUnderCompression = value

    @property
    def rotation_angle(self) -> 'float':
        '''float: 'RotationAngle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RotationAngle

    @property
    def radii_of_curvature_at_tip(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'RadiiOfCurvatureAtTip' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.RadiiOfCurvatureAtTip) if self.wrapped.RadiiOfCurvatureAtTip else None

    @radii_of_curvature_at_tip.setter
    def radii_of_curvature_at_tip(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.RadiiOfCurvatureAtTip = value

    @property
    def maximum_tip_diameter(self) -> 'float':
        '''float: 'MaximumTipDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MaximumTipDiameter

    @property
    def minimum_root_diameter(self) -> 'float':
        '''float: 'MinimumRootDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MinimumRootDiameter

    @property
    def number_of_teeth_with_centre_distance_adjustment(self) -> 'int':
        '''int: 'NumberOfTeethWithCentreDistanceAdjustment' is the original name of this property.'''

        return self.wrapped.NumberOfTeethWithCentreDistanceAdjustment

    @number_of_teeth_with_centre_distance_adjustment.setter
    def number_of_teeth_with_centre_distance_adjustment(self, value: 'int'):
        self.wrapped.NumberOfTeethWithCentreDistanceAdjustment = int(value) if value else 0

    @property
    def iso6336_geometry(self) -> '_1007.ISO6336GeometryBase':
        '''ISO6336GeometryBase: 'ISO6336Geometry' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1007.ISO6336GeometryBase)(self.wrapped.ISO6336Geometry) if self.wrapped.ISO6336Geometry else None

    @property
    def iso6336_geometry_of_type_iso6336_geometry(self) -> '_1006.ISO6336Geometry':
        '''ISO6336Geometry: 'ISO6336Geometry' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1006.ISO6336Geometry.TYPE not in self.wrapped.ISO6336Geometry.__class__.__mro__:
            raise CastException('Failed to cast iso6336_geometry to ISO6336Geometry. Expected: {}.'.format(self.wrapped.ISO6336Geometry.__class__.__qualname__))

        return constructor.new(_1006.ISO6336Geometry)(self.wrapped.ISO6336Geometry) if self.wrapped.ISO6336Geometry else None

    @property
    def iso6336_geometry_of_type_iso6336_geometry_for_shaped_gears(self) -> '_1008.ISO6336GeometryForShapedGears':
        '''ISO6336GeometryForShapedGears: 'ISO6336Geometry' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1008.ISO6336GeometryForShapedGears.TYPE not in self.wrapped.ISO6336Geometry.__class__.__mro__:
            raise CastException('Failed to cast iso6336_geometry to ISO6336GeometryForShapedGears. Expected: {}.'.format(self.wrapped.ISO6336Geometry.__class__.__qualname__))

        return constructor.new(_1008.ISO6336GeometryForShapedGears)(self.wrapped.ISO6336Geometry) if self.wrapped.ISO6336Geometry else None

    @property
    def iso6336_geometry_of_type_iso6336_geometry_manufactured(self) -> '_1009.ISO6336GeometryManufactured':
        '''ISO6336GeometryManufactured: 'ISO6336Geometry' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1009.ISO6336GeometryManufactured.TYPE not in self.wrapped.ISO6336Geometry.__class__.__mro__:
            raise CastException('Failed to cast iso6336_geometry to ISO6336GeometryManufactured. Expected: {}.'.format(self.wrapped.ISO6336Geometry.__class__.__qualname__))

        return constructor.new(_1009.ISO6336GeometryManufactured)(self.wrapped.ISO6336Geometry) if self.wrapped.ISO6336Geometry else None

    @property
    def surface_roughness(self) -> '_1020.SurfaceRoughness':
        '''SurfaceRoughness: 'SurfaceRoughness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1020.SurfaceRoughness)(self.wrapped.SurfaceRoughness) if self.wrapped.SurfaceRoughness else None

    @property
    def tip_diameter_reporting(self) -> '_648.CylindricalGearProfileMeasurement':
        '''CylindricalGearProfileMeasurement: 'TipDiameterReporting' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_648.CylindricalGearProfileMeasurement)(self.wrapped.TipDiameterReporting) if self.wrapped.TipDiameterReporting else None

    @property
    def root_diameter_reporting(self) -> '_648.CylindricalGearProfileMeasurement':
        '''CylindricalGearProfileMeasurement: 'RootDiameterReporting' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_648.CylindricalGearProfileMeasurement)(self.wrapped.RootDiameterReporting) if self.wrapped.RootDiameterReporting else None

    @property
    def cylindrical_gear_set(self) -> '_402.CylindricalGearSetDesign':
        '''CylindricalGearSetDesign: 'CylindricalGearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_402.CylindricalGearSetDesign)(self.wrapped.CylindricalGearSet) if self.wrapped.CylindricalGearSet else None

    @property
    def cylindrical_gear_micro_geometry(self) -> '_1034.CylindricalGearMicroGeometry':
        '''CylindricalGearMicroGeometry: 'CylindricalGearMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1034.CylindricalGearMicroGeometry)(self.wrapped.CylindricalGearMicroGeometry) if self.wrapped.CylindricalGearMicroGeometry else None

    @property
    def cylindrical_gear_manufacturing_configuration(self) -> '_615.CylindricalGearManufacturingConfig':
        '''CylindricalGearManufacturingConfig: 'CylindricalGearManufacturingConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_615.CylindricalGearManufacturingConfig)(self.wrapped.CylindricalGearManufacturingConfiguration) if self.wrapped.CylindricalGearManufacturingConfiguration else None

    @property
    def lowest_start_of_active_profile(self) -> '_648.CylindricalGearProfileMeasurement':
        '''CylindricalGearProfileMeasurement: 'LowestStartOfActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_648.CylindricalGearProfileMeasurement)(self.wrapped.LowestStartOfActiveProfile) if self.wrapped.LowestStartOfActiveProfile else None

    @property
    def material(self) -> '_599.GearMaterial':
        '''GearMaterial: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_599.GearMaterial)(self.wrapped.Material) if self.wrapped.Material else None

    @property
    def material_of_type_agma_cylindrical_gear_material(self) -> '_590.AGMACylindricalGearMaterial':
        '''AGMACylindricalGearMaterial: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _590.AGMACylindricalGearMaterial.TYPE not in self.wrapped.Material.__class__.__mro__:
            raise CastException('Failed to cast material to AGMACylindricalGearMaterial. Expected: {}.'.format(self.wrapped.Material.__class__.__qualname__))

        return constructor.new(_590.AGMACylindricalGearMaterial)(self.wrapped.Material) if self.wrapped.Material else None

    @property
    def material_of_type_bevel_gear_iso_material(self) -> '_591.BevelGearISOMaterial':
        '''BevelGearISOMaterial: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _591.BevelGearISOMaterial.TYPE not in self.wrapped.Material.__class__.__mro__:
            raise CastException('Failed to cast material to BevelGearISOMaterial. Expected: {}.'.format(self.wrapped.Material.__class__.__qualname__))

        return constructor.new(_591.BevelGearISOMaterial)(self.wrapped.Material) if self.wrapped.Material else None

    @property
    def material_of_type_bevel_gear_material(self) -> '_593.BevelGearMaterial':
        '''BevelGearMaterial: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _593.BevelGearMaterial.TYPE not in self.wrapped.Material.__class__.__mro__:
            raise CastException('Failed to cast material to BevelGearMaterial. Expected: {}.'.format(self.wrapped.Material.__class__.__qualname__))

        return constructor.new(_593.BevelGearMaterial)(self.wrapped.Material) if self.wrapped.Material else None

    @property
    def material_of_type_cylindrical_gear_material(self) -> '_597.CylindricalGearMaterial':
        '''CylindricalGearMaterial: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _597.CylindricalGearMaterial.TYPE not in self.wrapped.Material.__class__.__mro__:
            raise CastException('Failed to cast material to CylindricalGearMaterial. Expected: {}.'.format(self.wrapped.Material.__class__.__qualname__))

        return constructor.new(_597.CylindricalGearMaterial)(self.wrapped.Material) if self.wrapped.Material else None

    @property
    def material_of_type_iso_cylindrical_gear_material(self) -> '_600.ISOCylindricalGearMaterial':
        '''ISOCylindricalGearMaterial: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _600.ISOCylindricalGearMaterial.TYPE not in self.wrapped.Material.__class__.__mro__:
            raise CastException('Failed to cast material to ISOCylindricalGearMaterial. Expected: {}.'.format(self.wrapped.Material.__class__.__qualname__))

        return constructor.new(_600.ISOCylindricalGearMaterial)(self.wrapped.Material) if self.wrapped.Material else None

    @property
    def material_of_type_klingelnberg_cyclo_palloid_conical_gear_material(self) -> '_606.KlingelnbergCycloPalloidConicalGearMaterial':
        '''KlingelnbergCycloPalloidConicalGearMaterial: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _606.KlingelnbergCycloPalloidConicalGearMaterial.TYPE not in self.wrapped.Material.__class__.__mro__:
            raise CastException('Failed to cast material to KlingelnbergCycloPalloidConicalGearMaterial. Expected: {}.'.format(self.wrapped.Material.__class__.__qualname__))

        return constructor.new(_606.KlingelnbergCycloPalloidConicalGearMaterial)(self.wrapped.Material) if self.wrapped.Material else None

    @property
    def material_of_type_plastic_cylindrical_gear_material(self) -> '_608.PlasticCylindricalGearMaterial':
        '''PlasticCylindricalGearMaterial: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _608.PlasticCylindricalGearMaterial.TYPE not in self.wrapped.Material.__class__.__mro__:
            raise CastException('Failed to cast material to PlasticCylindricalGearMaterial. Expected: {}.'.format(self.wrapped.Material.__class__.__qualname__))

        return constructor.new(_608.PlasticCylindricalGearMaterial)(self.wrapped.Material) if self.wrapped.Material else None

    @property
    def system_of_gear_fits(self) -> '_1064.DIN3967SystemOfGearFits':
        '''DIN3967SystemOfGearFits: 'SystemOfGearFits' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1064.DIN3967SystemOfGearFits)(self.wrapped.SystemOfGearFits) if self.wrapped.SystemOfGearFits else None

    @property
    def iso_accuracy_grade(self) -> '_1067.ISO1328AccuracyGrades':
        '''ISO1328AccuracyGrades: 'ISOAccuracyGrade' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1067.ISO1328AccuracyGrades)(self.wrapped.ISOAccuracyGrade) if self.wrapped.ISOAccuracyGrade else None

    @property
    def agma_accuracy_grade(self) -> '_1059.AGMA20151AccuracyGrades':
        '''AGMA20151AccuracyGrades: 'AGMAAccuracyGrade' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1059.AGMA20151AccuracyGrades)(self.wrapped.AGMAAccuracyGrade) if self.wrapped.AGMAAccuracyGrade else None

    @property
    def accuracy_grade_allowances_and_tolerances(self) -> '_1061.CylindricalAccuracyGrader':
        '''CylindricalAccuracyGrader: 'AccuracyGradeAllowancesAndTolerances' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1061.CylindricalAccuracyGrader)(self.wrapped.AccuracyGradeAllowancesAndTolerances) if self.wrapped.AccuracyGradeAllowancesAndTolerances else None

    @property
    def accuracy_grade_allowances_and_tolerances_of_type_agma2000_accuracy_grader(self) -> '_1057.AGMA2000AccuracyGrader':
        '''AGMA2000AccuracyGrader: 'AccuracyGradeAllowancesAndTolerances' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1057.AGMA2000AccuracyGrader.TYPE not in self.wrapped.AccuracyGradeAllowancesAndTolerances.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grade_allowances_and_tolerances to AGMA2000AccuracyGrader. Expected: {}.'.format(self.wrapped.AccuracyGradeAllowancesAndTolerances.__class__.__qualname__))

        return constructor.new(_1057.AGMA2000AccuracyGrader)(self.wrapped.AccuracyGradeAllowancesAndTolerances) if self.wrapped.AccuracyGradeAllowancesAndTolerances else None

    @property
    def accuracy_grade_allowances_and_tolerances_of_type_agma20151_accuracy_grader(self) -> '_1058.AGMA20151AccuracyGrader':
        '''AGMA20151AccuracyGrader: 'AccuracyGradeAllowancesAndTolerances' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1058.AGMA20151AccuracyGrader.TYPE not in self.wrapped.AccuracyGradeAllowancesAndTolerances.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grade_allowances_and_tolerances to AGMA20151AccuracyGrader. Expected: {}.'.format(self.wrapped.AccuracyGradeAllowancesAndTolerances.__class__.__qualname__))

        return constructor.new(_1058.AGMA20151AccuracyGrader)(self.wrapped.AccuracyGradeAllowancesAndTolerances) if self.wrapped.AccuracyGradeAllowancesAndTolerances else None

    @property
    def accuracy_grade_allowances_and_tolerances_of_type_agmaiso13282013_accuracy_grader(self) -> '_1060.AGMAISO13282013AccuracyGrader':
        '''AGMAISO13282013AccuracyGrader: 'AccuracyGradeAllowancesAndTolerances' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1060.AGMAISO13282013AccuracyGrader.TYPE not in self.wrapped.AccuracyGradeAllowancesAndTolerances.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grade_allowances_and_tolerances to AGMAISO13282013AccuracyGrader. Expected: {}.'.format(self.wrapped.AccuracyGradeAllowancesAndTolerances.__class__.__qualname__))

        return constructor.new(_1060.AGMAISO13282013AccuracyGrader)(self.wrapped.AccuracyGradeAllowancesAndTolerances) if self.wrapped.AccuracyGradeAllowancesAndTolerances else None

    @property
    def accuracy_grade_allowances_and_tolerances_of_type_cylindrical_accuracy_grader_with_profile_form_and_slope(self) -> '_1062.CylindricalAccuracyGraderWithProfileFormAndSlope':
        '''CylindricalAccuracyGraderWithProfileFormAndSlope: 'AccuracyGradeAllowancesAndTolerances' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1062.CylindricalAccuracyGraderWithProfileFormAndSlope.TYPE not in self.wrapped.AccuracyGradeAllowancesAndTolerances.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grade_allowances_and_tolerances to CylindricalAccuracyGraderWithProfileFormAndSlope. Expected: {}.'.format(self.wrapped.AccuracyGradeAllowancesAndTolerances.__class__.__qualname__))

        return constructor.new(_1062.CylindricalAccuracyGraderWithProfileFormAndSlope)(self.wrapped.AccuracyGradeAllowancesAndTolerances) if self.wrapped.AccuracyGradeAllowancesAndTolerances else None

    @property
    def accuracy_grade_allowances_and_tolerances_of_type_iso13282013_accuracy_grader(self) -> '_1065.ISO13282013AccuracyGrader':
        '''ISO13282013AccuracyGrader: 'AccuracyGradeAllowancesAndTolerances' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1065.ISO13282013AccuracyGrader.TYPE not in self.wrapped.AccuracyGradeAllowancesAndTolerances.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grade_allowances_and_tolerances to ISO13282013AccuracyGrader. Expected: {}.'.format(self.wrapped.AccuracyGradeAllowancesAndTolerances.__class__.__qualname__))

        return constructor.new(_1065.ISO13282013AccuracyGrader)(self.wrapped.AccuracyGradeAllowancesAndTolerances) if self.wrapped.AccuracyGradeAllowancesAndTolerances else None

    @property
    def accuracy_grade_allowances_and_tolerances_of_type_iso1328_accuracy_grader(self) -> '_1066.ISO1328AccuracyGrader':
        '''ISO1328AccuracyGrader: 'AccuracyGradeAllowancesAndTolerances' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1066.ISO1328AccuracyGrader.TYPE not in self.wrapped.AccuracyGradeAllowancesAndTolerances.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grade_allowances_and_tolerances to ISO1328AccuracyGrader. Expected: {}.'.format(self.wrapped.AccuracyGradeAllowancesAndTolerances.__class__.__qualname__))

        return constructor.new(_1066.ISO1328AccuracyGrader)(self.wrapped.AccuracyGradeAllowancesAndTolerances) if self.wrapped.AccuracyGradeAllowancesAndTolerances else None

    @property
    def accuracy_grades_specified_accuracy(self) -> '_290.AccuracyGrades':
        '''AccuracyGrades: 'AccuracyGradesSpecifiedAccuracy' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_290.AccuracyGrades)(self.wrapped.AccuracyGradesSpecifiedAccuracy) if self.wrapped.AccuracyGradesSpecifiedAccuracy else None

    @property
    def accuracy_grades_specified_accuracy_of_type_agma20151_accuracy_grades(self) -> '_1059.AGMA20151AccuracyGrades':
        '''AGMA20151AccuracyGrades: 'AccuracyGradesSpecifiedAccuracy' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1059.AGMA20151AccuracyGrades.TYPE not in self.wrapped.AccuracyGradesSpecifiedAccuracy.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grades_specified_accuracy to AGMA20151AccuracyGrades. Expected: {}.'.format(self.wrapped.AccuracyGradesSpecifiedAccuracy.__class__.__qualname__))

        return constructor.new(_1059.AGMA20151AccuracyGrades)(self.wrapped.AccuracyGradesSpecifiedAccuracy) if self.wrapped.AccuracyGradesSpecifiedAccuracy else None

    @property
    def accuracy_grades_specified_accuracy_of_type_cylindrical_accuracy_grades(self) -> '_1063.CylindricalAccuracyGrades':
        '''CylindricalAccuracyGrades: 'AccuracyGradesSpecifiedAccuracy' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1063.CylindricalAccuracyGrades.TYPE not in self.wrapped.AccuracyGradesSpecifiedAccuracy.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grades_specified_accuracy to CylindricalAccuracyGrades. Expected: {}.'.format(self.wrapped.AccuracyGradesSpecifiedAccuracy.__class__.__qualname__))

        return constructor.new(_1063.CylindricalAccuracyGrades)(self.wrapped.AccuracyGradesSpecifiedAccuracy) if self.wrapped.AccuracyGradesSpecifiedAccuracy else None

    @property
    def accuracy_grades_specified_accuracy_of_type_iso1328_accuracy_grades(self) -> '_1067.ISO1328AccuracyGrades':
        '''ISO1328AccuracyGrades: 'AccuracyGradesSpecifiedAccuracy' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1067.ISO1328AccuracyGrades.TYPE not in self.wrapped.AccuracyGradesSpecifiedAccuracy.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grades_specified_accuracy to ISO1328AccuracyGrades. Expected: {}.'.format(self.wrapped.AccuracyGradesSpecifiedAccuracy.__class__.__qualname__))

        return constructor.new(_1067.ISO1328AccuracyGrades)(self.wrapped.AccuracyGradesSpecifiedAccuracy) if self.wrapped.AccuracyGradesSpecifiedAccuracy else None

    @property
    def accuracy_grades_specified_accuracy_of_type_agma_gleason_conical_accuracy_grades(self) -> '_1085.AGMAGleasonConicalAccuracyGrades':
        '''AGMAGleasonConicalAccuracyGrades: 'AccuracyGradesSpecifiedAccuracy' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1085.AGMAGleasonConicalAccuracyGrades.TYPE not in self.wrapped.AccuracyGradesSpecifiedAccuracy.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grades_specified_accuracy to AGMAGleasonConicalAccuracyGrades. Expected: {}.'.format(self.wrapped.AccuracyGradesSpecifiedAccuracy.__class__.__qualname__))

        return constructor.new(_1085.AGMAGleasonConicalAccuracyGrades)(self.wrapped.AccuracyGradesSpecifiedAccuracy) if self.wrapped.AccuracyGradesSpecifiedAccuracy else None

    @property
    def tip_form(self) -> '_648.CylindricalGearProfileMeasurement':
        '''CylindricalGearProfileMeasurement: 'TipForm' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_648.CylindricalGearProfileMeasurement)(self.wrapped.TipForm) if self.wrapped.TipForm else None

    @property
    def root_form(self) -> '_648.CylindricalGearProfileMeasurement':
        '''CylindricalGearProfileMeasurement: 'RootForm' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_648.CylindricalGearProfileMeasurement)(self.wrapped.RootForm) if self.wrapped.RootForm else None

    @property
    def tiff_analysis_settings(self) -> '_1021.TiffAnalysisSettings':
        '''TiffAnalysisSettings: 'TIFFAnalysisSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1021.TiffAnalysisSettings)(self.wrapped.TIFFAnalysisSettings) if self.wrapped.TIFFAnalysisSettings else None

    @property
    def finished_tooth_thickness_specification(self) -> '_737.FinishToothThicknessDesignSpecification':
        '''FinishToothThicknessDesignSpecification: 'FinishedToothThicknessSpecification' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_737.FinishToothThicknessDesignSpecification)(self.wrapped.FinishedToothThicknessSpecification) if self.wrapped.FinishedToothThicknessSpecification else None

    @property
    def rough_tooth_thickness_specification(self) -> '_738.ToothThicknessSpecification':
        '''ToothThicknessSpecification: 'RoughToothThicknessSpecification' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_738.ToothThicknessSpecification)(self.wrapped.RoughToothThicknessSpecification) if self.wrapped.RoughToothThicknessSpecification else None

    @property
    def finish_stock_specification(self) -> '_753.FinishStockSpecification':
        '''FinishStockSpecification: 'FinishStockSpecification' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_753.FinishStockSpecification)(self.wrapped.FinishStockSpecification) if self.wrapped.FinishStockSpecification else None

    @property
    def cylindrical_gear_cutting_options(self) -> '_981.CylindricalGearCuttingOptions':
        '''CylindricalGearCuttingOptions: 'CylindricalGearCuttingOptions' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_981.CylindricalGearCuttingOptions)(self.wrapped.CylindricalGearCuttingOptions) if self.wrapped.CylindricalGearCuttingOptions else None

    @property
    def cylindrical_meshes(self) -> 'List[_500.CylindricalGearMeshDesign]':
        '''List[CylindricalGearMeshDesign]: 'CylindricalMeshes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalMeshes, constructor.new(_500.CylindricalGearMeshDesign))
        return value
