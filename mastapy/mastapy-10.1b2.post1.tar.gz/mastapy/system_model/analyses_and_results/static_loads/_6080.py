'''_6080.py

ElectricMachineDetailDatabase
'''


from typing import Iterable

from mastapy.system_model.analyses_and_results.static_loads import _6079
from mastapy._internal import constructor, conversion
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_DETAIL_DATABASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ElectricMachineDetailDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineDetailDatabase',)


class ElectricMachineDetailDatabase(_1.APIBase):
    '''ElectricMachineDetailDatabase

    This is a mastapy class.
    '''

    TYPE = _ELECTRIC_MACHINE_DETAIL_DATABASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElectricMachineDetailDatabase.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def item(self) -> '_6079.ElectricMachineDetail':
        '''ElectricMachineDetail: 'Item' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6079.ElectricMachineDetail)(self.wrapped.Item) if self.wrapped.Item else None

    def create(self, name: 'str') -> '_6079.ElectricMachineDetail':
        ''' 'Create' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ElectricMachineDetail
        '''

        name = str(name)
        method_result = self.wrapped.Create(name if name else None)
        return constructor.new(_6079.ElectricMachineDetail)(method_result) if method_result else None

    def can_be_removed(self, electric_machine_detail: '_6079.ElectricMachineDetail') -> 'bool':
        ''' 'CanBeRemoved' is the original name of this method.

        Args:
            electric_machine_detail (mastapy.system_model.analyses_and_results.static_loads.ElectricMachineDetail)

        Returns:
            bool
        '''

        method_result = self.wrapped.CanBeRemoved(electric_machine_detail.wrapped if electric_machine_detail else None)
        return method_result

    def rename(self, electric_machine_detail: '_6079.ElectricMachineDetail', new_name: 'str') -> 'bool':
        ''' 'Rename' is the original name of this method.

        Args:
            electric_machine_detail (mastapy.system_model.analyses_and_results.static_loads.ElectricMachineDetail)
            new_name (str)

        Returns:
            bool
        '''

        new_name = str(new_name)
        method_result = self.wrapped.Rename(electric_machine_detail.wrapped if electric_machine_detail else None, new_name if new_name else None)
        return method_result

    def remove(self, electric_machine_detail: '_6079.ElectricMachineDetail'):
        ''' 'Remove' is the original name of this method.

        Args:
            electric_machine_detail (mastapy.system_model.analyses_and_results.static_loads.ElectricMachineDetail)
        '''

        self.wrapped.Remove(electric_machine_detail.wrapped if electric_machine_detail else None)

    def get_all_items(self) -> 'Iterable[_6079.ElectricMachineDetail]':
        ''' 'GetAllItems' is the original name of this method.

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.static_loads.ElectricMachineDetail]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.GetAllItems(), constructor.new(_6079.ElectricMachineDetail))

    def save_changes(self, electric_machine_detail: '_6079.ElectricMachineDetail'):
        ''' 'SaveChanges' is the original name of this method.

        Args:
            electric_machine_detail (mastapy.system_model.analyses_and_results.static_loads.ElectricMachineDetail)
        '''

        self.wrapped.SaveChanges(electric_machine_detail.wrapped if electric_machine_detail else None)
