'''_6092.py

FaceGearMeshLoadCase
'''


from mastapy.system_model.connections_and_sockets.gears import _1851
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6098
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'FaceGearMeshLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshLoadCase',)


class FaceGearMeshLoadCase(_6098.GearMeshLoadCase):
    '''FaceGearMeshLoadCase

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_MESH_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMeshLoadCase.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def connection_design(self) -> '_1851.FaceGearMesh':
        '''FaceGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1851.FaceGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None
