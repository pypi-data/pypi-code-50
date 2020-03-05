'''_5335.py

RollingRingConnectionSingleMeshWhineAnalysis
'''


from typing import List

from mastapy.system_model.connections_and_sockets import _1781
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _5994
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5312
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'RollingRingConnectionSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingConnectionSingleMeshWhineAnalysis',)


class RollingRingConnectionSingleMeshWhineAnalysis(_5312.InterMountableComponentConnectionSingleMeshWhineAnalysis):
    '''RollingRingConnectionSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _ROLLING_RING_CONNECTION_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRingConnectionSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def connection_design(self) -> '_1781.RollingRingConnection':
        '''RollingRingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1781.RollingRingConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_5994.RollingRingConnectionLoadCase':
        '''RollingRingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5994.RollingRingConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None

    @property
    def planetaries(self) -> 'List[RollingRingConnectionSingleMeshWhineAnalysis]':
        '''List[RollingRingConnectionSingleMeshWhineAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(RollingRingConnectionSingleMeshWhineAnalysis))
        return value
