'''_1862.py

ImportedFEElectricMachineStatorLink
'''


from mastapy.system_model.imported_fes import _1852, _1867
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_IMPORTED_FE_ELECTRIC_MACHINE_STATOR_LINK = python_net_import('SMT.MastaAPI.SystemModel.ImportedFEs', 'ImportedFEElectricMachineStatorLink')


__docformat__ = 'restructuredtext en'
__all__ = ('ImportedFEElectricMachineStatorLink',)


class ImportedFEElectricMachineStatorLink(_1867.ImportedFEMultiNodeLink):
    '''ImportedFEElectricMachineStatorLink

    This is a mastapy class.
    '''

    TYPE = _IMPORTED_FE_ELECTRIC_MACHINE_STATOR_LINK

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ImportedFEElectricMachineStatorLink.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def electric_machine_dynamic_load_data(self) -> '_1852.ElectricMachineDynamicLoadData':
        '''ElectricMachineDynamicLoadData: 'ElectricMachineDynamicLoadData' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1852.ElectricMachineDynamicLoadData)(self.wrapped.ElectricMachineDynamicLoadData) if self.wrapped.ElectricMachineDynamicLoadData else None
