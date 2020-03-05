'''_1776.py

DutyCycleImporter
'''


from typing import List

from mastapy.system_model import _1780, _1777
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _1991, _1990
from mastapy.system_model.analyses_and_results.load_case_groups import _5215
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_IMPORTER = python_net_import('SMT.MastaAPI.SystemModel', 'DutyCycleImporter')


__docformat__ = 'restructuredtext en'
__all__ = ('DutyCycleImporter',)


class DutyCycleImporter(_1.APIBase):
    '''DutyCycleImporter

    This is a mastapy class.
    '''

    TYPE = _DUTY_CYCLE_IMPORTER

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DutyCycleImporter.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def duty_cycles_to_import(self) -> 'List[_1780.IncludeDutyCycleOption]':
        '''List[IncludeDutyCycleOption]: 'DutyCyclesToImport' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.DutyCyclesToImport, constructor.new(_1780.IncludeDutyCycleOption))
        return value

    @property
    def power_load_destinations(self) -> 'List[_1777.DutyCycleImporterDesignEntityMatch[_1991.PowerLoad]]':
        '''List[DutyCycleImporterDesignEntityMatch[PowerLoad]]: 'PowerLoadDestinations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoadDestinations, constructor.new(_1777.DutyCycleImporterDesignEntityMatch)[_1991.PowerLoad])
        return value

    @property
    def point_load_destinations(self) -> 'List[_1777.DutyCycleImporterDesignEntityMatch[_1990.PointLoad]]':
        '''List[DutyCycleImporterDesignEntityMatch[PointLoad]]: 'PointLoadDestinations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoadDestinations, constructor.new(_1777.DutyCycleImporterDesignEntityMatch)[_1990.PointLoad])
        return value

    @property
    def design_state_destinations(self) -> 'List[_1777.DutyCycleImporterDesignEntityMatch[_5215.DesignState]]':
        '''List[DutyCycleImporterDesignEntityMatch[DesignState]]: 'DesignStateDestinations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.DesignStateDestinations, constructor.new(_1777.DutyCycleImporterDesignEntityMatch)[_5215.DesignState])
        return value
