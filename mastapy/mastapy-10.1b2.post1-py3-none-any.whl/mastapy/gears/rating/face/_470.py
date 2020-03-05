'''_470.py

FaceGearMeshRating
'''


from typing import List

from mastapy.gears import _301
from mastapy._internal import constructor, conversion
from mastapy.gears.load_case.face import _368
from mastapy.gears.rating.face import _424, _471
from mastapy.gears.rating.cylindrical.iso6336 import _493
from mastapy.gears.gear_designs.face import _558
from mastapy.gears.rating import _339
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Face', 'FaceGearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshRating',)


class FaceGearMeshRating(_339.GearMeshRating):
    '''FaceGearMeshRating

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_MESH_RATING
    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def active_flank(self) -> '_301.GearFlanks':
        '''GearFlanks: 'ActiveFlank' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_enum(self.wrapped.ActiveFlank)
        return constructor.new(_301.GearFlanks)(value) if value else None

    @property
    def mesh_load_case(self) -> '_368.FaceMeshLoadCase':
        '''FaceMeshLoadCase: 'MeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_368.FaceMeshLoadCase)(self.wrapped.MeshLoadCase) if self.wrapped.MeshLoadCase else None

    @property
    def gear_set_rating(self) -> '_424.FaceGearSetRating':
        '''FaceGearSetRating: 'GearSetRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_424.FaceGearSetRating)(self.wrapped.GearSetRating) if self.wrapped.GearSetRating else None

    @property
    def mesh_single_flank_rating(self) -> '_493.ISO63362006MeshSingleFlankRating':
        '''ISO63362006MeshSingleFlankRating: 'MeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_493.ISO63362006MeshSingleFlankRating)(self.wrapped.MeshSingleFlankRating) if self.wrapped.MeshSingleFlankRating else None

    @property
    def face_gear_mesh(self) -> '_558.FaceGearMeshDesign':
        '''FaceGearMeshDesign: 'FaceGearMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_558.FaceGearMeshDesign)(self.wrapped.FaceGearMesh) if self.wrapped.FaceGearMesh else None

    @property
    def face_gear_ratings(self) -> 'List[_471.FaceGearRating]':
        '''List[FaceGearRating]: 'FaceGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearRatings, constructor.new(_471.FaceGearRating))
        return value
