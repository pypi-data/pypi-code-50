'''_4079.py

CylindricalPlanetGearParametricStudyTool
'''


from mastapy.system_model.part_model.gears import _1994
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4077
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'CylindricalPlanetGearParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlanetGearParametricStudyTool',)


class CylindricalPlanetGearParametricStudyTool(_4077.CylindricalGearParametricStudyTool):
    '''CylindricalPlanetGearParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL
    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalPlanetGearParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1994.CylindricalPlanetGear':
        '''CylindricalPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1994.CylindricalPlanetGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None
