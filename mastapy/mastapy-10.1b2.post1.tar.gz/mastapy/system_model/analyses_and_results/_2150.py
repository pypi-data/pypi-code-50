'''_2150.py

SingleMeshWhineAnalysisAnalysis
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
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import (
    _5504, _5508, _5507, _5463,
    _5462, _5394, _5407, _5406,
    _5412, _5411, _5423, _5422,
    _5426, _5425, _5469, _5474,
    _5472, _5470, _5484, _5483,
    _5495, _5493, _5494, _5496,
    _5499, _5498, _5500, _5424,
    _5393, _5408, _5419, _5445,
    _5464, _5471, _5476, _5395,
    _5413, _5433, _5485, _5400,
    _5416, _5388, _5427, _5441,
    _5446, _5449, _5452, _5479,
    _5488, _5503, _5506, _5437,
    _5461, _5405, _5410, _5421,
    _5482, _5497, _5386, _5387,
    _5392, _5404, _5403, _5409,
    _5420, _5431, _5432, _5436,
    _5391, _5440, _5444, _5455,
    _5456, _5458, _5459, _5460,
    _5466, _5467, _5468, _5473,
    _5478, _5501, _5502, _5475,
    _5415, _5414, _5435, _5434,
    _5390, _5389, _5397, _5396,
    _5398, _5399, _5402, _5401,
    _5418, _5417, _5429, _5428,
    _5430, _5439, _5438, _5443,
    _5442, _5448, _5447, _5451,
    _5450, _5454, _5453, _5465,
    _5481, _5480, _5487, _5486,
    _5490, _5489, _5491, _5492,
    _5505
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

_SINGLE_MESH_WHINE_ANALYSIS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'SingleMeshWhineAnalysisAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SingleMeshWhineAnalysisAnalysis',)


class SingleMeshWhineAnalysisAnalysis(_2131.SingleAnalysis):
    '''SingleMeshWhineAnalysisAnalysis

    This is a mastapy class.
    '''

    TYPE = _SINGLE_MESH_WHINE_ANALYSIS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SingleMeshWhineAnalysisAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    def results_for_worm_gear_set_load_case(self, design_entity_analysis: '_6189.WormGearSetLoadCase') -> '_5504.WormGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.WormGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5504.WormGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear(self, design_entity: '_2070.ZerolBevelGear') -> '_5508.ZerolBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ZerolBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5508.ZerolBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_load_case(self, design_entity_analysis: '_6190.ZerolBevelGearLoadCase') -> '_5508.ZerolBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ZerolBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5508.ZerolBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2071.ZerolBevelGearSet') -> '_5507.ZerolBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ZerolBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5507.ZerolBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set_load_case(self, design_entity_analysis: '_6192.ZerolBevelGearSetLoadCase') -> '_5507.ZerolBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ZerolBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5507.ZerolBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2100.PartToPartShearCoupling') -> '_5463.PartToPartShearCouplingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PartToPartShearCouplingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5463.PartToPartShearCouplingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_load_case(self, design_entity_analysis: '_6136.PartToPartShearCouplingLoadCase') -> '_5463.PartToPartShearCouplingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PartToPartShearCouplingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5463.PartToPartShearCouplingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2101.PartToPartShearCouplingHalf') -> '_5462.PartToPartShearCouplingHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PartToPartShearCouplingHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5462.PartToPartShearCouplingHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half_load_case(self, design_entity_analysis: '_6135.PartToPartShearCouplingHalfLoadCase') -> '_5462.PartToPartShearCouplingHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PartToPartShearCouplingHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5462.PartToPartShearCouplingHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_drive(self, design_entity: '_2089.BeltDrive') -> '_5394.BeltDriveSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BeltDriveSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5394.BeltDriveSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_drive_load_case(self, design_entity_analysis: '_6034.BeltDriveLoadCase') -> '_5394.BeltDriveSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BeltDriveSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5394.BeltDriveSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch(self, design_entity: '_2091.Clutch') -> '_5407.ClutchSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ClutchSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5407.ClutchSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_load_case(self, design_entity_analysis: '_6047.ClutchLoadCase') -> '_5407.ClutchSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ClutchSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5407.ClutchSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_half(self, design_entity: '_2092.ClutchHalf') -> '_5406.ClutchHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ClutchHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5406.ClutchHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_half_load_case(self, design_entity_analysis: '_6046.ClutchHalfLoadCase') -> '_5406.ClutchHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ClutchHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5406.ClutchHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling(self, design_entity: '_2094.ConceptCoupling') -> '_5412.ConceptCouplingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptCouplingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5412.ConceptCouplingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_load_case(self, design_entity_analysis: '_6052.ConceptCouplingLoadCase') -> '_5412.ConceptCouplingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptCouplingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5412.ConceptCouplingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_half(self, design_entity: '_2095.ConceptCouplingHalf') -> '_5411.ConceptCouplingHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptCouplingHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5411.ConceptCouplingHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_half_load_case(self, design_entity_analysis: '_6051.ConceptCouplingHalfLoadCase') -> '_5411.ConceptCouplingHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptCouplingHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5411.ConceptCouplingHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling(self, design_entity: '_2096.Coupling') -> '_5423.CouplingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CouplingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5423.CouplingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_load_case(self, design_entity_analysis: '_6065.CouplingLoadCase') -> '_5423.CouplingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CouplingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5423.CouplingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_half(self, design_entity: '_2097.CouplingHalf') -> '_5422.CouplingHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CouplingHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5422.CouplingHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_half_load_case(self, design_entity_analysis: '_6064.CouplingHalfLoadCase') -> '_5422.CouplingHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CouplingHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5422.CouplingHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt(self, design_entity: '_2098.CVT') -> '_5426.CVTSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CVTSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5426.CVTSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_load_case(self, design_entity_analysis: '_6067.CVTLoadCase') -> '_5426.CVTSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CVTSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5426.CVTSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_pulley(self, design_entity: '_2099.CVTPulley') -> '_5425.CVTPulleySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CVTPulleySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5425.CVTPulleySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_pulley_load_case(self, design_entity_analysis: '_6068.CVTPulleyLoadCase') -> '_5425.CVTPulleySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CVTPulleySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5425.CVTPulleySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_pulley(self, design_entity: '_2102.Pulley') -> '_5469.PulleySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PulleySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5469.PulleySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_pulley_load_case(self, design_entity_analysis: '_6145.PulleyLoadCase') -> '_5469.PulleySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PulleySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5469.PulleySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_hub_connection(self, design_entity: '_2110.ShaftHubConnection') -> '_5474.ShaftHubConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ShaftHubConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5474.ShaftHubConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_hub_connection_load_case(self, design_entity_analysis: '_6151.ShaftHubConnectionLoadCase') -> '_5474.ShaftHubConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ShaftHubConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5474.ShaftHubConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring(self, design_entity: '_2108.RollingRing') -> '_5472.RollingRingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RollingRingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5472.RollingRingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_load_case(self, design_entity_analysis: '_6149.RollingRingLoadCase') -> '_5472.RollingRingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RollingRingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5472.RollingRingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_assembly(self, design_entity: '_2109.RollingRingAssembly') -> '_5470.RollingRingAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RollingRingAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5470.RollingRingAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_assembly_load_case(self, design_entity_analysis: '_6147.RollingRingAssemblyLoadCase') -> '_5470.RollingRingAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RollingRingAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5470.RollingRingAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper(self, design_entity: '_2111.SpringDamper') -> '_5484.SpringDamperSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpringDamperSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5484.SpringDamperSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_load_case(self, design_entity_analysis: '_6161.SpringDamperLoadCase') -> '_5484.SpringDamperSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpringDamperSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5484.SpringDamperSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_half(self, design_entity: '_2112.SpringDamperHalf') -> '_5483.SpringDamperHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpringDamperHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5483.SpringDamperHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_half_load_case(self, design_entity_analysis: '_6160.SpringDamperHalfLoadCase') -> '_5483.SpringDamperHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpringDamperHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5483.SpringDamperHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser(self, design_entity: '_2113.Synchroniser') -> '_5495.SynchroniserSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5495.SynchroniserSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_load_case(self, design_entity_analysis: '_6172.SynchroniserLoadCase') -> '_5495.SynchroniserSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5495.SynchroniserSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_half(self, design_entity: '_2115.SynchroniserHalf') -> '_5493.SynchroniserHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5493.SynchroniserHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_half_load_case(self, design_entity_analysis: '_6171.SynchroniserHalfLoadCase') -> '_5493.SynchroniserHalfSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserHalfSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5493.SynchroniserHalfSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_part(self, design_entity: '_2116.SynchroniserPart') -> '_5494.SynchroniserPartSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserPartSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5494.SynchroniserPartSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_part_load_case(self, design_entity_analysis: '_6173.SynchroniserPartLoadCase') -> '_5494.SynchroniserPartSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserPartSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5494.SynchroniserPartSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_sleeve(self, design_entity: '_2117.SynchroniserSleeve') -> '_5496.SynchroniserSleeveSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserSleeveSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5496.SynchroniserSleeveSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_sleeve_load_case(self, design_entity_analysis: '_6174.SynchroniserSleeveLoadCase') -> '_5496.SynchroniserSleeveSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SynchroniserSleeveSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5496.SynchroniserSleeveSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter(self, design_entity: '_2118.TorqueConverter') -> '_5499.TorqueConverterSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5499.TorqueConverterSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_load_case(self, design_entity_analysis: '_6178.TorqueConverterLoadCase') -> '_5499.TorqueConverterSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5499.TorqueConverterSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_pump(self, design_entity: '_2119.TorqueConverterPump') -> '_5498.TorqueConverterPumpSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterPumpSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5498.TorqueConverterPumpSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_pump_load_case(self, design_entity_analysis: '_6179.TorqueConverterPumpLoadCase') -> '_5498.TorqueConverterPumpSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterPumpSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5498.TorqueConverterPumpSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_turbine(self, design_entity: '_2121.TorqueConverterTurbine') -> '_5500.TorqueConverterTurbineSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterTurbineSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5500.TorqueConverterTurbineSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_turbine_load_case(self, design_entity_analysis: '_6180.TorqueConverterTurbineLoadCase') -> '_5500.TorqueConverterTurbineSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterTurbineSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5500.TorqueConverterTurbineSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_belt_connection(self, design_entity: '_1816.CVTBeltConnection') -> '_5424.CVTBeltConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CVTBeltConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5424.CVTBeltConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cvt_belt_connection_load_case(self, design_entity_analysis: '_6066.CVTBeltConnectionLoadCase') -> '_5424.CVTBeltConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CVTBeltConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5424.CVTBeltConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_connection(self, design_entity: '_1811.BeltConnection') -> '_5393.BeltConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BeltConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5393.BeltConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_belt_connection_load_case(self, design_entity_analysis: '_6033.BeltConnectionLoadCase') -> '_5393.BeltConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BeltConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5393.BeltConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coaxial_connection(self, design_entity: '_1812.CoaxialConnection') -> '_5408.CoaxialConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CoaxialConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5408.CoaxialConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coaxial_connection_load_case(self, design_entity_analysis: '_6048.CoaxialConnectionLoadCase') -> '_5408.CoaxialConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CoaxialConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5408.CoaxialConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_connection(self, design_entity: '_1815.Connection') -> '_5419.ConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5419.ConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_connection_load_case(self, design_entity_analysis: '_6061.ConnectionLoadCase') -> '_5419.ConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5419.ConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection(self, design_entity: '_1824.InterMountableComponentConnection') -> '_5445.InterMountableComponentConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.InterMountableComponentConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5445.InterMountableComponentConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection_load_case(self, design_entity_analysis: '_6116.InterMountableComponentConnectionLoadCase') -> '_5445.InterMountableComponentConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.InterMountableComponentConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5445.InterMountableComponentConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_connection(self, design_entity: '_1827.PlanetaryConnection') -> '_5464.PlanetaryConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PlanetaryConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5464.PlanetaryConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_connection_load_case(self, design_entity_analysis: '_6137.PlanetaryConnectionLoadCase') -> '_5464.PlanetaryConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PlanetaryConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5464.PlanetaryConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_connection(self, design_entity: '_1831.RollingRingConnection') -> '_5471.RollingRingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RollingRingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5471.RollingRingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_connection_load_case(self, design_entity_analysis: '_6148.RollingRingConnectionLoadCase') -> '_5471.RollingRingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RollingRingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5471.RollingRingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1835.ShaftToMountableComponentConnection') -> '_5476.ShaftToMountableComponentConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ShaftToMountableComponentConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5476.ShaftToMountableComponentConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection_load_case(self, design_entity_analysis: '_6153.ShaftToMountableComponentConnectionLoadCase') -> '_5476.ShaftToMountableComponentConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ShaftToMountableComponentConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5476.ShaftToMountableComponentConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1841.BevelDifferentialGearMesh') -> '_5395.BevelDifferentialGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5395.BevelDifferentialGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh_load_case(self, design_entity_analysis: '_6036.BevelDifferentialGearMeshLoadCase') -> '_5395.BevelDifferentialGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5395.BevelDifferentialGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_mesh(self, design_entity: '_1845.ConceptGearMesh') -> '_5413.ConceptGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5413.ConceptGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_mesh_load_case(self, design_entity_analysis: '_6054.ConceptGearMeshLoadCase') -> '_5413.ConceptGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5413.ConceptGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_mesh(self, design_entity: '_1851.FaceGearMesh') -> '_5433.FaceGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FaceGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5433.FaceGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_mesh_load_case(self, design_entity_analysis: '_6092.FaceGearMeshLoadCase') -> '_5433.FaceGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FaceGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5433.FaceGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1865.StraightBevelDiffGearMesh') -> '_5485.StraightBevelDiffGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelDiffGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5485.StraightBevelDiffGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh_load_case(self, design_entity_analysis: '_6164.StraightBevelDiffGearMeshLoadCase') -> '_5485.StraightBevelDiffGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelDiffGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5485.StraightBevelDiffGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_mesh(self, design_entity: '_1843.BevelGearMesh') -> '_5400.BevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5400.BevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6041.BevelGearMeshLoadCase') -> '_5400.BevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5400.BevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_mesh(self, design_entity: '_1847.ConicalGearMesh') -> '_5416.ConicalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConicalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5416.ConicalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_mesh_load_case(self, design_entity_analysis: '_6058.ConicalGearMeshLoadCase') -> '_5416.ConicalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConicalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5416.ConicalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1839.AGMAGleasonConicalGearMesh') -> '_5388.AGMAGleasonConicalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AGMAGleasonConicalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5388.AGMAGleasonConicalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh_load_case(self, design_entity_analysis: '_6028.AGMAGleasonConicalGearMeshLoadCase') -> '_5388.AGMAGleasonConicalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AGMAGleasonConicalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5388.AGMAGleasonConicalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1849.CylindricalGearMesh') -> '_5427.CylindricalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5427.CylindricalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh_load_case(self, design_entity_analysis: '_6071.CylindricalGearMeshLoadCase') -> '_5427.CylindricalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5427.CylindricalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh(self, design_entity: '_1855.HypoidGearMesh') -> '_5441.HypoidGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.HypoidGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5441.HypoidGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6112.HypoidGearMeshLoadCase') -> '_5441.HypoidGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.HypoidGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5441.HypoidGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1858.KlingelnbergCycloPalloidConicalGearMesh') -> '_5446.KlingelnbergCycloPalloidConicalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidConicalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5446.KlingelnbergCycloPalloidConicalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self, design_entity_analysis: '_6118.KlingelnbergCycloPalloidConicalGearMeshLoadCase') -> '_5446.KlingelnbergCycloPalloidConicalGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidConicalGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5446.KlingelnbergCycloPalloidConicalGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1859.KlingelnbergCycloPalloidHypoidGearMesh') -> '_5449.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5449.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6121.KlingelnbergCycloPalloidHypoidGearMeshLoadCase') -> '_5449.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5449.KlingelnbergCycloPalloidHypoidGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1860.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> '_5452.KlingelnbergCycloPalloidSpiralBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5452.KlingelnbergCycloPalloidSpiralBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6124.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase') -> '_5452.KlingelnbergCycloPalloidSpiralBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5452.KlingelnbergCycloPalloidSpiralBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1863.SpiralBevelGearMesh') -> '_5479.SpiralBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpiralBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5479.SpiralBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6157.SpiralBevelGearMeshLoadCase') -> '_5479.SpiralBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpiralBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5479.SpiralBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1867.StraightBevelGearMesh') -> '_5488.StraightBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5488.StraightBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6167.StraightBevelGearMeshLoadCase') -> '_5488.StraightBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5488.StraightBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_mesh(self, design_entity: '_1869.WormGearMesh') -> '_5503.WormGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.WormGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5503.WormGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_mesh_load_case(self, design_entity_analysis: '_6188.WormGearMeshLoadCase') -> '_5503.WormGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.WormGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5503.WormGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1871.ZerolBevelGearMesh') -> '_5506.ZerolBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ZerolBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5506.ZerolBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6191.ZerolBevelGearMeshLoadCase') -> '_5506.ZerolBevelGearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ZerolBevelGearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5506.ZerolBevelGearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_mesh(self, design_entity: '_1853.GearMesh') -> '_5437.GearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5437.GearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_mesh_load_case(self, design_entity_analysis: '_6098.GearMeshLoadCase') -> '_5437.GearMeshSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GearMeshSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5437.GearMeshSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_1879.PartToPartShearCouplingConnection') -> '_5461.PartToPartShearCouplingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PartToPartShearCouplingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5461.PartToPartShearCouplingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection_load_case(self, design_entity_analysis: '_6134.PartToPartShearCouplingConnectionLoadCase') -> '_5461.PartToPartShearCouplingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PartToPartShearCouplingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5461.PartToPartShearCouplingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_connection(self, design_entity: '_1873.ClutchConnection') -> '_5405.ClutchConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ClutchConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5405.ClutchConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_clutch_connection_load_case(self, design_entity_analysis: '_6045.ClutchConnectionLoadCase') -> '_5405.ClutchConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ClutchConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5405.ClutchConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_connection(self, design_entity: '_1875.ConceptCouplingConnection') -> '_5410.ConceptCouplingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptCouplingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5410.ConceptCouplingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_connection_load_case(self, design_entity_analysis: '_6050.ConceptCouplingConnectionLoadCase') -> '_5410.ConceptCouplingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptCouplingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5410.ConceptCouplingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_connection(self, design_entity: '_1877.CouplingConnection') -> '_5421.CouplingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CouplingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5421.CouplingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_coupling_connection_load_case(self, design_entity_analysis: '_6063.CouplingConnectionLoadCase') -> '_5421.CouplingConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CouplingConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5421.CouplingConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_connection(self, design_entity: '_1881.SpringDamperConnection') -> '_5482.SpringDamperConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpringDamperConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5482.SpringDamperConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_connection_load_case(self, design_entity_analysis: '_6159.SpringDamperConnectionLoadCase') -> '_5482.SpringDamperConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpringDamperConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5482.SpringDamperConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_connection(self, design_entity: '_1883.TorqueConverterConnection') -> '_5497.TorqueConverterConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5497.TorqueConverterConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_connection_load_case(self, design_entity_analysis: '_6177.TorqueConverterConnectionLoadCase') -> '_5497.TorqueConverterConnectionSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.TorqueConverterConnectionSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5497.TorqueConverterConnectionSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_assembly(self, design_entity: '_1959.AbstractAssembly') -> '_5386.AbstractAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AbstractAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5386.AbstractAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_assembly_load_case(self, design_entity_analysis: '_6024.AbstractAssemblyLoadCase') -> '_5386.AbstractAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AbstractAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5386.AbstractAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing(self, design_entity: '_1960.AbstractShaftOrHousing') -> '_5387.AbstractShaftOrHousingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AbstractShaftOrHousingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5387.AbstractShaftOrHousingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing_load_case(self, design_entity_analysis: '_6025.AbstractShaftOrHousingLoadCase') -> '_5387.AbstractShaftOrHousingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AbstractShaftOrHousingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5387.AbstractShaftOrHousingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bearing(self, design_entity: '_1963.Bearing') -> '_5392.BearingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BearingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5392.BearingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bearing_load_case(self, design_entity_analysis: '_6032.BearingLoadCase') -> '_5392.BearingSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BearingSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5392.BearingSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bolt(self, design_entity: '_1965.Bolt') -> '_5404.BoltSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BoltSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5404.BoltSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bolt_load_case(self, design_entity_analysis: '_6044.BoltLoadCase') -> '_5404.BoltSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BoltSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5404.BoltSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bolted_joint(self, design_entity: '_1966.BoltedJoint') -> '_5403.BoltedJointSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BoltedJointSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5403.BoltedJointSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bolted_joint_load_case(self, design_entity_analysis: '_6043.BoltedJointLoadCase') -> '_5403.BoltedJointSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BoltedJointSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5403.BoltedJointSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_component(self, design_entity: '_1967.Component') -> '_5409.ComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5409.ComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_component_load_case(self, design_entity_analysis: '_6049.ComponentLoadCase') -> '_5409.ComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5409.ComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_connector(self, design_entity: '_1970.Connector') -> '_5420.ConnectorSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConnectorSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5420.ConnectorSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_connector_load_case(self, design_entity_analysis: '_6062.ConnectorLoadCase') -> '_5420.ConnectorSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConnectorSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5420.ConnectorSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_datum(self, design_entity: '_1971.Datum') -> '_5431.DatumSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.DatumSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5431.DatumSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_datum_load_case(self, design_entity_analysis: '_6077.DatumLoadCase') -> '_5431.DatumSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.DatumSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5431.DatumSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_external_cad_model(self, design_entity: '_1974.ExternalCADModel') -> '_5432.ExternalCADModelSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ExternalCADModelSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5432.ExternalCADModelSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_external_cad_model_load_case(self, design_entity_analysis: '_6090.ExternalCADModelLoadCase') -> '_5432.ExternalCADModelSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ExternalCADModelSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5432.ExternalCADModelSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_flexible_pin_assembly(self, design_entity: '_1975.FlexiblePinAssembly') -> '_5436.FlexiblePinAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FlexiblePinAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5436.FlexiblePinAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_flexible_pin_assembly_load_case(self, design_entity_analysis: '_6094.FlexiblePinAssemblyLoadCase') -> '_5436.FlexiblePinAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FlexiblePinAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5436.FlexiblePinAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_assembly(self, design_entity: '_1958.Assembly') -> '_5391.AssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5391.AssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_assembly_load_case(self, design_entity_analysis: '_6031.AssemblyLoadCase') -> '_5391.AssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5391.AssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_guide_dxf_model(self, design_entity: '_1976.GuideDxfModel') -> '_5440.GuideDxfModelSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GuideDxfModelSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5440.GuideDxfModelSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_guide_dxf_model_load_case(self, design_entity_analysis: '_6102.GuideDxfModelLoadCase') -> '_5440.GuideDxfModelSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GuideDxfModelSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5440.GuideDxfModelSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_imported_fe_component(self, design_entity: '_1979.ImportedFEComponent') -> '_5444.ImportedFEComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ImportedFEComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5444.ImportedFEComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_imported_fe_component_load_case(self, design_entity_analysis: '_6114.ImportedFEComponentLoadCase') -> '_5444.ImportedFEComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ImportedFEComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ImportedFEComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5444.ImportedFEComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_mass_disc(self, design_entity: '_1982.MassDisc') -> '_5455.MassDiscSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.MassDiscSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5455.MassDiscSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_mass_disc_load_case(self, design_entity_analysis: '_6126.MassDiscLoadCase') -> '_5455.MassDiscSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.MassDiscSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5455.MassDiscSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_measurement_component(self, design_entity: '_1983.MeasurementComponent') -> '_5456.MeasurementComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.MeasurementComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5456.MeasurementComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_measurement_component_load_case(self, design_entity_analysis: '_6127.MeasurementComponentLoadCase') -> '_5456.MeasurementComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.MeasurementComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5456.MeasurementComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_mountable_component(self, design_entity: '_1984.MountableComponent') -> '_5458.MountableComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.MountableComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5458.MountableComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_mountable_component_load_case(self, design_entity_analysis: '_6129.MountableComponentLoadCase') -> '_5458.MountableComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.MountableComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5458.MountableComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_oil_seal(self, design_entity: '_1986.OilSeal') -> '_5459.OilSealSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.OilSealSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5459.OilSealSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_oil_seal_load_case(self, design_entity_analysis: '_6131.OilSealLoadCase') -> '_5459.OilSealSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.OilSealSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5459.OilSealSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_part(self, design_entity: '_1987.Part') -> '_5460.PartSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PartSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5460.PartSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_part_load_case(self, design_entity_analysis: '_6133.PartLoadCase') -> '_5460.PartSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PartSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5460.PartSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_planet_carrier(self, design_entity: '_1988.PlanetCarrier') -> '_5466.PlanetCarrierSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PlanetCarrierSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5466.PlanetCarrierSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_planet_carrier_load_case(self, design_entity_analysis: '_6140.PlanetCarrierLoadCase') -> '_5466.PlanetCarrierSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PlanetCarrierSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5466.PlanetCarrierSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_point_load(self, design_entity: '_1990.PointLoad') -> '_5467.PointLoadSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PointLoadSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5467.PointLoadSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_point_load_load_case(self, design_entity_analysis: '_6143.PointLoadLoadCase') -> '_5467.PointLoadSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PointLoadSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5467.PointLoadSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_power_load(self, design_entity: '_1991.PowerLoad') -> '_5468.PowerLoadSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PowerLoadSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5468.PowerLoadSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_power_load_load_case(self, design_entity_analysis: '_6144.PowerLoadLoadCase') -> '_5468.PowerLoadSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PowerLoadSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5468.PowerLoadSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_root_assembly(self, design_entity: '_1993.RootAssembly') -> '_5473.RootAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RootAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5473.RootAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_root_assembly_load_case(self, design_entity_analysis: '_6150.RootAssemblyLoadCase') -> '_5473.RootAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.RootAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5473.RootAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_specialised_assembly(self, design_entity: '_1995.SpecialisedAssembly') -> '_5478.SpecialisedAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpecialisedAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5478.SpecialisedAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_specialised_assembly_load_case(self, design_entity_analysis: '_6154.SpecialisedAssemblyLoadCase') -> '_5478.SpecialisedAssemblySingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpecialisedAssemblySingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5478.SpecialisedAssemblySingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_unbalanced_mass(self, design_entity: '_1996.UnbalancedMass') -> '_5501.UnbalancedMassSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.UnbalancedMassSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5501.UnbalancedMassSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_unbalanced_mass_load_case(self, design_entity_analysis: '_6185.UnbalancedMassLoadCase') -> '_5501.UnbalancedMassSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.UnbalancedMassSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5501.UnbalancedMassSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_virtual_component(self, design_entity: '_1997.VirtualComponent') -> '_5502.VirtualComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.VirtualComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5502.VirtualComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_virtual_component_load_case(self, design_entity_analysis: '_6186.VirtualComponentLoadCase') -> '_5502.VirtualComponentSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.VirtualComponentSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5502.VirtualComponentSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft(self, design_entity: '_2000.Shaft') -> '_5475.ShaftSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ShaftSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5475.ShaftSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_shaft_load_case(self, design_entity_analysis: '_6152.ShaftLoadCase') -> '_5475.ShaftSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ShaftSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5475.ShaftSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear(self, design_entity: '_2038.ConceptGear') -> '_5415.ConceptGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5415.ConceptGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_load_case(self, design_entity_analysis: '_6053.ConceptGearLoadCase') -> '_5415.ConceptGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5415.ConceptGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_set(self, design_entity: '_2039.ConceptGearSet') -> '_5414.ConceptGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5414.ConceptGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_set_load_case(self, design_entity_analysis: '_6055.ConceptGearSetLoadCase') -> '_5414.ConceptGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConceptGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5414.ConceptGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear(self, design_entity: '_2045.FaceGear') -> '_5435.FaceGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FaceGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5435.FaceGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_load_case(self, design_entity_analysis: '_6091.FaceGearLoadCase') -> '_5435.FaceGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FaceGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5435.FaceGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_set(self, design_entity: '_2046.FaceGearSet') -> '_5434.FaceGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FaceGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5434.FaceGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_face_gear_set_load_case(self, design_entity_analysis: '_6093.FaceGearSetLoadCase') -> '_5434.FaceGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.FaceGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5434.FaceGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2030.AGMAGleasonConicalGear') -> '_5390.AGMAGleasonConicalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AGMAGleasonConicalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5390.AGMAGleasonConicalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_load_case(self, design_entity_analysis: '_6027.AGMAGleasonConicalGearLoadCase') -> '_5390.AGMAGleasonConicalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AGMAGleasonConicalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5390.AGMAGleasonConicalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2031.AGMAGleasonConicalGearSet') -> '_5389.AGMAGleasonConicalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AGMAGleasonConicalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5389.AGMAGleasonConicalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set_load_case(self, design_entity_analysis: '_6029.AGMAGleasonConicalGearSetLoadCase') -> '_5389.AGMAGleasonConicalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.AGMAGleasonConicalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5389.AGMAGleasonConicalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear(self, design_entity: '_2032.BevelDifferentialGear') -> '_5397.BevelDifferentialGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5397.BevelDifferentialGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_load_case(self, design_entity_analysis: '_6035.BevelDifferentialGearLoadCase') -> '_5397.BevelDifferentialGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5397.BevelDifferentialGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set(self, design_entity: '_2033.BevelDifferentialGearSet') -> '_5396.BevelDifferentialGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5396.BevelDifferentialGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set_load_case(self, design_entity_analysis: '_6037.BevelDifferentialGearSetLoadCase') -> '_5396.BevelDifferentialGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5396.BevelDifferentialGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2034.BevelDifferentialPlanetGear') -> '_5398.BevelDifferentialPlanetGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialPlanetGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5398.BevelDifferentialPlanetGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear_load_case(self, design_entity_analysis: '_6038.BevelDifferentialPlanetGearLoadCase') -> '_5398.BevelDifferentialPlanetGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialPlanetGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5398.BevelDifferentialPlanetGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2035.BevelDifferentialSunGear') -> '_5399.BevelDifferentialSunGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialSunGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5399.BevelDifferentialSunGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear_load_case(self, design_entity_analysis: '_6039.BevelDifferentialSunGearLoadCase') -> '_5399.BevelDifferentialSunGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelDifferentialSunGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5399.BevelDifferentialSunGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear(self, design_entity: '_2036.BevelGear') -> '_5402.BevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5402.BevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_load_case(self, design_entity_analysis: '_6040.BevelGearLoadCase') -> '_5402.BevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5402.BevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_set(self, design_entity: '_2037.BevelGearSet') -> '_5401.BevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5401.BevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_set_load_case(self, design_entity_analysis: '_6042.BevelGearSetLoadCase') -> '_5401.BevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.BevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5401.BevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear(self, design_entity: '_2040.ConicalGear') -> '_5418.ConicalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConicalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5418.ConicalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_load_case(self, design_entity_analysis: '_6056.ConicalGearLoadCase') -> '_5418.ConicalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConicalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5418.ConicalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_set(self, design_entity: '_2041.ConicalGearSet') -> '_5417.ConicalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConicalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5417.ConicalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_set_load_case(self, design_entity_analysis: '_6060.ConicalGearSetLoadCase') -> '_5417.ConicalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.ConicalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5417.ConicalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear(self, design_entity: '_2042.CylindricalGear') -> '_5429.CylindricalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5429.CylindricalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_load_case(self, design_entity_analysis: '_6069.CylindricalGearLoadCase') -> '_5429.CylindricalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5429.CylindricalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_set(self, design_entity: '_2043.CylindricalGearSet') -> '_5428.CylindricalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5428.CylindricalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_set_load_case(self, design_entity_analysis: '_6073.CylindricalGearSetLoadCase') -> '_5428.CylindricalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5428.CylindricalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear(self, design_entity: '_2044.CylindricalPlanetGear') -> '_5430.CylindricalPlanetGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalPlanetGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5430.CylindricalPlanetGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear_load_case(self, design_entity_analysis: '_6074.CylindricalPlanetGearLoadCase') -> '_5430.CylindricalPlanetGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.CylindricalPlanetGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5430.CylindricalPlanetGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_gear(self, design_entity: '_2047.Gear') -> '_5439.GearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5439.GearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_load_case(self, design_entity_analysis: '_6096.GearLoadCase') -> '_5439.GearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5439.GearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_set(self, design_entity: '_2049.GearSet') -> '_5438.GearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5438.GearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_gear_set_load_case(self, design_entity_analysis: '_6101.GearSetLoadCase') -> '_5438.GearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.GearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5438.GearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear(self, design_entity: '_2051.HypoidGear') -> '_5443.HypoidGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.HypoidGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5443.HypoidGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_load_case(self, design_entity_analysis: '_6111.HypoidGearLoadCase') -> '_5443.HypoidGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.HypoidGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5443.HypoidGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_set(self, design_entity: '_2052.HypoidGearSet') -> '_5442.HypoidGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.HypoidGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5442.HypoidGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_set_load_case(self, design_entity_analysis: '_6113.HypoidGearSetLoadCase') -> '_5442.HypoidGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.HypoidGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5442.HypoidGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2053.KlingelnbergCycloPalloidConicalGear') -> '_5448.KlingelnbergCycloPalloidConicalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidConicalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5448.KlingelnbergCycloPalloidConicalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_load_case(self, design_entity_analysis: '_6117.KlingelnbergCycloPalloidConicalGearLoadCase') -> '_5448.KlingelnbergCycloPalloidConicalGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidConicalGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5448.KlingelnbergCycloPalloidConicalGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2054.KlingelnbergCycloPalloidConicalGearSet') -> '_5447.KlingelnbergCycloPalloidConicalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidConicalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5447.KlingelnbergCycloPalloidConicalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set_load_case(self, design_entity_analysis: '_6119.KlingelnbergCycloPalloidConicalGearSetLoadCase') -> '_5447.KlingelnbergCycloPalloidConicalGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidConicalGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5447.KlingelnbergCycloPalloidConicalGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2055.KlingelnbergCycloPalloidHypoidGear') -> '_5451.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5451.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_load_case(self, design_entity_analysis: '_6120.KlingelnbergCycloPalloidHypoidGearLoadCase') -> '_5451.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5451.KlingelnbergCycloPalloidHypoidGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2056.KlingelnbergCycloPalloidHypoidGearSet') -> '_5450.KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5450.KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self, design_entity_analysis: '_6122.KlingelnbergCycloPalloidHypoidGearSetLoadCase') -> '_5450.KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5450.KlingelnbergCycloPalloidHypoidGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2057.KlingelnbergCycloPalloidSpiralBevelGear') -> '_5454.KlingelnbergCycloPalloidSpiralBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5454.KlingelnbergCycloPalloidSpiralBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6123.KlingelnbergCycloPalloidSpiralBevelGearLoadCase') -> '_5454.KlingelnbergCycloPalloidSpiralBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5454.KlingelnbergCycloPalloidSpiralBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2058.KlingelnbergCycloPalloidSpiralBevelGearSet') -> '_5453.KlingelnbergCycloPalloidSpiralBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5453.KlingelnbergCycloPalloidSpiralBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6125.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase') -> '_5453.KlingelnbergCycloPalloidSpiralBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5453.KlingelnbergCycloPalloidSpiralBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_gear_set(self, design_entity: '_2059.PlanetaryGearSet') -> '_5465.PlanetaryGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PlanetaryGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5465.PlanetaryGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_planetary_gear_set_load_case(self, design_entity_analysis: '_6138.PlanetaryGearSetLoadCase') -> '_5465.PlanetaryGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.PlanetaryGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5465.PlanetaryGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear(self, design_entity: '_2060.SpiralBevelGear') -> '_5481.SpiralBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpiralBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5481.SpiralBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6156.SpiralBevelGearLoadCase') -> '_5481.SpiralBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpiralBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5481.SpiralBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2061.SpiralBevelGearSet') -> '_5480.SpiralBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpiralBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5480.SpiralBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6158.SpiralBevelGearSetLoadCase') -> '_5480.SpiralBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.SpiralBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5480.SpiralBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2062.StraightBevelDiffGear') -> '_5487.StraightBevelDiffGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelDiffGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5487.StraightBevelDiffGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_load_case(self, design_entity_analysis: '_6163.StraightBevelDiffGearLoadCase') -> '_5487.StraightBevelDiffGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelDiffGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5487.StraightBevelDiffGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2063.StraightBevelDiffGearSet') -> '_5486.StraightBevelDiffGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelDiffGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5486.StraightBevelDiffGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set_load_case(self, design_entity_analysis: '_6165.StraightBevelDiffGearSetLoadCase') -> '_5486.StraightBevelDiffGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelDiffGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5486.StraightBevelDiffGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear(self, design_entity: '_2064.StraightBevelGear') -> '_5490.StraightBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5490.StraightBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_load_case(self, design_entity_analysis: '_6166.StraightBevelGearLoadCase') -> '_5490.StraightBevelGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5490.StraightBevelGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set(self, design_entity: '_2065.StraightBevelGearSet') -> '_5489.StraightBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5489.StraightBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set_load_case(self, design_entity_analysis: '_6168.StraightBevelGearSetLoadCase') -> '_5489.StraightBevelGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5489.StraightBevelGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2066.StraightBevelPlanetGear') -> '_5491.StraightBevelPlanetGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelPlanetGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5491.StraightBevelPlanetGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear_load_case(self, design_entity_analysis: '_6169.StraightBevelPlanetGearLoadCase') -> '_5491.StraightBevelPlanetGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelPlanetGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5491.StraightBevelPlanetGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2067.StraightBevelSunGear') -> '_5492.StraightBevelSunGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelSunGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5492.StraightBevelSunGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear_load_case(self, design_entity_analysis: '_6170.StraightBevelSunGearLoadCase') -> '_5492.StraightBevelSunGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.StraightBevelSunGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5492.StraightBevelSunGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear(self, design_entity: '_2068.WormGear') -> '_5505.WormGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.WormGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5505.WormGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_load_case(self, design_entity_analysis: '_6187.WormGearLoadCase') -> '_5505.WormGearSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.WormGearSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_5505.WormGearSingleMeshWhineAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_set(self, design_entity: '_2069.WormGearSet') -> '_5504.WormGearSetSingleMeshWhineAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.WormGearSetSingleMeshWhineAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5504.WormGearSetSingleMeshWhineAnalysis)(method_result) if method_result else None
