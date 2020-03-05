'''_763.py

ConicalMeshLoadDistributionAnalysis
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.load_case.conical import _780
from mastapy.gears.manufacturing.bevel import _688
from mastapy.gears.ltca.conical import _762
from mastapy.gears.ltca import _736
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_LOAD_DISTRIBUTION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.LTCA.Conical', 'ConicalMeshLoadDistributionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshLoadDistributionAnalysis',)


class ConicalMeshLoadDistributionAnalysis(_736.GearMeshLoadDistributionAnalysis):
    '''ConicalMeshLoadDistributionAnalysis

    This is a mastapy class.
    '''

    TYPE = _CONICAL_MESH_LOAD_DISTRIBUTION_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalMeshLoadDistributionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def number_of_roll_angles(self) -> 'int':
        '''int: 'NumberOfRollAngles' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfRollAngles

    @property
    def pinion_mean_te(self) -> 'float':
        '''float: 'PinionMeanTE' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PinionMeanTE

    @property
    def pinion_peak_to_peak_te(self) -> 'float':
        '''float: 'PinionPeakToPeakTE' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PinionPeakToPeakTE

    @property
    def wheel_peak_to_peak_te(self) -> 'float':
        '''float: 'WheelPeakToPeakTE' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.WheelPeakToPeakTE

    @property
    def conical_mesh_load_case(self) -> '_780.ConicalMeshLoadCase':
        '''ConicalMeshLoadCase: 'ConicalMeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_780.ConicalMeshLoadCase)(self.wrapped.ConicalMeshLoadCase) if self.wrapped.ConicalMeshLoadCase else None

    @property
    def conical_mesh_manufacturing_analysis(self) -> '_688.ConicalMeshManufacturingAnalysis':
        '''ConicalMeshManufacturingAnalysis: 'ConicalMeshManufacturingAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_688.ConicalMeshManufacturingAnalysis)(self.wrapped.ConicalMeshManufacturingAnalysis) if self.wrapped.ConicalMeshManufacturingAnalysis else None

    @property
    def meshed_gears(self) -> 'List[_762.ConicalMeshedGearLoadDistributionAnalysis]':
        '''List[ConicalMeshedGearLoadDistributionAnalysis]: 'MeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeshedGears, constructor.new(_762.ConicalMeshedGearLoadDistributionAnalysis))
        return value
