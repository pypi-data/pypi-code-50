'''_486.py

ConicalGearMeshRating
'''


from typing import List

from mastapy.gears.load_case.conical import _370
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.conical import _522
from mastapy.gears.rating import _339
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Conical', 'ConicalGearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearMeshRating',)


class ConicalGearMeshRating(_339.GearMeshRating):
    '''ConicalGearMeshRating

    This is a mastapy class.
    '''

    TYPE = _CONICAL_GEAR_MESH_RATING
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def mesh_load_case(self) -> '_370.ConicalMeshLoadCase':
        '''ConicalMeshLoadCase: 'MeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_370.ConicalMeshLoadCase)(self.wrapped.MeshLoadCase) if self.wrapped.MeshLoadCase else None

    @property
    def conical_mesh_load_case(self) -> '_370.ConicalMeshLoadCase':
        '''ConicalMeshLoadCase: 'ConicalMeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_370.ConicalMeshLoadCase)(self.wrapped.ConicalMeshLoadCase) if self.wrapped.ConicalMeshLoadCase else None

    @property
    def meshed_gears(self) -> 'List[_522.ConicalMeshedGearRating]':
        '''List[ConicalMeshedGearRating]: 'MeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeshedGears, constructor.new(_522.ConicalMeshedGearRating))
        return value
