'''_4.py

MastaSettings
'''


from mastapy.bearings import _1494
from mastapy._internal import constructor
from mastapy.gears import _119, _120
from mastapy.gears.gear_designs.cylindrical import _766, _771, _772
from mastapy.gears.gear_designs import _707
from mastapy.gears.ltca.cylindrical import _622
from mastapy.gears.materials import _376
from mastapy.gears.rating.cylindrical import _262, _269
from mastapy.materials import _78
from mastapy.nodal_analysis import _1339, _1355
from mastapy.shafts import _38
from mastapy.system_model.part_model import _1989
from mastapy.utility.cad_export import _1325
from mastapy.utility.databases import _1322
from mastapy.utility import _1129, _1130
from mastapy.utility.scripting import _1251
from mastapy.utility.units_and_measurements import _1139
from mastapy._internal.python_net import python_net_import

_MASTA_SETTINGS = python_net_import('SMT.MastaAPI', 'MastaSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('MastaSettings',)


class MastaSettings:
    '''MastaSettings

    This is a mastapy class.
    '''

    TYPE = _MASTA_SETTINGS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MastaSettings.TYPE'):
        self.wrapped = instance_to_wrap

    @property
    def bearing_settings(self) -> '_1494.BearingSettings':
        '''BearingSettings: 'BearingSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1494.BearingSettings)(self.wrapped.BearingSettings) if self.wrapped.BearingSettings else None

    @property
    def bevel_hypoid_gear_design_settings(self) -> '_119.BevelHypoidGearDesignSettings':
        '''BevelHypoidGearDesignSettings: 'BevelHypoidGearDesignSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_119.BevelHypoidGearDesignSettings)(self.wrapped.BevelHypoidGearDesignSettings) if self.wrapped.BevelHypoidGearDesignSettings else None

    @property
    def bevel_hypoid_gear_rating_settings(self) -> '_120.BevelHypoidGearRatingSettings':
        '''BevelHypoidGearRatingSettings: 'BevelHypoidGearRatingSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_120.BevelHypoidGearRatingSettings)(self.wrapped.BevelHypoidGearRatingSettings) if self.wrapped.BevelHypoidGearRatingSettings else None

    @property
    def cylindrical_gear_defaults(self) -> '_766.CylindricalGearDefaults':
        '''CylindricalGearDefaults: 'CylindricalGearDefaults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_766.CylindricalGearDefaults)(self.wrapped.CylindricalGearDefaults) if self.wrapped.CylindricalGearDefaults else None

    @property
    def cylindrical_gear_design_constraint_settings(self) -> '_771.CylindricalGearDesignConstraintSettings':
        '''CylindricalGearDesignConstraintSettings: 'CylindricalGearDesignConstraintSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_771.CylindricalGearDesignConstraintSettings)(self.wrapped.CylindricalGearDesignConstraintSettings) if self.wrapped.CylindricalGearDesignConstraintSettings else None

    @property
    def cylindrical_gear_design_settings(self) -> '_772.CylindricalGearDesignSettings':
        '''CylindricalGearDesignSettings: 'CylindricalGearDesignSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_772.CylindricalGearDesignSettings)(self.wrapped.CylindricalGearDesignSettings) if self.wrapped.CylindricalGearDesignSettings else None

    @property
    def selected_design_constraints_collection(self) -> '_707.SelectedDesignConstraintsCollection':
        '''SelectedDesignConstraintsCollection: 'SelectedDesignConstraintsCollection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_707.SelectedDesignConstraintsCollection)(self.wrapped.SelectedDesignConstraintsCollection) if self.wrapped.SelectedDesignConstraintsCollection else None

    @property
    def cylindrical_gear_fe_settings(self) -> '_622.CylindricalGearFESettings':
        '''CylindricalGearFESettings: 'CylindricalGearFESettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_622.CylindricalGearFESettings)(self.wrapped.CylindricalGearFESettings) if self.wrapped.CylindricalGearFESettings else None

    @property
    def gear_material_expert_system_factor_settings(self) -> '_376.GearMaterialExpertSystemFactorSettings':
        '''GearMaterialExpertSystemFactorSettings: 'GearMaterialExpertSystemFactorSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_376.GearMaterialExpertSystemFactorSettings)(self.wrapped.GearMaterialExpertSystemFactorSettings) if self.wrapped.GearMaterialExpertSystemFactorSettings else None

    @property
    def cylindrical_gear_rating_settings(self) -> '_262.CylindricalGearRatingSettings':
        '''CylindricalGearRatingSettings: 'CylindricalGearRatingSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_262.CylindricalGearRatingSettings)(self.wrapped.CylindricalGearRatingSettings) if self.wrapped.CylindricalGearRatingSettings else None

    @property
    def cylindrical_plastic_gear_rating_settings(self) -> '_269.CylindricalPlasticGearRatingSettings':
        '''CylindricalPlasticGearRatingSettings: 'CylindricalPlasticGearRatingSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_269.CylindricalPlasticGearRatingSettings)(self.wrapped.CylindricalPlasticGearRatingSettings) if self.wrapped.CylindricalPlasticGearRatingSettings else None

    @property
    def materials_settings(self) -> '_78.MaterialsSettings':
        '''MaterialsSettings: 'MaterialsSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_78.MaterialsSettings)(self.wrapped.MaterialsSettings) if self.wrapped.MaterialsSettings else None

    @property
    def analysis_settings(self) -> '_1339.AnalysisSettings':
        '''AnalysisSettings: 'AnalysisSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1339.AnalysisSettings)(self.wrapped.AnalysisSettings) if self.wrapped.AnalysisSettings else None

    @property
    def fe_user_settings(self) -> '_1355.FEUserSettings':
        '''FEUserSettings: 'FEUserSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1355.FEUserSettings)(self.wrapped.FEUserSettings) if self.wrapped.FEUserSettings else None

    @property
    def shaft_settings(self) -> '_38.ShaftSettings':
        '''ShaftSettings: 'ShaftSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_38.ShaftSettings)(self.wrapped.ShaftSettings) if self.wrapped.ShaftSettings else None

    @property
    def planet_carrier_settings(self) -> '_1989.PlanetCarrierSettings':
        '''PlanetCarrierSettings: 'PlanetCarrierSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1989.PlanetCarrierSettings)(self.wrapped.PlanetCarrierSettings) if self.wrapped.PlanetCarrierSettings else None

    @property
    def cad_export_settings(self) -> '_1325.CADExportSettings':
        '''CADExportSettings: 'CADExportSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1325.CADExportSettings)(self.wrapped.CADExportSettings) if self.wrapped.CADExportSettings else None

    @property
    def database_settings(self) -> '_1322.DatabaseSettings':
        '''DatabaseSettings: 'DatabaseSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1322.DatabaseSettings)(self.wrapped.DatabaseSettings) if self.wrapped.DatabaseSettings else None

    @property
    def program_settings(self) -> '_1129.ProgramSettings':
        '''ProgramSettings: 'ProgramSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1129.ProgramSettings)(self.wrapped.ProgramSettings) if self.wrapped.ProgramSettings else None

    @property
    def pushbullet_settings(self) -> '_1130.PushbulletSettings':
        '''PushbulletSettings: 'PushbulletSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1130.PushbulletSettings)(self.wrapped.PushbulletSettings) if self.wrapped.PushbulletSettings else None

    @property
    def scripting_setup(self) -> '_1251.ScriptingSetup':
        '''ScriptingSetup: 'ScriptingSetup' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1251.ScriptingSetup)(self.wrapped.ScriptingSetup) if self.wrapped.ScriptingSetup else None

    @property
    def measurement_settings(self) -> '_1139.MeasurementSettings':
        '''MeasurementSettings: 'MeasurementSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1139.MeasurementSettings)(self.wrapped.MeasurementSettings) if self.wrapped.MeasurementSettings else None
