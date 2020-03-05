'''_748.py

FaceGearMeshMicroGeometry
'''


from typing import List

from mastapy.gears.gear_designs.face import _747, _752, _749
from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _947
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Face', 'FaceGearMeshMicroGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshMicroGeometry',)


class FaceGearMeshMicroGeometry(_947.GearMeshImplementationDetail):
    '''FaceGearMeshMicroGeometry

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_MESH_MICRO_GEOMETRY

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMeshMicroGeometry.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def face_mesh(self) -> '_747.FaceGearMeshDesign':
        '''FaceGearMeshDesign: 'FaceMesh' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_747.FaceGearMeshDesign)(self.wrapped.FaceMesh) if self.wrapped.FaceMesh else None

    @property
    def face_gear_set_micro_geometry(self) -> '_752.FaceGearSetMicroGeometry':
        '''FaceGearSetMicroGeometry: 'FaceGearSetMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_752.FaceGearSetMicroGeometry)(self.wrapped.FaceGearSetMicroGeometry) if self.wrapped.FaceGearSetMicroGeometry else None

    @property
    def face_gear_micro_geometries(self) -> 'List[_749.FaceGearMicroGeometry]':
        '''List[FaceGearMicroGeometry]: 'FaceGearMicroGeometries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearMicroGeometries, constructor.new(_749.FaceGearMicroGeometry))
        return value
