'''_5427.py

CylindricalGearMeshSingleMeshWhineAnalysis
'''


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _1849
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6071
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5437
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'CylindricalGearMeshSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshSingleMeshWhineAnalysis',)


class CylindricalGearMeshSingleMeshWhineAnalysis(_5437.GearMeshSingleMeshWhineAnalysis):
    '''CylindricalGearMeshSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_MESH_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def connection_design(self) -> '_1849.CylindricalGearMesh':
        '''CylindricalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1849.CylindricalGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_6071.CylindricalGearMeshLoadCase':
        '''CylindricalGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6071.CylindricalGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None

    @property
    def planetaries(self) -> 'List[CylindricalGearMeshSingleMeshWhineAnalysis]':
        '''List[CylindricalGearMeshSingleMeshWhineAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(CylindricalGearMeshSingleMeshWhineAnalysis))
        return value
