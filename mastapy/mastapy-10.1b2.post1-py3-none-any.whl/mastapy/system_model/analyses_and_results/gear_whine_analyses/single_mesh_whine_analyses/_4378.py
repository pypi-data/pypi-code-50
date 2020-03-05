'''_4378.py

CylindricalGearSetSingleMeshWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _1995
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2338
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _4377, _4327, _4381
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'CylindricalGearSetSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetSingleMeshWhineAnalysis',)


class CylindricalGearSetSingleMeshWhineAnalysis(_4381.GearSetSingleMeshWhineAnalysis):
    '''CylindricalGearSetSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_SET_SINGLE_MESH_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1995.CylindricalGearSet':
        '''CylindricalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1995.CylindricalGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2338.CylindricalGearSetLoadCase':
        '''CylindricalGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2338.CylindricalGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def cylindrical_gears_single_mesh_whine_analysis(self) -> 'List[_4377.CylindricalGearSingleMeshWhineAnalysis]':
        '''List[CylindricalGearSingleMeshWhineAnalysis]: 'CylindricalGearsSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearsSingleMeshWhineAnalysis, constructor.new(_4377.CylindricalGearSingleMeshWhineAnalysis))
        return value

    @property
    def cylindrical_meshes_single_mesh_whine_analysis(self) -> 'List[_4327.CylindricalGearMeshSingleMeshWhineAnalysis]':
        '''List[CylindricalGearMeshSingleMeshWhineAnalysis]: 'CylindricalMeshesSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalMeshesSingleMeshWhineAnalysis, constructor.new(_4327.CylindricalGearMeshSingleMeshWhineAnalysis))
        return value
