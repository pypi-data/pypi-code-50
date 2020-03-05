'''_5295.py

WormGearSetModalAnalysesAtSpeeds
'''


from typing import List

from mastapy.system_model.part_model.gears import _1980
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2218
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _5294, _5293, _5231
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'WormGearSetModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetModalAnalysesAtSpeeds',)


class WormGearSetModalAnalysesAtSpeeds(_5231.GearSetModalAnalysesAtSpeeds):
    '''WormGearSetModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_SET_MODAL_ANALYSES_AT_SPEEDS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1980.WormGearSet':
        '''WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1980.WormGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2218.WormGearSetLoadCase':
        '''WormGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2218.WormGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def worm_gears_modal_analyses_at_speeds(self) -> 'List[_5294.WormGearModalAnalysesAtSpeeds]':
        '''List[WormGearModalAnalysesAtSpeeds]: 'WormGearsModalAnalysesAtSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearsModalAnalysesAtSpeeds, constructor.new(_5294.WormGearModalAnalysesAtSpeeds))
        return value

    @property
    def worm_meshes_modal_analyses_at_speeds(self) -> 'List[_5293.WormGearMeshModalAnalysesAtSpeeds]':
        '''List[WormGearMeshModalAnalysesAtSpeeds]: 'WormMeshesModalAnalysesAtSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormMeshesModalAnalysesAtSpeeds, constructor.new(_5293.WormGearMeshModalAnalysesAtSpeeds))
        return value
