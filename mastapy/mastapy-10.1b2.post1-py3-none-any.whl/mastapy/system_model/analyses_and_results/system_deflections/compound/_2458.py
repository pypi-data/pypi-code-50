'''_2458.py

GearCompoundSystemDeflection
'''


from mastapy.gears.rating import _337
from mastapy._internal import constructor
from mastapy.gears.rating.worm import _362
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.face import _475
from mastapy.gears.rating.cylindrical import _481
from mastapy.gears.rating.conical import _549
from mastapy.gears.rating.concept import _555
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2478
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'GearCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('GearCompoundSystemDeflection',)


class GearCompoundSystemDeflection(_2478.MountableComponentCompoundSystemDeflection):
    '''GearCompoundSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _GEAR_COMPOUND_SYSTEM_DEFLECTION
    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def duty_cycle_rating(self) -> '_337.GearDutyCycleRating':
        '''GearDutyCycleRating: 'DutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_337.GearDutyCycleRating)(self.wrapped.DutyCycleRating) if self.wrapped.DutyCycleRating else None

    @property
    def duty_cycle_rating_of_type_worm_gear_duty_cycle_rating(self) -> '_362.WormGearDutyCycleRating':
        '''WormGearDutyCycleRating: 'DutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _362.WormGearDutyCycleRating.TYPE not in self.wrapped.DutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast duty_cycle_rating to WormGearDutyCycleRating. Expected: {}.'.format(self.wrapped.DutyCycleRating.__class__.__qualname__))

        return constructor.new(_362.WormGearDutyCycleRating)(self.wrapped.DutyCycleRating) if self.wrapped.DutyCycleRating else None

    @property
    def duty_cycle_rating_of_type_face_gear_duty_cycle_rating(self) -> '_475.FaceGearDutyCycleRating':
        '''FaceGearDutyCycleRating: 'DutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _475.FaceGearDutyCycleRating.TYPE not in self.wrapped.DutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast duty_cycle_rating to FaceGearDutyCycleRating. Expected: {}.'.format(self.wrapped.DutyCycleRating.__class__.__qualname__))

        return constructor.new(_475.FaceGearDutyCycleRating)(self.wrapped.DutyCycleRating) if self.wrapped.DutyCycleRating else None

    @property
    def duty_cycle_rating_of_type_cylindrical_gear_duty_cycle_rating(self) -> '_481.CylindricalGearDutyCycleRating':
        '''CylindricalGearDutyCycleRating: 'DutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _481.CylindricalGearDutyCycleRating.TYPE not in self.wrapped.DutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast duty_cycle_rating to CylindricalGearDutyCycleRating. Expected: {}.'.format(self.wrapped.DutyCycleRating.__class__.__qualname__))

        return constructor.new(_481.CylindricalGearDutyCycleRating)(self.wrapped.DutyCycleRating) if self.wrapped.DutyCycleRating else None

    @property
    def duty_cycle_rating_of_type_conical_gear_duty_cycle_rating(self) -> '_549.ConicalGearDutyCycleRating':
        '''ConicalGearDutyCycleRating: 'DutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _549.ConicalGearDutyCycleRating.TYPE not in self.wrapped.DutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast duty_cycle_rating to ConicalGearDutyCycleRating. Expected: {}.'.format(self.wrapped.DutyCycleRating.__class__.__qualname__))

        return constructor.new(_549.ConicalGearDutyCycleRating)(self.wrapped.DutyCycleRating) if self.wrapped.DutyCycleRating else None

    @property
    def duty_cycle_rating_of_type_concept_gear_duty_cycle_rating(self) -> '_555.ConceptGearDutyCycleRating':
        '''ConceptGearDutyCycleRating: 'DutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _555.ConceptGearDutyCycleRating.TYPE not in self.wrapped.DutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast duty_cycle_rating to ConceptGearDutyCycleRating. Expected: {}.'.format(self.wrapped.DutyCycleRating.__class__.__qualname__))

        return constructor.new(_555.ConceptGearDutyCycleRating)(self.wrapped.DutyCycleRating) if self.wrapped.DutyCycleRating else None
