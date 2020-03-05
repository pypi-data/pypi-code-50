'''_5962.py

DatumMultiBodyDynamicsAnalysis
'''


from mastapy.system_model.part_model import _1926
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _2324
from mastapy.system_model.analyses_and_results.mbd_analyses import _5940
from mastapy._internal.python_net import python_net_import

_DATUM_MULTI_BODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'DatumMultiBodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumMultiBodyDynamicsAnalysis',)


class DatumMultiBodyDynamicsAnalysis(_5940.ComponentMultiBodyDynamicsAnalysis):
    '''DatumMultiBodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _DATUM_MULTI_BODY_DYNAMICS_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'DatumMultiBodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1926.Datum':
        '''Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1926.Datum)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_2324.DatumLoadCase':
        '''DatumLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2324.DatumLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
