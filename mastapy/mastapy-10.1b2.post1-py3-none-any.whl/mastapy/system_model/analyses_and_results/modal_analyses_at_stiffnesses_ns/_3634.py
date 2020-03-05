'''_3634.py

ConceptGearSetModalAnalysesAtStiffnesses
'''


from typing import List

from mastapy.system_model.part_model.gears import _1984
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _5907
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3633, _3632, _3659
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS', 'ConceptGearSetModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetModalAnalysesAtStiffnesses',)


class ConceptGearSetModalAnalysesAtStiffnesses(_3659.GearSetModalAnalysesAtStiffnesses):
    '''ConceptGearSetModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR_SET_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearSetModalAnalysesAtStiffnesses.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1984.ConceptGearSet':
        '''ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1984.ConceptGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_5907.ConceptGearSetLoadCase':
        '''ConceptGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5907.ConceptGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def concept_gears_modal_analyses_at_stiffnesses(self) -> 'List[_3633.ConceptGearModalAnalysesAtStiffnesses]':
        '''List[ConceptGearModalAnalysesAtStiffnesses]: 'ConceptGearsModalAnalysesAtStiffnesses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearsModalAnalysesAtStiffnesses, constructor.new(_3633.ConceptGearModalAnalysesAtStiffnesses))
        return value

    @property
    def concept_meshes_modal_analyses_at_stiffnesses(self) -> 'List[_3632.ConceptGearMeshModalAnalysesAtStiffnesses]':
        '''List[ConceptGearMeshModalAnalysesAtStiffnesses]: 'ConceptMeshesModalAnalysesAtStiffnesses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptMeshesModalAnalysesAtStiffnesses, constructor.new(_3632.ConceptGearMeshModalAnalysesAtStiffnesses))
        return value
