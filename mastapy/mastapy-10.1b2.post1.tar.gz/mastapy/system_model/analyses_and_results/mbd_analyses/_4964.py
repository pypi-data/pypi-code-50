'''_4964.py

BoltMultiBodyDynamicsAnalysis
'''


from mastapy.system_model.part_model import _1965
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6044
from mastapy.system_model.analyses_and_results.mbd_analyses import _4970
from mastapy._internal.python_net import python_net_import

_BOLT_MULTI_BODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'BoltMultiBodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltMultiBodyDynamicsAnalysis',)


class BoltMultiBodyDynamicsAnalysis(_4970.ComponentMultiBodyDynamicsAnalysis):
    '''BoltMultiBodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _BOLT_MULTI_BODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltMultiBodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1965.Bolt':
        '''Bolt: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1965.Bolt)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6044.BoltLoadCase':
        '''BoltLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6044.BoltLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
