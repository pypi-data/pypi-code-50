'''_4344.py

DatumSingleMeshWhineAnalysis
'''


from mastapy.system_model.part_model import _1926
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _2282
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _4342
from mastapy._internal.python_net import python_net_import

_DATUM_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'DatumSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumSingleMeshWhineAnalysis',)


class DatumSingleMeshWhineAnalysis(_4342.ComponentSingleMeshWhineAnalysis):
    '''DatumSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _DATUM_SINGLE_MESH_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'DatumSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1926.Datum':
        '''Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1926.Datum)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_2282.DatumLoadCase':
        '''DatumLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2282.DatumLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
