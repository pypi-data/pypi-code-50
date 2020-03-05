'''_3888.py

KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtStiffnesses
'''


from typing import List

from mastapy.system_model.part_model.gears import _2056
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns.compound import _3886, _3887, _3885
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3765
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS.Compound', 'KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtStiffnesses',)


class KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtStiffnesses(_3885.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysesAtStiffnesses):
    '''KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtStiffnesses.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2056.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2056.KlingelnbergCycloPalloidHypoidGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2056.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2056.KlingelnbergCycloPalloidHypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_compound_modal_analyses_at_stiffnesses(self) -> 'List[_3886.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysesAtStiffnesses]':
        '''List[KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysesAtStiffnesses]: 'KlingelnbergCycloPalloidHypoidGearsCompoundModalAnalysesAtStiffnesses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearsCompoundModalAnalysesAtStiffnesses, constructor.new(_3886.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_compound_modal_analyses_at_stiffnesses(self) -> 'List[_3887.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysesAtStiffnesses]':
        '''List[KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysesAtStiffnesses]: 'KlingelnbergCycloPalloidHypoidMeshesCompoundModalAnalysesAtStiffnesses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCompoundModalAnalysesAtStiffnesses, constructor.new(_3887.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def load_case_analyses_ready(self) -> 'List[_3765.KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtStiffnesses]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtStiffnesses]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_3765.KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtStiffnesses))
        return value

    @property
    def assembly_modal_analyses_at_stiffnesses_load_cases(self) -> 'List[_3765.KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtStiffnesses]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtStiffnesses]: 'AssemblyModalAnalysesAtStiffnessesLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyModalAnalysesAtStiffnessesLoadCases, constructor.new(_3765.KlingelnbergCycloPalloidHypoidGearSetModalAnalysesAtStiffnesses))
        return value
