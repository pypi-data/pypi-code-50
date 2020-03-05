'''_5682.py

FaceGearSetDynamicAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _1991
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _5943
from mastapy.system_model.analyses_and_results.dynamic_analyses import _5680, _5681, _5686
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'FaceGearSetDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetDynamicAnalysis',)


class FaceGearSetDynamicAnalysis(_5686.GearSetDynamicAnalysis):
    '''FaceGearSetDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_SET_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1991.FaceGearSet':
        '''FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1991.FaceGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_5943.FaceGearSetLoadCase':
        '''FaceGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5943.FaceGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def face_gears_dynamic_analysis(self) -> 'List[_5680.FaceGearDynamicAnalysis]':
        '''List[FaceGearDynamicAnalysis]: 'FaceGearsDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearsDynamicAnalysis, constructor.new(_5680.FaceGearDynamicAnalysis))
        return value

    @property
    def face_meshes_dynamic_analysis(self) -> 'List[_5681.FaceGearMeshDynamicAnalysis]':
        '''List[FaceGearMeshDynamicAnalysis]: 'FaceMeshesDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceMeshesDynamicAnalysis, constructor.new(_5681.FaceGearMeshDynamicAnalysis))
        return value
