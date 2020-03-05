'''_2140.py

GearWhineAnalysisAnalysis
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
from mastapy.system_model.analyses_and_results.gear_whine_analyses import (
    _5372, _5373, _5375, _5326,
    _5327, _5239, _5251, _5252,
    _5257, _5258, _5268, _5269,
    _5271, _5272, _5334, _5340,
    _5337, _5335, _5349, _5350,
    _5359, _5360, _5361, _5362,
    _5364, _5365, _5366, _5270,
    _5238, _5253, _5265, _5310,
    _5329, _5336, _5341, _5241,
    _5260, _5292, _5352, _5246,
    _5263, _5234, _5274, _5307,
    _5312, _5315, _5318, _5346,
    _5355, _5371, _5374, _5297,
    _5325, _5250, _5256, _5267,
    _5348, _5363, _5230, _5232,
    _5237, _5249, _5248, _5255,
    _5266, _5277, _5290, _5294,
    _5236, _5304, _5309, _5320,
    _5321, _5322, _5323, _5324,
    _5331, _5332, _5333, _5338,
    _5343, _5368, _5369, _5339,
    _5259, _5261, _5291, _5293,
    _5233, _5235, _5240, _5242,
    _5243, _5244, _5245, _5247,
    _5262, _5264, _5273, _5275,
    _5276, _5296, _5299, _5306,
    _5308, _5311, _5313, _5314,
    _5316, _5317, _5319, _5330,
    _5345, _5347, _5351, _5353,
    _5354, _5356, _5357, _5358,
    _5370
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

_GEAR_WHINE_ANALYSIS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'GearWhineAnalysisAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearWhineAnalysisAnalysis',)


class GearWhineAnalysisAnalysis(_2131.SingleAnalysis):
    '''GearWhineAnalysisAnalysis

    This is a mastapy class.
    '''

    TYPE = _GEAR_WHINE_ANALYSIS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearWhineAnalysisAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    def results_for_worm_gear_set_load_case(self, design_entity_analysis: '_6189.WormGearSetLoadCase') -> '_5372.WormGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.WormGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5372.WormGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear(self, design_entity: '_2070.ZerolBevelGear') -> '_5373.ZerolBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ZerolBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5373.ZerolBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_load_case(self, design_entity_analysis: '_6190.ZerolBevelGearLoadCase') -> '_5373.ZerolBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ZerolBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5373.ZerolBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2071.ZerolBevelGearSet') -> '_5375.ZerolBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ZerolBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5375.ZerolBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set_load_case(self, design_entity_analysis: '_6192.ZerolBevelGearSetLoadCase') -> '_5375.ZerolBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ZerolBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5375.ZerolBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2100.PartToPartShearCoupling') -> '_5326.PartToPartShearCouplingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartToPartShearCouplingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5326.PartToPartShearCouplingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_load_case(self, design_entity_analysis: '_6136.PartToPartShearCouplingLoadCase') -> '_5326.PartToPartShearCouplingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartToPartShearCouplingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5326.PartToPartShearCouplingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2101.PartToPartShearCouplingHalf') -> '_5327.PartToPartShearCouplingHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartToPartShearCouplingHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5327.PartToPartShearCouplingHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half_load_case(self, design_entity_analysis: '_6135.PartToPartShearCouplingHalfLoadCase') -> '_5327.PartToPartShearCouplingHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartToPartShearCouplingHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5327.PartToPartShearCouplingHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_drive(self, design_entity: '_2089.BeltDrive') -> '_5239.BeltDriveGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BeltDriveGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5239.BeltDriveGearWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_drive_load_case(self, design_entity_analysis: '_6034.BeltDriveLoadCase') -> '_5239.BeltDriveGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BeltDriveGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5239.BeltDriveGearWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch(self, design_entity: '_2091.Clutch') -> '_5251.ClutchGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ClutchGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5251.ClutchGearWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_load_case(self, design_entity_analysis: '_6047.ClutchLoadCase') -> '_5251.ClutchGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ClutchGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5251.ClutchGearWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_half(self, design_entity: '_2092.ClutchHalf') -> '_5252.ClutchHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ClutchHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5252.ClutchHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_half_load_case(self, design_entity_analysis: '_6046.ClutchHalfLoadCase') -> '_5252.ClutchHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ClutchHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5252.ClutchHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling(self, design_entity: '_2094.ConceptCoupling') -> '_5257.ConceptCouplingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptCouplingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5257.ConceptCouplingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_load_case(self, design_entity_analysis: '_6052.ConceptCouplingLoadCase') -> '_5257.ConceptCouplingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptCouplingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5257.ConceptCouplingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_half(self, design_entity: '_2095.ConceptCouplingHalf') -> '_5258.ConceptCouplingHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptCouplingHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5258.ConceptCouplingHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_half_load_case(self, design_entity_analysis: '_6051.ConceptCouplingHalfLoadCase') -> '_5258.ConceptCouplingHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptCouplingHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5258.ConceptCouplingHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling(self, design_entity: '_2096.Coupling') -> '_5268.CouplingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CouplingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5268.CouplingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_load_case(self, design_entity_analysis: '_6065.CouplingLoadCase') -> '_5268.CouplingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CouplingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5268.CouplingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_half(self, design_entity: '_2097.CouplingHalf') -> '_5269.CouplingHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CouplingHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5269.CouplingHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_half_load_case(self, design_entity_analysis: '_6064.CouplingHalfLoadCase') -> '_5269.CouplingHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CouplingHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5269.CouplingHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt(self, design_entity: '_2098.CVT') -> '_5271.CVTGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CVTGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5271.CVTGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_load_case(self, design_entity_analysis: '_6067.CVTLoadCase') -> '_5271.CVTGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CVTGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5271.CVTGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_pulley(self, design_entity: '_2099.CVTPulley') -> '_5272.CVTPulleyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CVTPulleyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5272.CVTPulleyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_pulley_load_case(self, design_entity_analysis: '_6068.CVTPulleyLoadCase') -> '_5272.CVTPulleyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CVTPulleyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5272.CVTPulleyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_pulley(self, design_entity: '_2102.Pulley') -> '_5334.PulleyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PulleyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5334.PulleyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_pulley_load_case(self, design_entity_analysis: '_6145.PulleyLoadCase') -> '_5334.PulleyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PulleyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5334.PulleyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_hub_connection(self, design_entity: '_2110.ShaftHubConnection') -> '_5340.ShaftHubConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ShaftHubConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5340.ShaftHubConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_hub_connection_load_case(self, design_entity_analysis: '_6151.ShaftHubConnectionLoadCase') -> '_5340.ShaftHubConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ShaftHubConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5340.ShaftHubConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring(self, design_entity: '_2108.RollingRing') -> '_5337.RollingRingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RollingRingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5337.RollingRingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_load_case(self, design_entity_analysis: '_6149.RollingRingLoadCase') -> '_5337.RollingRingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RollingRingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5337.RollingRingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_assembly(self, design_entity: '_2109.RollingRingAssembly') -> '_5335.RollingRingAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RollingRingAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5335.RollingRingAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_assembly_load_case(self, design_entity_analysis: '_6147.RollingRingAssemblyLoadCase') -> '_5335.RollingRingAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RollingRingAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5335.RollingRingAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper(self, design_entity: '_2111.SpringDamper') -> '_5349.SpringDamperGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpringDamperGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5349.SpringDamperGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_load_case(self, design_entity_analysis: '_6161.SpringDamperLoadCase') -> '_5349.SpringDamperGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpringDamperGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5349.SpringDamperGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_half(self, design_entity: '_2112.SpringDamperHalf') -> '_5350.SpringDamperHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpringDamperHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5350.SpringDamperHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_half_load_case(self, design_entity_analysis: '_6160.SpringDamperHalfLoadCase') -> '_5350.SpringDamperHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpringDamperHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5350.SpringDamperHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser(self, design_entity: '_2113.Synchroniser') -> '_5359.SynchroniserGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5359.SynchroniserGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_load_case(self, design_entity_analysis: '_6172.SynchroniserLoadCase') -> '_5359.SynchroniserGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5359.SynchroniserGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_half(self, design_entity: '_2115.SynchroniserHalf') -> '_5360.SynchroniserHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5360.SynchroniserHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_half_load_case(self, design_entity_analysis: '_6171.SynchroniserHalfLoadCase') -> '_5360.SynchroniserHalfGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserHalfGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5360.SynchroniserHalfGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_part(self, design_entity: '_2116.SynchroniserPart') -> '_5361.SynchroniserPartGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserPartGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5361.SynchroniserPartGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_part_load_case(self, design_entity_analysis: '_6173.SynchroniserPartLoadCase') -> '_5361.SynchroniserPartGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserPartGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5361.SynchroniserPartGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_sleeve(self, design_entity: '_2117.SynchroniserSleeve') -> '_5362.SynchroniserSleeveGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserSleeveGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5362.SynchroniserSleeveGearWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_sleeve_load_case(self, design_entity_analysis: '_6174.SynchroniserSleeveLoadCase') -> '_5362.SynchroniserSleeveGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SynchroniserSleeveGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5362.SynchroniserSleeveGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter(self, design_entity: '_2118.TorqueConverter') -> '_5364.TorqueConverterGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5364.TorqueConverterGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_load_case(self, design_entity_analysis: '_6178.TorqueConverterLoadCase') -> '_5364.TorqueConverterGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5364.TorqueConverterGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_pump(self, design_entity: '_2119.TorqueConverterPump') -> '_5365.TorqueConverterPumpGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterPumpGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5365.TorqueConverterPumpGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_pump_load_case(self, design_entity_analysis: '_6179.TorqueConverterPumpLoadCase') -> '_5365.TorqueConverterPumpGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterPumpGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5365.TorqueConverterPumpGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_turbine(self, design_entity: '_2121.TorqueConverterTurbine') -> '_5366.TorqueConverterTurbineGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterTurbineGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5366.TorqueConverterTurbineGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_turbine_load_case(self, design_entity_analysis: '_6180.TorqueConverterTurbineLoadCase') -> '_5366.TorqueConverterTurbineGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterTurbineGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5366.TorqueConverterTurbineGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_belt_connection(self, design_entity: '_1816.CVTBeltConnection') -> '_5270.CVTBeltConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CVTBeltConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5270.CVTBeltConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_belt_connection_load_case(self, design_entity_analysis: '_6066.CVTBeltConnectionLoadCase') -> '_5270.CVTBeltConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CVTBeltConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5270.CVTBeltConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_connection(self, design_entity: '_1811.BeltConnection') -> '_5238.BeltConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BeltConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5238.BeltConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_connection_load_case(self, design_entity_analysis: '_6033.BeltConnectionLoadCase') -> '_5238.BeltConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BeltConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5238.BeltConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coaxial_connection(self, design_entity: '_1812.CoaxialConnection') -> '_5253.CoaxialConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CoaxialConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5253.CoaxialConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coaxial_connection_load_case(self, design_entity_analysis: '_6048.CoaxialConnectionLoadCase') -> '_5253.CoaxialConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CoaxialConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5253.CoaxialConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_connection(self, design_entity: '_1815.Connection') -> '_5265.ConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5265.ConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_connection_load_case(self, design_entity_analysis: '_6061.ConnectionLoadCase') -> '_5265.ConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5265.ConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection(self, design_entity: '_1824.InterMountableComponentConnection') -> '_5310.InterMountableComponentConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.InterMountableComponentConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5310.InterMountableComponentConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection_load_case(self, design_entity_analysis: '_6116.InterMountableComponentConnectionLoadCase') -> '_5310.InterMountableComponentConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.InterMountableComponentConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5310.InterMountableComponentConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_connection(self, design_entity: '_1827.PlanetaryConnection') -> '_5329.PlanetaryConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PlanetaryConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5329.PlanetaryConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_connection_load_case(self, design_entity_analysis: '_6137.PlanetaryConnectionLoadCase') -> '_5329.PlanetaryConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PlanetaryConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5329.PlanetaryConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_connection(self, design_entity: '_1831.RollingRingConnection') -> '_5336.RollingRingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RollingRingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5336.RollingRingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_connection_load_case(self, design_entity_analysis: '_6148.RollingRingConnectionLoadCase') -> '_5336.RollingRingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RollingRingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5336.RollingRingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1835.ShaftToMountableComponentConnection') -> '_5341.ShaftToMountableComponentConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ShaftToMountableComponentConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5341.ShaftToMountableComponentConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection_load_case(self, design_entity_analysis: '_6153.ShaftToMountableComponentConnectionLoadCase') -> '_5341.ShaftToMountableComponentConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ShaftToMountableComponentConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5341.ShaftToMountableComponentConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1841.BevelDifferentialGearMesh') -> '_5241.BevelDifferentialGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5241.BevelDifferentialGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh_load_case(self, design_entity_analysis: '_6036.BevelDifferentialGearMeshLoadCase') -> '_5241.BevelDifferentialGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5241.BevelDifferentialGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_mesh(self, design_entity: '_1845.ConceptGearMesh') -> '_5260.ConceptGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5260.ConceptGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_mesh_load_case(self, design_entity_analysis: '_6054.ConceptGearMeshLoadCase') -> '_5260.ConceptGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5260.ConceptGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_mesh(self, design_entity: '_1851.FaceGearMesh') -> '_5292.FaceGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FaceGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5292.FaceGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_mesh_load_case(self, design_entity_analysis: '_6092.FaceGearMeshLoadCase') -> '_5292.FaceGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FaceGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5292.FaceGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1865.StraightBevelDiffGearMesh') -> '_5352.StraightBevelDiffGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelDiffGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5352.StraightBevelDiffGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh_load_case(self, design_entity_analysis: '_6164.StraightBevelDiffGearMeshLoadCase') -> '_5352.StraightBevelDiffGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelDiffGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5352.StraightBevelDiffGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_mesh(self, design_entity: '_1843.BevelGearMesh') -> '_5246.BevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5246.BevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6041.BevelGearMeshLoadCase') -> '_5246.BevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5246.BevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_mesh(self, design_entity: '_1847.ConicalGearMesh') -> '_5263.ConicalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConicalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5263.ConicalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_mesh_load_case(self, design_entity_analysis: '_6058.ConicalGearMeshLoadCase') -> '_5263.ConicalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConicalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5263.ConicalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1839.AGMAGleasonConicalGearMesh') -> '_5234.AGMAGleasonConicalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AGMAGleasonConicalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5234.AGMAGleasonConicalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh_load_case(self, design_entity_analysis: '_6028.AGMAGleasonConicalGearMeshLoadCase') -> '_5234.AGMAGleasonConicalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AGMAGleasonConicalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5234.AGMAGleasonConicalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1849.CylindricalGearMesh') -> '_5274.CylindricalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5274.CylindricalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh_load_case(self, design_entity_analysis: '_6071.CylindricalGearMeshLoadCase') -> '_5274.CylindricalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5274.CylindricalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh(self, design_entity: '_1855.HypoidGearMesh') -> '_5307.HypoidGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.HypoidGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5307.HypoidGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6112.HypoidGearMeshLoadCase') -> '_5307.HypoidGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.HypoidGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5307.HypoidGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1858.KlingelnbergCycloPalloidConicalGearMesh') -> '_5312.KlingelnbergCycloPalloidConicalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidConicalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5312.KlingelnbergCycloPalloidConicalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self, design_entity_analysis: '_6118.KlingelnbergCycloPalloidConicalGearMeshLoadCase') -> '_5312.KlingelnbergCycloPalloidConicalGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidConicalGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5312.KlingelnbergCycloPalloidConicalGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1859.KlingelnbergCycloPalloidHypoidGearMesh') -> '_5315.KlingelnbergCycloPalloidHypoidGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidHypoidGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5315.KlingelnbergCycloPalloidHypoidGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6121.KlingelnbergCycloPalloidHypoidGearMeshLoadCase') -> '_5315.KlingelnbergCycloPalloidHypoidGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidHypoidGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5315.KlingelnbergCycloPalloidHypoidGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1860.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> '_5318.KlingelnbergCycloPalloidSpiralBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5318.KlingelnbergCycloPalloidSpiralBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6124.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase') -> '_5318.KlingelnbergCycloPalloidSpiralBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5318.KlingelnbergCycloPalloidSpiralBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1863.SpiralBevelGearMesh') -> '_5346.SpiralBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpiralBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5346.SpiralBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6157.SpiralBevelGearMeshLoadCase') -> '_5346.SpiralBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpiralBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5346.SpiralBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1867.StraightBevelGearMesh') -> '_5355.StraightBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5355.StraightBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6167.StraightBevelGearMeshLoadCase') -> '_5355.StraightBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5355.StraightBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_mesh(self, design_entity: '_1869.WormGearMesh') -> '_5371.WormGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.WormGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5371.WormGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_mesh_load_case(self, design_entity_analysis: '_6188.WormGearMeshLoadCase') -> '_5371.WormGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.WormGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5371.WormGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1871.ZerolBevelGearMesh') -> '_5374.ZerolBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ZerolBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5374.ZerolBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6191.ZerolBevelGearMeshLoadCase') -> '_5374.ZerolBevelGearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ZerolBevelGearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5374.ZerolBevelGearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_mesh(self, design_entity: '_1853.GearMesh') -> '_5297.GearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5297.GearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_mesh_load_case(self, design_entity_analysis: '_6098.GearMeshLoadCase') -> '_5297.GearMeshGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GearMeshGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5297.GearMeshGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_1879.PartToPartShearCouplingConnection') -> '_5325.PartToPartShearCouplingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartToPartShearCouplingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5325.PartToPartShearCouplingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection_load_case(self, design_entity_analysis: '_6134.PartToPartShearCouplingConnectionLoadCase') -> '_5325.PartToPartShearCouplingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartToPartShearCouplingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5325.PartToPartShearCouplingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_connection(self, design_entity: '_1873.ClutchConnection') -> '_5250.ClutchConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ClutchConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5250.ClutchConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_connection_load_case(self, design_entity_analysis: '_6045.ClutchConnectionLoadCase') -> '_5250.ClutchConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ClutchConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5250.ClutchConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_connection(self, design_entity: '_1875.ConceptCouplingConnection') -> '_5256.ConceptCouplingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptCouplingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5256.ConceptCouplingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_connection_load_case(self, design_entity_analysis: '_6050.ConceptCouplingConnectionLoadCase') -> '_5256.ConceptCouplingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptCouplingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5256.ConceptCouplingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_connection(self, design_entity: '_1877.CouplingConnection') -> '_5267.CouplingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CouplingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5267.CouplingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_connection_load_case(self, design_entity_analysis: '_6063.CouplingConnectionLoadCase') -> '_5267.CouplingConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CouplingConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5267.CouplingConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_connection(self, design_entity: '_1881.SpringDamperConnection') -> '_5348.SpringDamperConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpringDamperConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5348.SpringDamperConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_connection_load_case(self, design_entity_analysis: '_6159.SpringDamperConnectionLoadCase') -> '_5348.SpringDamperConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpringDamperConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5348.SpringDamperConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_connection(self, design_entity: '_1883.TorqueConverterConnection') -> '_5363.TorqueConverterConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5363.TorqueConverterConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_connection_load_case(self, design_entity_analysis: '_6177.TorqueConverterConnectionLoadCase') -> '_5363.TorqueConverterConnectionGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.TorqueConverterConnectionGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5363.TorqueConverterConnectionGearWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_assembly(self, design_entity: '_1959.AbstractAssembly') -> '_5230.AbstractAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AbstractAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5230.AbstractAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_assembly_load_case(self, design_entity_analysis: '_6024.AbstractAssemblyLoadCase') -> '_5230.AbstractAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AbstractAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5230.AbstractAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing(self, design_entity: '_1960.AbstractShaftOrHousing') -> '_5232.AbstractShaftOrHousingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AbstractShaftOrHousingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5232.AbstractShaftOrHousingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing_load_case(self, design_entity_analysis: '_6025.AbstractShaftOrHousingLoadCase') -> '_5232.AbstractShaftOrHousingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AbstractShaftOrHousingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5232.AbstractShaftOrHousingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bearing(self, design_entity: '_1963.Bearing') -> '_5237.BearingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BearingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5237.BearingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bearing_load_case(self, design_entity_analysis: '_6032.BearingLoadCase') -> '_5237.BearingGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BearingGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5237.BearingGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bolt(self, design_entity: '_1965.Bolt') -> '_5249.BoltGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BoltGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5249.BoltGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bolt_load_case(self, design_entity_analysis: '_6044.BoltLoadCase') -> '_5249.BoltGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BoltGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5249.BoltGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bolted_joint(self, design_entity: '_1966.BoltedJoint') -> '_5248.BoltedJointGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BoltedJointGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5248.BoltedJointGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bolted_joint_load_case(self, design_entity_analysis: '_6043.BoltedJointLoadCase') -> '_5248.BoltedJointGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BoltedJointGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5248.BoltedJointGearWhineAnalysis)(method_result) if method_result else None

    def results_for_component(self, design_entity: '_1967.Component') -> '_5255.ComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5255.ComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_component_load_case(self, design_entity_analysis: '_6049.ComponentLoadCase') -> '_5255.ComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5255.ComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_connector(self, design_entity: '_1970.Connector') -> '_5266.ConnectorGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConnectorGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5266.ConnectorGearWhineAnalysis)(method_result) if method_result else None

    def results_for_connector_load_case(self, design_entity_analysis: '_6062.ConnectorLoadCase') -> '_5266.ConnectorGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConnectorGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5266.ConnectorGearWhineAnalysis)(method_result) if method_result else None

    def results_for_datum(self, design_entity: '_1971.Datum') -> '_5277.DatumGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.DatumGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5277.DatumGearWhineAnalysis)(method_result) if method_result else None

    def results_for_datum_load_case(self, design_entity_analysis: '_6077.DatumLoadCase') -> '_5277.DatumGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.DatumGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5277.DatumGearWhineAnalysis)(method_result) if method_result else None

    def results_for_external_cad_model(self, design_entity: '_1974.ExternalCADModel') -> '_5290.ExternalCADModelGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ExternalCADModelGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5290.ExternalCADModelGearWhineAnalysis)(method_result) if method_result else None

    def results_for_external_cad_model_load_case(self, design_entity_analysis: '_6090.ExternalCADModelLoadCase') -> '_5290.ExternalCADModelGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ExternalCADModelGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5290.ExternalCADModelGearWhineAnalysis)(method_result) if method_result else None

    def results_for_flexible_pin_assembly(self, design_entity: '_1975.FlexiblePinAssembly') -> '_5294.FlexiblePinAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FlexiblePinAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5294.FlexiblePinAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_flexible_pin_assembly_load_case(self, design_entity_analysis: '_6094.FlexiblePinAssemblyLoadCase') -> '_5294.FlexiblePinAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FlexiblePinAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5294.FlexiblePinAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_assembly(self, design_entity: '_1958.Assembly') -> '_5236.AssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5236.AssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_assembly_load_case(self, design_entity_analysis: '_6031.AssemblyLoadCase') -> '_5236.AssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5236.AssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_guide_dxf_model(self, design_entity: '_1976.GuideDxfModel') -> '_5304.GuideDxfModelGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GuideDxfModelGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5304.GuideDxfModelGearWhineAnalysis)(method_result) if method_result else None

    def results_for_guide_dxf_model_load_case(self, design_entity_analysis: '_6102.GuideDxfModelLoadCase') -> '_5304.GuideDxfModelGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GuideDxfModelGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5304.GuideDxfModelGearWhineAnalysis)(method_result) if method_result else None

    def results_for_imported_fe_component(self, design_entity: '_1979.ImportedFEComponent') -> '_5309.ImportedFEComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ImportedFEComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5309.ImportedFEComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_imported_fe_component_load_case(self, design_entity_analysis: '_6114.ImportedFEComponentLoadCase') -> '_5309.ImportedFEComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ImportedFEComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ImportedFEComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5309.ImportedFEComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_mass_disc(self, design_entity: '_1982.MassDisc') -> '_5320.MassDiscGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.MassDiscGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5320.MassDiscGearWhineAnalysis)(method_result) if method_result else None

    def results_for_mass_disc_load_case(self, design_entity_analysis: '_6126.MassDiscLoadCase') -> '_5320.MassDiscGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.MassDiscGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5320.MassDiscGearWhineAnalysis)(method_result) if method_result else None

    def results_for_measurement_component(self, design_entity: '_1983.MeasurementComponent') -> '_5321.MeasurementComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.MeasurementComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5321.MeasurementComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_measurement_component_load_case(self, design_entity_analysis: '_6127.MeasurementComponentLoadCase') -> '_5321.MeasurementComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.MeasurementComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5321.MeasurementComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_mountable_component(self, design_entity: '_1984.MountableComponent') -> '_5322.MountableComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.MountableComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5322.MountableComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_mountable_component_load_case(self, design_entity_analysis: '_6129.MountableComponentLoadCase') -> '_5322.MountableComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.MountableComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5322.MountableComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_oil_seal(self, design_entity: '_1986.OilSeal') -> '_5323.OilSealGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.OilSealGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5323.OilSealGearWhineAnalysis)(method_result) if method_result else None

    def results_for_oil_seal_load_case(self, design_entity_analysis: '_6131.OilSealLoadCase') -> '_5323.OilSealGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.OilSealGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5323.OilSealGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part(self, design_entity: '_1987.Part') -> '_5324.PartGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5324.PartGearWhineAnalysis)(method_result) if method_result else None

    def results_for_part_load_case(self, design_entity_analysis: '_6133.PartLoadCase') -> '_5324.PartGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PartGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5324.PartGearWhineAnalysis)(method_result) if method_result else None

    def results_for_planet_carrier(self, design_entity: '_1988.PlanetCarrier') -> '_5331.PlanetCarrierGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PlanetCarrierGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5331.PlanetCarrierGearWhineAnalysis)(method_result) if method_result else None

    def results_for_planet_carrier_load_case(self, design_entity_analysis: '_6140.PlanetCarrierLoadCase') -> '_5331.PlanetCarrierGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PlanetCarrierGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5331.PlanetCarrierGearWhineAnalysis)(method_result) if method_result else None

    def results_for_point_load(self, design_entity: '_1990.PointLoad') -> '_5332.PointLoadGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PointLoadGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5332.PointLoadGearWhineAnalysis)(method_result) if method_result else None

    def results_for_point_load_load_case(self, design_entity_analysis: '_6143.PointLoadLoadCase') -> '_5332.PointLoadGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PointLoadGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5332.PointLoadGearWhineAnalysis)(method_result) if method_result else None

    def results_for_power_load(self, design_entity: '_1991.PowerLoad') -> '_5333.PowerLoadGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PowerLoadGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5333.PowerLoadGearWhineAnalysis)(method_result) if method_result else None

    def results_for_power_load_load_case(self, design_entity_analysis: '_6144.PowerLoadLoadCase') -> '_5333.PowerLoadGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PowerLoadGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5333.PowerLoadGearWhineAnalysis)(method_result) if method_result else None

    def results_for_root_assembly(self, design_entity: '_1993.RootAssembly') -> '_5338.RootAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RootAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5338.RootAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_root_assembly_load_case(self, design_entity_analysis: '_6150.RootAssemblyLoadCase') -> '_5338.RootAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.RootAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5338.RootAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_specialised_assembly(self, design_entity: '_1995.SpecialisedAssembly') -> '_5343.SpecialisedAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpecialisedAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5343.SpecialisedAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_specialised_assembly_load_case(self, design_entity_analysis: '_6154.SpecialisedAssemblyLoadCase') -> '_5343.SpecialisedAssemblyGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpecialisedAssemblyGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5343.SpecialisedAssemblyGearWhineAnalysis)(method_result) if method_result else None

    def results_for_unbalanced_mass(self, design_entity: '_1996.UnbalancedMass') -> '_5368.UnbalancedMassGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.UnbalancedMassGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5368.UnbalancedMassGearWhineAnalysis)(method_result) if method_result else None

    def results_for_unbalanced_mass_load_case(self, design_entity_analysis: '_6185.UnbalancedMassLoadCase') -> '_5368.UnbalancedMassGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.UnbalancedMassGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5368.UnbalancedMassGearWhineAnalysis)(method_result) if method_result else None

    def results_for_virtual_component(self, design_entity: '_1997.VirtualComponent') -> '_5369.VirtualComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.VirtualComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5369.VirtualComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_virtual_component_load_case(self, design_entity_analysis: '_6186.VirtualComponentLoadCase') -> '_5369.VirtualComponentGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.VirtualComponentGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5369.VirtualComponentGearWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft(self, design_entity: '_2000.Shaft') -> '_5339.ShaftGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ShaftGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5339.ShaftGearWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_load_case(self, design_entity_analysis: '_6152.ShaftLoadCase') -> '_5339.ShaftGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ShaftGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5339.ShaftGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear(self, design_entity: '_2038.ConceptGear') -> '_5259.ConceptGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5259.ConceptGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_load_case(self, design_entity_analysis: '_6053.ConceptGearLoadCase') -> '_5259.ConceptGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5259.ConceptGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_set(self, design_entity: '_2039.ConceptGearSet') -> '_5261.ConceptGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5261.ConceptGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_set_load_case(self, design_entity_analysis: '_6055.ConceptGearSetLoadCase') -> '_5261.ConceptGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConceptGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5261.ConceptGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear(self, design_entity: '_2045.FaceGear') -> '_5291.FaceGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FaceGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5291.FaceGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_load_case(self, design_entity_analysis: '_6091.FaceGearLoadCase') -> '_5291.FaceGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FaceGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5291.FaceGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_set(self, design_entity: '_2046.FaceGearSet') -> '_5293.FaceGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FaceGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5293.FaceGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_set_load_case(self, design_entity_analysis: '_6093.FaceGearSetLoadCase') -> '_5293.FaceGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.FaceGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5293.FaceGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2030.AGMAGleasonConicalGear') -> '_5233.AGMAGleasonConicalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AGMAGleasonConicalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5233.AGMAGleasonConicalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_load_case(self, design_entity_analysis: '_6027.AGMAGleasonConicalGearLoadCase') -> '_5233.AGMAGleasonConicalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AGMAGleasonConicalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5233.AGMAGleasonConicalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2031.AGMAGleasonConicalGearSet') -> '_5235.AGMAGleasonConicalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AGMAGleasonConicalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5235.AGMAGleasonConicalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set_load_case(self, design_entity_analysis: '_6029.AGMAGleasonConicalGearSetLoadCase') -> '_5235.AGMAGleasonConicalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.AGMAGleasonConicalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5235.AGMAGleasonConicalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear(self, design_entity: '_2032.BevelDifferentialGear') -> '_5240.BevelDifferentialGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5240.BevelDifferentialGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_load_case(self, design_entity_analysis: '_6035.BevelDifferentialGearLoadCase') -> '_5240.BevelDifferentialGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5240.BevelDifferentialGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set(self, design_entity: '_2033.BevelDifferentialGearSet') -> '_5242.BevelDifferentialGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5242.BevelDifferentialGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set_load_case(self, design_entity_analysis: '_6037.BevelDifferentialGearSetLoadCase') -> '_5242.BevelDifferentialGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5242.BevelDifferentialGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2034.BevelDifferentialPlanetGear') -> '_5243.BevelDifferentialPlanetGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialPlanetGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5243.BevelDifferentialPlanetGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear_load_case(self, design_entity_analysis: '_6038.BevelDifferentialPlanetGearLoadCase') -> '_5243.BevelDifferentialPlanetGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialPlanetGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5243.BevelDifferentialPlanetGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2035.BevelDifferentialSunGear') -> '_5244.BevelDifferentialSunGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialSunGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5244.BevelDifferentialSunGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear_load_case(self, design_entity_analysis: '_6039.BevelDifferentialSunGearLoadCase') -> '_5244.BevelDifferentialSunGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelDifferentialSunGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5244.BevelDifferentialSunGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear(self, design_entity: '_2036.BevelGear') -> '_5245.BevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5245.BevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_load_case(self, design_entity_analysis: '_6040.BevelGearLoadCase') -> '_5245.BevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5245.BevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_set(self, design_entity: '_2037.BevelGearSet') -> '_5247.BevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5247.BevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_set_load_case(self, design_entity_analysis: '_6042.BevelGearSetLoadCase') -> '_5247.BevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.BevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5247.BevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear(self, design_entity: '_2040.ConicalGear') -> '_5262.ConicalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConicalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5262.ConicalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_load_case(self, design_entity_analysis: '_6056.ConicalGearLoadCase') -> '_5262.ConicalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConicalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5262.ConicalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_set(self, design_entity: '_2041.ConicalGearSet') -> '_5264.ConicalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConicalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5264.ConicalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_set_load_case(self, design_entity_analysis: '_6060.ConicalGearSetLoadCase') -> '_5264.ConicalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.ConicalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5264.ConicalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear(self, design_entity: '_2042.CylindricalGear') -> '_5273.CylindricalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5273.CylindricalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_load_case(self, design_entity_analysis: '_6069.CylindricalGearLoadCase') -> '_5273.CylindricalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5273.CylindricalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_set(self, design_entity: '_2043.CylindricalGearSet') -> '_5275.CylindricalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5275.CylindricalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_set_load_case(self, design_entity_analysis: '_6073.CylindricalGearSetLoadCase') -> '_5275.CylindricalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5275.CylindricalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear(self, design_entity: '_2044.CylindricalPlanetGear') -> '_5276.CylindricalPlanetGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalPlanetGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5276.CylindricalPlanetGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear_load_case(self, design_entity_analysis: '_6074.CylindricalPlanetGearLoadCase') -> '_5276.CylindricalPlanetGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.CylindricalPlanetGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5276.CylindricalPlanetGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_gear(self, design_entity: '_2047.Gear') -> '_5296.GearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5296.GearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_load_case(self, design_entity_analysis: '_6096.GearLoadCase') -> '_5296.GearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5296.GearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_set(self, design_entity: '_2049.GearSet') -> '_5299.GearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5299.GearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_set_load_case(self, design_entity_analysis: '_6101.GearSetLoadCase') -> '_5299.GearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.GearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5299.GearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear(self, design_entity: '_2051.HypoidGear') -> '_5306.HypoidGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.HypoidGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5306.HypoidGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_load_case(self, design_entity_analysis: '_6111.HypoidGearLoadCase') -> '_5306.HypoidGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.HypoidGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5306.HypoidGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_set(self, design_entity: '_2052.HypoidGearSet') -> '_5308.HypoidGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.HypoidGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5308.HypoidGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_set_load_case(self, design_entity_analysis: '_6113.HypoidGearSetLoadCase') -> '_5308.HypoidGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.HypoidGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5308.HypoidGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2053.KlingelnbergCycloPalloidConicalGear') -> '_5311.KlingelnbergCycloPalloidConicalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidConicalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5311.KlingelnbergCycloPalloidConicalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_load_case(self, design_entity_analysis: '_6117.KlingelnbergCycloPalloidConicalGearLoadCase') -> '_5311.KlingelnbergCycloPalloidConicalGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidConicalGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5311.KlingelnbergCycloPalloidConicalGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2054.KlingelnbergCycloPalloidConicalGearSet') -> '_5313.KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5313.KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set_load_case(self, design_entity_analysis: '_6119.KlingelnbergCycloPalloidConicalGearSetLoadCase') -> '_5313.KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5313.KlingelnbergCycloPalloidConicalGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2055.KlingelnbergCycloPalloidHypoidGear') -> '_5314.KlingelnbergCycloPalloidHypoidGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidHypoidGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5314.KlingelnbergCycloPalloidHypoidGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_load_case(self, design_entity_analysis: '_6120.KlingelnbergCycloPalloidHypoidGearLoadCase') -> '_5314.KlingelnbergCycloPalloidHypoidGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidHypoidGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5314.KlingelnbergCycloPalloidHypoidGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2056.KlingelnbergCycloPalloidHypoidGearSet') -> '_5316.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5316.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self, design_entity_analysis: '_6122.KlingelnbergCycloPalloidHypoidGearSetLoadCase') -> '_5316.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5316.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2057.KlingelnbergCycloPalloidSpiralBevelGear') -> '_5317.KlingelnbergCycloPalloidSpiralBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5317.KlingelnbergCycloPalloidSpiralBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6123.KlingelnbergCycloPalloidSpiralBevelGearLoadCase') -> '_5317.KlingelnbergCycloPalloidSpiralBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5317.KlingelnbergCycloPalloidSpiralBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2058.KlingelnbergCycloPalloidSpiralBevelGearSet') -> '_5319.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5319.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6125.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase') -> '_5319.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5319.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_gear_set(self, design_entity: '_2059.PlanetaryGearSet') -> '_5330.PlanetaryGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PlanetaryGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5330.PlanetaryGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_gear_set_load_case(self, design_entity_analysis: '_6138.PlanetaryGearSetLoadCase') -> '_5330.PlanetaryGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.PlanetaryGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5330.PlanetaryGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear(self, design_entity: '_2060.SpiralBevelGear') -> '_5345.SpiralBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpiralBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5345.SpiralBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6156.SpiralBevelGearLoadCase') -> '_5345.SpiralBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpiralBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5345.SpiralBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2061.SpiralBevelGearSet') -> '_5347.SpiralBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpiralBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5347.SpiralBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6158.SpiralBevelGearSetLoadCase') -> '_5347.SpiralBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.SpiralBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5347.SpiralBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2062.StraightBevelDiffGear') -> '_5351.StraightBevelDiffGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelDiffGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5351.StraightBevelDiffGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_load_case(self, design_entity_analysis: '_6163.StraightBevelDiffGearLoadCase') -> '_5351.StraightBevelDiffGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelDiffGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5351.StraightBevelDiffGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2063.StraightBevelDiffGearSet') -> '_5353.StraightBevelDiffGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelDiffGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5353.StraightBevelDiffGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set_load_case(self, design_entity_analysis: '_6165.StraightBevelDiffGearSetLoadCase') -> '_5353.StraightBevelDiffGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelDiffGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5353.StraightBevelDiffGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear(self, design_entity: '_2064.StraightBevelGear') -> '_5354.StraightBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5354.StraightBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_load_case(self, design_entity_analysis: '_6166.StraightBevelGearLoadCase') -> '_5354.StraightBevelGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5354.StraightBevelGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set(self, design_entity: '_2065.StraightBevelGearSet') -> '_5356.StraightBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5356.StraightBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set_load_case(self, design_entity_analysis: '_6168.StraightBevelGearSetLoadCase') -> '_5356.StraightBevelGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5356.StraightBevelGearSetGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2066.StraightBevelPlanetGear') -> '_5357.StraightBevelPlanetGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelPlanetGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5357.StraightBevelPlanetGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear_load_case(self, design_entity_analysis: '_6169.StraightBevelPlanetGearLoadCase') -> '_5357.StraightBevelPlanetGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelPlanetGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5357.StraightBevelPlanetGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2067.StraightBevelSunGear') -> '_5358.StraightBevelSunGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelSunGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5358.StraightBevelSunGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear_load_case(self, design_entity_analysis: '_6170.StraightBevelSunGearLoadCase') -> '_5358.StraightBevelSunGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.StraightBevelSunGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5358.StraightBevelSunGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear(self, design_entity: '_2068.WormGear') -> '_5370.WormGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.WormGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5370.WormGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_load_case(self, design_entity_analysis: '_6187.WormGearLoadCase') -> '_5370.WormGearGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.WormGearGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5370.WormGearGearWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_set(self, design_entity: '_2069.WormGearSet') -> '_5372.WormGearSetGearWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.WormGearSetGearWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5372.WormGearSetGearWhineAnalysis)(method_result) if method_result else None
