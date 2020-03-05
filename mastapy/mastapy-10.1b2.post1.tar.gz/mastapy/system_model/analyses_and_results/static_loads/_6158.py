'''_6158.py

SpiralBevelGearSetLoadCase
'''


from typing import List

from mastapy.system_model.part_model.gears import _2061
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6156, _6157, _6042
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SpiralBevelGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetLoadCase',)


class SpiralBevelGearSetLoadCase(_6042.BevelGearSetLoadCase):
    '''SpiralBevelGearSetLoadCase

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_SET_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2061.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2061.SpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def spiral_bevel_gears_load_case(self) -> 'List[_6156.SpiralBevelGearLoadCase]':
        '''List[SpiralBevelGearLoadCase]: 'SpiralBevelGearsLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearsLoadCase, constructor.new(_6156.SpiralBevelGearLoadCase))
        return value

    @property
    def spiral_bevel_meshes_load_case(self) -> 'List[_6157.SpiralBevelGearMeshLoadCase]':
        '''List[SpiralBevelGearMeshLoadCase]: 'SpiralBevelMeshesLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelMeshesLoadCase, constructor.new(_6157.SpiralBevelGearMeshLoadCase))
        return value
