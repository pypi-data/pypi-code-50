'''_2149.py

PowerFlowAnalysis
'''


from mastapy.system_model.analyses_and_results.static_loads import (
    _6189, _6190, _6192, _6136,
    _6135, _6034, _6047, _6046,
    _6052, _6051, _6065, _6064,
    _6067, _6068, _6145, _6151,
    _6149, _6147, _6161, _6160,
    _6172, _6171, _6173, _6174,
    _6178, _6179, _6180, _6066,
    _6033, _6048, _6061, _6116,
    _6137, _6148, _6153, _6036,
    _6054, _6092, _6164, _6041,
    _6058, _6028, _6071, _6112,
    _6118, _6121, _6124, _6157,
    _6167, _6188, _6191, _6098,
    _6134, _6045, _6050, _6063,
    _6159, _6177, _6024, _6025,
    _6032, _6044, _6043, _6049,
    _6062, _6077, _6090, _6094,
    _6031, _6102, _6114, _6126,
    _6127, _6129, _6131, _6133,
    _6140, _6143, _6144, _6150,
    _6154, _6185, _6186, _6152,
    _6053, _6055, _6091, _6093,
    _6027, _6029, _6035, _6037,
    _6038, _6039, _6040, _6042,
    _6056, _6060, _6069, _6073,
    _6074, _6096, _6101, _6111,
    _6113, _6117, _6119, _6120,
    _6122, _6123, _6125, _6138,
    _6156, _6158, _6163, _6165,
    _6166, _6168, _6169, _6170,
    _6187
)
from mastapy.system_model.analyses_and_results.power_flows import (
    _3315, _3317, _3318, _3271,
    _3270, _3202, _3215, _3214,
    _3220, _3219, _3231, _3230,
    _3233, _3234, _3279, _3284,
    _3282, _3280, _3293, _3292,
    _3304, _3302, _3303, _3305,
    _3308, _3309, _3310, _3232,
    _3201, _3216, _3227, _3254,
    _3272, _3281, _3286, _3203,
    _3221, _3242, _3294, _3208,
    _3224, _3196, _3236, _3250,
    _3255, _3258, _3261, _3288,
    _3297, _3313, _3316, _3246,
    _3269, _3213, _3218, _3229,
    _3291, _3307, _3194, _3195,
    _3200, _3212, _3211, _3217,
    _3228, _3240, _3241, _3245,
    _3199, _3249, _3253, _3264,
    _3265, _3266, _3267, _3268,
    _3274, _3275, _3278, _3283,
    _3287, _3311, _3312, _3285,
    _3222, _3223, _3243, _3244,
    _3197, _3198, _3204, _3205,
    _3206, _3207, _3209, _3210,
    _3225, _3226, _3237, _3238,
    _3239, _3247, _3248, _3251,
    _3252, _3256, _3257, _3259,
    _3260, _3262, _3263, _3273,
    _3289, _3290, _3295, _3296,
    _3298, _3299, _3300, _3301,
    _3314
)
from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import (
    _2070, _2071, _2038, _2039,
    _2045, _2046, _2030, _2031,
    _2032, _2033, _2034, _2035,
    _2036, _2037, _2040, _2041,
    _2042, _2043, _2044, _2047,
    _2049, _2051, _2052, _2053,
    _2054, _2055, _2056, _2057,
    _2058, _2059, _2060, _2061,
    _2062, _2063, _2064, _2065,
    _2066, _2067, _2068, _2069
)
from mastapy.system_model.part_model.couplings import (
    _2100, _2101, _2089, _2091,
    _2092, _2094, _2095, _2096,
    _2097, _2098, _2099, _2102,
    _2110, _2108, _2109, _2111,
    _2112, _2113, _2115, _2116,
    _2117, _2118, _2119, _2121
)
from mastapy.system_model.connections_and_sockets import (
    _1816, _1811, _1812, _1815,
    _1824, _1827, _1831, _1835
)
from mastapy.system_model.connections_and_sockets.gears import (
    _1841, _1845, _1851, _1865,
    _1843, _1847, _1839, _1849,
    _1855, _1858, _1859, _1860,
    _1863, _1867, _1869, _1871,
    _1853
)
from mastapy.system_model.connections_and_sockets.couplings import (
    _1879, _1873, _1875, _1877,
    _1881, _1883
)
from mastapy.system_model.part_model import (
    _1959, _1960, _1963, _1965,
    _1966, _1967, _1970, _1971,
    _1974, _1975, _1958, _1976,
    _1979, _1982, _1983, _1984,
    _1986, _1987, _1988, _1990,
    _1991, _1993, _1995, _1996,
    _1997
)
from mastapy.system_model.part_model.shaft_model import _2000
from mastapy.system_model.analyses_and_results import _2131
from mastapy._internal.python_net import python_net_import

_POWER_FLOW_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'PowerFlowAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerFlowAnalysis',)


