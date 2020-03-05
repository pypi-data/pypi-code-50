'''_749.py

FaceGearMicroGeometry
'''


from mastapy.gears.gear_designs.face import _745
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _837
from mastapy.gears.analysis import _943
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Face', 'FaceGearMicroGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMicroGeometry',)


class FaceGearMicroGeometry(_943.GearImplementationDetail):
    '''FaceGearMicroGeometry

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_MICRO_GEOMETRY

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMicroGeometry.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def face_gear(self) -> '_745.FaceGearDesign':
        '''FaceGearDesign: 'FaceGear' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_745.FaceGearDesign)(self.wrapped.FaceGear) if self.wrapped.FaceGear else None

    @property
    def micro_geometry(self) -> '_837.CylindricalGearMicroGeometry':
        '''CylindricalGearMicroGeometry: 'MicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_837.CylindricalGearMicroGeometry)(self.wrapped.MicroGeometry) if self.wrapped.MicroGeometry else None
