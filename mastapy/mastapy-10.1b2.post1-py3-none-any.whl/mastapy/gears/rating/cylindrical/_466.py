'''_466.py

CylindricalGearMeshRating
'''


from typing import List

from mastapy.gears import _294, _314
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.cylindrical import _480, _401, _468
from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _503, _507
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.cylindrical.iso6336 import (
    _528, _475, _531, _535
)
from mastapy.gears.rating.cylindrical.din3990 import _540
from mastapy.gears.rating.cylindrical.agma import _542
from mastapy.gears.load_case.cylindrical import _366
from mastapy.gears.rating.cylindrical.vdi import _502
from mastapy.gears.gear_designs.cylindrical import _556
from mastapy.gears.rating import _336
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalGearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshRating',)


class CylindricalGearMeshRating(_336.GearMeshRating):
    '''CylindricalGearMeshRating

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_MESH_RATING
    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def active_flank(self) -> '_294.CylindricalFlanks':
        '''CylindricalFlanks: 'ActiveFlank' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_enum(self.wrapped.ActiveFlank)
        return constructor.new(_294.CylindricalFlanks)(value) if value else None

    @property
    def sliding_ratio_at_start_of_approach(self) -> 'float':
        '''float: 'SlidingRatioAtStartOfApproach' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SlidingRatioAtStartOfApproach

    @property
    def sliding_ratio_at_end_of_recess(self) -> 'float':
        '''float: 'SlidingRatioAtEndOfRecess' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SlidingRatioAtEndOfRecess

    @property
    def mechanical_advantage(self) -> 'float':
        '''float: 'MechanicalAdvantage' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MechanicalAdvantage

    @property
    def mesh_coefficient_of_friction(self) -> 'float':
        '''float: 'MeshCoefficientOfFriction' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MeshCoefficientOfFriction

    @property
    def mesh_coefficient_of_friction_isotr1417912001(self) -> 'float':
        '''float: 'MeshCoefficientOfFrictionISOTR1417912001' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MeshCoefficientOfFrictionISOTR1417912001

    @property
    def mesh_coefficient_of_friction_isotr1417912001_with_surface_roughness_parameter(self) -> 'float':
        '''float: 'MeshCoefficientOfFrictionISOTR1417912001WithSurfaceRoughnessParameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MeshCoefficientOfFrictionISOTR1417912001WithSurfaceRoughnessParameter

    @property
    def mesh_coefficient_of_friction_isotr1417922001(self) -> 'float':
        '''float: 'MeshCoefficientOfFrictionISOTR1417922001' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MeshCoefficientOfFrictionISOTR1417922001

    @property
    def mesh_coefficient_of_friction_isotr1417922001_martins_et_al(self) -> 'float':
        '''float: 'MeshCoefficientOfFrictionISOTR1417922001MartinsEtAl' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MeshCoefficientOfFrictionISOTR1417922001MartinsEtAl

    @property
    def tooth_loss_factor(self) -> 'float':
        '''float: 'ToothLossFactor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ToothLossFactor

    @property
    def mesh_coefficient_of_friction_isotc60(self) -> 'float':
        '''float: 'MeshCoefficientOfFrictionISOTC60' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MeshCoefficientOfFrictionISOTC60

    @property
    def mesh_coefficient_of_friction_drozdov_and_gavrikov(self) -> 'float':
        '''float: 'MeshCoefficientOfFrictionDrozdovAndGavrikov' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MeshCoefficientOfFrictionDrozdovAndGavrikov

    @property
    def mesh_coefficient_of_friction_o_donoghue_and_cameron(self) -> 'float':
        '''float: 'MeshCoefficientOfFrictionODonoghueAndCameron' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MeshCoefficientOfFrictionODonoghueAndCameron

    @property
    def mesh_coefficient_of_friction_benedict_and_kelley(self) -> 'float':
        '''float: 'MeshCoefficientOfFrictionBenedictAndKelley' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MeshCoefficientOfFrictionBenedictAndKelley

    @property
    def mesh_coefficient_of_friction_misharin(self) -> 'float':
        '''float: 'MeshCoefficientOfFrictionMisharin' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MeshCoefficientOfFrictionMisharin

    @property
    def load_intensity(self) -> 'float':
        '''float: 'LoadIntensity' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LoadIntensity

    @property
    def load_sharing_factor_source(self) -> '_314.PlanetaryRatingLoadSharingOption':
        '''PlanetaryRatingLoadSharingOption: 'LoadSharingFactorSource' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_enum(self.wrapped.LoadSharingFactorSource)
        return constructor.new(_314.PlanetaryRatingLoadSharingOption)(value) if value else None

    @property
    def load_sharing_factor(self) -> 'float':
        '''float: 'LoadSharingFactor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LoadSharingFactor

    @property
    def cylindrical_mesh_single_flank_rating(self) -> '_480.CylindricalMeshSingleFlankRating':
        '''CylindricalMeshSingleFlankRating: 'CylindricalMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_480.CylindricalMeshSingleFlankRating)(self.wrapped.CylindricalMeshSingleFlankRating) if self.wrapped.CylindricalMeshSingleFlankRating else None

    @property
    def cylindrical_mesh_single_flank_rating_of_type_metal_plastic_or_plastic_metal_vdi2736_mesh_single_flank_rating(self) -> '_503.MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating':
        '''MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating: 'CylindricalMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.CylindricalMeshSingleFlankRating.__class__.__qualname__ != 'MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating':
            raise CastException('Failed to cast cylindrical_mesh_single_flank_rating to MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating. Expected: {}.'.format(self.wrapped.CylindricalMeshSingleFlankRating.__class__.__qualname__))

        return constructor.new(_503.MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating)(self.wrapped.CylindricalMeshSingleFlankRating) if self.wrapped.CylindricalMeshSingleFlankRating else None

    @property
    def cylindrical_mesh_single_flank_rating_of_type_plastic_plastic_vdi2736_mesh_single_flank_rating(self) -> '_507.PlasticPlasticVDI2736MeshSingleFlankRating':
        '''PlasticPlasticVDI2736MeshSingleFlankRating: 'CylindricalMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.CylindricalMeshSingleFlankRating.__class__.__qualname__ != 'PlasticPlasticVDI2736MeshSingleFlankRating':
            raise CastException('Failed to cast cylindrical_mesh_single_flank_rating to PlasticPlasticVDI2736MeshSingleFlankRating. Expected: {}.'.format(self.wrapped.CylindricalMeshSingleFlankRating.__class__.__qualname__))

        return constructor.new(_507.PlasticPlasticVDI2736MeshSingleFlankRating)(self.wrapped.CylindricalMeshSingleFlankRating) if self.wrapped.CylindricalMeshSingleFlankRating else None

    @property
    def cylindrical_mesh_single_flank_rating_of_type_iso63361996_mesh_single_flank_rating(self) -> '_528.ISO63361996MeshSingleFlankRating':
        '''ISO63361996MeshSingleFlankRating: 'CylindricalMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.CylindricalMeshSingleFlankRating.__class__.__qualname__ != 'ISO63361996MeshSingleFlankRating':
            raise CastException('Failed to cast cylindrical_mesh_single_flank_rating to ISO63361996MeshSingleFlankRating. Expected: {}.'.format(self.wrapped.CylindricalMeshSingleFlankRating.__class__.__qualname__))

        return constructor.new(_528.ISO63361996MeshSingleFlankRating)(self.wrapped.CylindricalMeshSingleFlankRating) if self.wrapped.CylindricalMeshSingleFlankRating else None

    @property
    def cylindrical_mesh_single_flank_rating_of_type_iso63362006_mesh_single_flank_rating(self) -> '_475.ISO63362006MeshSingleFlankRating':
        '''ISO63362006MeshSingleFlankRating: 'CylindricalMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.CylindricalMeshSingleFlankRating.__class__.__qualname__ != 'ISO63362006MeshSingleFlankRating':
            raise CastException('Failed to cast cylindrical_mesh_single_flank_rating to ISO63362006MeshSingleFlankRating. Expected: {}.'.format(self.wrapped.CylindricalMeshSingleFlankRating.__class__.__qualname__))

        return constructor.new(_475.ISO63362006MeshSingleFlankRating)(self.wrapped.CylindricalMeshSingleFlankRating) if self.wrapped.CylindricalMeshSingleFlankRating else None

    @property
    def cylindrical_mesh_single_flank_rating_of_type_iso63362019_mesh_single_flank_rating(self) -> '_531.ISO63362019MeshSingleFlankRating':
        '''ISO63362019MeshSingleFlankRating: 'CylindricalMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.CylindricalMeshSingleFlankRating.__class__.__qualname__ != 'ISO63362019MeshSingleFlankRating':
            raise CastException('Failed to cast cylindrical_mesh_single_flank_rating to ISO63362019MeshSingleFlankRating. Expected: {}.'.format(self.wrapped.CylindricalMeshSingleFlankRating.__class__.__qualname__))

        return constructor.new(_531.ISO63362019MeshSingleFlankRating)(self.wrapped.CylindricalMeshSingleFlankRating) if self.wrapped.CylindricalMeshSingleFlankRating else None

    @property
    def cylindrical_mesh_single_flank_rating_of_type_din3990_mesh_single_flank_rating(self) -> '_540.DIN3990MeshSingleFlankRating':
        '''DIN3990MeshSingleFlankRating: 'CylindricalMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.CylindricalMeshSingleFlankRating.__class__.__qualname__ != 'DIN3990MeshSingleFlankRating':
            raise CastException('Failed to cast cylindrical_mesh_single_flank_rating to DIN3990MeshSingleFlankRating. Expected: {}.'.format(self.wrapped.CylindricalMeshSingleFlankRating.__class__.__qualname__))

        return constructor.new(_540.DIN3990MeshSingleFlankRating)(self.wrapped.CylindricalMeshSingleFlankRating) if self.wrapped.CylindricalMeshSingleFlankRating else None

    @property
    def cylindrical_mesh_single_flank_rating_of_type_agma2101_mesh_single_flank_rating(self) -> '_542.AGMA2101MeshSingleFlankRating':
        '''AGMA2101MeshSingleFlankRating: 'CylindricalMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.CylindricalMeshSingleFlankRating.__class__.__qualname__ != 'AGMA2101MeshSingleFlankRating':
            raise CastException('Failed to cast cylindrical_mesh_single_flank_rating to AGMA2101MeshSingleFlankRating. Expected: {}.'.format(self.wrapped.CylindricalMeshSingleFlankRating.__class__.__qualname__))

        return constructor.new(_542.AGMA2101MeshSingleFlankRating)(self.wrapped.CylindricalMeshSingleFlankRating) if self.wrapped.CylindricalMeshSingleFlankRating else None

    @property
    def mesh_load_case(self) -> '_366.CylindricalMeshLoadCase':
        '''CylindricalMeshLoadCase: 'MeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_366.CylindricalMeshLoadCase)(self.wrapped.MeshLoadCase) if self.wrapped.MeshLoadCase else None

    @property
    def gear_set_rating(self) -> '_401.CylindricalGearSetRating':
        '''CylindricalGearSetRating: 'GearSetRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_401.CylindricalGearSetRating)(self.wrapped.GearSetRating) if self.wrapped.GearSetRating else None

    @property
    def vdi_cylindrical_gear_single_flank_rating(self) -> '_502.VDI2737InternalGearSingleFlankRating':
        '''VDI2737InternalGearSingleFlankRating: 'VDICylindricalGearSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_502.VDI2737InternalGearSingleFlankRating)(self.wrapped.VDICylindricalGearSingleFlankRating) if self.wrapped.VDICylindricalGearSingleFlankRating else None

    @property
    def isodin_cylindrical_mesh_single_flank_rating(self) -> '_535.ISO6336AbstractMetalMeshSingleFlankRating':
        '''ISO6336AbstractMetalMeshSingleFlankRating: 'ISODINCylindricalMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_535.ISO6336AbstractMetalMeshSingleFlankRating)(self.wrapped.ISODINCylindricalMeshSingleFlankRating) if self.wrapped.ISODINCylindricalMeshSingleFlankRating else None

    @property
    def isodin_cylindrical_mesh_single_flank_rating_of_type_iso63361996_mesh_single_flank_rating(self) -> '_528.ISO63361996MeshSingleFlankRating':
        '''ISO63361996MeshSingleFlankRating: 'ISODINCylindricalMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.ISODINCylindricalMeshSingleFlankRating.__class__.__qualname__ != 'ISO63361996MeshSingleFlankRating':
            raise CastException('Failed to cast isodin_cylindrical_mesh_single_flank_rating to ISO63361996MeshSingleFlankRating. Expected: {}.'.format(self.wrapped.ISODINCylindricalMeshSingleFlankRating.__class__.__qualname__))

        return constructor.new(_528.ISO63361996MeshSingleFlankRating)(self.wrapped.ISODINCylindricalMeshSingleFlankRating) if self.wrapped.ISODINCylindricalMeshSingleFlankRating else None

    @property
    def isodin_cylindrical_mesh_single_flank_rating_of_type_iso63362006_mesh_single_flank_rating(self) -> '_475.ISO63362006MeshSingleFlankRating':
        '''ISO63362006MeshSingleFlankRating: 'ISODINCylindricalMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.ISODINCylindricalMeshSingleFlankRating.__class__.__qualname__ != 'ISO63362006MeshSingleFlankRating':
            raise CastException('Failed to cast isodin_cylindrical_mesh_single_flank_rating to ISO63362006MeshSingleFlankRating. Expected: {}.'.format(self.wrapped.ISODINCylindricalMeshSingleFlankRating.__class__.__qualname__))

        return constructor.new(_475.ISO63362006MeshSingleFlankRating)(self.wrapped.ISODINCylindricalMeshSingleFlankRating) if self.wrapped.ISODINCylindricalMeshSingleFlankRating else None

    @property
    def isodin_cylindrical_mesh_single_flank_rating_of_type_iso63362019_mesh_single_flank_rating(self) -> '_531.ISO63362019MeshSingleFlankRating':
        '''ISO63362019MeshSingleFlankRating: 'ISODINCylindricalMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.ISODINCylindricalMeshSingleFlankRating.__class__.__qualname__ != 'ISO63362019MeshSingleFlankRating':
            raise CastException('Failed to cast isodin_cylindrical_mesh_single_flank_rating to ISO63362019MeshSingleFlankRating. Expected: {}.'.format(self.wrapped.ISODINCylindricalMeshSingleFlankRating.__class__.__qualname__))

        return constructor.new(_531.ISO63362019MeshSingleFlankRating)(self.wrapped.ISODINCylindricalMeshSingleFlankRating) if self.wrapped.ISODINCylindricalMeshSingleFlankRating else None

    @property
    def isodin_cylindrical_mesh_single_flank_rating_of_type_din3990_mesh_single_flank_rating(self) -> '_540.DIN3990MeshSingleFlankRating':
        '''DIN3990MeshSingleFlankRating: 'ISODINCylindricalMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.ISODINCylindricalMeshSingleFlankRating.__class__.__qualname__ != 'DIN3990MeshSingleFlankRating':
            raise CastException('Failed to cast isodin_cylindrical_mesh_single_flank_rating to DIN3990MeshSingleFlankRating. Expected: {}.'.format(self.wrapped.ISODINCylindricalMeshSingleFlankRating.__class__.__qualname__))

        return constructor.new(_540.DIN3990MeshSingleFlankRating)(self.wrapped.ISODINCylindricalMeshSingleFlankRating) if self.wrapped.ISODINCylindricalMeshSingleFlankRating else None

    @property
    def mesh_single_flank_rating(self) -> '_480.CylindricalMeshSingleFlankRating':
        '''CylindricalMeshSingleFlankRating: 'MeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_480.CylindricalMeshSingleFlankRating)(self.wrapped.MeshSingleFlankRating) if self.wrapped.MeshSingleFlankRating else None

    @property
    def mesh_single_flank_rating_of_type_metal_plastic_or_plastic_metal_vdi2736_mesh_single_flank_rating(self) -> '_503.MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating':
        '''MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating: 'MeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.MeshSingleFlankRating.__class__.__qualname__ != 'MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating':
            raise CastException('Failed to cast mesh_single_flank_rating to MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating. Expected: {}.'.format(self.wrapped.MeshSingleFlankRating.__class__.__qualname__))

        return constructor.new(_503.MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating)(self.wrapped.MeshSingleFlankRating) if self.wrapped.MeshSingleFlankRating else None

    @property
    def mesh_single_flank_rating_of_type_plastic_plastic_vdi2736_mesh_single_flank_rating(self) -> '_507.PlasticPlasticVDI2736MeshSingleFlankRating':
        '''PlasticPlasticVDI2736MeshSingleFlankRating: 'MeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.MeshSingleFlankRating.__class__.__qualname__ != 'PlasticPlasticVDI2736MeshSingleFlankRating':
            raise CastException('Failed to cast mesh_single_flank_rating to PlasticPlasticVDI2736MeshSingleFlankRating. Expected: {}.'.format(self.wrapped.MeshSingleFlankRating.__class__.__qualname__))

        return constructor.new(_507.PlasticPlasticVDI2736MeshSingleFlankRating)(self.wrapped.MeshSingleFlankRating) if self.wrapped.MeshSingleFlankRating else None

    @property
    def mesh_single_flank_rating_of_type_iso63361996_mesh_single_flank_rating(self) -> '_528.ISO63361996MeshSingleFlankRating':
        '''ISO63361996MeshSingleFlankRating: 'MeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.MeshSingleFlankRating.__class__.__qualname__ != 'ISO63361996MeshSingleFlankRating':
            raise CastException('Failed to cast mesh_single_flank_rating to ISO63361996MeshSingleFlankRating. Expected: {}.'.format(self.wrapped.MeshSingleFlankRating.__class__.__qualname__))

        return constructor.new(_528.ISO63361996MeshSingleFlankRating)(self.wrapped.MeshSingleFlankRating) if self.wrapped.MeshSingleFlankRating else None

    @property
    def mesh_single_flank_rating_of_type_iso63362006_mesh_single_flank_rating(self) -> '_475.ISO63362006MeshSingleFlankRating':
        '''ISO63362006MeshSingleFlankRating: 'MeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.MeshSingleFlankRating.__class__.__qualname__ != 'ISO63362006MeshSingleFlankRating':
            raise CastException('Failed to cast mesh_single_flank_rating to ISO63362006MeshSingleFlankRating. Expected: {}.'.format(self.wrapped.MeshSingleFlankRating.__class__.__qualname__))

        return constructor.new(_475.ISO63362006MeshSingleFlankRating)(self.wrapped.MeshSingleFlankRating) if self.wrapped.MeshSingleFlankRating else None

    @property
    def mesh_single_flank_rating_of_type_iso63362019_mesh_single_flank_rating(self) -> '_531.ISO63362019MeshSingleFlankRating':
        '''ISO63362019MeshSingleFlankRating: 'MeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.MeshSingleFlankRating.__class__.__qualname__ != 'ISO63362019MeshSingleFlankRating':
            raise CastException('Failed to cast mesh_single_flank_rating to ISO63362019MeshSingleFlankRating. Expected: {}.'.format(self.wrapped.MeshSingleFlankRating.__class__.__qualname__))

        return constructor.new(_531.ISO63362019MeshSingleFlankRating)(self.wrapped.MeshSingleFlankRating) if self.wrapped.MeshSingleFlankRating else None

    @property
    def mesh_single_flank_rating_of_type_din3990_mesh_single_flank_rating(self) -> '_540.DIN3990MeshSingleFlankRating':
        '''DIN3990MeshSingleFlankRating: 'MeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.MeshSingleFlankRating.__class__.__qualname__ != 'DIN3990MeshSingleFlankRating':
            raise CastException('Failed to cast mesh_single_flank_rating to DIN3990MeshSingleFlankRating. Expected: {}.'.format(self.wrapped.MeshSingleFlankRating.__class__.__qualname__))

        return constructor.new(_540.DIN3990MeshSingleFlankRating)(self.wrapped.MeshSingleFlankRating) if self.wrapped.MeshSingleFlankRating else None

    @property
    def mesh_single_flank_rating_of_type_agma2101_mesh_single_flank_rating(self) -> '_542.AGMA2101MeshSingleFlankRating':
        '''AGMA2101MeshSingleFlankRating: 'MeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.MeshSingleFlankRating.__class__.__qualname__ != 'AGMA2101MeshSingleFlankRating':
            raise CastException('Failed to cast mesh_single_flank_rating to AGMA2101MeshSingleFlankRating. Expected: {}.'.format(self.wrapped.MeshSingleFlankRating.__class__.__qualname__))

        return constructor.new(_542.AGMA2101MeshSingleFlankRating)(self.wrapped.MeshSingleFlankRating) if self.wrapped.MeshSingleFlankRating else None

    @property
    def agma_cylindrical_mesh_single_flank_rating(self) -> '_542.AGMA2101MeshSingleFlankRating':
        '''AGMA2101MeshSingleFlankRating: 'AGMACylindricalMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_542.AGMA2101MeshSingleFlankRating)(self.wrapped.AGMACylindricalMeshSingleFlankRating) if self.wrapped.AGMACylindricalMeshSingleFlankRating else None

    @property
    def cylindrical_gear_mesh(self) -> '_556.CylindricalGearMeshDesign':
        '''CylindricalGearMeshDesign: 'CylindricalGearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_556.CylindricalGearMeshDesign)(self.wrapped.CylindricalGearMesh) if self.wrapped.CylindricalGearMesh else None

    @property
    def cylindrical_gear_ratings(self) -> 'List[_468.CylindricalGearRating]':
        '''List[CylindricalGearRating]: 'CylindricalGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearRatings, constructor.new(_468.CylindricalGearRating))
        return value
