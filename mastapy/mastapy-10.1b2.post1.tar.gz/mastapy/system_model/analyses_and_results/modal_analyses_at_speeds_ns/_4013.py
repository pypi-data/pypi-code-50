'''_4013.py

KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysesAtSpeeds
'''


from typing import List

from mastapy.system_model.part_model.gears import _2058
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6125
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4012, _4011, _4007
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysesAtSpeeds',)


class KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysesAtSpeeds(_4007.KlingelnbergCycloPalloidConicalGearSetModalAnalysesAtSpeeds):
    '''KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2058.KlingelnbergCycloPalloidSpiralBevelGearSet':
        '''KlingelnbergCycloPalloidSpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2058.KlingelnbergCycloPalloidSpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6125.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase':
        '''KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6125.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_modal_analyses_at_speeds(self) -> 'List[_4012.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysesAtSpeeds]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearModalAnalysesAtSpeeds]: 'KlingelnbergCycloPalloidSpiralBevelGearsModalAnalysesAtSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsModalAnalysesAtSpeeds, constructor.new(_4012.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysesAtSpeeds))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_modal_analyses_at_speeds(self) -> 'List[_4011.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysesAtSpeeds]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysesAtSpeeds]: 'KlingelnbergCycloPalloidSpiralBevelMeshesModalAnalysesAtSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesModalAnalysesAtSpeeds, constructor.new(_4011.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysesAtSpeeds))
        return value
