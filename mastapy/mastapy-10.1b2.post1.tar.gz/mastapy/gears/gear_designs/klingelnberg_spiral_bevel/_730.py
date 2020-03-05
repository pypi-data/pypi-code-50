'''_730.py

KlingelnbergCycloPalloidSpiralBevelGearMeshDesign
'''


from typing import List

from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _731, _729, _732
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.klingelnberg_conical import _738
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.KlingelnbergSpiralBevel', 'KlingelnbergCycloPalloidSpiralBevelGearMeshDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearMeshDesign',)


class KlingelnbergCycloPalloidSpiralBevelGearMeshDesign(_738.KlingelnbergConicalGearMeshDesign):
    '''KlingelnbergCycloPalloidSpiralBevelGearMeshDesign

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> '_731.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        '''KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'KlingelnbergCycloPalloidSpiralBevelGearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_731.KlingelnbergCycloPalloidSpiralBevelGearSetDesign)(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSet) if self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSet else None

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears(self) -> 'List[_729.KlingelnbergCycloPalloidSpiralBevelGearDesign]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearDesign]: 'KlingelnbergCycloPalloidSpiralBevelGears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGears, constructor.new(_729.KlingelnbergCycloPalloidSpiralBevelGearDesign))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshed_gears(self) -> 'List[_732.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign]':
        '''List[KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign]: 'KlingelnbergCycloPalloidSpiralBevelMeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshedGears, constructor.new(_732.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign))
        return value
