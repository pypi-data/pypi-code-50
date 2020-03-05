'''_816.py

ConicalMeshManufacturingAnalysis
'''


from typing import List

from mastapy.gears.load_case.conical import _350
from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.bevel import _827, _811
from mastapy.gears.analysis import _736
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MANUFACTURING_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalMeshManufacturingAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshManufacturingAnalysis',)


class ConicalMeshManufacturingAnalysis(_736.GearMeshImplementationAnalysis):
    '''ConicalMeshManufacturingAnalysis

    This is a mastapy class.
    '''

    TYPE = _CONICAL_MESH_MANUFACTURING_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalMeshManufacturingAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def conical_mesh_load_case(self) -> '_350.ConicalMeshLoadCase':
        '''ConicalMeshLoadCase: 'ConicalMeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_350.ConicalMeshLoadCase)(self.wrapped.ConicalMeshLoadCase) if self.wrapped.ConicalMeshLoadCase else None

    @property
    def tca(self) -> '_827.EaseOffBasedTCA':
        '''EaseOffBasedTCA: 'TCA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_827.EaseOffBasedTCA)(self.wrapped.TCA) if self.wrapped.TCA else None

    @property
    def meshed_gears(self) -> 'List[_811.ConicalMeshedGearManufacturingAnalysis]':
        '''List[ConicalMeshedGearManufacturingAnalysis]: 'MeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeshedGears, constructor.new(_811.ConicalMeshedGearManufacturingAnalysis))
        return value
