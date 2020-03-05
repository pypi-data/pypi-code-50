'''_2093.py

SingleMeshWhineAnalysisAnalysis
'''


from mastapy.system_model.analyses_and_results.static_loads import (
    _6034, _6035, _6037, _5886,
    _5899, _5898, _5904, _5903,
    _5917, _5916, _5919, _5920,
    _5991, _5997, _5995, _5993,
    _6007, _6006, _6018, _6017,
    _6019, _6020, _6024, _6025,
    _6026, _5918, _5885, _5900,
    _5913, _5966, _5983, _5994,
    _5999, _5897, _5902, _5915,
    _6005, _6023, _5888, _5906,
    _5942, _6010, _5893, _5910,
    _5880, _5923, _5962, _5968,
    _5971, _5974, _6003, _6013,
    _6033, _6036, _5948, _5876,
    _5877, _5884, _5896, _5895,
    _5901, _5914, _5929, _5940,
    _5944, _5883, _5952, _5964,
    _5976, _5977, _5978, _5980,
    _5982, _5986, _5989, _5990,
    _5996, _6000, _6030, _6031,
    _5998, _5905, _5907, _5941,
    _5943, _5879, _5881, _5887,
    _5889, _5890, _5891, _5892,
    _5894, _5908, _5912, _5921,
    _5925, _5926, _5946, _5951,
    _5961, _5963, _5967, _5969,
    _5970, _5972, _5973, _5975,
    _5984, _6002, _6004, _6009,
    _6011, _6012, _6014, _6015,
    _6016, _6032
)
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import (
    _5368, _5372, _5371, _5261,
    _5274, _5273, _5279, _5278,
    _5290, _5289, _5293, _5292,
    _5333, _5338, _5336, _5334,
    _5348, _5347, _5359, _5357,
    _5358, _5360, _5363, _5362,
    _5364, _5291, _5260, _5275,
    _5286, _5312, _5328, _5335,
    _5340, _5272, _5277, _5288,
    _5346, _5361, _5262, _5280,
    _5300, _5349, _5267, _5283,
    _5255, _5294, _5308, _5313,
    _5316, _5319, _5343, _5352,
    _5367, _5370, _5304, _5253,
    _5254, _5259, _5271, _5270,
    _5276, _5287, _5298, _5299,
    _5303, _5258, _5307, _5311,
    _5322, _5323, _5325, _5326,
    _5327, _5330, _5331, _5332,
    _5337, _5342, _5365, _5366,
    _5339, _5282, _5281, _5302,
    _5301, _5257, _5256, _5264,
    _5263, _5265, _5266, _5269,
    _5268, _5285, _5284, _5296,
    _5295, _5297, _5306, _5305,
    _5310, _5309, _5315, _5314,
    _5318, _5317, _5321, _5320,
    _5329, _5345, _5344, _5351,
    _5350, _5354, _5353, _5355,
    _5356, _5369
)
from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import (
    _2015, _2016, _1983, _1984,
    _1990, _1991, _1975, _1976,
    _1977, _1978, _1979, _1980,
    _1981, _1982, _1985, _1986,
    _1987, _1988, _1989, _1992,
    _1994, _1996, _1997, _1998,
    _1999, _2000, _2001, _2002,
    _2003, _2004, _2005, _2006,
    _2007, _2008, _2009, _2010,
    _2011, _2012, _2013, _2014
)
from mastapy.system_model.part_model.couplings import (
    _2034, _2036, _2037, _2039,
    _2040, _2041, _2042, _2043,
    _2044, _2045, _2053, _2051,
    _2052, _2054, _2055, _2056,
    _2058, _2059, _2060, _2061,
    _2062, _2064
)
from mastapy.system_model.connections_and_sockets import (
    _1766, _1761, _1762, _1765,
    _1774, _1777, _1781, _1785
)
from mastapy.system_model.connections_and_sockets.couplings import (
    _1823, _1825, _1827, _1829,
    _1831
)
from mastapy.system_model.connections_and_sockets.gears import (
    _1791, _1795, _1801, _1815,
    _1793, _1797, _1789, _1799,
    _1805, _1808, _1809, _1810,
    _1813, _1817, _1819, _1821,
    _1803
)
from mastapy.system_model.part_model import (
    _1907, _1908, _1910, _1912,
    _1913, _1914, _1917, _1918,
    _1921, _1922, _1906, _1923,
    _1926, _1928, _1929, _1930,
    _1931, _1933, _1934, _1936,
    _1937, _1938, _1940, _1941,
    _1942
)
from mastapy.system_model.part_model.shaft_model import _1945
from mastapy.system_model.analyses_and_results import _2074
from mastapy._internal.python_net import python_net_import

_SINGLE_MESH_WHINE_ANALYSIS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'SingleMeshWhineAnalysisAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SingleMeshWhineAnalysisAnalysis',)


