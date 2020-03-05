'''_3985.py

BeltDriveParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2015
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2241
from mastapy.system_model.analyses_and_results.system_deflections import _2153
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4059
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'BeltDriveParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltDriveParametricStudyTool',)


class BeltDriveParametricStudyTool(_4059.SpecialisedAssemblyParametricStudyTool):
    '''BeltDriveParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _BELT_DRIVE_PARAMETRIC_STUDY_TOOL
    __hash__ = None

    def __init__(self, instance_to_wrap: 'BeltDriveParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2015.BeltDrive':
        '''BeltDrive: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2015.BeltDrive)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2241.BeltDriveLoadCase':
        '''BeltDriveLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2241.BeltDriveLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2153.BeltDriveSystemDeflection]':
        '''List[BeltDriveSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionResults, constructor.new(_2153.BeltDriveSystemDeflection))
        return value
