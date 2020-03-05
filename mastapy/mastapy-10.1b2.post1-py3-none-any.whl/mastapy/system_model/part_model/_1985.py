'''_1985.py

OilLevelSpecification
'''


from mastapy._internal import constructor
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.part_model import _1971
from mastapy.materials.efficiency import _106
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_OIL_LEVEL_SPECIFICATION = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'OilLevelSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('OilLevelSpecification',)


class OilLevelSpecification(_1.APIBase):
    '''OilLevelSpecification

    This is a mastapy class.
    '''

    TYPE = _OIL_LEVEL_SPECIFICATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'OilLevelSpecification.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def oil_level_specified(self) -> 'bool':
        '''bool: 'OilLevelSpecified' is the original name of this property.'''

        return self.wrapped.OilLevelSpecified

    @oil_level_specified.setter
    def oil_level_specified(self, value: 'bool'):
        self.wrapped.OilLevelSpecified = bool(value) if value else False

    @property
    def oil_level_reference_datum(self) -> 'list_with_selected_item.ListWithSelectedItem_Datum':
        '''list_with_selected_item.ListWithSelectedItem_Datum: 'OilLevelReferenceDatum' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_Datum)(self.wrapped.OilLevelReferenceDatum) if self.wrapped.OilLevelReferenceDatum else None

    @oil_level_reference_datum.setter
    def oil_level_reference_datum(self, value: 'list_with_selected_item.ListWithSelectedItem_Datum.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Datum.TYPE
        enclosed_type = list_with_selected_item.ListWithSelectedItem_Datum.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value else None)
        self.wrapped.OilLevelReferenceDatum = value

    @property
    def oil_level(self) -> 'float':
        '''float: 'OilLevel' is the original name of this property.'''

        return self.wrapped.OilLevel

    @oil_level.setter
    def oil_level(self, value: 'float'):
        self.wrapped.OilLevel = float(value) if value else 0.0

    @property
    def oil_volume_specification(self) -> '_106.OilVolumeSpecification':
        '''OilVolumeSpecification: 'OilVolumeSpecification' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_106.OilVolumeSpecification)(self.wrapped.OilVolumeSpecification) if self.wrapped.OilVolumeSpecification else None