class SingleMeshWhineAnalysisAnalysis(_2074.SingleAnalysis):
    '''SingleMeshWhineAnalysisAnalysis

    This is a mastapy class.
    '''

    TYPE = _SINGLE_MESH_WHINE_ANALYSIS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SingleMeshWhineAnalysisAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    def results_for_worm_gear_set_load_case(self, design_entity_analysis: '_6034.WormGearSetLoadCase') -> '_5368.WormGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.WormGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5368.WormGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear(self, design_entity: '_2015.ZerolBevelGear') -> '_5372.ZerolBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ZerolBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5372.ZerolBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_load_case(self, design_entity_analysis: '_6035.ZerolBevelGearLoadCase') -> '_5372.ZerolBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ZerolBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5372.ZerolBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2016.ZerolBevelGearSet') -> '_5371.ZerolBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ZerolBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5371.ZerolBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set_load_case(self, design_entity_analysis: '_6037.ZerolBevelGearSetLoadCase') -> '_5371.ZerolBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ZerolBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5371.ZerolBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_drive(self, design_entity: '_2034.BeltDrive') -> '_5261.BeltDriveSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BeltDriveSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5261.BeltDriveSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_drive_load_case(self, design_entity_analysis: '_5886.BeltDriveLoadCase') -> '_5261.BeltDriveSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BeltDriveSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5261.BeltDriveSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch(self, design_entity: '_2036.Clutch') -> '_5274.ClutchSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ClutchSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5274.ClutchSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_load_case(self, design_entity_analysis: '_5899.ClutchLoadCase') -> '_5274.ClutchSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ClutchSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5274.ClutchSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_half(self, design_entity: '_2037.ClutchHalf') -> '_5273.ClutchHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ClutchHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5273.ClutchHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_half_load_case(self, design_entity_analysis: '_5898.ClutchHalfLoadCase') -> '_5273.ClutchHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ClutchHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5273.ClutchHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling(self, design_entity: '_2039.ConceptCoupling') -> '_5279.ConceptCouplingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptCouplingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5279.ConceptCouplingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_load_case(self, design_entity_analysis: '_5904.ConceptCouplingLoadCase') -> '_5279.ConceptCouplingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptCouplingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5279.ConceptCouplingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_half(self, design_entity: '_2040.ConceptCouplingHalf') -> '_5278.ConceptCouplingHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptCouplingHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5278.ConceptCouplingHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_half_load_case(self, design_entity_analysis: '_5903.ConceptCouplingHalfLoadCase') -> '_5278.ConceptCouplingHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptCouplingHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5278.ConceptCouplingHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling(self, design_entity: '_2041.Coupling') -> '_5290.CouplingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CouplingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5290.CouplingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_load_case(self, design_entity_analysis: '_5917.CouplingLoadCase') -> '_5290.CouplingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CouplingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5290.CouplingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_half(self, design_entity: '_2042.CouplingHalf') -> '_5289.CouplingHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CouplingHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5289.CouplingHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_half_load_case(self, design_entity_analysis: '_5916.CouplingHalfLoadCase') -> '_5289.CouplingHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CouplingHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5289.CouplingHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt(self, design_entity: '_2043.CVT') -> '_5293.CVTSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CVTSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5293.CVTSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_load_case(self, design_entity_analysis: '_5919.CVTLoadCase') -> '_5293.CVTSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CVTSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5293.CVTSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_pulley(self, design_entity: '_2044.CVTPulley') -> '_5292.CVTPulleySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CVTPulleySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5292.CVTPulleySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_pulley_load_case(self, design_entity_analysis: '_5920.CVTPulleyLoadCase') -> '_5292.CVTPulleySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CVTPulleySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5292.CVTPulleySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_pulley(self, design_entity: '_2045.Pulley') -> '_5333.PulleySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PulleySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5333.PulleySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_pulley_load_case(self, design_entity_analysis: '_5991.PulleyLoadCase') -> '_5333.PulleySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PulleySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5333.PulleySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_hub_connection(self, design_entity: '_2053.ShaftHubConnection') -> '_5338.ShaftHubConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ShaftHubConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5338.ShaftHubConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_hub_connection_load_case(self, design_entity_analysis: '_5997.ShaftHubConnectionLoadCase') -> '_5338.ShaftHubConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ShaftHubConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5338.ShaftHubConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring(self, design_entity: '_2051.RollingRing') -> '_5336.RollingRingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RollingRingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5336.RollingRingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_load_case(self, design_entity_analysis: '_5995.RollingRingLoadCase') -> '_5336.RollingRingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RollingRingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5336.RollingRingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_assembly(self, design_entity: '_2052.RollingRingAssembly') -> '_5334.RollingRingAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RollingRingAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5334.RollingRingAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_assembly_load_case(self, design_entity_analysis: '_5993.RollingRingAssemblyLoadCase') -> '_5334.RollingRingAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RollingRingAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5334.RollingRingAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper(self, design_entity: '_2054.SpringDamper') -> '_5348.SpringDamperSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpringDamperSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5348.SpringDamperSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_load_case(self, design_entity_analysis: '_6007.SpringDamperLoadCase') -> '_5348.SpringDamperSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpringDamperSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5348.SpringDamperSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_half(self, design_entity: '_2055.SpringDamperHalf') -> '_5347.SpringDamperHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpringDamperHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5347.SpringDamperHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_half_load_case(self, design_entity_analysis: '_6006.SpringDamperHalfLoadCase') -> '_5347.SpringDamperHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpringDamperHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5347.SpringDamperHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser(self, design_entity: '_2056.Synchroniser') -> '_5359.SynchroniserSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5359.SynchroniserSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_load_case(self, design_entity_analysis: '_6018.SynchroniserLoadCase') -> '_5359.SynchroniserSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5359.SynchroniserSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_half(self, design_entity: '_2058.SynchroniserHalf') -> '_5357.SynchroniserHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5357.SynchroniserHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_half_load_case(self, design_entity_analysis: '_6017.SynchroniserHalfLoadCase') -> '_5357.SynchroniserHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5357.SynchroniserHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_part(self, design_entity: '_2059.SynchroniserPart') -> '_5358.SynchroniserPartSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserPartSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5358.SynchroniserPartSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_part_load_case(self, design_entity_analysis: '_6019.SynchroniserPartLoadCase') -> '_5358.SynchroniserPartSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserPartSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5358.SynchroniserPartSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_sleeve(self, design_entity: '_2060.SynchroniserSleeve') -> '_5360.SynchroniserSleeveSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserSleeveSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5360.SynchroniserSleeveSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_sleeve_load_case(self, design_entity_analysis: '_6020.SynchroniserSleeveLoadCase') -> '_5360.SynchroniserSleeveSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserSleeveSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5360.SynchroniserSleeveSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter(self, design_entity: '_2061.TorqueConverter') -> '_5363.TorqueConverterSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5363.TorqueConverterSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_load_case(self, design_entity_analysis: '_6024.TorqueConverterLoadCase') -> '_5363.TorqueConverterSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5363.TorqueConverterSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_pump(self, design_entity: '_2062.TorqueConverterPump') -> '_5362.TorqueConverterPumpSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterPumpSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5362.TorqueConverterPumpSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_pump_load_case(self, design_entity_analysis: '_6025.TorqueConverterPumpLoadCase') -> '_5362.TorqueConverterPumpSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterPumpSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5362.TorqueConverterPumpSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_turbine(self, design_entity: '_2064.TorqueConverterTurbine') -> '_5364.TorqueConverterTurbineSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterTurbineSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5364.TorqueConverterTurbineSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_turbine_load_case(self, design_entity_analysis: '_6026.TorqueConverterTurbineLoadCase') -> '_5364.TorqueConverterTurbineSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterTurbineSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5364.TorqueConverterTurbineSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_belt_connection(self, design_entity: '_1766.CVTBeltConnection') -> '_5291.CVTBeltConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CVTBeltConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5291.CVTBeltConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_belt_connection_load_case(self, design_entity_analysis: '_5918.CVTBeltConnectionLoadCase') -> '_5291.CVTBeltConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CVTBeltConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5291.CVTBeltConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_connection(self, design_entity: '_1761.BeltConnection') -> '_5260.BeltConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BeltConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5260.BeltConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_connection_load_case(self, design_entity_analysis: '_5885.BeltConnectionLoadCase') -> '_5260.BeltConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BeltConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5260.BeltConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coaxial_connection(self, design_entity: '_1762.CoaxialConnection') -> '_5275.CoaxialConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CoaxialConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5275.CoaxialConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coaxial_connection_load_case(self, design_entity_analysis: '_5900.CoaxialConnectionLoadCase') -> '_5275.CoaxialConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CoaxialConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5275.CoaxialConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_connection(self, design_entity: '_1765.Connection') -> '_5286.ConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5286.ConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_connection_load_case(self, design_entity_analysis: '_5913.ConnectionLoadCase') -> '_5286.ConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5286.ConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection(self, design_entity: '_1774.InterMountableComponentConnection') -> '_5312.InterMountableComponentConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.InterMountableComponentConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5312.InterMountableComponentConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection_load_case(self, design_entity_analysis: '_5966.InterMountableComponentConnectionLoadCase') -> '_5312.InterMountableComponentConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.InterMountableComponentConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5312.InterMountableComponentConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_connection(self, design_entity: '_1777.PlanetaryConnection') -> '_5328.PlanetaryConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PlanetaryConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5328.PlanetaryConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_connection_load_case(self, design_entity_analysis: '_5983.PlanetaryConnectionLoadCase') -> '_5328.PlanetaryConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PlanetaryConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5328.PlanetaryConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_connection(self, design_entity: '_1781.RollingRingConnection') -> '_5335.RollingRingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RollingRingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5335.RollingRingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_connection_load_case(self, design_entity_analysis: '_5994.RollingRingConnectionLoadCase') -> '_5335.RollingRingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RollingRingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5335.RollingRingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1785.ShaftToMountableComponentConnection') -> '_5340.ShaftToMountableComponentConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ShaftToMountableComponentConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5340.ShaftToMountableComponentConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection_load_case(self, design_entity_analysis: '_5999.ShaftToMountableComponentConnectionLoadCase') -> '_5340.ShaftToMountableComponentConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ShaftToMountableComponentConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5340.ShaftToMountableComponentConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_connection(self, design_entity: '_1823.ClutchConnection') -> '_5272.ClutchConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ClutchConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5272.ClutchConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_connection_load_case(self, design_entity_analysis: '_5897.ClutchConnectionLoadCase') -> '_5272.ClutchConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ClutchConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5272.ClutchConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_connection(self, design_entity: '_1825.ConceptCouplingConnection') -> '_5277.ConceptCouplingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptCouplingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5277.ConceptCouplingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_connection_load_case(self, design_entity_analysis: '_5902.ConceptCouplingConnectionLoadCase') -> '_5277.ConceptCouplingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptCouplingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5277.ConceptCouplingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_connection(self, design_entity: '_1827.CouplingConnection') -> '_5288.CouplingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CouplingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5288.CouplingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_connection_load_case(self, design_entity_analysis: '_5915.CouplingConnectionLoadCase') -> '_5288.CouplingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CouplingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5288.CouplingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_connection(self, design_entity: '_1829.SpringDamperConnection') -> '_5346.SpringDamperConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpringDamperConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5346.SpringDamperConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_connection_load_case(self, design_entity_analysis: '_6005.SpringDamperConnectionLoadCase') -> '_5346.SpringDamperConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpringDamperConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5346.SpringDamperConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_connection(self, design_entity: '_1831.TorqueConverterConnection') -> '_5361.TorqueConverterConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5361.TorqueConverterConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_connection_load_case(self, design_entity_analysis: '_6023.TorqueConverterConnectionLoadCase') -> '_5361.TorqueConverterConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5361.TorqueConverterConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1791.BevelDifferentialGearMesh') -> '_5262.BevelDifferentialGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5262.BevelDifferentialGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh_load_case(self, design_entity_analysis: '_5888.BevelDifferentialGearMeshLoadCase') -> '_5262.BevelDifferentialGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5262.BevelDifferentialGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_mesh(self, design_entity: '_1795.ConceptGearMesh') -> '_5280.ConceptGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5280.ConceptGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_mesh_load_case(self, design_entity_analysis: '_5906.ConceptGearMeshLoadCase') -> '_5280.ConceptGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5280.ConceptGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_mesh(self, design_entity: '_1801.FaceGearMesh') -> '_5300.FaceGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FaceGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5300.FaceGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_mesh_load_case(self, design_entity_analysis: '_5942.FaceGearMeshLoadCase') -> '_5300.FaceGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FaceGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5300.FaceGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1815.StraightBevelDiffGearMesh') -> '_5349.StraightBevelDiffGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelDiffGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5349.StraightBevelDiffGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh_load_case(self, design_entity_analysis: '_6010.StraightBevelDiffGearMeshLoadCase') -> '_5349.StraightBevelDiffGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelDiffGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5349.StraightBevelDiffGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_mesh(self, design_entity: '_1793.BevelGearMesh') -> '_5267.BevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5267.BevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_mesh_load_case(self, design_entity_analysis: '_5893.BevelGearMeshLoadCase') -> '_5267.BevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5267.BevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_mesh(self, design_entity: '_1797.ConicalGearMesh') -> '_5283.ConicalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConicalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5283.ConicalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_mesh_load_case(self, design_entity_analysis: '_5910.ConicalGearMeshLoadCase') -> '_5283.ConicalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConicalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5283.ConicalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1789.AGMAGleasonConicalGearMesh') -> '_5255.AGMAGleasonConicalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AGMAGleasonConicalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5255.AGMAGleasonConicalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh_load_case(self, design_entity_analysis: '_5880.AGMAGleasonConicalGearMeshLoadCase') -> '_5255.AGMAGleasonConicalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AGMAGleasonConicalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5255.AGMAGleasonConicalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1799.CylindricalGearMesh') -> '_5294.CylindricalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5294.CylindricalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh_load_case(self, design_entity_analysis: '_5923.CylindricalGearMeshLoadCase') -> '_5294.CylindricalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5294.CylindricalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh(self, design_entity: '_1805.HypoidGearMesh') -> '_5308.HypoidGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.HypoidGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5308.HypoidGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_5962.HypoidGearMeshLoadCase') -> '_5308.HypoidGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.HypoidGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5308.HypoidGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1808.KlingelnbergCycloPalloidConicalGearMesh') -> '_5313.KlingelnbergCycloPalloidConicalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidConicalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5313.KlingelnbergCycloPalloidConicalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self, design_entity_analysis: '_5968.KlingelnbergCycloPalloidConicalGearMeshLoadCase') -> '_5313.KlingelnbergCycloPalloidConicalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidConicalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5313.KlingelnbergCycloPalloidConicalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1809.KlingelnbergCycloPalloidHypoidGearMesh') -> '_5316.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5316.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_5971.KlingelnbergCycloPalloidHypoidGearMeshLoadCase') -> '_5316.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5316.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1810.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> '_5319.KlingelnbergCycloPalloidSpiralBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5319.KlingelnbergCycloPalloidSpiralBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_5974.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase') -> '_5319.KlingelnbergCycloPalloidSpiralBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5319.KlingelnbergCycloPalloidSpiralBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1813.SpiralBevelGearMesh') -> '_5343.SpiralBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpiralBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5343.SpiralBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6003.SpiralBevelGearMeshLoadCase') -> '_5343.SpiralBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpiralBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5343.SpiralBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1817.StraightBevelGearMesh') -> '_5352.StraightBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5352.StraightBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6013.StraightBevelGearMeshLoadCase') -> '_5352.StraightBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5352.StraightBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_mesh(self, design_entity: '_1819.WormGearMesh') -> '_5367.WormGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.WormGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5367.WormGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_mesh_load_case(self, design_entity_analysis: '_6033.WormGearMeshLoadCase') -> '_5367.WormGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.WormGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5367.WormGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1821.ZerolBevelGearMesh') -> '_5370.ZerolBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ZerolBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5370.ZerolBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6036.ZerolBevelGearMeshLoadCase') -> '_5370.ZerolBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ZerolBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5370.ZerolBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_mesh(self, design_entity: '_1803.GearMesh') -> '_5304.GearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5304.GearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_mesh_load_case(self, design_entity_analysis: '_5948.GearMeshLoadCase') -> '_5304.GearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5304.GearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_assembly(self, design_entity: '_1907.AbstractAssembly') -> '_5253.AbstractAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AbstractAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5253.AbstractAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_assembly_load_case(self, design_entity_analysis: '_5876.AbstractAssemblyLoadCase') -> '_5253.AbstractAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AbstractAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5253.AbstractAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing(self, design_entity: '_1908.AbstractShaftOrHousing') -> '_5254.AbstractShaftOrHousingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AbstractShaftOrHousingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5254.AbstractShaftOrHousingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing_load_case(self, design_entity_analysis: '_5877.AbstractShaftOrHousingLoadCase') -> '_5254.AbstractShaftOrHousingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AbstractShaftOrHousingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5254.AbstractShaftOrHousingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bearing(self, design_entity: '_1910.Bearing') -> '_5259.BearingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BearingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5259.BearingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bearing_load_case(self, design_entity_analysis: '_5884.BearingLoadCase') -> '_5259.BearingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BearingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5259.BearingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bolt(self, design_entity: '_1912.Bolt') -> '_5271.BoltSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BoltSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5271.BoltSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bolt_load_case(self, design_entity_analysis: '_5896.BoltLoadCase') -> '_5271.BoltSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BoltSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5271.BoltSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bolted_joint(self, design_entity: '_1913.BoltedJoint') -> '_5270.BoltedJointSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BoltedJointSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5270.BoltedJointSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bolted_joint_load_case(self, design_entity_analysis: '_5895.BoltedJointLoadCase') -> '_5270.BoltedJointSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BoltedJointSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5270.BoltedJointSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_component(self, design_entity: '_1914.Component') -> '_5276.ComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5276.ComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_component_load_case(self, design_entity_analysis: '_5901.ComponentLoadCase') -> '_5276.ComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5276.ComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_connector(self, design_entity: '_1917.Connector') -> '_5287.ConnectorSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConnectorSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5287.ConnectorSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_connector_load_case(self, design_entity_analysis: '_5914.ConnectorLoadCase') -> '_5287.ConnectorSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConnectorSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5287.ConnectorSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_datum(self, design_entity: '_1918.Datum') -> '_5298.DatumSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.DatumSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5298.DatumSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_datum_load_case(self, design_entity_analysis: '_5929.DatumLoadCase') -> '_5298.DatumSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.DatumSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5298.DatumSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_external_cad_model(self, design_entity: '_1921.ExternalCADModel') -> '_5299.ExternalCADModelSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ExternalCADModelSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5299.ExternalCADModelSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_external_cad_model_load_case(self, design_entity_analysis: '_5940.ExternalCADModelLoadCase') -> '_5299.ExternalCADModelSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ExternalCADModelSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5299.ExternalCADModelSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_flexible_pin_assembly(self, design_entity: '_1922.FlexiblePinAssembly') -> '_5303.FlexiblePinAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FlexiblePinAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5303.FlexiblePinAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_flexible_pin_assembly_load_case(self, design_entity_analysis: '_5944.FlexiblePinAssemblyLoadCase') -> '_5303.FlexiblePinAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FlexiblePinAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5303.FlexiblePinAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_assembly(self, design_entity: '_1906.Assembly') -> '_5258.AssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5258.AssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_assembly_load_case(self, design_entity_analysis: '_5883.AssemblyLoadCase') -> '_5258.AssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5258.AssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_guide_dxf_model(self, design_entity: '_1923.GuideDxfModel') -> '_5307.GuideDxfModelSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GuideDxfModelSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5307.GuideDxfModelSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_guide_dxf_model_load_case(self, design_entity_analysis: '_5952.GuideDxfModelLoadCase') -> '_5307.GuideDxfModelSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GuideDxfModelSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5307.GuideDxfModelSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_imported_fe_component(self, design_entity: '_1926.ImportedFEComponent') -> '_5311.ImportedFEComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ImportedFEComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5311.ImportedFEComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_imported_fe_component_load_case(self, design_entity_analysis: '_5964.ImportedFEComponentLoadCase') -> '_5311.ImportedFEComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ImportedFEComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ImportedFEComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5311.ImportedFEComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_mass_disc(self, design_entity: '_1928.MassDisc') -> '_5322.MassDiscSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.MassDiscSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5322.MassDiscSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_mass_disc_load_case(self, design_entity_analysis: '_5976.MassDiscLoadCase') -> '_5322.MassDiscSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.MassDiscSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5322.MassDiscSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_measurement_component(self, design_entity: '_1929.MeasurementComponent') -> '_5323.MeasurementComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.MeasurementComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5323.MeasurementComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_measurement_component_load_case(self, design_entity_analysis: '_5977.MeasurementComponentLoadCase') -> '_5323.MeasurementComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.MeasurementComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5323.MeasurementComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_mountable_component(self, design_entity: '_1930.MountableComponent') -> '_5325.MountableComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.MountableComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5325.MountableComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_mountable_component_load_case(self, design_entity_analysis: '_5978.MountableComponentLoadCase') -> '_5325.MountableComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.MountableComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5325.MountableComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_oil_seal(self, design_entity: '_1931.OilSeal') -> '_5326.OilSealSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.OilSealSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5326.OilSealSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_oil_seal_load_case(self, design_entity_analysis: '_5980.OilSealLoadCase') -> '_5326.OilSealSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.OilSealSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5326.OilSealSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_part(self, design_entity: '_1933.Part') -> '_5327.PartSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PartSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5327.PartSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_part_load_case(self, design_entity_analysis: '_5982.PartLoadCase') -> '_5327.PartSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PartSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5327.PartSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_planet_carrier(self, design_entity: '_1934.PlanetCarrier') -> '_5330.PlanetCarrierSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PlanetCarrierSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5330.PlanetCarrierSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_planet_carrier_load_case(self, design_entity_analysis: '_5986.PlanetCarrierLoadCase') -> '_5330.PlanetCarrierSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PlanetCarrierSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5330.PlanetCarrierSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_point_load(self, design_entity: '_1936.PointLoad') -> '_5331.PointLoadSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PointLoadSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5331.PointLoadSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_point_load_load_case(self, design_entity_analysis: '_5989.PointLoadLoadCase') -> '_5331.PointLoadSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PointLoadSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5331.PointLoadSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_power_load(self, design_entity: '_1937.PowerLoad') -> '_5332.PowerLoadSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PowerLoadSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5332.PowerLoadSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_power_load_load_case(self, design_entity_analysis: '_5990.PowerLoadLoadCase') -> '_5332.PowerLoadSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PowerLoadSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5332.PowerLoadSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_root_assembly(self, design_entity: '_1938.RootAssembly') -> '_5337.RootAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RootAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5337.RootAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_root_assembly_load_case(self, design_entity_analysis: '_5996.RootAssemblyLoadCase') -> '_5337.RootAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RootAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5337.RootAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_specialised_assembly(self, design_entity: '_1940.SpecialisedAssembly') -> '_5342.SpecialisedAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpecialisedAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5342.SpecialisedAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_specialised_assembly_load_case(self, design_entity_analysis: '_6000.SpecialisedAssemblyLoadCase') -> '_5342.SpecialisedAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpecialisedAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5342.SpecialisedAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_unbalanced_mass(self, design_entity: '_1941.UnbalancedMass') -> '_5365.UnbalancedMassSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.UnbalancedMassSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5365.UnbalancedMassSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_unbalanced_mass_load_case(self, design_entity_analysis: '_6030.UnbalancedMassLoadCase') -> '_5365.UnbalancedMassSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.UnbalancedMassSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5365.UnbalancedMassSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_virtual_component(self, design_entity: '_1942.VirtualComponent') -> '_5366.VirtualComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.VirtualComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5366.VirtualComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_virtual_component_load_case(self, design_entity_analysis: '_6031.VirtualComponentLoadCase') -> '_5366.VirtualComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.VirtualComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5366.VirtualComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft(self, design_entity: '_1945.Shaft') -> '_5339.ShaftSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ShaftSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5339.ShaftSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_load_case(self, design_entity_analysis: '_5998.ShaftLoadCase') -> '_5339.ShaftSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ShaftSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5339.ShaftSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear(self, design_entity: '_1983.ConceptGear') -> '_5282.ConceptGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5282.ConceptGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_load_case(self, design_entity_analysis: '_5905.ConceptGearLoadCase') -> '_5282.ConceptGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5282.ConceptGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_set(self, design_entity: '_1984.ConceptGearSet') -> '_5281.ConceptGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5281.ConceptGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_set_load_case(self, design_entity_analysis: '_5907.ConceptGearSetLoadCase') -> '_5281.ConceptGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5281.ConceptGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear(self, design_entity: '_1990.FaceGear') -> '_5302.FaceGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FaceGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5302.FaceGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_load_case(self, design_entity_analysis: '_5941.FaceGearLoadCase') -> '_5302.FaceGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FaceGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5302.FaceGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_set(self, design_entity: '_1991.FaceGearSet') -> '_5301.FaceGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FaceGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5301.FaceGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_set_load_case(self, design_entity_analysis: '_5943.FaceGearSetLoadCase') -> '_5301.FaceGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FaceGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5301.FaceGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear(self, design_entity: '_1975.AGMAGleasonConicalGear') -> '_5257.AGMAGleasonConicalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AGMAGleasonConicalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5257.AGMAGleasonConicalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_load_case(self, design_entity_analysis: '_5879.AGMAGleasonConicalGearLoadCase') -> '_5257.AGMAGleasonConicalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AGMAGleasonConicalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5257.AGMAGleasonConicalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_1976.AGMAGleasonConicalGearSet') -> '_5256.AGMAGleasonConicalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AGMAGleasonConicalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5256.AGMAGleasonConicalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set_load_case(self, design_entity_analysis: '_5881.AGMAGleasonConicalGearSetLoadCase') -> '_5256.AGMAGleasonConicalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AGMAGleasonConicalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5256.AGMAGleasonConicalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear(self, design_entity: '_1977.BevelDifferentialGear') -> '_5264.BevelDifferentialGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5264.BevelDifferentialGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_load_case(self, design_entity_analysis: '_5887.BevelDifferentialGearLoadCase') -> '_5264.BevelDifferentialGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5264.BevelDifferentialGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set(self, design_entity: '_1978.BevelDifferentialGearSet') -> '_5263.BevelDifferentialGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5263.BevelDifferentialGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set_load_case(self, design_entity_analysis: '_5889.BevelDifferentialGearSetLoadCase') -> '_5263.BevelDifferentialGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5263.BevelDifferentialGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear(self, design_entity: '_1979.BevelDifferentialPlanetGear') -> '_5265.BevelDifferentialPlanetGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialPlanetGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5265.BevelDifferentialPlanetGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear_load_case(self, design_entity_analysis: '_5890.BevelDifferentialPlanetGearLoadCase') -> '_5265.BevelDifferentialPlanetGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialPlanetGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5265.BevelDifferentialPlanetGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear(self, design_entity: '_1980.BevelDifferentialSunGear') -> '_5266.BevelDifferentialSunGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialSunGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5266.BevelDifferentialSunGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear_load_case(self, design_entity_analysis: '_5891.BevelDifferentialSunGearLoadCase') -> '_5266.BevelDifferentialSunGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialSunGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5266.BevelDifferentialSunGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear(self, design_entity: '_1981.BevelGear') -> '_5269.BevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5269.BevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_load_case(self, design_entity_analysis: '_5892.BevelGearLoadCase') -> '_5269.BevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5269.BevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_set(self, design_entity: '_1982.BevelGearSet') -> '_5268.BevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5268.BevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_set_load_case(self, design_entity_analysis: '_5894.BevelGearSetLoadCase') -> '_5268.BevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5268.BevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear(self, design_entity: '_1985.ConicalGear') -> '_5285.ConicalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConicalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5285.ConicalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_load_case(self, design_entity_analysis: '_5908.ConicalGearLoadCase') -> '_5285.ConicalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConicalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5285.ConicalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_set(self, design_entity: '_1986.ConicalGearSet') -> '_5284.ConicalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConicalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5284.ConicalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_set_load_case(self, design_entity_analysis: '_5912.ConicalGearSetLoadCase') -> '_5284.ConicalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConicalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5284.ConicalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear(self, design_entity: '_1987.CylindricalGear') -> '_5296.CylindricalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5296.CylindricalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_load_case(self, design_entity_analysis: '_5921.CylindricalGearLoadCase') -> '_5296.CylindricalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5296.CylindricalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_set(self, design_entity: '_1988.CylindricalGearSet') -> '_5295.CylindricalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5295.CylindricalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_set_load_case(self, design_entity_analysis: '_5925.CylindricalGearSetLoadCase') -> '_5295.CylindricalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5295.CylindricalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear(self, design_entity: '_1989.CylindricalPlanetGear') -> '_5297.CylindricalPlanetGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalPlanetGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5297.CylindricalPlanetGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear_load_case(self, design_entity_analysis: '_5926.CylindricalPlanetGearLoadCase') -> '_5297.CylindricalPlanetGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalPlanetGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5297.CylindricalPlanetGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_gear(self, design_entity: '_1992.Gear') -> '_5306.GearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5306.GearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_load_case(self, design_entity_analysis: '_5946.GearLoadCase') -> '_5306.GearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5306.GearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_set(self, design_entity: '_1994.GearSet') -> '_5305.GearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5305.GearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_set_load_case(self, design_entity_analysis: '_5951.GearSetLoadCase') -> '_5305.GearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5305.GearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear(self, design_entity: '_1996.HypoidGear') -> '_5310.HypoidGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.HypoidGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5310.HypoidGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_load_case(self, design_entity_analysis: '_5961.HypoidGearLoadCase') -> '_5310.HypoidGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.HypoidGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5310.HypoidGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_set(self, design_entity: '_1997.HypoidGearSet') -> '_5309.HypoidGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.HypoidGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5309.HypoidGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_set_load_case(self, design_entity_analysis: '_5963.HypoidGearSetLoadCase') -> '_5309.HypoidGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.HypoidGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5309.HypoidGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_1998.KlingelnbergCycloPalloidConicalGear') -> '_5315.KlingelnbergCycloPalloidConicalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidConicalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5315.KlingelnbergCycloPalloidConicalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_load_case(self, design_entity_analysis: '_5967.KlingelnbergCycloPalloidConicalGearLoadCase') -> '_5315.KlingelnbergCycloPalloidConicalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidConicalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5315.KlingelnbergCycloPalloidConicalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_1999.KlingelnbergCycloPalloidConicalGearSet') -> '_5314.KlingelnbergCycloPalloidConicalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidConicalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5314.KlingelnbergCycloPalloidConicalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set_load_case(self, design_entity_analysis: '_5969.KlingelnbergCycloPalloidConicalGearSetLoadCase') -> '_5314.KlingelnbergCycloPalloidConicalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidConicalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5314.KlingelnbergCycloPalloidConicalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2000.KlingelnbergCycloPalloidHypoidGear') -> '_5318.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5318.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_load_case(self, design_entity_analysis: '_5970.KlingelnbergCycloPalloidHypoidGearLoadCase') -> '_5318.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5318.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2001.KlingelnbergCycloPalloidHypoidGearSet') -> '_5317.KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5317.KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self, design_entity_analysis: '_5972.KlingelnbergCycloPalloidHypoidGearSetLoadCase') -> '_5317.KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5317.KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2002.KlingelnbergCycloPalloidSpiralBevelGear') -> '_5321.KlingelnbergCycloPalloidSpiralBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5321.KlingelnbergCycloPalloidSpiralBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self, design_entity_analysis: '_5973.KlingelnbergCycloPalloidSpiralBevelGearLoadCase') -> '_5321.KlingelnbergCycloPalloidSpiralBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5321.KlingelnbergCycloPalloidSpiralBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2003.KlingelnbergCycloPalloidSpiralBevelGearSet') -> '_5320.KlingelnbergCycloPalloidSpiralBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5320.KlingelnbergCycloPalloidSpiralBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_5975.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase') -> '_5320.KlingelnbergCycloPalloidSpiralBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5320.KlingelnbergCycloPalloidSpiralBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_gear_set(self, design_entity: '_2004.PlanetaryGearSet') -> '_5329.PlanetaryGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PlanetaryGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5329.PlanetaryGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_gear_set_load_case(self, design_entity_analysis: '_5984.PlanetaryGearSetLoadCase') -> '_5329.PlanetaryGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PlanetaryGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5329.PlanetaryGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear(self, design_entity: '_2005.SpiralBevelGear') -> '_5345.SpiralBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpiralBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5345.SpiralBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6002.SpiralBevelGearLoadCase') -> '_5345.SpiralBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpiralBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5345.SpiralBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2006.SpiralBevelGearSet') -> '_5344.SpiralBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpiralBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5344.SpiralBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6004.SpiralBevelGearSetLoadCase') -> '_5344.SpiralBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpiralBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5344.SpiralBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2007.StraightBevelDiffGear') -> '_5351.StraightBevelDiffGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelDiffGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5351.StraightBevelDiffGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_load_case(self, design_entity_analysis: '_6009.StraightBevelDiffGearLoadCase') -> '_5351.StraightBevelDiffGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelDiffGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5351.StraightBevelDiffGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2008.StraightBevelDiffGearSet') -> '_5350.StraightBevelDiffGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelDiffGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5350.StraightBevelDiffGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set_load_case(self, design_entity_analysis: '_6011.StraightBevelDiffGearSetLoadCase') -> '_5350.StraightBevelDiffGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelDiffGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5350.StraightBevelDiffGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear(self, design_entity: '_2009.StraightBevelGear') -> '_5354.StraightBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5354.StraightBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_load_case(self, design_entity_analysis: '_6012.StraightBevelGearLoadCase') -> '_5354.StraightBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5354.StraightBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set(self, design_entity: '_2010.StraightBevelGearSet') -> '_5353.StraightBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5353.StraightBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set_load_case(self, design_entity_analysis: '_6014.StraightBevelGearSetLoadCase') -> '_5353.StraightBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5353.StraightBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2011.StraightBevelPlanetGear') -> '_5355.StraightBevelPlanetGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelPlanetGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5355.StraightBevelPlanetGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear_load_case(self, design_entity_analysis: '_6015.StraightBevelPlanetGearLoadCase') -> '_5355.StraightBevelPlanetGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelPlanetGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5355.StraightBevelPlanetGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2012.StraightBevelSunGear') -> '_5356.StraightBevelSunGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelSunGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5356.StraightBevelSunGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear_load_case(self, design_entity_analysis: '_6016.StraightBevelSunGearLoadCase') -> '_5356.StraightBevelSunGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelSunGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5356.StraightBevelSunGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear(self, design_entity: '_2013.WormGear') -> '_5369.WormGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.WormGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5369.WormGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_load_case(self, design_entity_analysis: '_6032.WormGearLoadCase') -> '_5369.WormGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.WormGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5369.WormGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_set(self, design_entity: '_2014.WormGearSet') -> '_5368.WormGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.WormGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5368.WormGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None