class PowerFlowAnalysis(_2131.SingleAnalysis):
    '''PowerFlowAnalysis

    This is a mastapy class.
    '''

    TYPE = _POWER_FLOW_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PowerFlowAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    def results_for_worm_gear_set_load_case(self, design_entity_analysis: '_6189.WormGearSetLoadCase') -> '_3315.WormGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.WormGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3315.WormGearSetPowerFlow)(method_result) if method_result else None

    def results_for_zerol_bevel_gear(self, design_entity: '_2070.ZerolBevelGear') -> '_3317.ZerolBevelGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ZerolBevelGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3317.ZerolBevelGearPowerFlow)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_load_case(self, design_entity_analysis: '_6190.ZerolBevelGearLoadCase') -> '_3317.ZerolBevelGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ZerolBevelGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3317.ZerolBevelGearPowerFlow)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2071.ZerolBevelGearSet') -> '_3318.ZerolBevelGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ZerolBevelGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3318.ZerolBevelGearSetPowerFlow)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set_load_case(self, design_entity_analysis: '_6192.ZerolBevelGearSetLoadCase') -> '_3318.ZerolBevelGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ZerolBevelGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3318.ZerolBevelGearSetPowerFlow)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2100.PartToPartShearCoupling') -> '_3271.PartToPartShearCouplingPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PartToPartShearCouplingPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3271.PartToPartShearCouplingPowerFlow)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_load_case(self, design_entity_analysis: '_6136.PartToPartShearCouplingLoadCase') -> '_3271.PartToPartShearCouplingPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PartToPartShearCouplingPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3271.PartToPartShearCouplingPowerFlow)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2101.PartToPartShearCouplingHalf') -> '_3270.PartToPartShearCouplingHalfPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PartToPartShearCouplingHalfPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3270.PartToPartShearCouplingHalfPowerFlow)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half_load_case(self, design_entity_analysis: '_6135.PartToPartShearCouplingHalfLoadCase') -> '_3270.PartToPartShearCouplingHalfPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PartToPartShearCouplingHalfPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3270.PartToPartShearCouplingHalfPowerFlow)(method_result) if method_result else None

    def results_for_belt_drive(self, design_entity: '_2089.BeltDrive') -> '_3202.BeltDrivePowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BeltDrivePowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3202.BeltDrivePowerFlow)(method_result) if method_result else None

    def results_for_belt_drive_load_case(self, design_entity_analysis: '_6034.BeltDriveLoadCase') -> '_3202.BeltDrivePowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BeltDrivePowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3202.BeltDrivePowerFlow)(method_result) if method_result else None

    def results_for_clutch(self, design_entity: '_2091.Clutch') -> '_3215.ClutchPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ClutchPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3215.ClutchPowerFlow)(method_result) if method_result else None

    def results_for_clutch_load_case(self, design_entity_analysis: '_6047.ClutchLoadCase') -> '_3215.ClutchPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ClutchPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3215.ClutchPowerFlow)(method_result) if method_result else None

    def results_for_clutch_half(self, design_entity: '_2092.ClutchHalf') -> '_3214.ClutchHalfPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ClutchHalfPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3214.ClutchHalfPowerFlow)(method_result) if method_result else None

    def results_for_clutch_half_load_case(self, design_entity_analysis: '_6046.ClutchHalfLoadCase') -> '_3214.ClutchHalfPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ClutchHalfPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3214.ClutchHalfPowerFlow)(method_result) if method_result else None

    def results_for_concept_coupling(self, design_entity: '_2094.ConceptCoupling') -> '_3220.ConceptCouplingPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConceptCouplingPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3220.ConceptCouplingPowerFlow)(method_result) if method_result else None

    def results_for_concept_coupling_load_case(self, design_entity_analysis: '_6052.ConceptCouplingLoadCase') -> '_3220.ConceptCouplingPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConceptCouplingPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3220.ConceptCouplingPowerFlow)(method_result) if method_result else None

    def results_for_concept_coupling_half(self, design_entity: '_2095.ConceptCouplingHalf') -> '_3219.ConceptCouplingHalfPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConceptCouplingHalfPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3219.ConceptCouplingHalfPowerFlow)(method_result) if method_result else None

    def results_for_concept_coupling_half_load_case(self, design_entity_analysis: '_6051.ConceptCouplingHalfLoadCase') -> '_3219.ConceptCouplingHalfPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConceptCouplingHalfPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3219.ConceptCouplingHalfPowerFlow)(method_result) if method_result else None

    def results_for_coupling(self, design_entity: '_2096.Coupling') -> '_3231.CouplingPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CouplingPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3231.CouplingPowerFlow)(method_result) if method_result else None

    def results_for_coupling_load_case(self, design_entity_analysis: '_6065.CouplingLoadCase') -> '_3231.CouplingPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CouplingPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3231.CouplingPowerFlow)(method_result) if method_result else None

    def results_for_coupling_half(self, design_entity: '_2097.CouplingHalf') -> '_3230.CouplingHalfPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CouplingHalfPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3230.CouplingHalfPowerFlow)(method_result) if method_result else None

    def results_for_coupling_half_load_case(self, design_entity_analysis: '_6064.CouplingHalfLoadCase') -> '_3230.CouplingHalfPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CouplingHalfPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3230.CouplingHalfPowerFlow)(method_result) if method_result else None

    def results_for_cvt(self, design_entity: '_2098.CVT') -> '_3233.CVTPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CVTPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3233.CVTPowerFlow)(method_result) if method_result else None

    def results_for_cvt_load_case(self, design_entity_analysis: '_6067.CVTLoadCase') -> '_3233.CVTPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CVTPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3233.CVTPowerFlow)(method_result) if method_result else None

    def results_for_cvt_pulley(self, design_entity: '_2099.CVTPulley') -> '_3234.CVTPulleyPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CVTPulleyPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3234.CVTPulleyPowerFlow)(method_result) if method_result else None

    def results_for_cvt_pulley_load_case(self, design_entity_analysis: '_6068.CVTPulleyLoadCase') -> '_3234.CVTPulleyPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CVTPulleyPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3234.CVTPulleyPowerFlow)(method_result) if method_result else None

    def results_for_pulley(self, design_entity: '_2102.Pulley') -> '_3279.PulleyPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PulleyPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3279.PulleyPowerFlow)(method_result) if method_result else None

    def results_for_pulley_load_case(self, design_entity_analysis: '_6145.PulleyLoadCase') -> '_3279.PulleyPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PulleyPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3279.PulleyPowerFlow)(method_result) if method_result else None

    def results_for_shaft_hub_connection(self, design_entity: '_2110.ShaftHubConnection') -> '_3284.ShaftHubConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ShaftHubConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3284.ShaftHubConnectionPowerFlow)(method_result) if method_result else None

    def results_for_shaft_hub_connection_load_case(self, design_entity_analysis: '_6151.ShaftHubConnectionLoadCase') -> '_3284.ShaftHubConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ShaftHubConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3284.ShaftHubConnectionPowerFlow)(method_result) if method_result else None

    def results_for_rolling_ring(self, design_entity: '_2108.RollingRing') -> '_3282.RollingRingPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.RollingRingPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3282.RollingRingPowerFlow)(method_result) if method_result else None

    def results_for_rolling_ring_load_case(self, design_entity_analysis: '_6149.RollingRingLoadCase') -> '_3282.RollingRingPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.RollingRingPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3282.RollingRingPowerFlow)(method_result) if method_result else None

    def results_for_rolling_ring_assembly(self, design_entity: '_2109.RollingRingAssembly') -> '_3280.RollingRingAssemblyPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.RollingRingAssemblyPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3280.RollingRingAssemblyPowerFlow)(method_result) if method_result else None

    def results_for_rolling_ring_assembly_load_case(self, design_entity_analysis: '_6147.RollingRingAssemblyLoadCase') -> '_3280.RollingRingAssemblyPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.RollingRingAssemblyPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3280.RollingRingAssemblyPowerFlow)(method_result) if method_result else None

    def results_for_spring_damper(self, design_entity: '_2111.SpringDamper') -> '_3293.SpringDamperPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SpringDamperPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3293.SpringDamperPowerFlow)(method_result) if method_result else None

    def results_for_spring_damper_load_case(self, design_entity_analysis: '_6161.SpringDamperLoadCase') -> '_3293.SpringDamperPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SpringDamperPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3293.SpringDamperPowerFlow)(method_result) if method_result else None

    def results_for_spring_damper_half(self, design_entity: '_2112.SpringDamperHalf') -> '_3292.SpringDamperHalfPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SpringDamperHalfPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3292.SpringDamperHalfPowerFlow)(method_result) if method_result else None

    def results_for_spring_damper_half_load_case(self, design_entity_analysis: '_6160.SpringDamperHalfLoadCase') -> '_3292.SpringDamperHalfPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SpringDamperHalfPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3292.SpringDamperHalfPowerFlow)(method_result) if method_result else None

    def results_for_synchroniser(self, design_entity: '_2113.Synchroniser') -> '_3304.SynchroniserPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SynchroniserPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3304.SynchroniserPowerFlow)(method_result) if method_result else None

    def results_for_synchroniser_load_case(self, design_entity_analysis: '_6172.SynchroniserLoadCase') -> '_3304.SynchroniserPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SynchroniserPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3304.SynchroniserPowerFlow)(method_result) if method_result else None

    def results_for_synchroniser_half(self, design_entity: '_2115.SynchroniserHalf') -> '_3302.SynchroniserHalfPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SynchroniserHalfPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3302.SynchroniserHalfPowerFlow)(method_result) if method_result else None

    def results_for_synchroniser_half_load_case(self, design_entity_analysis: '_6171.SynchroniserHalfLoadCase') -> '_3302.SynchroniserHalfPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SynchroniserHalfPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3302.SynchroniserHalfPowerFlow)(method_result) if method_result else None

    def results_for_synchroniser_part(self, design_entity: '_2116.SynchroniserPart') -> '_3303.SynchroniserPartPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SynchroniserPartPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3303.SynchroniserPartPowerFlow)(method_result) if method_result else None

    def results_for_synchroniser_part_load_case(self, design_entity_analysis: '_6173.SynchroniserPartLoadCase') -> '_3303.SynchroniserPartPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SynchroniserPartPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3303.SynchroniserPartPowerFlow)(method_result) if method_result else None

    def results_for_synchroniser_sleeve(self, design_entity: '_2117.SynchroniserSleeve') -> '_3305.SynchroniserSleevePowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SynchroniserSleevePowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3305.SynchroniserSleevePowerFlow)(method_result) if method_result else None

    def results_for_synchroniser_sleeve_load_case(self, design_entity_analysis: '_6174.SynchroniserSleeveLoadCase') -> '_3305.SynchroniserSleevePowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SynchroniserSleevePowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3305.SynchroniserSleevePowerFlow)(method_result) if method_result else None

    def results_for_torque_converter(self, design_entity: '_2118.TorqueConverter') -> '_3308.TorqueConverterPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.TorqueConverterPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3308.TorqueConverterPowerFlow)(method_result) if method_result else None

    def results_for_torque_converter_load_case(self, design_entity_analysis: '_6178.TorqueConverterLoadCase') -> '_3308.TorqueConverterPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.TorqueConverterPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3308.TorqueConverterPowerFlow)(method_result) if method_result else None

    def results_for_torque_converter_pump(self, design_entity: '_2119.TorqueConverterPump') -> '_3309.TorqueConverterPumpPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.TorqueConverterPumpPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3309.TorqueConverterPumpPowerFlow)(method_result) if method_result else None

    def results_for_torque_converter_pump_load_case(self, design_entity_analysis: '_6179.TorqueConverterPumpLoadCase') -> '_3309.TorqueConverterPumpPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.TorqueConverterPumpPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3309.TorqueConverterPumpPowerFlow)(method_result) if method_result else None

    def results_for_torque_converter_turbine(self, design_entity: '_2121.TorqueConverterTurbine') -> '_3310.TorqueConverterTurbinePowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.TorqueConverterTurbinePowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3310.TorqueConverterTurbinePowerFlow)(method_result) if method_result else None

    def results_for_torque_converter_turbine_load_case(self, design_entity_analysis: '_6180.TorqueConverterTurbineLoadCase') -> '_3310.TorqueConverterTurbinePowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.TorqueConverterTurbinePowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3310.TorqueConverterTurbinePowerFlow)(method_result) if method_result else None

    def results_for_cvt_belt_connection(self, design_entity: '_1816.CVTBeltConnection') -> '_3232.CVTBeltConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CVTBeltConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3232.CVTBeltConnectionPowerFlow)(method_result) if method_result else None

    def results_for_cvt_belt_connection_load_case(self, design_entity_analysis: '_6066.CVTBeltConnectionLoadCase') -> '_3232.CVTBeltConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CVTBeltConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3232.CVTBeltConnectionPowerFlow)(method_result) if method_result else None

    def results_for_belt_connection(self, design_entity: '_1811.BeltConnection') -> '_3201.BeltConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BeltConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3201.BeltConnectionPowerFlow)(method_result) if method_result else None

    def results_for_belt_connection_load_case(self, design_entity_analysis: '_6033.BeltConnectionLoadCase') -> '_3201.BeltConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BeltConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3201.BeltConnectionPowerFlow)(method_result) if method_result else None

    def results_for_coaxial_connection(self, design_entity: '_1812.CoaxialConnection') -> '_3216.CoaxialConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CoaxialConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3216.CoaxialConnectionPowerFlow)(method_result) if method_result else None

    def results_for_coaxial_connection_load_case(self, design_entity_analysis: '_6048.CoaxialConnectionLoadCase') -> '_3216.CoaxialConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CoaxialConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3216.CoaxialConnectionPowerFlow)(method_result) if method_result else None

    def results_for_connection(self, design_entity: '_1815.Connection') -> '_3227.ConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3227.ConnectionPowerFlow)(method_result) if method_result else None

    def results_for_connection_load_case(self, design_entity_analysis: '_6061.ConnectionLoadCase') -> '_3227.ConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3227.ConnectionPowerFlow)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection(self, design_entity: '_1824.InterMountableComponentConnection') -> '_3254.InterMountableComponentConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.InterMountableComponentConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3254.InterMountableComponentConnectionPowerFlow)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection_load_case(self, design_entity_analysis: '_6116.InterMountableComponentConnectionLoadCase') -> '_3254.InterMountableComponentConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.InterMountableComponentConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3254.InterMountableComponentConnectionPowerFlow)(method_result) if method_result else None

    def results_for_planetary_connection(self, design_entity: '_1827.PlanetaryConnection') -> '_3272.PlanetaryConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PlanetaryConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3272.PlanetaryConnectionPowerFlow)(method_result) if method_result else None

    def results_for_planetary_connection_load_case(self, design_entity_analysis: '_6137.PlanetaryConnectionLoadCase') -> '_3272.PlanetaryConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PlanetaryConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3272.PlanetaryConnectionPowerFlow)(method_result) if method_result else None

    def results_for_rolling_ring_connection(self, design_entity: '_1831.RollingRingConnection') -> '_3281.RollingRingConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.RollingRingConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3281.RollingRingConnectionPowerFlow)(method_result) if method_result else None

    def results_for_rolling_ring_connection_load_case(self, design_entity_analysis: '_6148.RollingRingConnectionLoadCase') -> '_3281.RollingRingConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.RollingRingConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3281.RollingRingConnectionPowerFlow)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1835.ShaftToMountableComponentConnection') -> '_3286.ShaftToMountableComponentConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ShaftToMountableComponentConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3286.ShaftToMountableComponentConnectionPowerFlow)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection_load_case(self, design_entity_analysis: '_6153.ShaftToMountableComponentConnectionLoadCase') -> '_3286.ShaftToMountableComponentConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ShaftToMountableComponentConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3286.ShaftToMountableComponentConnectionPowerFlow)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1841.BevelDifferentialGearMesh') -> '_3203.BevelDifferentialGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3203.BevelDifferentialGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh_load_case(self, design_entity_analysis: '_6036.BevelDifferentialGearMeshLoadCase') -> '_3203.BevelDifferentialGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3203.BevelDifferentialGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_concept_gear_mesh(self, design_entity: '_1845.ConceptGearMesh') -> '_3221.ConceptGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConceptGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3221.ConceptGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_concept_gear_mesh_load_case(self, design_entity_analysis: '_6054.ConceptGearMeshLoadCase') -> '_3221.ConceptGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConceptGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3221.ConceptGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_face_gear_mesh(self, design_entity: '_1851.FaceGearMesh') -> '_3242.FaceGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.FaceGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3242.FaceGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_face_gear_mesh_load_case(self, design_entity_analysis: '_6092.FaceGearMeshLoadCase') -> '_3242.FaceGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.FaceGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3242.FaceGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1865.StraightBevelDiffGearMesh') -> '_3294.StraightBevelDiffGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.StraightBevelDiffGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3294.StraightBevelDiffGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh_load_case(self, design_entity_analysis: '_6164.StraightBevelDiffGearMeshLoadCase') -> '_3294.StraightBevelDiffGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.StraightBevelDiffGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3294.StraightBevelDiffGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_bevel_gear_mesh(self, design_entity: '_1843.BevelGearMesh') -> '_3208.BevelGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BevelGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3208.BevelGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6041.BevelGearMeshLoadCase') -> '_3208.BevelGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BevelGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3208.BevelGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_conical_gear_mesh(self, design_entity: '_1847.ConicalGearMesh') -> '_3224.ConicalGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConicalGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3224.ConicalGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_conical_gear_mesh_load_case(self, design_entity_analysis: '_6058.ConicalGearMeshLoadCase') -> '_3224.ConicalGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConicalGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3224.ConicalGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1839.AGMAGleasonConicalGearMesh') -> '_3196.AGMAGleasonConicalGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3196.AGMAGleasonConicalGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh_load_case(self, design_entity_analysis: '_6028.AGMAGleasonConicalGearMeshLoadCase') -> '_3196.AGMAGleasonConicalGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3196.AGMAGleasonConicalGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1849.CylindricalGearMesh') -> '_3236.CylindricalGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CylindricalGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3236.CylindricalGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh_load_case(self, design_entity_analysis: '_6071.CylindricalGearMeshLoadCase') -> '_3236.CylindricalGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CylindricalGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3236.CylindricalGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh(self, design_entity: '_1855.HypoidGearMesh') -> '_3250.HypoidGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.HypoidGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3250.HypoidGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6112.HypoidGearMeshLoadCase') -> '_3250.HypoidGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.HypoidGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3250.HypoidGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1858.KlingelnbergCycloPalloidConicalGearMesh') -> '_3255.KlingelnbergCycloPalloidConicalGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3255.KlingelnbergCycloPalloidConicalGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self, design_entity_analysis: '_6118.KlingelnbergCycloPalloidConicalGearMeshLoadCase') -> '_3255.KlingelnbergCycloPalloidConicalGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3255.KlingelnbergCycloPalloidConicalGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1859.KlingelnbergCycloPalloidHypoidGearMesh') -> '_3258.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3258.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6121.KlingelnbergCycloPalloidHypoidGearMeshLoadCase') -> '_3258.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3258.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1860.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> '_3261.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3261.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6124.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase') -> '_3261.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3261.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1863.SpiralBevelGearMesh') -> '_3288.SpiralBevelGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3288.SpiralBevelGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6157.SpiralBevelGearMeshLoadCase') -> '_3288.SpiralBevelGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3288.SpiralBevelGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1867.StraightBevelGearMesh') -> '_3297.StraightBevelGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.StraightBevelGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3297.StraightBevelGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6167.StraightBevelGearMeshLoadCase') -> '_3297.StraightBevelGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.StraightBevelGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3297.StraightBevelGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_worm_gear_mesh(self, design_entity: '_1869.WormGearMesh') -> '_3313.WormGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.WormGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3313.WormGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_worm_gear_mesh_load_case(self, design_entity_analysis: '_6188.WormGearMeshLoadCase') -> '_3313.WormGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.WormGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3313.WormGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1871.ZerolBevelGearMesh') -> '_3316.ZerolBevelGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ZerolBevelGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3316.ZerolBevelGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6191.ZerolBevelGearMeshLoadCase') -> '_3316.ZerolBevelGearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ZerolBevelGearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3316.ZerolBevelGearMeshPowerFlow)(method_result) if method_result else None

    def results_for_gear_mesh(self, design_entity: '_1853.GearMesh') -> '_3246.GearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.GearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3246.GearMeshPowerFlow)(method_result) if method_result else None

    def results_for_gear_mesh_load_case(self, design_entity_analysis: '_6098.GearMeshLoadCase') -> '_3246.GearMeshPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.GearMeshPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3246.GearMeshPowerFlow)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_1879.PartToPartShearCouplingConnection') -> '_3269.PartToPartShearCouplingConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PartToPartShearCouplingConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3269.PartToPartShearCouplingConnectionPowerFlow)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection_load_case(self, design_entity_analysis: '_6134.PartToPartShearCouplingConnectionLoadCase') -> '_3269.PartToPartShearCouplingConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PartToPartShearCouplingConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3269.PartToPartShearCouplingConnectionPowerFlow)(method_result) if method_result else None

    def results_for_clutch_connection(self, design_entity: '_1873.ClutchConnection') -> '_3213.ClutchConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ClutchConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3213.ClutchConnectionPowerFlow)(method_result) if method_result else None

    def results_for_clutch_connection_load_case(self, design_entity_analysis: '_6045.ClutchConnectionLoadCase') -> '_3213.ClutchConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ClutchConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3213.ClutchConnectionPowerFlow)(method_result) if method_result else None

    def results_for_concept_coupling_connection(self, design_entity: '_1875.ConceptCouplingConnection') -> '_3218.ConceptCouplingConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConceptCouplingConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3218.ConceptCouplingConnectionPowerFlow)(method_result) if method_result else None

    def results_for_concept_coupling_connection_load_case(self, design_entity_analysis: '_6050.ConceptCouplingConnectionLoadCase') -> '_3218.ConceptCouplingConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConceptCouplingConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3218.ConceptCouplingConnectionPowerFlow)(method_result) if method_result else None

    def results_for_coupling_connection(self, design_entity: '_1877.CouplingConnection') -> '_3229.CouplingConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CouplingConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3229.CouplingConnectionPowerFlow)(method_result) if method_result else None

    def results_for_coupling_connection_load_case(self, design_entity_analysis: '_6063.CouplingConnectionLoadCase') -> '_3229.CouplingConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CouplingConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3229.CouplingConnectionPowerFlow)(method_result) if method_result else None

    def results_for_spring_damper_connection(self, design_entity: '_1881.SpringDamperConnection') -> '_3291.SpringDamperConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SpringDamperConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3291.SpringDamperConnectionPowerFlow)(method_result) if method_result else None

    def results_for_spring_damper_connection_load_case(self, design_entity_analysis: '_6159.SpringDamperConnectionLoadCase') -> '_3291.SpringDamperConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SpringDamperConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3291.SpringDamperConnectionPowerFlow)(method_result) if method_result else None

    def results_for_torque_converter_connection(self, design_entity: '_1883.TorqueConverterConnection') -> '_3307.TorqueConverterConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.TorqueConverterConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3307.TorqueConverterConnectionPowerFlow)(method_result) if method_result else None

    def results_for_torque_converter_connection_load_case(self, design_entity_analysis: '_6177.TorqueConverterConnectionLoadCase') -> '_3307.TorqueConverterConnectionPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.TorqueConverterConnectionPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3307.TorqueConverterConnectionPowerFlow)(method_result) if method_result else None

    def results_for_abstract_assembly(self, design_entity: '_1959.AbstractAssembly') -> '_3194.AbstractAssemblyPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.AbstractAssemblyPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3194.AbstractAssemblyPowerFlow)(method_result) if method_result else None

    def results_for_abstract_assembly_load_case(self, design_entity_analysis: '_6024.AbstractAssemblyLoadCase') -> '_3194.AbstractAssemblyPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.AbstractAssemblyPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3194.AbstractAssemblyPowerFlow)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing(self, design_entity: '_1960.AbstractShaftOrHousing') -> '_3195.AbstractShaftOrHousingPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.AbstractShaftOrHousingPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3195.AbstractShaftOrHousingPowerFlow)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing_load_case(self, design_entity_analysis: '_6025.AbstractShaftOrHousingLoadCase') -> '_3195.AbstractShaftOrHousingPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.AbstractShaftOrHousingPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3195.AbstractShaftOrHousingPowerFlow)(method_result) if method_result else None

    def results_for_bearing(self, design_entity: '_1963.Bearing') -> '_3200.BearingPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BearingPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3200.BearingPowerFlow)(method_result) if method_result else None

    def results_for_bearing_load_case(self, design_entity_analysis: '_6032.BearingLoadCase') -> '_3200.BearingPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BearingPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3200.BearingPowerFlow)(method_result) if method_result else None

    def results_for_bolt(self, design_entity: '_1965.Bolt') -> '_3212.BoltPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BoltPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3212.BoltPowerFlow)(method_result) if method_result else None

    def results_for_bolt_load_case(self, design_entity_analysis: '_6044.BoltLoadCase') -> '_3212.BoltPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BoltPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3212.BoltPowerFlow)(method_result) if method_result else None

    def results_for_bolted_joint(self, design_entity: '_1966.BoltedJoint') -> '_3211.BoltedJointPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BoltedJointPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3211.BoltedJointPowerFlow)(method_result) if method_result else None

    def results_for_bolted_joint_load_case(self, design_entity_analysis: '_6043.BoltedJointLoadCase') -> '_3211.BoltedJointPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BoltedJointPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3211.BoltedJointPowerFlow)(method_result) if method_result else None

    def results_for_component(self, design_entity: '_1967.Component') -> '_3217.ComponentPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ComponentPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3217.ComponentPowerFlow)(method_result) if method_result else None

    def results_for_component_load_case(self, design_entity_analysis: '_6049.ComponentLoadCase') -> '_3217.ComponentPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ComponentPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3217.ComponentPowerFlow)(method_result) if method_result else None

    def results_for_connector(self, design_entity: '_1970.Connector') -> '_3228.ConnectorPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConnectorPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3228.ConnectorPowerFlow)(method_result) if method_result else None

    def results_for_connector_load_case(self, design_entity_analysis: '_6062.ConnectorLoadCase') -> '_3228.ConnectorPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConnectorPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3228.ConnectorPowerFlow)(method_result) if method_result else None

    def results_for_datum(self, design_entity: '_1971.Datum') -> '_3240.DatumPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.DatumPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3240.DatumPowerFlow)(method_result) if method_result else None

    def results_for_datum_load_case(self, design_entity_analysis: '_6077.DatumLoadCase') -> '_3240.DatumPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.DatumPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3240.DatumPowerFlow)(method_result) if method_result else None

    def results_for_external_cad_model(self, design_entity: '_1974.ExternalCADModel') -> '_3241.ExternalCADModelPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ExternalCADModelPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3241.ExternalCADModelPowerFlow)(method_result) if method_result else None

    def results_for_external_cad_model_load_case(self, design_entity_analysis: '_6090.ExternalCADModelLoadCase') -> '_3241.ExternalCADModelPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ExternalCADModelPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3241.ExternalCADModelPowerFlow)(method_result) if method_result else None

    def results_for_flexible_pin_assembly(self, design_entity: '_1975.FlexiblePinAssembly') -> '_3245.FlexiblePinAssemblyPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.FlexiblePinAssemblyPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3245.FlexiblePinAssemblyPowerFlow)(method_result) if method_result else None

    def results_for_flexible_pin_assembly_load_case(self, design_entity_analysis: '_6094.FlexiblePinAssemblyLoadCase') -> '_3245.FlexiblePinAssemblyPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.FlexiblePinAssemblyPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3245.FlexiblePinAssemblyPowerFlow)(method_result) if method_result else None

    def results_for_assembly(self, design_entity: '_1958.Assembly') -> '_3199.AssemblyPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.AssemblyPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3199.AssemblyPowerFlow)(method_result) if method_result else None

    def results_for_assembly_load_case(self, design_entity_analysis: '_6031.AssemblyLoadCase') -> '_3199.AssemblyPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.AssemblyPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3199.AssemblyPowerFlow)(method_result) if method_result else None

    def results_for_guide_dxf_model(self, design_entity: '_1976.GuideDxfModel') -> '_3249.GuideDxfModelPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.GuideDxfModelPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3249.GuideDxfModelPowerFlow)(method_result) if method_result else None

    def results_for_guide_dxf_model_load_case(self, design_entity_analysis: '_6102.GuideDxfModelLoadCase') -> '_3249.GuideDxfModelPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.GuideDxfModelPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3249.GuideDxfModelPowerFlow)(method_result) if method_result else None

    def results_for_imported_fe_component(self, design_entity: '_1979.ImportedFEComponent') -> '_3253.ImportedFEComponentPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ImportedFEComponentPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3253.ImportedFEComponentPowerFlow)(method_result) if method_result else None

    def results_for_imported_fe_component_load_case(self, design_entity_analysis: '_6114.ImportedFEComponentLoadCase') -> '_3253.ImportedFEComponentPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ImportedFEComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ImportedFEComponentPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3253.ImportedFEComponentPowerFlow)(method_result) if method_result else None

    def results_for_mass_disc(self, design_entity: '_1982.MassDisc') -> '_3264.MassDiscPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.MassDiscPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3264.MassDiscPowerFlow)(method_result) if method_result else None

    def results_for_mass_disc_load_case(self, design_entity_analysis: '_6126.MassDiscLoadCase') -> '_3264.MassDiscPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.MassDiscPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3264.MassDiscPowerFlow)(method_result) if method_result else None

    def results_for_measurement_component(self, design_entity: '_1983.MeasurementComponent') -> '_3265.MeasurementComponentPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.MeasurementComponentPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3265.MeasurementComponentPowerFlow)(method_result) if method_result else None

    def results_for_measurement_component_load_case(self, design_entity_analysis: '_6127.MeasurementComponentLoadCase') -> '_3265.MeasurementComponentPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.MeasurementComponentPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3265.MeasurementComponentPowerFlow)(method_result) if method_result else None

    def results_for_mountable_component(self, design_entity: '_1984.MountableComponent') -> '_3266.MountableComponentPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.MountableComponentPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3266.MountableComponentPowerFlow)(method_result) if method_result else None

    def results_for_mountable_component_load_case(self, design_entity_analysis: '_6129.MountableComponentLoadCase') -> '_3266.MountableComponentPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.MountableComponentPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3266.MountableComponentPowerFlow)(method_result) if method_result else None

    def results_for_oil_seal(self, design_entity: '_1986.OilSeal') -> '_3267.OilSealPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.OilSealPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3267.OilSealPowerFlow)(method_result) if method_result else None

    def results_for_oil_seal_load_case(self, design_entity_analysis: '_6131.OilSealLoadCase') -> '_3267.OilSealPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.OilSealPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3267.OilSealPowerFlow)(method_result) if method_result else None

    def results_for_part(self, design_entity: '_1987.Part') -> '_3268.PartPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PartPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3268.PartPowerFlow)(method_result) if method_result else None

    def results_for_part_load_case(self, design_entity_analysis: '_6133.PartLoadCase') -> '_3268.PartPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PartPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3268.PartPowerFlow)(method_result) if method_result else None

    def results_for_planet_carrier(self, design_entity: '_1988.PlanetCarrier') -> '_3274.PlanetCarrierPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PlanetCarrierPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3274.PlanetCarrierPowerFlow)(method_result) if method_result else None

    def results_for_planet_carrier_load_case(self, design_entity_analysis: '_6140.PlanetCarrierLoadCase') -> '_3274.PlanetCarrierPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PlanetCarrierPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3274.PlanetCarrierPowerFlow)(method_result) if method_result else None

    def results_for_point_load(self, design_entity: '_1990.PointLoad') -> '_3275.PointLoadPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PointLoadPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3275.PointLoadPowerFlow)(method_result) if method_result else None

    def results_for_point_load_load_case(self, design_entity_analysis: '_6143.PointLoadLoadCase') -> '_3275.PointLoadPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PointLoadPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3275.PointLoadPowerFlow)(method_result) if method_result else None

    def results_for_power_load(self, design_entity: '_1991.PowerLoad') -> '_3278.PowerLoadPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PowerLoadPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3278.PowerLoadPowerFlow)(method_result) if method_result else None

    def results_for_power_load_load_case(self, design_entity_analysis: '_6144.PowerLoadLoadCase') -> '_3278.PowerLoadPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PowerLoadPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3278.PowerLoadPowerFlow)(method_result) if method_result else None

    def results_for_root_assembly(self, design_entity: '_1993.RootAssembly') -> '_3283.RootAssemblyPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.RootAssemblyPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3283.RootAssemblyPowerFlow)(method_result) if method_result else None

    def results_for_root_assembly_load_case(self, design_entity_analysis: '_6150.RootAssemblyLoadCase') -> '_3283.RootAssemblyPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.RootAssemblyPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3283.RootAssemblyPowerFlow)(method_result) if method_result else None

    def results_for_specialised_assembly(self, design_entity: '_1995.SpecialisedAssembly') -> '_3287.SpecialisedAssemblyPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SpecialisedAssemblyPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3287.SpecialisedAssemblyPowerFlow)(method_result) if method_result else None

    def results_for_specialised_assembly_load_case(self, design_entity_analysis: '_6154.SpecialisedAssemblyLoadCase') -> '_3287.SpecialisedAssemblyPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SpecialisedAssemblyPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3287.SpecialisedAssemblyPowerFlow)(method_result) if method_result else None

    def results_for_unbalanced_mass(self, design_entity: '_1996.UnbalancedMass') -> '_3311.UnbalancedMassPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.UnbalancedMassPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3311.UnbalancedMassPowerFlow)(method_result) if method_result else None

    def results_for_unbalanced_mass_load_case(self, design_entity_analysis: '_6185.UnbalancedMassLoadCase') -> '_3311.UnbalancedMassPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.UnbalancedMassPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3311.UnbalancedMassPowerFlow)(method_result) if method_result else None

    def results_for_virtual_component(self, design_entity: '_1997.VirtualComponent') -> '_3312.VirtualComponentPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.VirtualComponentPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3312.VirtualComponentPowerFlow)(method_result) if method_result else None

    def results_for_virtual_component_load_case(self, design_entity_analysis: '_6186.VirtualComponentLoadCase') -> '_3312.VirtualComponentPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.VirtualComponentPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3312.VirtualComponentPowerFlow)(method_result) if method_result else None

    def results_for_shaft(self, design_entity: '_2000.Shaft') -> '_3285.ShaftPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ShaftPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3285.ShaftPowerFlow)(method_result) if method_result else None

    def results_for_shaft_load_case(self, design_entity_analysis: '_6152.ShaftLoadCase') -> '_3285.ShaftPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ShaftPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3285.ShaftPowerFlow)(method_result) if method_result else None

    def results_for_concept_gear(self, design_entity: '_2038.ConceptGear') -> '_3222.ConceptGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConceptGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3222.ConceptGearPowerFlow)(method_result) if method_result else None

    def results_for_concept_gear_load_case(self, design_entity_analysis: '_6053.ConceptGearLoadCase') -> '_3222.ConceptGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConceptGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3222.ConceptGearPowerFlow)(method_result) if method_result else None

    def results_for_concept_gear_set(self, design_entity: '_2039.ConceptGearSet') -> '_3223.ConceptGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConceptGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3223.ConceptGearSetPowerFlow)(method_result) if method_result else None

    def results_for_concept_gear_set_load_case(self, design_entity_analysis: '_6055.ConceptGearSetLoadCase') -> '_3223.ConceptGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConceptGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3223.ConceptGearSetPowerFlow)(method_result) if method_result else None

    def results_for_face_gear(self, design_entity: '_2045.FaceGear') -> '_3243.FaceGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.FaceGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3243.FaceGearPowerFlow)(method_result) if method_result else None

    def results_for_face_gear_load_case(self, design_entity_analysis: '_6091.FaceGearLoadCase') -> '_3243.FaceGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.FaceGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3243.FaceGearPowerFlow)(method_result) if method_result else None

    def results_for_face_gear_set(self, design_entity: '_2046.FaceGearSet') -> '_3244.FaceGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.FaceGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3244.FaceGearSetPowerFlow)(method_result) if method_result else None

    def results_for_face_gear_set_load_case(self, design_entity_analysis: '_6093.FaceGearSetLoadCase') -> '_3244.FaceGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.FaceGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3244.FaceGearSetPowerFlow)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2030.AGMAGleasonConicalGear') -> '_3197.AGMAGleasonConicalGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3197.AGMAGleasonConicalGearPowerFlow)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_load_case(self, design_entity_analysis: '_6027.AGMAGleasonConicalGearLoadCase') -> '_3197.AGMAGleasonConicalGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3197.AGMAGleasonConicalGearPowerFlow)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2031.AGMAGleasonConicalGearSet') -> '_3198.AGMAGleasonConicalGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3198.AGMAGleasonConicalGearSetPowerFlow)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set_load_case(self, design_entity_analysis: '_6029.AGMAGleasonConicalGearSetLoadCase') -> '_3198.AGMAGleasonConicalGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3198.AGMAGleasonConicalGearSetPowerFlow)(method_result) if method_result else None

    def results_for_bevel_differential_gear(self, design_entity: '_2032.BevelDifferentialGear') -> '_3204.BevelDifferentialGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3204.BevelDifferentialGearPowerFlow)(method_result) if method_result else None

    def results_for_bevel_differential_gear_load_case(self, design_entity_analysis: '_6035.BevelDifferentialGearLoadCase') -> '_3204.BevelDifferentialGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3204.BevelDifferentialGearPowerFlow)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set(self, design_entity: '_2033.BevelDifferentialGearSet') -> '_3205.BevelDifferentialGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3205.BevelDifferentialGearSetPowerFlow)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set_load_case(self, design_entity_analysis: '_6037.BevelDifferentialGearSetLoadCase') -> '_3205.BevelDifferentialGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3205.BevelDifferentialGearSetPowerFlow)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2034.BevelDifferentialPlanetGear') -> '_3206.BevelDifferentialPlanetGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialPlanetGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3206.BevelDifferentialPlanetGearPowerFlow)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear_load_case(self, design_entity_analysis: '_6038.BevelDifferentialPlanetGearLoadCase') -> '_3206.BevelDifferentialPlanetGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialPlanetGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3206.BevelDifferentialPlanetGearPowerFlow)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2035.BevelDifferentialSunGear') -> '_3207.BevelDifferentialSunGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialSunGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3207.BevelDifferentialSunGearPowerFlow)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear_load_case(self, design_entity_analysis: '_6039.BevelDifferentialSunGearLoadCase') -> '_3207.BevelDifferentialSunGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialSunGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3207.BevelDifferentialSunGearPowerFlow)(method_result) if method_result else None

    def results_for_bevel_gear(self, design_entity: '_2036.BevelGear') -> '_3209.BevelGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BevelGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3209.BevelGearPowerFlow)(method_result) if method_result else None

    def results_for_bevel_gear_load_case(self, design_entity_analysis: '_6040.BevelGearLoadCase') -> '_3209.BevelGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BevelGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3209.BevelGearPowerFlow)(method_result) if method_result else None

    def results_for_bevel_gear_set(self, design_entity: '_2037.BevelGearSet') -> '_3210.BevelGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BevelGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3210.BevelGearSetPowerFlow)(method_result) if method_result else None

    def results_for_bevel_gear_set_load_case(self, design_entity_analysis: '_6042.BevelGearSetLoadCase') -> '_3210.BevelGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.BevelGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3210.BevelGearSetPowerFlow)(method_result) if method_result else None

    def results_for_conical_gear(self, design_entity: '_2040.ConicalGear') -> '_3225.ConicalGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConicalGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3225.ConicalGearPowerFlow)(method_result) if method_result else None

    def results_for_conical_gear_load_case(self, design_entity_analysis: '_6056.ConicalGearLoadCase') -> '_3225.ConicalGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConicalGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3225.ConicalGearPowerFlow)(method_result) if method_result else None

    def results_for_conical_gear_set(self, design_entity: '_2041.ConicalGearSet') -> '_3226.ConicalGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConicalGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3226.ConicalGearSetPowerFlow)(method_result) if method_result else None

    def results_for_conical_gear_set_load_case(self, design_entity_analysis: '_6060.ConicalGearSetLoadCase') -> '_3226.ConicalGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.ConicalGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3226.ConicalGearSetPowerFlow)(method_result) if method_result else None

    def results_for_cylindrical_gear(self, design_entity: '_2042.CylindricalGear') -> '_3237.CylindricalGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CylindricalGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3237.CylindricalGearPowerFlow)(method_result) if method_result else None

    def results_for_cylindrical_gear_load_case(self, design_entity_analysis: '_6069.CylindricalGearLoadCase') -> '_3237.CylindricalGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CylindricalGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3237.CylindricalGearPowerFlow)(method_result) if method_result else None

    def results_for_cylindrical_gear_set(self, design_entity: '_2043.CylindricalGearSet') -> '_3238.CylindricalGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CylindricalGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3238.CylindricalGearSetPowerFlow)(method_result) if method_result else None

    def results_for_cylindrical_gear_set_load_case(self, design_entity_analysis: '_6073.CylindricalGearSetLoadCase') -> '_3238.CylindricalGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CylindricalGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3238.CylindricalGearSetPowerFlow)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear(self, design_entity: '_2044.CylindricalPlanetGear') -> '_3239.CylindricalPlanetGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CylindricalPlanetGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3239.CylindricalPlanetGearPowerFlow)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear_load_case(self, design_entity_analysis: '_6074.CylindricalPlanetGearLoadCase') -> '_3239.CylindricalPlanetGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.CylindricalPlanetGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3239.CylindricalPlanetGearPowerFlow)(method_result) if method_result else None

    def results_for_gear(self, design_entity: '_2047.Gear') -> '_3247.GearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.GearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3247.GearPowerFlow)(method_result) if method_result else None

    def results_for_gear_load_case(self, design_entity_analysis: '_6096.GearLoadCase') -> '_3247.GearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.GearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3247.GearPowerFlow)(method_result) if method_result else None

    def results_for_gear_set(self, design_entity: '_2049.GearSet') -> '_3248.GearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.GearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3248.GearSetPowerFlow)(method_result) if method_result else None

    def results_for_gear_set_load_case(self, design_entity_analysis: '_6101.GearSetLoadCase') -> '_3248.GearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.GearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3248.GearSetPowerFlow)(method_result) if method_result else None

    def results_for_hypoid_gear(self, design_entity: '_2051.HypoidGear') -> '_3251.HypoidGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.HypoidGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3251.HypoidGearPowerFlow)(method_result) if method_result else None

    def results_for_hypoid_gear_load_case(self, design_entity_analysis: '_6111.HypoidGearLoadCase') -> '_3251.HypoidGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.HypoidGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3251.HypoidGearPowerFlow)(method_result) if method_result else None

    def results_for_hypoid_gear_set(self, design_entity: '_2052.HypoidGearSet') -> '_3252.HypoidGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.HypoidGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3252.HypoidGearSetPowerFlow)(method_result) if method_result else None

    def results_for_hypoid_gear_set_load_case(self, design_entity_analysis: '_6113.HypoidGearSetLoadCase') -> '_3252.HypoidGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.HypoidGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3252.HypoidGearSetPowerFlow)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2053.KlingelnbergCycloPalloidConicalGear') -> '_3256.KlingelnbergCycloPalloidConicalGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3256.KlingelnbergCycloPalloidConicalGearPowerFlow)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_load_case(self, design_entity_analysis: '_6117.KlingelnbergCycloPalloidConicalGearLoadCase') -> '_3256.KlingelnbergCycloPalloidConicalGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3256.KlingelnbergCycloPalloidConicalGearPowerFlow)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2054.KlingelnbergCycloPalloidConicalGearSet') -> '_3257.KlingelnbergCycloPalloidConicalGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3257.KlingelnbergCycloPalloidConicalGearSetPowerFlow)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set_load_case(self, design_entity_analysis: '_6119.KlingelnbergCycloPalloidConicalGearSetLoadCase') -> '_3257.KlingelnbergCycloPalloidConicalGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3257.KlingelnbergCycloPalloidConicalGearSetPowerFlow)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2055.KlingelnbergCycloPalloidHypoidGear') -> '_3259.KlingelnbergCycloPalloidHypoidGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3259.KlingelnbergCycloPalloidHypoidGearPowerFlow)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_load_case(self, design_entity_analysis: '_6120.KlingelnbergCycloPalloidHypoidGearLoadCase') -> '_3259.KlingelnbergCycloPalloidHypoidGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3259.KlingelnbergCycloPalloidHypoidGearPowerFlow)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2056.KlingelnbergCycloPalloidHypoidGearSet') -> '_3260.KlingelnbergCycloPalloidHypoidGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3260.KlingelnbergCycloPalloidHypoidGearSetPowerFlow)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self, design_entity_analysis: '_6122.KlingelnbergCycloPalloidHypoidGearSetLoadCase') -> '_3260.KlingelnbergCycloPalloidHypoidGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3260.KlingelnbergCycloPalloidHypoidGearSetPowerFlow)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2057.KlingelnbergCycloPalloidSpiralBevelGear') -> '_3262.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3262.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6123.KlingelnbergCycloPalloidSpiralBevelGearLoadCase') -> '_3262.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3262.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2058.KlingelnbergCycloPalloidSpiralBevelGearSet') -> '_3263.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3263.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6125.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase') -> '_3263.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3263.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow)(method_result) if method_result else None

    def results_for_planetary_gear_set(self, design_entity: '_2059.PlanetaryGearSet') -> '_3273.PlanetaryGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PlanetaryGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3273.PlanetaryGearSetPowerFlow)(method_result) if method_result else None

    def results_for_planetary_gear_set_load_case(self, design_entity_analysis: '_6138.PlanetaryGearSetLoadCase') -> '_3273.PlanetaryGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.PlanetaryGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3273.PlanetaryGearSetPowerFlow)(method_result) if method_result else None

    def results_for_spiral_bevel_gear(self, design_entity: '_2060.SpiralBevelGear') -> '_3289.SpiralBevelGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3289.SpiralBevelGearPowerFlow)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6156.SpiralBevelGearLoadCase') -> '_3289.SpiralBevelGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3289.SpiralBevelGearPowerFlow)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2061.SpiralBevelGearSet') -> '_3290.SpiralBevelGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3290.SpiralBevelGearSetPowerFlow)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6158.SpiralBevelGearSetLoadCase') -> '_3290.SpiralBevelGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3290.SpiralBevelGearSetPowerFlow)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2062.StraightBevelDiffGear') -> '_3295.StraightBevelDiffGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.StraightBevelDiffGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3295.StraightBevelDiffGearPowerFlow)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_load_case(self, design_entity_analysis: '_6163.StraightBevelDiffGearLoadCase') -> '_3295.StraightBevelDiffGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.StraightBevelDiffGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3295.StraightBevelDiffGearPowerFlow)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2063.StraightBevelDiffGearSet') -> '_3296.StraightBevelDiffGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.StraightBevelDiffGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3296.StraightBevelDiffGearSetPowerFlow)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set_load_case(self, design_entity_analysis: '_6165.StraightBevelDiffGearSetLoadCase') -> '_3296.StraightBevelDiffGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.StraightBevelDiffGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3296.StraightBevelDiffGearSetPowerFlow)(method_result) if method_result else None

    def results_for_straight_bevel_gear(self, design_entity: '_2064.StraightBevelGear') -> '_3298.StraightBevelGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.StraightBevelGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3298.StraightBevelGearPowerFlow)(method_result) if method_result else None

    def results_for_straight_bevel_gear_load_case(self, design_entity_analysis: '_6166.StraightBevelGearLoadCase') -> '_3298.StraightBevelGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.StraightBevelGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3298.StraightBevelGearPowerFlow)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set(self, design_entity: '_2065.StraightBevelGearSet') -> '_3299.StraightBevelGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.StraightBevelGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3299.StraightBevelGearSetPowerFlow)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set_load_case(self, design_entity_analysis: '_6168.StraightBevelGearSetLoadCase') -> '_3299.StraightBevelGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.StraightBevelGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3299.StraightBevelGearSetPowerFlow)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2066.StraightBevelPlanetGear') -> '_3300.StraightBevelPlanetGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.StraightBevelPlanetGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3300.StraightBevelPlanetGearPowerFlow)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear_load_case(self, design_entity_analysis: '_6169.StraightBevelPlanetGearLoadCase') -> '_3300.StraightBevelPlanetGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.StraightBevelPlanetGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3300.StraightBevelPlanetGearPowerFlow)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2067.StraightBevelSunGear') -> '_3301.StraightBevelSunGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.StraightBevelSunGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3301.StraightBevelSunGearPowerFlow)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear_load_case(self, design_entity_analysis: '_6170.StraightBevelSunGearLoadCase') -> '_3301.StraightBevelSunGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.StraightBevelSunGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3301.StraightBevelSunGearPowerFlow)(method_result) if method_result else None

    def results_for_worm_gear(self, design_entity: '_2068.WormGear') -> '_3314.WormGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.WormGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3314.WormGearPowerFlow)(method_result) if method_result else None

    def results_for_worm_gear_load_case(self, design_entity_analysis: '_6187.WormGearLoadCase') -> '_3314.WormGearPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.WormGearPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_3314.WormGearPowerFlow)(method_result) if method_result else None

    def results_for_worm_gear_set(self, design_entity: '_2069.WormGearSet') -> '_3315.WormGearSetPowerFlow':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.power_flows.WormGearSetPowerFlow
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_3315.WormGearSetPowerFlow)(method_result) if method_result else None
