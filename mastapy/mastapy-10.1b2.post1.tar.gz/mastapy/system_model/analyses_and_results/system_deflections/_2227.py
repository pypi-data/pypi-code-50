'''_2227.py

CVTSystemDeflection
'''


from mastapy._internal import constructor
from mastapy.system_model.part_model.couplings import _2098
from mastapy.system_model.analyses_and_results.power_flows import _3233
from mastapy.system_model.analyses_and_results.system_deflections import _2193
from mastapy._internal.python_net import python_net_import

_CVT_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'CVTSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTSystemDeflection',)


class CVTSystemDeflection(_2193.BeltDriveSystemDeflection):
    '''CVTSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CVT_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CVTSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def minimum_required_clamping_force(self) -> 'float':
        '''float: 'MinimumRequiredClampingForce' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MinimumRequiredClampingForce

    @property
    def minimum_belt_clamping_force_safety_factor(self) -> 'float':
        '''float: 'MinimumBeltClampingForceSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MinimumBeltClampingForceSafetyFactor

    @property
    def assembly_design(self) -> '_2098.CVT':
        '''CVT: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2098.CVT)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def power_flow_results(self) -> '_3233.CVTPowerFlow':
        '''CVTPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3233.CVTPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None
