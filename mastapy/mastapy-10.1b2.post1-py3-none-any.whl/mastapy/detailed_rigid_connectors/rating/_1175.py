'''_1175.py

ShaftHubConnectionRating
'''


from mastapy._internal import constructor
from mastapy.detailed_rigid_connectors import _1125
from mastapy.detailed_rigid_connectors.splines import (
    _1128, _1131, _1135, _1138,
    _1139, _1146, _1154, _1159
)
from mastapy._internal.cast_exception import CastException
from mastapy.detailed_rigid_connectors.keyed_joints import _1176
from mastapy.detailed_rigid_connectors.interference_fits import _1184
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_RATING = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Rating', 'ShaftHubConnectionRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHubConnectionRating',)


class ShaftHubConnectionRating(_1.APIBase):
    '''ShaftHubConnectionRating

    This is a mastapy class.
    '''

    TYPE = _SHAFT_HUB_CONNECTION_RATING
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftHubConnectionRating.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def additional_rating_information(self) -> 'str':
        '''str: 'AdditionalRatingInformation' is the original name of this property.'''

        return self.wrapped.AdditionalRatingInformation

    @additional_rating_information.setter
    def additional_rating_information(self, value: 'str'):
        self.wrapped.AdditionalRatingInformation = str(value) if value else None

    @property
    def joint_design(self) -> '_1125.DetailedRigidConnectorDesign':
        '''DetailedRigidConnectorDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1125.DetailedRigidConnectorDesign)(self.wrapped.JointDesign) if self.wrapped.JointDesign else None

    @property
    def joint_design_of_type_custom_spline_joint_design(self) -> '_1128.CustomSplineJointDesign':
        '''CustomSplineJointDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1128.CustomSplineJointDesign.TYPE not in self.wrapped.JointDesign.__class__.__mro__:
            raise CastException('Failed to cast joint_design to CustomSplineJointDesign. Expected: {}.'.format(self.wrapped.JointDesign.__class__.__qualname__))

        return constructor.new(_1128.CustomSplineJointDesign)(self.wrapped.JointDesign) if self.wrapped.JointDesign else None

    @property
    def joint_design_of_type_din5480_spline_joint_design(self) -> '_1131.DIN5480SplineJointDesign':
        '''DIN5480SplineJointDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1131.DIN5480SplineJointDesign.TYPE not in self.wrapped.JointDesign.__class__.__mro__:
            raise CastException('Failed to cast joint_design to DIN5480SplineJointDesign. Expected: {}.'.format(self.wrapped.JointDesign.__class__.__qualname__))

        return constructor.new(_1131.DIN5480SplineJointDesign)(self.wrapped.JointDesign) if self.wrapped.JointDesign else None

    @property
    def joint_design_of_type_gbt3478_spline_joint_design(self) -> '_1135.GBT3478SplineJointDesign':
        '''GBT3478SplineJointDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1135.GBT3478SplineJointDesign.TYPE not in self.wrapped.JointDesign.__class__.__mro__:
            raise CastException('Failed to cast joint_design to GBT3478SplineJointDesign. Expected: {}.'.format(self.wrapped.JointDesign.__class__.__qualname__))

        return constructor.new(_1135.GBT3478SplineJointDesign)(self.wrapped.JointDesign) if self.wrapped.JointDesign else None

    @property
    def joint_design_of_type_iso4156_spline_joint_design(self) -> '_1138.ISO4156SplineJointDesign':
        '''ISO4156SplineJointDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1138.ISO4156SplineJointDesign.TYPE not in self.wrapped.JointDesign.__class__.__mro__:
            raise CastException('Failed to cast joint_design to ISO4156SplineJointDesign. Expected: {}.'.format(self.wrapped.JointDesign.__class__.__qualname__))

        return constructor.new(_1138.ISO4156SplineJointDesign)(self.wrapped.JointDesign) if self.wrapped.JointDesign else None

    @property
    def joint_design_of_type_jisb1603_spline_joint_design(self) -> '_1139.JISB1603SplineJointDesign':
        '''JISB1603SplineJointDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1139.JISB1603SplineJointDesign.TYPE not in self.wrapped.JointDesign.__class__.__mro__:
            raise CastException('Failed to cast joint_design to JISB1603SplineJointDesign. Expected: {}.'.format(self.wrapped.JointDesign.__class__.__qualname__))

        return constructor.new(_1139.JISB1603SplineJointDesign)(self.wrapped.JointDesign) if self.wrapped.JointDesign else None

    @property
    def joint_design_of_type_sae_spline_joint_design(self) -> '_1146.SAESplineJointDesign':
        '''SAESplineJointDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1146.SAESplineJointDesign.TYPE not in self.wrapped.JointDesign.__class__.__mro__:
            raise CastException('Failed to cast joint_design to SAESplineJointDesign. Expected: {}.'.format(self.wrapped.JointDesign.__class__.__qualname__))

        return constructor.new(_1146.SAESplineJointDesign)(self.wrapped.JointDesign) if self.wrapped.JointDesign else None

    @property
    def joint_design_of_type_spline_joint_design(self) -> '_1154.SplineJointDesign':
        '''SplineJointDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1154.SplineJointDesign.TYPE not in self.wrapped.JointDesign.__class__.__mro__:
            raise CastException('Failed to cast joint_design to SplineJointDesign. Expected: {}.'.format(self.wrapped.JointDesign.__class__.__qualname__))

        return constructor.new(_1154.SplineJointDesign)(self.wrapped.JointDesign) if self.wrapped.JointDesign else None

    @property
    def joint_design_of_type_standard_spline_joint_design(self) -> '_1159.StandardSplineJointDesign':
        '''StandardSplineJointDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1159.StandardSplineJointDesign.TYPE not in self.wrapped.JointDesign.__class__.__mro__:
            raise CastException('Failed to cast joint_design to StandardSplineJointDesign. Expected: {}.'.format(self.wrapped.JointDesign.__class__.__qualname__))

        return constructor.new(_1159.StandardSplineJointDesign)(self.wrapped.JointDesign) if self.wrapped.JointDesign else None

    @property
    def joint_design_of_type_keyed_joint_design(self) -> '_1176.KeyedJointDesign':
        '''KeyedJointDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1176.KeyedJointDesign.TYPE not in self.wrapped.JointDesign.__class__.__mro__:
            raise CastException('Failed to cast joint_design to KeyedJointDesign. Expected: {}.'.format(self.wrapped.JointDesign.__class__.__qualname__))

        return constructor.new(_1176.KeyedJointDesign)(self.wrapped.JointDesign) if self.wrapped.JointDesign else None

    @property
    def joint_design_of_type_interference_fit_design(self) -> '_1184.InterferenceFitDesign':
        '''InterferenceFitDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1184.InterferenceFitDesign.TYPE not in self.wrapped.JointDesign.__class__.__mro__:
            raise CastException('Failed to cast joint_design to InterferenceFitDesign. Expected: {}.'.format(self.wrapped.JointDesign.__class__.__qualname__))

        return constructor.new(_1184.InterferenceFitDesign)(self.wrapped.JointDesign) if self.wrapped.JointDesign else None
