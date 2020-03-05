'''_3758.py

ImportedFEComponentModalAnalysesAtStiffnesses
'''


from typing import List

from mastapy.system_model.part_model import _1979
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6114
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3700
from mastapy._internal.python_net import python_net_import

_IMPORTED_FE_COMPONENT_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS', 'ImportedFEComponentModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('ImportedFEComponentModalAnalysesAtStiffnesses',)


class ImportedFEComponentModalAnalysesAtStiffnesses(_3700.AbstractShaftOrHousingModalAnalysesAtStiffnesses):
    '''ImportedFEComponentModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _IMPORTED_FE_COMPONENT_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ImportedFEComponentModalAnalysesAtStiffnesses.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1979.ImportedFEComponent':
        '''ImportedFEComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1979.ImportedFEComponent)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6114.ImportedFEComponentLoadCase':
        '''ImportedFEComponentLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6114.ImportedFEComponentLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def planetaries(self) -> 'List[ImportedFEComponentModalAnalysesAtStiffnesses]':
        '''List[ImportedFEComponentModalAnalysesAtStiffnesses]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(ImportedFEComponentModalAnalysesAtStiffnesses))
        return value
