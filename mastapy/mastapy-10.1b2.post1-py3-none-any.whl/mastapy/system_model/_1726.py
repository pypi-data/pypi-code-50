'''_1726.py

DutyCycleImporter
'''


from typing import List

from mastapy.system_model import _1730, _1727
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _1937, _1936
from mastapy.system_model.analyses_and_results.load_case_groups import _5085
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
    def duty_cycles_to_import(self) -> 'List[_1730.IncludeDutyCycleOption]':
        '''List[IncludeDutyCycleOption]: 'DutyCyclesToImport' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.DutyCyclesToImport, constructor.new(_1730.IncludeDutyCycleOption))
        return value

    @property
    def power_load_destinations(self) -> 'List[_1727.DutyCycleImporterDesignEntityMatch[_1937.PowerLoad]]':
        '''List[DutyCycleImporterDesignEntityMatch[PowerLoad]]: 'PowerLoadDestinations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoadDestinations, constructor.new(_1727.DutyCycleImporterDesignEntityMatch)[_1937.PowerLoad])
        return value

    @property
    def point_load_destinations(self) -> 'List[_1727.DutyCycleImporterDesignEntityMatch[_1936.PointLoad]]':
        '''List[DutyCycleImporterDesignEntityMatch[PointLoad]]: 'PointLoadDestinations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoadDestinations, constructor.new(_1727.DutyCycleImporterDesignEntityMatch)[_1936.PointLoad])
        return value

    @property
    def design_state_destinations(self) -> 'List[_1727.DutyCycleImporterDesignEntityMatch[_5085.DesignState]]':
        '''List[DutyCycleImporterDesignEntityMatch[DesignState]]: 'DesignStateDestinations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.DesignStateDestinations, constructor.new(_1727.DutyCycleImporterDesignEntityMatch)[_5085.DesignState])
        return value
