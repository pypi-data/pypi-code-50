'''_4954.py

BeltDriveMultiBodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2089
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6034
from mastapy.system_model.analyses_and_results.mbd_analyses import _5038, _5049
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_MULTI_BODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'BeltDriveMultiBodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltDriveMultiBodyDynamicsAnalysis',)


class BeltDriveMultiBodyDynamicsAnalysis(_5049.SpecialisedAssemblyMultiBodyDynamicsAnalysis):
    '''BeltDriveMultiBodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _BELT_DRIVE_MULTI_BODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BeltDriveMultiBodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2089.BeltDrive':
        '''BeltDrive: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2089.BeltDrive)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6034.BeltDriveLoadCase':
        '''BeltDriveLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6034.BeltDriveLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def pulleys(self) -> 'List[_5038.PulleyMultiBodyDynamicsAnalysis]':
        '''List[PulleyMultiBodyDynamicsAnalysis]: 'Pulleys' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Pulleys, constructor.new(_5038.PulleyMultiBodyDynamicsAnalysis))
        return value
