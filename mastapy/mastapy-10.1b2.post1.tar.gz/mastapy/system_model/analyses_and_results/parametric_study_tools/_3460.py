'''_3460.py

ClutchConnectionParametricStudyTool
'''


from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _1873
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6045
from mastapy.system_model.analyses_and_results.system_deflections import _2204
from mastapy.system_model.analyses_and_results.parametric_study_tools import _3476
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'ClutchConnectionParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchConnectionParametricStudyTool',)


class ClutchConnectionParametricStudyTool(_3476.CouplingConnectionParametricStudyTool):
    '''ClutchConnectionParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_CONNECTION_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchConnectionParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def connection_design(self) -> '_1873.ClutchConnection':
        '''ClutchConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1873.ClutchConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_6045.ClutchConnectionLoadCase':
        '''ClutchConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6045.ClutchConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2204.ClutchConnectionSystemDeflection]':
        '''List[ClutchConnectionSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionSystemDeflectionResults, constructor.new(_2204.ClutchConnectionSystemDeflection))
        return value
