'''_1175.py

CoordinateSystemEditor
'''


from typing import Callable

from mastapy._internal import constructor, conversion
from mastapy.math_utility import (
    _1177, _1194, _1176, _1174
)
from mastapy.scripting import _6321
from mastapy._internal.vector_3d import Vector3D
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_COORDINATE_SYSTEM_EDITOR = python_net_import('SMT.MastaAPI.MathUtility', 'CoordinateSystemEditor')


__docformat__ = 'restructuredtext en'
__all__ = ('CoordinateSystemEditor',)


class CoordinateSystemEditor(_1.APIBase):
    '''CoordinateSystemEditor

    This is a mastapy class.
    '''

    TYPE = _COORDINATE_SYSTEM_EDITOR

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CoordinateSystemEditor.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def has_modified_coordinate_system(self) -> 'bool':
        '''bool: 'HasModifiedCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.HasModifiedCoordinateSystem

    @property
    def has_modified_coordinate_system_rotation(self) -> 'bool':
        '''bool: 'HasModifiedCoordinateSystemRotation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.HasModifiedCoordinateSystemRotation

    @property
    def has_modified_coordinate_system_translation(self) -> 'bool':
        '''bool: 'HasModifiedCoordinateSystemTranslation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.HasModifiedCoordinateSystemTranslation

    @property
    def has_rotation(self) -> 'bool':
        '''bool: 'HasRotation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.HasRotation

    @property
    def has_translation(self) -> 'bool':
        '''bool: 'HasTranslation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.HasTranslation

    @property
    def coordinate_system_for_rotation_origin(self) -> '_1177.CoordinateSystemForRotationOrigin':
        '''CoordinateSystemForRotationOrigin: 'CoordinateSystemForRotationOrigin' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.CoordinateSystemForRotationOrigin)
        return constructor.new(_1177.CoordinateSystemForRotationOrigin)(value) if value else None

    @coordinate_system_for_rotation_origin.setter
    def coordinate_system_for_rotation_origin(self, value: '_1177.CoordinateSystemForRotationOrigin'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.CoordinateSystemForRotationOrigin = value

    @property
    def rotation_angle(self) -> 'float':
        '''float: 'RotationAngle' is the original name of this property.'''

        return self.wrapped.RotationAngle

    @rotation_angle.setter
    def rotation_angle(self, value: 'float'):
        self.wrapped.RotationAngle = float(value) if value else 0.0

    @property
    def rotation_axis(self) -> '_1194.RotationAxis':
        '''RotationAxis: 'RotationAxis' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.RotationAxis)
        return constructor.new(_1194.RotationAxis)(value) if value else None

    @rotation_axis.setter
    def rotation_axis(self, value: '_1194.RotationAxis'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.RotationAxis = value

    @property
    def coordinate_system_for_rotation_axes(self) -> '_1176.CoordinateSystemForRotation':
        '''CoordinateSystemForRotation: 'CoordinateSystemForRotationAxes' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.CoordinateSystemForRotationAxes)
        return constructor.new(_1176.CoordinateSystemForRotation)(value) if value else None

    @coordinate_system_for_rotation_axes.setter
    def coordinate_system_for_rotation_axes(self, value: '_1176.CoordinateSystemForRotation'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.CoordinateSystemForRotationAxes = value

    @property
    def apply_rotation(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'ApplyRotation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ApplyRotation

    @property
    def update_origin(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'UpdateOrigin' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.UpdateOrigin

    @property
    def cancel_pending_changes(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'CancelPendingChanges' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.CancelPendingChanges

    @property
    def align_to_world_coordinate_system(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'AlignToWorldCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AlignToWorldCoordinateSystem

    @property
    def set_local_origin_to_world_origin(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'SetLocalOriginToWorldOrigin' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SetLocalOriginToWorldOrigin

    @property
    def show_preview(self) -> 'bool':
        '''bool: 'ShowPreview' is the original name of this property.'''

        return self.wrapped.ShowPreview

    @show_preview.setter
    def show_preview(self, value: 'bool'):
        self.wrapped.ShowPreview = bool(value) if value else False

    @property
    def containing_assembly_image(self) -> '_6321.SMTBitmap':
        '''SMTBitmap: 'ContainingAssemblyImage' is the original name of this property.'''

        return constructor.new(_6321.SMTBitmap)(self.wrapped.ContainingAssemblyImage) if self.wrapped.ContainingAssemblyImage else None

    @containing_assembly_image.setter
    def containing_assembly_image(self, value: '_6321.SMTBitmap'):
        value = value.wrapped if value else None
        self.wrapped.ContainingAssemblyImage = value

    @property
    def containing_assembly_text(self) -> 'str':
        '''str: 'ContainingAssemblyText' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ContainingAssemblyText

    @property
    def root_assembly_text(self) -> 'str':
        '''str: 'RootAssemblyText' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RootAssemblyText

    @property
    def root_assembly_image(self) -> '_6321.SMTBitmap':
        '''SMTBitmap: 'RootAssemblyImage' is the original name of this property.'''

        return constructor.new(_6321.SMTBitmap)(self.wrapped.RootAssemblyImage) if self.wrapped.RootAssemblyImage else None

    @root_assembly_image.setter
    def root_assembly_image(self, value: '_6321.SMTBitmap'):
        value = value.wrapped if value else None
        self.wrapped.RootAssemblyImage = value

    @property
    def coordinate_system(self) -> '_1174.CoordinateSystem3D':
        '''CoordinateSystem3D: 'CoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1174.CoordinateSystem3D)(self.wrapped.CoordinateSystem) if self.wrapped.CoordinateSystem else None

    @property
    def modified_coordinate_system_for_rotation(self) -> '_1174.CoordinateSystem3D':
        '''CoordinateSystem3D: 'ModifiedCoordinateSystemForRotation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1174.CoordinateSystem3D)(self.wrapped.ModifiedCoordinateSystemForRotation) if self.wrapped.ModifiedCoordinateSystemForRotation else None

    @property
    def modified_coordinate_system_for_translation(self) -> '_1174.CoordinateSystem3D':
        '''CoordinateSystem3D: 'ModifiedCoordinateSystemForTranslation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1174.CoordinateSystem3D)(self.wrapped.ModifiedCoordinateSystemForTranslation) if self.wrapped.ModifiedCoordinateSystemForTranslation else None

    @property
    def translation(self) -> 'Vector3D':
        '''Vector3D: 'Translation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_vector3d(self.wrapped.Translation)
        return value

    @property
    def rotation_origin(self) -> 'Vector3D':
        '''Vector3D: 'RotationOrigin' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_vector3d(self.wrapped.RotationOrigin)
        return value

    @property
    def specified_rotation_axis(self) -> 'Vector3D':
        '''Vector3D: 'SpecifiedRotationAxis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_vector3d(self.wrapped.SpecifiedRotationAxis)
        return value
