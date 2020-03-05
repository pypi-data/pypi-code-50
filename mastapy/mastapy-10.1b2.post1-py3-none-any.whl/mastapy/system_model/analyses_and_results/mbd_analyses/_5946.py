'''_5946.py

ConceptGearSetMultiBodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _1991
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2347
from mastapy.system_model.analyses_and_results.mbd_analyses import _5945, _5944, _5971
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_MULTI_BODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'ConceptGearSetMultiBodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetMultiBodyDynamicsAnalysis',)


class ConceptGearSetMultiBodyDynamicsAnalysis(_5971.GearSetMultiBodyDynamicsAnalysis):
    '''ConceptGearSetMultiBodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR_SET_MULTI_BODY_DYNAMICS_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearSetMultiBodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1991.ConceptGearSet':
        '''ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1991.ConceptGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2347.ConceptGearSetLoadCase':
        '''ConceptGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2347.ConceptGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def gears(self) -> 'List[_5945.ConceptGearMultiBodyDynamicsAnalysis]':
        '''List[ConceptGearMultiBodyDynamicsAnalysis]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Gears, constructor.new(_5945.ConceptGearMultiBodyDynamicsAnalysis))
        return value

    @property
    def concept_gears_multi_body_dynamics_analysis(self) -> 'List[_5945.ConceptGearMultiBodyDynamicsAnalysis]':
        '''List[ConceptGearMultiBodyDynamicsAnalysis]: 'ConceptGearsMultiBodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearsMultiBodyDynamicsAnalysis, constructor.new(_5945.ConceptGearMultiBodyDynamicsAnalysis))
        return value

    @property
    def concept_meshes_multi_body_dynamics_analysis(self) -> 'List[_5944.ConceptGearMeshMultiBodyDynamicsAnalysis]':
        '''List[ConceptGearMeshMultiBodyDynamicsAnalysis]: 'ConceptMeshesMultiBodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptMeshesMultiBodyDynamicsAnalysis, constructor.new(_5944.ConceptGearMeshMultiBodyDynamicsAnalysis))
        return value
