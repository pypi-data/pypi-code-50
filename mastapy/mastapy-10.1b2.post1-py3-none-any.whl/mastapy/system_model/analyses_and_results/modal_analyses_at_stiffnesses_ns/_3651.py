'''_3651.py

DatumModalAnalysesAtStiffnesses
'''


from mastapy.system_model.part_model import _1918
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _5929
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3628
from mastapy._internal.python_net import python_net_import

_DATUM_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS', 'DatumModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumModalAnalysesAtStiffnesses',)


class DatumModalAnalysesAtStiffnesses(_3628.ComponentModalAnalysesAtStiffnesses):
    '''DatumModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _DATUM_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DatumModalAnalysesAtStiffnesses.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1918.Datum':
        '''Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1918.Datum)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_5929.DatumLoadCase':
        '''DatumLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5929.DatumLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
