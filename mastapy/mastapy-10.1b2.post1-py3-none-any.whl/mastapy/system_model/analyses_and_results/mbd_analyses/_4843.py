'''_4843.py

ClutchMultiBodyDynamicsAnalysis
'''


from mastapy.system_model.part_model.couplings import _2036
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _5899
from mastapy.system_model.analyses_and_results.mbd_analyses import _4841, _4860
from mastapy._internal.python_net import python_net_import

_CLUTCH_MULTI_BODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'ClutchMultiBodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchMultiBodyDynamicsAnalysis',)


class ClutchMultiBodyDynamicsAnalysis(_4860.CouplingMultiBodyDynamicsAnalysis):
    '''ClutchMultiBodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_MULTI_BODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchMultiBodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2036.Clutch':
        '''Clutch: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2036.Clutch)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_5899.ClutchLoadCase':
        '''ClutchLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5899.ClutchLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def clutch_connection(self) -> '_4841.ClutchConnectionMultiBodyDynamicsAnalysis':
        '''ClutchConnectionMultiBodyDynamicsAnalysis: 'ClutchConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_4841.ClutchConnectionMultiBodyDynamicsAnalysis)(self.wrapped.ClutchConnection) if self.wrapped.ClutchConnection else None
