'''_350.py

AbstractGearMeshAnalysis
'''


from mastapy._internal import constructor
from mastapy.gears.analysis import _360
from mastapy.gears.rating.zerol_bevel import _346
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.worm import _348, _351
from mastapy.gears.rating.straight_bevel_diff import _413
from mastapy.gears.rating.straight_bevel import _417
from mastapy.gears.rating.spiral_bevel import _420
from mastapy.gears.rating.klingelnberg_spiral_bevel import _422
from mastapy.gears.rating.klingelnberg_hypoid import _424
from mastapy.gears.rating.hypoid import _454
from mastapy.gears.rating.face import _458, _461
from mastapy.gears.rating.cylindrical import _463, _468
from mastapy.gears.rating.conical import _544
from mastapy.gears.rating.concept import _547, _550
from mastapy.gears.manufacturing.cylindrical import _610, _614, _615
from mastapy.gears.manufacturing.bevel import (
    _796, _798, _809, _810,
    _817
)
from mastapy.gears.ltca.cylindrical import _868
from mastapy.gears.ltca.conical import _877
from mastapy.gears.load_case.worm import _885
from mastapy.gears.load_case.face import _887
from mastapy.gears.load_case.cylindrical import _889
from mastapy.gears.load_case.conical import _893
from mastapy.gears.load_case.concept import _895
from mastapy.gears.load_case.bevel import _897
from mastapy.gears.gear_twod_fe_analysis import _901
from mastapy.gears.gear_designs.face import _962
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1031, _1032
from mastapy.gears.fe_model.cylindrical import _1115
from mastapy.gears.fe_model.conical import _1117
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_MESH_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Analysis', 'AbstractGearMeshAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractGearMeshAnalysis',)


