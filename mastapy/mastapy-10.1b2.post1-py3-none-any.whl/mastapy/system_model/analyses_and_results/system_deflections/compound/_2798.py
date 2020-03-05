'''_2798.py

CylindricalGearSetCompoundSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.gears import _1989
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.cylindrical import _400, _401
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1037
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2796, _2797, _2808
from mastapy.system_model.analyses_and_results.system_deflections import _2382
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'CylindricalGearSetCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetCompoundSystemDeflection',)


class CylindricalGearSetCompoundSystemDeflection(_2808.GearSetCompoundSystemDeflection):
    '''CylindricalGearSetCompoundSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION
    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1989.CylindricalGearSet':
        '''CylindricalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1989.CylindricalGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_1989.CylindricalGearSet':
        '''CylindricalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1989.CylindricalGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def cylindrical_gear_set_rating_using_basic_ltca(self) -> '_400.CylindricalGearSetDutyCycleRating':
        '''CylindricalGearSetDutyCycleRating: 'CylindricalGearSetRatingUsingBasicLTCA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_400.CylindricalGearSetDutyCycleRating)(self.wrapped.CylindricalGearSetRatingUsingBasicLTCA) if self.wrapped.CylindricalGearSetRatingUsingBasicLTCA else None

    @property
    def cylindrical_gear_set_rating(self) -> '_400.CylindricalGearSetDutyCycleRating':
        '''CylindricalGearSetDutyCycleRating: 'CylindricalGearSetRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_400.CylindricalGearSetDutyCycleRating)(self.wrapped.CylindricalGearSetRating) if self.wrapped.CylindricalGearSetRating else None

    @property
    def load_case_rating_with_lowest_safety_factor_for_scuffing(self) -> '_401.CylindricalGearSetRating':
        '''CylindricalGearSetRating: 'LoadCaseRatingWithLowestSafetyFactorForScuffing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_401.CylindricalGearSetRating)(self.wrapped.LoadCaseRatingWithLowestSafetyFactorForScuffing) if self.wrapped.LoadCaseRatingWithLowestSafetyFactorForScuffing else None

    @property
    def basic_ltca_results(self) -> '_1037.CylindricalGearSetMicroGeometryDutyCycle':
        '''CylindricalGearSetMicroGeometryDutyCycle: 'BasicLTCAResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1037.CylindricalGearSetMicroGeometryDutyCycle)(self.wrapped.BasicLTCAResults) if self.wrapped.BasicLTCAResults else None

    @property
    def basic_ltca_results_only_first_planetary_mesh(self) -> '_1037.CylindricalGearSetMicroGeometryDutyCycle':
        '''CylindricalGearSetMicroGeometryDutyCycle: 'BasicLTCAResultsOnlyFirstPlanetaryMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1037.CylindricalGearSetMicroGeometryDutyCycle)(self.wrapped.BasicLTCAResultsOnlyFirstPlanetaryMesh) if self.wrapped.BasicLTCAResultsOnlyFirstPlanetaryMesh else None

    @property
    def advanced_ltca_results(self) -> '_1037.CylindricalGearSetMicroGeometryDutyCycle':
        '''CylindricalGearSetMicroGeometryDutyCycle: 'AdvancedLTCAResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1037.CylindricalGearSetMicroGeometryDutyCycle)(self.wrapped.AdvancedLTCAResults) if self.wrapped.AdvancedLTCAResults else None

    @property
    def advanced_ltca_results_only_first_planetary_mesh(self) -> '_1037.CylindricalGearSetMicroGeometryDutyCycle':
        '''CylindricalGearSetMicroGeometryDutyCycle: 'AdvancedLTCAResultsOnlyFirstPlanetaryMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1037.CylindricalGearSetMicroGeometryDutyCycle)(self.wrapped.AdvancedLTCAResultsOnlyFirstPlanetaryMesh) if self.wrapped.AdvancedLTCAResultsOnlyFirstPlanetaryMesh else None

    @property
    def cylindrical_gears_compound_system_deflection(self) -> 'List[_2796.CylindricalGearCompoundSystemDeflection]':
        '''List[CylindricalGearCompoundSystemDeflection]: 'CylindricalGearsCompoundSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearsCompoundSystemDeflection, constructor.new(_2796.CylindricalGearCompoundSystemDeflection))
        return value

    @property
    def cylindrical_meshes_compound_system_deflection(self) -> 'List[_2797.CylindricalGearMeshCompoundSystemDeflection]':
        '''List[CylindricalGearMeshCompoundSystemDeflection]: 'CylindricalMeshesCompoundSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalMeshesCompoundSystemDeflection, constructor.new(_2797.CylindricalGearMeshCompoundSystemDeflection))
        return value

    @property
    def load_case_analyses_ready(self) -> 'List[_2382.CylindricalGearSetSystemDeflection]':
        '''List[CylindricalGearSetSystemDeflection]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_2382.CylindricalGearSetSystemDeflection))
        return value

    @property
    def assembly_system_deflection_load_cases(self) -> 'List[_2382.CylindricalGearSetSystemDeflection]':
        '''List[CylindricalGearSetSystemDeflection]: 'AssemblySystemDeflectionLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionLoadCases, constructor.new(_2382.CylindricalGearSetSystemDeflection))
        return value
