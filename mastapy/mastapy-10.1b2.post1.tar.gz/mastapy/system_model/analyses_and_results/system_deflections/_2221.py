'''_2221.py

ConnectorSystemDeflection
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _1970, _1963, _1986
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.couplings import _2110
from mastapy.system_model.analyses_and_results.system_deflections import _2252, _2267
from mastapy.math_utility.measured_vectors import _1106
from mastapy.utility.units_and_measurements.measurements import _1168, _1240
from mastapy.system_model.imported_fes import _1925
from mastapy.system_model.analyses_and_results.power_flows import (
    _3228, _3200, _3267, _3284
)
from mastapy._internal.python_net import python_net_import

_CONNECTOR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ConnectorSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectorSystemDeflection',)


class ConnectorSystemDeflection(_2267.MountableComponentSystemDeflection):
    '''ConnectorSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CONNECTOR_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConnectorSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def convergence_delta_energy(self) -> 'float':
        '''float: 'ConvergenceDeltaEnergy' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ConvergenceDeltaEnergy

    @property
    def component_design(self) -> '_1970.Connector':
        '''Connector: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1970.Connector)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_bearing(self) -> '_1963.Bearing':
        '''Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1963.Bearing.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Bearing. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1963.Bearing)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_oil_seal(self) -> '_1986.OilSeal':
        '''OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1986.OilSeal.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to OilSeal. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1986.OilSeal)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_shaft_hub_connection(self) -> '_2110.ShaftHubConnection':
        '''ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2110.ShaftHubConnection.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ShaftHubConnection. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_2110.ShaftHubConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def outer_imported_fe(self) -> '_2252.ImportedFEComponentSystemDeflection':
        '''ImportedFEComponentSystemDeflection: 'OuterImportedFE' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2252.ImportedFEComponentSystemDeflection)(self.wrapped.OuterImportedFE) if self.wrapped.OuterImportedFE else None

    @property
    def force_on_outer_support_in_wcs(self) -> '_1106.VectorWithLinearAndAngularComponents[_1168.Force, _1240.Torque]':
        '''VectorWithLinearAndAngularComponents[Force, Torque]: 'ForceOnOuterSupportInWCS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1106.VectorWithLinearAndAngularComponents)[_1168.Force, _1240.Torque](self.wrapped.ForceOnOuterSupportInWCS) if self.wrapped.ForceOnOuterSupportInWCS else None

    @property
    def force_on_outer_support_in_lcs(self) -> '_1106.VectorWithLinearAndAngularComponents[_1168.Force, _1240.Torque]':
        '''VectorWithLinearAndAngularComponents[Force, Torque]: 'ForceOnOuterSupportInLCS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1106.VectorWithLinearAndAngularComponents)[_1168.Force, _1240.Torque](self.wrapped.ForceOnOuterSupportInLCS) if self.wrapped.ForceOnOuterSupportInLCS else None

    @property
    def outer_imported_fe_nodes(self) -> 'List[_1925.ImportedFEStiffnessNode]':
        '''List[ImportedFEStiffnessNode]: 'OuterImportedFENodes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OuterImportedFENodes, constructor.new(_1925.ImportedFEStiffnessNode))
        return value

    @property
    def power_flow_results(self) -> '_3228.ConnectorPowerFlow':
        '''ConnectorPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3228.ConnectorPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None

    @property
    def power_flow_results_of_type_bearing_power_flow(self) -> '_3200.BearingPowerFlow':
        '''BearingPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _3200.BearingPowerFlow.TYPE not in self.wrapped.PowerFlowResults.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to BearingPowerFlow. Expected: {}.'.format(self.wrapped.PowerFlowResults.__class__.__qualname__))

        return constructor.new(_3200.BearingPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None

    @property
    def power_flow_results_of_type_oil_seal_power_flow(self) -> '_3267.OilSealPowerFlow':
        '''OilSealPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _3267.OilSealPowerFlow.TYPE not in self.wrapped.PowerFlowResults.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to OilSealPowerFlow. Expected: {}.'.format(self.wrapped.PowerFlowResults.__class__.__qualname__))

        return constructor.new(_3267.OilSealPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None

    @property
    def power_flow_results_of_type_shaft_hub_connection_power_flow(self) -> '_3284.ShaftHubConnectionPowerFlow':
        '''ShaftHubConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _3284.ShaftHubConnectionPowerFlow.TYPE not in self.wrapped.PowerFlowResults.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ShaftHubConnectionPowerFlow. Expected: {}.'.format(self.wrapped.PowerFlowResults.__class__.__qualname__))

        return constructor.new(_3284.ShaftHubConnectionPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None
