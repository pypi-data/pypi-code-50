'''_4301.py

ConceptGearSetSingleMeshWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _1991
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2347
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _4300, _4258, _4318
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'ConceptGearSetSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetSingleMeshWhineAnalysis',)


class ConceptGearSetSingleMeshWhineAnalysis(_4318.GearSetSingleMeshWhineAnalysis):
    '''ConceptGearSetSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR_SET_SINGLE_MESH_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearSetSingleMeshWhineAnalysis.TYPE'):
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
    def concept_gears_single_mesh_whine_analysis(self) -> 'List[_4300.ConceptGearSingleMeshWhineAnalysis]':
        '''List[ConceptGearSingleMeshWhineAnalysis]: 'ConceptGearsSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearsSingleMeshWhineAnalysis, constructor.new(_4300.ConceptGearSingleMeshWhineAnalysis))
        return value

    @property
    def concept_meshes_single_mesh_whine_analysis(self) -> 'List[_4258.ConceptGearMeshSingleMeshWhineAnalysis]':
        '''List[ConceptGearMeshSingleMeshWhineAnalysis]: 'ConceptMeshesSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptMeshesSingleMeshWhineAnalysis, constructor.new(_4258.ConceptGearMeshSingleMeshWhineAnalysis))
        return value