class AbstractGearMeshAnalysis(_1.APIBase):
    '''AbstractGearMeshAnalysis

    This is a mastapy class.
    '''

    TYPE = _ABSTRACT_GEAR_MESH_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'AbstractGearMeshAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def mesh_name(self) -> 'str':
        '''str: 'MeshName' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MeshName

    @property
    def name(self) -> 'str':
        '''str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Name

    @property
    def gear_a(self) -> '_360.AbstractGearAnalysis':
        '''AbstractGearAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_360.AbstractGearAnalysis)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_zerol_bevel_gear_rating(self) -> '_346.ZerolBevelGearRating':
        '''ZerolBevelGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'ZerolBevelGearRating':
            raise CastException('Failed to cast gear_a to ZerolBevelGearRating. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_346.ZerolBevelGearRating)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_worm_gear_duty_cycle_rating(self) -> '_348.WormGearDutyCycleRating':
        '''WormGearDutyCycleRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'WormGearDutyCycleRating':
            raise CastException('Failed to cast gear_a to WormGearDutyCycleRating. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_348.WormGearDutyCycleRating)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_worm_gear_rating(self) -> '_351.WormGearRating':
        '''WormGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'WormGearRating':
            raise CastException('Failed to cast gear_a to WormGearRating. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_351.WormGearRating)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_straight_bevel_diff_gear_rating(self) -> '_413.StraightBevelDiffGearRating':
        '''StraightBevelDiffGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'StraightBevelDiffGearRating':
            raise CastException('Failed to cast gear_a to StraightBevelDiffGearRating. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_413.StraightBevelDiffGearRating)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_straight_bevel_gear_rating(self) -> '_417.StraightBevelGearRating':
        '''StraightBevelGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'StraightBevelGearRating':
            raise CastException('Failed to cast gear_a to StraightBevelGearRating. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_417.StraightBevelGearRating)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_spiral_bevel_gear_rating(self) -> '_420.SpiralBevelGearRating':
        '''SpiralBevelGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'SpiralBevelGearRating':
            raise CastException('Failed to cast gear_a to SpiralBevelGearRating. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_420.SpiralBevelGearRating)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(self) -> '_422.KlingelnbergCycloPalloidSpiralBevelGearRating':
        '''KlingelnbergCycloPalloidSpiralBevelGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'KlingelnbergCycloPalloidSpiralBevelGearRating':
            raise CastException('Failed to cast gear_a to KlingelnbergCycloPalloidSpiralBevelGearRating. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_422.KlingelnbergCycloPalloidSpiralBevelGearRating)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_klingelnberg_cyclo_palloid_hypoid_gear_rating(self) -> '_424.KlingelnbergCycloPalloidHypoidGearRating':
        '''KlingelnbergCycloPalloidHypoidGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'KlingelnbergCycloPalloidHypoidGearRating':
            raise CastException('Failed to cast gear_a to KlingelnbergCycloPalloidHypoidGearRating. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_424.KlingelnbergCycloPalloidHypoidGearRating)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_hypoid_gear_rating(self) -> '_454.HypoidGearRating':
        '''HypoidGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'HypoidGearRating':
            raise CastException('Failed to cast gear_a to HypoidGearRating. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_454.HypoidGearRating)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_face_gear_duty_cycle_rating(self) -> '_458.FaceGearDutyCycleRating':
        '''FaceGearDutyCycleRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'FaceGearDutyCycleRating':
            raise CastException('Failed to cast gear_a to FaceGearDutyCycleRating. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_458.FaceGearDutyCycleRating)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_face_gear_rating(self) -> '_461.FaceGearRating':
        '''FaceGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'FaceGearRating':
            raise CastException('Failed to cast gear_a to FaceGearRating. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_461.FaceGearRating)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_cylindrical_gear_duty_cycle_rating(self) -> '_463.CylindricalGearDutyCycleRating':
        '''CylindricalGearDutyCycleRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'CylindricalGearDutyCycleRating':
            raise CastException('Failed to cast gear_a to CylindricalGearDutyCycleRating. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_463.CylindricalGearDutyCycleRating)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_cylindrical_gear_rating(self) -> '_468.CylindricalGearRating':
        '''CylindricalGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'CylindricalGearRating':
            raise CastException('Failed to cast gear_a to CylindricalGearRating. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_468.CylindricalGearRating)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_conical_gear_duty_cycle_rating(self) -> '_544.ConicalGearDutyCycleRating':
        '''ConicalGearDutyCycleRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'ConicalGearDutyCycleRating':
            raise CastException('Failed to cast gear_a to ConicalGearDutyCycleRating. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_544.ConicalGearDutyCycleRating)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_concept_gear_duty_cycle_rating(self) -> '_547.ConceptGearDutyCycleRating':
        '''ConceptGearDutyCycleRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'ConceptGearDutyCycleRating':
            raise CastException('Failed to cast gear_a to ConceptGearDutyCycleRating. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_547.ConceptGearDutyCycleRating)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_concept_gear_rating(self) -> '_550.ConceptGearRating':
        '''ConceptGearRating: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'ConceptGearRating':
            raise CastException('Failed to cast gear_a to ConceptGearRating. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_550.ConceptGearRating)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_cylindrical_gear_manufacturing_config(self) -> '_610.CylindricalGearManufacturingConfig':
        '''CylindricalGearManufacturingConfig: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'CylindricalGearManufacturingConfig':
            raise CastException('Failed to cast gear_a to CylindricalGearManufacturingConfig. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_610.CylindricalGearManufacturingConfig)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_cylindrical_manufactured_gear_duty_cycle(self) -> '_614.CylindricalManufacturedGearDutyCycle':
        '''CylindricalManufacturedGearDutyCycle: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'CylindricalManufacturedGearDutyCycle':
            raise CastException('Failed to cast gear_a to CylindricalManufacturedGearDutyCycle. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_614.CylindricalManufacturedGearDutyCycle)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_cylindrical_manufactured_gear_load_case(self) -> '_615.CylindricalManufacturedGearLoadCase':
        '''CylindricalManufacturedGearLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'CylindricalManufacturedGearLoadCase':
            raise CastException('Failed to cast gear_a to CylindricalManufacturedGearLoadCase. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_615.CylindricalManufacturedGearLoadCase)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_conical_gear_manufacturing_analysis(self) -> '_796.ConicalGearManufacturingAnalysis':
        '''ConicalGearManufacturingAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'ConicalGearManufacturingAnalysis':
            raise CastException('Failed to cast gear_a to ConicalGearManufacturingAnalysis. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_796.ConicalGearManufacturingAnalysis)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_conical_gear_micro_geometry_config(self) -> '_798.ConicalGearMicroGeometryConfig':
        '''ConicalGearMicroGeometryConfig: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'ConicalGearMicroGeometryConfig':
            raise CastException('Failed to cast gear_a to ConicalGearMicroGeometryConfig. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_798.ConicalGearMicroGeometryConfig)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_conical_pinion_manufacturing_config(self) -> '_809.ConicalPinionManufacturingConfig':
        '''ConicalPinionManufacturingConfig: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'ConicalPinionManufacturingConfig':
            raise CastException('Failed to cast gear_a to ConicalPinionManufacturingConfig. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_809.ConicalPinionManufacturingConfig)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_conical_pinion_micro_geometry_config(self) -> '_810.ConicalPinionMicroGeometryConfig':
        '''ConicalPinionMicroGeometryConfig: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'ConicalPinionMicroGeometryConfig':
            raise CastException('Failed to cast gear_a to ConicalPinionMicroGeometryConfig. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_810.ConicalPinionMicroGeometryConfig)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_conical_wheel_manufacturing_config(self) -> '_817.ConicalWheelManufacturingConfig':
        '''ConicalWheelManufacturingConfig: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'ConicalWheelManufacturingConfig':
            raise CastException('Failed to cast gear_a to ConicalWheelManufacturingConfig. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_817.ConicalWheelManufacturingConfig)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_cylindrical_gear_load_distribution_analysis(self) -> '_868.CylindricalGearLoadDistributionAnalysis':
        '''CylindricalGearLoadDistributionAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'CylindricalGearLoadDistributionAnalysis':
            raise CastException('Failed to cast gear_a to CylindricalGearLoadDistributionAnalysis. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_868.CylindricalGearLoadDistributionAnalysis)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_conical_gear_load_distribution_analysis(self) -> '_877.ConicalGearLoadDistributionAnalysis':
        '''ConicalGearLoadDistributionAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'ConicalGearLoadDistributionAnalysis':
            raise CastException('Failed to cast gear_a to ConicalGearLoadDistributionAnalysis. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_877.ConicalGearLoadDistributionAnalysis)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_worm_gear_load_case(self) -> '_885.WormGearLoadCase':
        '''WormGearLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'WormGearLoadCase':
            raise CastException('Failed to cast gear_a to WormGearLoadCase. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_885.WormGearLoadCase)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_face_gear_load_case(self) -> '_887.FaceGearLoadCase':
        '''FaceGearLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'FaceGearLoadCase':
            raise CastException('Failed to cast gear_a to FaceGearLoadCase. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_887.FaceGearLoadCase)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_cylindrical_gear_load_case(self) -> '_889.CylindricalGearLoadCase':
        '''CylindricalGearLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'CylindricalGearLoadCase':
            raise CastException('Failed to cast gear_a to CylindricalGearLoadCase. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_889.CylindricalGearLoadCase)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_conical_gear_load_case(self) -> '_893.ConicalGearLoadCase':
        '''ConicalGearLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'ConicalGearLoadCase':
            raise CastException('Failed to cast gear_a to ConicalGearLoadCase. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_893.ConicalGearLoadCase)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_concept_gear_load_case(self) -> '_895.ConceptGearLoadCase':
        '''ConceptGearLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'ConceptGearLoadCase':
            raise CastException('Failed to cast gear_a to ConceptGearLoadCase. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_895.ConceptGearLoadCase)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_bevel_load_case(self) -> '_897.BevelLoadCase':
        '''BevelLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'BevelLoadCase':
            raise CastException('Failed to cast gear_a to BevelLoadCase. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_897.BevelLoadCase)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_cylindrical_gear_tiff_analysis(self) -> '_901.CylindricalGearTIFFAnalysis':
        '''CylindricalGearTIFFAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'CylindricalGearTIFFAnalysis':
            raise CastException('Failed to cast gear_a to CylindricalGearTIFFAnalysis. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_901.CylindricalGearTIFFAnalysis)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_face_gear_micro_geometry(self) -> '_962.FaceGearMicroGeometry':
        '''FaceGearMicroGeometry: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'FaceGearMicroGeometry':
            raise CastException('Failed to cast gear_a to FaceGearMicroGeometry. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_962.FaceGearMicroGeometry)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_cylindrical_gear_micro_geometry(self) -> '_1031.CylindricalGearMicroGeometry':
        '''CylindricalGearMicroGeometry: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'CylindricalGearMicroGeometry':
            raise CastException('Failed to cast gear_a to CylindricalGearMicroGeometry. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_1031.CylindricalGearMicroGeometry)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_cylindrical_gear_micro_geometry_duty_cycle(self) -> '_1032.CylindricalGearMicroGeometryDutyCycle':
        '''CylindricalGearMicroGeometryDutyCycle: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'CylindricalGearMicroGeometryDutyCycle':
            raise CastException('Failed to cast gear_a to CylindricalGearMicroGeometryDutyCycle. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_1032.CylindricalGearMicroGeometryDutyCycle)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_cylindrical_gear_fe_model(self) -> '_1115.CylindricalGearFEModel':
        '''CylindricalGearFEModel: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'CylindricalGearFEModel':
            raise CastException('Failed to cast gear_a to CylindricalGearFEModel. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_1115.CylindricalGearFEModel)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_conical_gear_fe_model(self) -> '_1117.ConicalGearFEModel':
        '''ConicalGearFEModel: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'ConicalGearFEModel':
            raise CastException('Failed to cast gear_a to ConicalGearFEModel. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_1117.ConicalGearFEModel)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_b(self) -> '_360.AbstractGearAnalysis':
        '''AbstractGearAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_360.AbstractGearAnalysis)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_zerol_bevel_gear_rating(self) -> '_346.ZerolBevelGearRating':
        '''ZerolBevelGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'ZerolBevelGearRating':
            raise CastException('Failed to cast gear_b to ZerolBevelGearRating. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_346.ZerolBevelGearRating)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_worm_gear_duty_cycle_rating(self) -> '_348.WormGearDutyCycleRating':
        '''WormGearDutyCycleRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'WormGearDutyCycleRating':
            raise CastException('Failed to cast gear_b to WormGearDutyCycleRating. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_348.WormGearDutyCycleRating)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_worm_gear_rating(self) -> '_351.WormGearRating':
        '''WormGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'WormGearRating':
            raise CastException('Failed to cast gear_b to WormGearRating. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_351.WormGearRating)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_straight_bevel_diff_gear_rating(self) -> '_413.StraightBevelDiffGearRating':
        '''StraightBevelDiffGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'StraightBevelDiffGearRating':
            raise CastException('Failed to cast gear_b to StraightBevelDiffGearRating. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_413.StraightBevelDiffGearRating)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_straight_bevel_gear_rating(self) -> '_417.StraightBevelGearRating':
        '''StraightBevelGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'StraightBevelGearRating':
            raise CastException('Failed to cast gear_b to StraightBevelGearRating. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_417.StraightBevelGearRating)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_spiral_bevel_gear_rating(self) -> '_420.SpiralBevelGearRating':
        '''SpiralBevelGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'SpiralBevelGearRating':
            raise CastException('Failed to cast gear_b to SpiralBevelGearRating. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_420.SpiralBevelGearRating)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(self) -> '_422.KlingelnbergCycloPalloidSpiralBevelGearRating':
        '''KlingelnbergCycloPalloidSpiralBevelGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'KlingelnbergCycloPalloidSpiralBevelGearRating':
            raise CastException('Failed to cast gear_b to KlingelnbergCycloPalloidSpiralBevelGearRating. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_422.KlingelnbergCycloPalloidSpiralBevelGearRating)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_klingelnberg_cyclo_palloid_hypoid_gear_rating(self) -> '_424.KlingelnbergCycloPalloidHypoidGearRating':
        '''KlingelnbergCycloPalloidHypoidGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'KlingelnbergCycloPalloidHypoidGearRating':
            raise CastException('Failed to cast gear_b to KlingelnbergCycloPalloidHypoidGearRating. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_424.KlingelnbergCycloPalloidHypoidGearRating)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_hypoid_gear_rating(self) -> '_454.HypoidGearRating':
        '''HypoidGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'HypoidGearRating':
            raise CastException('Failed to cast gear_b to HypoidGearRating. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_454.HypoidGearRating)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_face_gear_duty_cycle_rating(self) -> '_458.FaceGearDutyCycleRating':
        '''FaceGearDutyCycleRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'FaceGearDutyCycleRating':
            raise CastException('Failed to cast gear_b to FaceGearDutyCycleRating. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_458.FaceGearDutyCycleRating)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_face_gear_rating(self) -> '_461.FaceGearRating':
        '''FaceGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'FaceGearRating':
            raise CastException('Failed to cast gear_b to FaceGearRating. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_461.FaceGearRating)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_cylindrical_gear_duty_cycle_rating(self) -> '_463.CylindricalGearDutyCycleRating':
        '''CylindricalGearDutyCycleRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'CylindricalGearDutyCycleRating':
            raise CastException('Failed to cast gear_b to CylindricalGearDutyCycleRating. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_463.CylindricalGearDutyCycleRating)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_cylindrical_gear_rating(self) -> '_468.CylindricalGearRating':
        '''CylindricalGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'CylindricalGearRating':
            raise CastException('Failed to cast gear_b to CylindricalGearRating. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_468.CylindricalGearRating)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_conical_gear_duty_cycle_rating(self) -> '_544.ConicalGearDutyCycleRating':
        '''ConicalGearDutyCycleRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'ConicalGearDutyCycleRating':
            raise CastException('Failed to cast gear_b to ConicalGearDutyCycleRating. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_544.ConicalGearDutyCycleRating)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_concept_gear_duty_cycle_rating(self) -> '_547.ConceptGearDutyCycleRating':
        '''ConceptGearDutyCycleRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'ConceptGearDutyCycleRating':
            raise CastException('Failed to cast gear_b to ConceptGearDutyCycleRating. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_547.ConceptGearDutyCycleRating)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_concept_gear_rating(self) -> '_550.ConceptGearRating':
        '''ConceptGearRating: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'ConceptGearRating':
            raise CastException('Failed to cast gear_b to ConceptGearRating. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_550.ConceptGearRating)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_cylindrical_gear_manufacturing_config(self) -> '_610.CylindricalGearManufacturingConfig':
        '''CylindricalGearManufacturingConfig: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'CylindricalGearManufacturingConfig':
            raise CastException('Failed to cast gear_b to CylindricalGearManufacturingConfig. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_610.CylindricalGearManufacturingConfig)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_cylindrical_manufactured_gear_duty_cycle(self) -> '_614.CylindricalManufacturedGearDutyCycle':
        '''CylindricalManufacturedGearDutyCycle: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'CylindricalManufacturedGearDutyCycle':
            raise CastException('Failed to cast gear_b to CylindricalManufacturedGearDutyCycle. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_614.CylindricalManufacturedGearDutyCycle)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_cylindrical_manufactured_gear_load_case(self) -> '_615.CylindricalManufacturedGearLoadCase':
        '''CylindricalManufacturedGearLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'CylindricalManufacturedGearLoadCase':
            raise CastException('Failed to cast gear_b to CylindricalManufacturedGearLoadCase. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_615.CylindricalManufacturedGearLoadCase)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_conical_gear_manufacturing_analysis(self) -> '_796.ConicalGearManufacturingAnalysis':
        '''ConicalGearManufacturingAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'ConicalGearManufacturingAnalysis':
            raise CastException('Failed to cast gear_b to ConicalGearManufacturingAnalysis. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_796.ConicalGearManufacturingAnalysis)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_conical_gear_micro_geometry_config(self) -> '_798.ConicalGearMicroGeometryConfig':
        '''ConicalGearMicroGeometryConfig: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'ConicalGearMicroGeometryConfig':
            raise CastException('Failed to cast gear_b to ConicalGearMicroGeometryConfig. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_798.ConicalGearMicroGeometryConfig)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_conical_pinion_manufacturing_config(self) -> '_809.ConicalPinionManufacturingConfig':
        '''ConicalPinionManufacturingConfig: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'ConicalPinionManufacturingConfig':
            raise CastException('Failed to cast gear_b to ConicalPinionManufacturingConfig. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_809.ConicalPinionManufacturingConfig)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_conical_pinion_micro_geometry_config(self) -> '_810.ConicalPinionMicroGeometryConfig':
        '''ConicalPinionMicroGeometryConfig: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'ConicalPinionMicroGeometryConfig':
            raise CastException('Failed to cast gear_b to ConicalPinionMicroGeometryConfig. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_810.ConicalPinionMicroGeometryConfig)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_conical_wheel_manufacturing_config(self) -> '_817.ConicalWheelManufacturingConfig':
        '''ConicalWheelManufacturingConfig: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'ConicalWheelManufacturingConfig':
            raise CastException('Failed to cast gear_b to ConicalWheelManufacturingConfig. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_817.ConicalWheelManufacturingConfig)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_cylindrical_gear_load_distribution_analysis(self) -> '_868.CylindricalGearLoadDistributionAnalysis':
        '''CylindricalGearLoadDistributionAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'CylindricalGearLoadDistributionAnalysis':
            raise CastException('Failed to cast gear_b to CylindricalGearLoadDistributionAnalysis. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_868.CylindricalGearLoadDistributionAnalysis)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_conical_gear_load_distribution_analysis(self) -> '_877.ConicalGearLoadDistributionAnalysis':
        '''ConicalGearLoadDistributionAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'ConicalGearLoadDistributionAnalysis':
            raise CastException('Failed to cast gear_b to ConicalGearLoadDistributionAnalysis. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_877.ConicalGearLoadDistributionAnalysis)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_worm_gear_load_case(self) -> '_885.WormGearLoadCase':
        '''WormGearLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'WormGearLoadCase':
            raise CastException('Failed to cast gear_b to WormGearLoadCase. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_885.WormGearLoadCase)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_face_gear_load_case(self) -> '_887.FaceGearLoadCase':
        '''FaceGearLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'FaceGearLoadCase':
            raise CastException('Failed to cast gear_b to FaceGearLoadCase. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_887.FaceGearLoadCase)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_cylindrical_gear_load_case(self) -> '_889.CylindricalGearLoadCase':
        '''CylindricalGearLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'CylindricalGearLoadCase':
            raise CastException('Failed to cast gear_b to CylindricalGearLoadCase. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_889.CylindricalGearLoadCase)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_conical_gear_load_case(self) -> '_893.ConicalGearLoadCase':
        '''ConicalGearLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'ConicalGearLoadCase':
            raise CastException('Failed to cast gear_b to ConicalGearLoadCase. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_893.ConicalGearLoadCase)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_concept_gear_load_case(self) -> '_895.ConceptGearLoadCase':
        '''ConceptGearLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'ConceptGearLoadCase':
            raise CastException('Failed to cast gear_b to ConceptGearLoadCase. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_895.ConceptGearLoadCase)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_bevel_load_case(self) -> '_897.BevelLoadCase':
        '''BevelLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'BevelLoadCase':
            raise CastException('Failed to cast gear_b to BevelLoadCase. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_897.BevelLoadCase)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_cylindrical_gear_tiff_analysis(self) -> '_901.CylindricalGearTIFFAnalysis':
        '''CylindricalGearTIFFAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'CylindricalGearTIFFAnalysis':
            raise CastException('Failed to cast gear_b to CylindricalGearTIFFAnalysis. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_901.CylindricalGearTIFFAnalysis)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_face_gear_micro_geometry(self) -> '_962.FaceGearMicroGeometry':
        '''FaceGearMicroGeometry: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'FaceGearMicroGeometry':
            raise CastException('Failed to cast gear_b to FaceGearMicroGeometry. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_962.FaceGearMicroGeometry)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_cylindrical_gear_micro_geometry(self) -> '_1031.CylindricalGearMicroGeometry':
        '''CylindricalGearMicroGeometry: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'CylindricalGearMicroGeometry':
            raise CastException('Failed to cast gear_b to CylindricalGearMicroGeometry. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_1031.CylindricalGearMicroGeometry)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_cylindrical_gear_micro_geometry_duty_cycle(self) -> '_1032.CylindricalGearMicroGeometryDutyCycle':
        '''CylindricalGearMicroGeometryDutyCycle: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'CylindricalGearMicroGeometryDutyCycle':
            raise CastException('Failed to cast gear_b to CylindricalGearMicroGeometryDutyCycle. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_1032.CylindricalGearMicroGeometryDutyCycle)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_cylindrical_gear_fe_model(self) -> '_1115.CylindricalGearFEModel':
        '''CylindricalGearFEModel: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'CylindricalGearFEModel':
            raise CastException('Failed to cast gear_b to CylindricalGearFEModel. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_1115.CylindricalGearFEModel)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_conical_gear_fe_model(self) -> '_1117.ConicalGearFEModel':
        '''ConicalGearFEModel: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'ConicalGearFEModel':
            raise CastException('Failed to cast gear_b to ConicalGearFEModel. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_1117.ConicalGearFEModel)(self.wrapped.GearB) if self.wrapped.GearB else None
