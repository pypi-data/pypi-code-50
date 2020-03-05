'''_460.py

FaceGearMeshRating
'''


from typing import List

from mastapy.gears import _299
from mastapy._internal import constructor, conversion
from mastapy.gears.load_case.face import _365
from mastapy.gears.rating.face import _399, _461
from mastapy.gears.rating.cylindrical.iso6336 import _475
from mastapy.gears.gear_designs.face import _476
from mastapy.gears.rating import _336
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Face', 'FaceGearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshRating',)


class FaceGearMeshRating(_336.GearMeshRating):
    '''FaceGearMeshRating

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_MESH_RATING
    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def active_flank(self) -> '_299.GearFlanks':
        '''GearFlanks: 'ActiveFlank' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_enum(self.wrapped.ActiveFlank)
        return constructor.new(_299.GearFlanks)(value) if value else None

    @property
    def mesh_load_case(self) -> '_365.FaceMeshLoadCase':
        '''FaceMeshLoadCase: 'MeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_365.FaceMeshLoadCase)(self.wrapped.MeshLoadCase) if self.wrapped.MeshLoadCase else None

    @property
    def gear_set_rating(self) -> '_399.FaceGearSetRating':
        '''FaceGearSetRating: 'GearSetRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_399.FaceGearSetRating)(self.wrapped.GearSetRating) if self.wrapped.GearSetRating else None

    @property
    def mesh_single_flank_rating(self) -> '_475.ISO63362006MeshSingleFlankRating':
        '''ISO63362006MeshSingleFlankRating: 'MeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_475.ISO63362006MeshSingleFlankRating)(self.wrapped.MeshSingleFlankRating) if self.wrapped.MeshSingleFlankRating else None

    @property
    def face_gear_mesh(self) -> '_476.FaceGearMeshDesign':
        '''FaceGearMeshDesign: 'FaceGearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_476.FaceGearMeshDesign)(self.wrapped.FaceGearMesh) if self.wrapped.FaceGearMesh else None

    @property
    def face_gear_ratings(self) -> 'List[_461.FaceGearRating]':
        '''List[FaceGearRating]: 'FaceGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearRatings, constructor.new(_461.FaceGearRating))
        return value
