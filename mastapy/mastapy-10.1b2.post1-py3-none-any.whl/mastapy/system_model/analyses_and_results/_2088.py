'''_2088.py

ModalAnalysisAnalysis
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
from mastapy.system_model.analyses_and_results.modal_analyses import (
    _4686, _4688, _4689, _4567,
    _4580, _4579, _4585, _4584,
    _4597, _4596, _4599, _4600,
    _4645, _4650, _4648, _4646,
    _4660, _4659, _4670, _4669,
    _4671, _4672, _4674, _4675,
    _4676, _4598, _4566, _4581,
    _4592, _4620, _4640, _4647,
    _4653, _4578, _4583, _4595,
    _4658, _4673, _4568, _4586,
    _4607, _4661, _4573, _4589,
    _4561, _4601, _4616, _4621,
    _4624, _4627, _4655, _4664,
    _4684, _4687, _4612, _4559,
    _4560, _4565, _4577, _4576,
    _4582, _4593, _4605, _4606,
    _4610, _4564, _4615, _4619,
    _4630, _4631, _4636, _4637,
    _4639, _4642, _4643, _4644,
    _4649, _4654, _4677, _4678,
    _4651, _4587, _4588, _4608,
    _4609, _4562, _4563, _4569,
    _4570, _4571, _4572, _4574,
    _4575, _4590, _4591, _4602,
    _4603, _4604, _4613, _4614,
    _4617, _4618, _4622, _4623,
    _4625, _4626, _4628, _4629,
    _4641, _4656, _4657, _4662,
    _4663, _4665, _4666, _4667,
    _4668, _4685
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

_MODAL_ANALYSIS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'ModalAnalysisAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ModalAnalysisAnalysis',)


class ModalAnalysisAnalysis(_2074.SingleAnalysis):
    '''ModalAnalysisAnalysis

    This is a mastapy class.
    '''

    TYPE = _MODAL_ANALYSIS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ModalAnalysisAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    def results_for_worm_gear_set_load_case(self, design_entity_analysis: '_6034.WormGearSetLoadCase') -> '_4686.WormGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.WormGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4686.WormGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear(self, design_entity: '_2015.ZerolBevelGear') -> '_4688.ZerolBevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4688.ZerolBevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_load_case(self, design_entity_analysis: '_6035.ZerolBevelGearLoadCase') -> '_4688.ZerolBevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4688.ZerolBevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2016.ZerolBevelGearSet') -> '_4689.ZerolBevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4689.ZerolBevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set_load_case(self, design_entity_analysis: '_6037.ZerolBevelGearSetLoadCase') -> '_4689.ZerolBevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4689.ZerolBevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_belt_drive(self, design_entity: '_2034.BeltDrive') -> '_4567.BeltDriveModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BeltDriveModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4567.BeltDriveModalAnalysis)(method_result) if method_result else None

    def results_for_belt_drive_load_case(self, design_entity_analysis: '_5886.BeltDriveLoadCase') -> '_4567.BeltDriveModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BeltDriveModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4567.BeltDriveModalAnalysis)(method_result) if method_result else None

    def results_for_clutch(self, design_entity: '_2036.Clutch') -> '_4580.ClutchModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ClutchModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4580.ClutchModalAnalysis)(method_result) if method_result else None

    def results_for_clutch_load_case(self, design_entity_analysis: '_5899.ClutchLoadCase') -> '_4580.ClutchModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ClutchModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4580.ClutchModalAnalysis)(method_result) if method_result else None

    def results_for_clutch_half(self, design_entity: '_2037.ClutchHalf') -> '_4579.ClutchHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ClutchHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4579.ClutchHalfModalAnalysis)(method_result) if method_result else None

    def results_for_clutch_half_load_case(self, design_entity_analysis: '_5898.ClutchHalfLoadCase') -> '_4579.ClutchHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ClutchHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4579.ClutchHalfModalAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling(self, design_entity: '_2039.ConceptCoupling') -> '_4585.ConceptCouplingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4585.ConceptCouplingModalAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_load_case(self, design_entity_analysis: '_5904.ConceptCouplingLoadCase') -> '_4585.ConceptCouplingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4585.ConceptCouplingModalAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_half(self, design_entity: '_2040.ConceptCouplingHalf') -> '_4584.ConceptCouplingHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4584.ConceptCouplingHalfModalAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_half_load_case(self, design_entity_analysis: '_5903.ConceptCouplingHalfLoadCase') -> '_4584.ConceptCouplingHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4584.ConceptCouplingHalfModalAnalysis)(method_result) if method_result else None

    def results_for_coupling(self, design_entity: '_2041.Coupling') -> '_4597.CouplingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CouplingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4597.CouplingModalAnalysis)(method_result) if method_result else None

    def results_for_coupling_load_case(self, design_entity_analysis: '_5917.CouplingLoadCase') -> '_4597.CouplingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CouplingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4597.CouplingModalAnalysis)(method_result) if method_result else None

    def results_for_coupling_half(self, design_entity: '_2042.CouplingHalf') -> '_4596.CouplingHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CouplingHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4596.CouplingHalfModalAnalysis)(method_result) if method_result else None

    def results_for_coupling_half_load_case(self, design_entity_analysis: '_5916.CouplingHalfLoadCase') -> '_4596.CouplingHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CouplingHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4596.CouplingHalfModalAnalysis)(method_result) if method_result else None

    def results_for_cvt(self, design_entity: '_2043.CVT') -> '_4599.CVTModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CVTModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4599.CVTModalAnalysis)(method_result) if method_result else None

    def results_for_cvt_load_case(self, design_entity_analysis: '_5919.CVTLoadCase') -> '_4599.CVTModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CVTModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4599.CVTModalAnalysis)(method_result) if method_result else None

    def results_for_cvt_pulley(self, design_entity: '_2044.CVTPulley') -> '_4600.CVTPulleyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CVTPulleyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4600.CVTPulleyModalAnalysis)(method_result) if method_result else None

    def results_for_cvt_pulley_load_case(self, design_entity_analysis: '_5920.CVTPulleyLoadCase') -> '_4600.CVTPulleyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CVTPulleyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4600.CVTPulleyModalAnalysis)(method_result) if method_result else None

    def results_for_pulley(self, design_entity: '_2045.Pulley') -> '_4645.PulleyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PulleyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4645.PulleyModalAnalysis)(method_result) if method_result else None

    def results_for_pulley_load_case(self, design_entity_analysis: '_5991.PulleyLoadCase') -> '_4645.PulleyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PulleyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4645.PulleyModalAnalysis)(method_result) if method_result else None

    def results_for_shaft_hub_connection(self, design_entity: '_2053.ShaftHubConnection') -> '_4650.ShaftHubConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ShaftHubConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4650.ShaftHubConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_shaft_hub_connection_load_case(self, design_entity_analysis: '_5997.ShaftHubConnectionLoadCase') -> '_4650.ShaftHubConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ShaftHubConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4650.ShaftHubConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring(self, design_entity: '_2051.RollingRing') -> '_4648.RollingRingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.RollingRingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4648.RollingRingModalAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_load_case(self, design_entity_analysis: '_5995.RollingRingLoadCase') -> '_4648.RollingRingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.RollingRingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4648.RollingRingModalAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_assembly(self, design_entity: '_2052.RollingRingAssembly') -> '_4646.RollingRingAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.RollingRingAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4646.RollingRingAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_assembly_load_case(self, design_entity_analysis: '_5993.RollingRingAssemblyLoadCase') -> '_4646.RollingRingAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.RollingRingAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4646.RollingRingAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_spring_damper(self, design_entity: '_2054.SpringDamper') -> '_4660.SpringDamperModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4660.SpringDamperModalAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_load_case(self, design_entity_analysis: '_6007.SpringDamperLoadCase') -> '_4660.SpringDamperModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4660.SpringDamperModalAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_half(self, design_entity: '_2055.SpringDamperHalf') -> '_4659.SpringDamperHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4659.SpringDamperHalfModalAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_half_load_case(self, design_entity_analysis: '_6006.SpringDamperHalfLoadCase') -> '_4659.SpringDamperHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4659.SpringDamperHalfModalAnalysis)(method_result) if method_result else None

    def results_for_synchroniser(self, design_entity: '_2056.Synchroniser') -> '_4670.SynchroniserModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4670.SynchroniserModalAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_load_case(self, design_entity_analysis: '_6018.SynchroniserLoadCase') -> '_4670.SynchroniserModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4670.SynchroniserModalAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_half(self, design_entity: '_2058.SynchroniserHalf') -> '_4669.SynchroniserHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4669.SynchroniserHalfModalAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_half_load_case(self, design_entity_analysis: '_6017.SynchroniserHalfLoadCase') -> '_4669.SynchroniserHalfModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserHalfModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4669.SynchroniserHalfModalAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_part(self, design_entity: '_2059.SynchroniserPart') -> '_4671.SynchroniserPartModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserPartModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4671.SynchroniserPartModalAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_part_load_case(self, design_entity_analysis: '_6019.SynchroniserPartLoadCase') -> '_4671.SynchroniserPartModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserPartModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4671.SynchroniserPartModalAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_sleeve(self, design_entity: '_2060.SynchroniserSleeve') -> '_4672.SynchroniserSleeveModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserSleeveModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4672.SynchroniserSleeveModalAnalysis)(method_result) if method_result else None

    def results_for_synchroniser_sleeve_load_case(self, design_entity_analysis: '_6020.SynchroniserSleeveLoadCase') -> '_4672.SynchroniserSleeveModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserSleeveModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4672.SynchroniserSleeveModalAnalysis)(method_result) if method_result else None

    def results_for_torque_converter(self, design_entity: '_2061.TorqueConverter') -> '_4674.TorqueConverterModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4674.TorqueConverterModalAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_load_case(self, design_entity_analysis: '_6024.TorqueConverterLoadCase') -> '_4674.TorqueConverterModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4674.TorqueConverterModalAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_pump(self, design_entity: '_2062.TorqueConverterPump') -> '_4675.TorqueConverterPumpModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterPumpModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4675.TorqueConverterPumpModalAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_pump_load_case(self, design_entity_analysis: '_6025.TorqueConverterPumpLoadCase') -> '_4675.TorqueConverterPumpModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterPumpModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4675.TorqueConverterPumpModalAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_turbine(self, design_entity: '_2064.TorqueConverterTurbine') -> '_4676.TorqueConverterTurbineModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterTurbineModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4676.TorqueConverterTurbineModalAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_turbine_load_case(self, design_entity_analysis: '_6026.TorqueConverterTurbineLoadCase') -> '_4676.TorqueConverterTurbineModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterTurbineModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4676.TorqueConverterTurbineModalAnalysis)(method_result) if method_result else None

    def results_for_cvt_belt_connection(self, design_entity: '_1766.CVTBeltConnection') -> '_4598.CVTBeltConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CVTBeltConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4598.CVTBeltConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_cvt_belt_connection_load_case(self, design_entity_analysis: '_5918.CVTBeltConnectionLoadCase') -> '_4598.CVTBeltConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CVTBeltConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4598.CVTBeltConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_belt_connection(self, design_entity: '_1761.BeltConnection') -> '_4566.BeltConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BeltConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4566.BeltConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_belt_connection_load_case(self, design_entity_analysis: '_5885.BeltConnectionLoadCase') -> '_4566.BeltConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BeltConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4566.BeltConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_coaxial_connection(self, design_entity: '_1762.CoaxialConnection') -> '_4581.CoaxialConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CoaxialConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4581.CoaxialConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_coaxial_connection_load_case(self, design_entity_analysis: '_5900.CoaxialConnectionLoadCase') -> '_4581.CoaxialConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CoaxialConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4581.CoaxialConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_connection(self, design_entity: '_1765.Connection') -> '_4592.ConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4592.ConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_connection_load_case(self, design_entity_analysis: '_5913.ConnectionLoadCase') -> '_4592.ConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4592.ConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection(self, design_entity: '_1774.InterMountableComponentConnection') -> '_4620.InterMountableComponentConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.InterMountableComponentConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4620.InterMountableComponentConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection_load_case(self, design_entity_analysis: '_5966.InterMountableComponentConnectionLoadCase') -> '_4620.InterMountableComponentConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.InterMountableComponentConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4620.InterMountableComponentConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_planetary_connection(self, design_entity: '_1777.PlanetaryConnection') -> '_4640.PlanetaryConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PlanetaryConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4640.PlanetaryConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_planetary_connection_load_case(self, design_entity_analysis: '_5983.PlanetaryConnectionLoadCase') -> '_4640.PlanetaryConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PlanetaryConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4640.PlanetaryConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_connection(self, design_entity: '_1781.RollingRingConnection') -> '_4647.RollingRingConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.RollingRingConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4647.RollingRingConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_rolling_ring_connection_load_case(self, design_entity_analysis: '_5994.RollingRingConnectionLoadCase') -> '_4647.RollingRingConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.RollingRingConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4647.RollingRingConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1785.ShaftToMountableComponentConnection') -> '_4653.ShaftToMountableComponentConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ShaftToMountableComponentConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4653.ShaftToMountableComponentConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection_load_case(self, design_entity_analysis: '_5999.ShaftToMountableComponentConnectionLoadCase') -> '_4653.ShaftToMountableComponentConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ShaftToMountableComponentConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4653.ShaftToMountableComponentConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_clutch_connection(self, design_entity: '_1823.ClutchConnection') -> '_4578.ClutchConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ClutchConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4578.ClutchConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_clutch_connection_load_case(self, design_entity_analysis: '_5897.ClutchConnectionLoadCase') -> '_4578.ClutchConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ClutchConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4578.ClutchConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_connection(self, design_entity: '_1825.ConceptCouplingConnection') -> '_4583.ConceptCouplingConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4583.ConceptCouplingConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_concept_coupling_connection_load_case(self, design_entity_analysis: '_5902.ConceptCouplingConnectionLoadCase') -> '_4583.ConceptCouplingConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4583.ConceptCouplingConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_coupling_connection(self, design_entity: '_1827.CouplingConnection') -> '_4595.CouplingConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CouplingConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4595.CouplingConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_coupling_connection_load_case(self, design_entity_analysis: '_5915.CouplingConnectionLoadCase') -> '_4595.CouplingConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CouplingConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4595.CouplingConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_connection(self, design_entity: '_1829.SpringDamperConnection') -> '_4658.SpringDamperConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4658.SpringDamperConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_spring_damper_connection_load_case(self, design_entity_analysis: '_6005.SpringDamperConnectionLoadCase') -> '_4658.SpringDamperConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4658.SpringDamperConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_connection(self, design_entity: '_1831.TorqueConverterConnection') -> '_4673.TorqueConverterConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4673.TorqueConverterConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_torque_converter_connection_load_case(self, design_entity_analysis: '_6023.TorqueConverterConnectionLoadCase') -> '_4673.TorqueConverterConnectionModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterConnectionModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4673.TorqueConverterConnectionModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1791.BevelDifferentialGearMesh') -> '_4568.BevelDifferentialGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4568.BevelDifferentialGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh_load_case(self, design_entity_analysis: '_5888.BevelDifferentialGearMeshLoadCase') -> '_4568.BevelDifferentialGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4568.BevelDifferentialGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_mesh(self, design_entity: '_1795.ConceptGearMesh') -> '_4586.ConceptGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4586.ConceptGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_mesh_load_case(self, design_entity_analysis: '_5906.ConceptGearMeshLoadCase') -> '_4586.ConceptGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4586.ConceptGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_face_gear_mesh(self, design_entity: '_1801.FaceGearMesh') -> '_4607.FaceGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.FaceGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4607.FaceGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_face_gear_mesh_load_case(self, design_entity_analysis: '_5942.FaceGearMeshLoadCase') -> '_4607.FaceGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.FaceGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4607.FaceGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1815.StraightBevelDiffGearMesh') -> '_4661.StraightBevelDiffGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4661.StraightBevelDiffGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh_load_case(self, design_entity_analysis: '_6010.StraightBevelDiffGearMeshLoadCase') -> '_4661.StraightBevelDiffGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4661.StraightBevelDiffGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_mesh(self, design_entity: '_1793.BevelGearMesh') -> '_4573.BevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4573.BevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_mesh_load_case(self, design_entity_analysis: '_5893.BevelGearMeshLoadCase') -> '_4573.BevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4573.BevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_mesh(self, design_entity: '_1797.ConicalGearMesh') -> '_4589.ConicalGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4589.ConicalGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_mesh_load_case(self, design_entity_analysis: '_5910.ConicalGearMeshLoadCase') -> '_4589.ConicalGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4589.ConicalGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1789.AGMAGleasonConicalGearMesh') -> '_4561.AGMAGleasonConicalGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4561.AGMAGleasonConicalGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh_load_case(self, design_entity_analysis: '_5880.AGMAGleasonConicalGearMeshLoadCase') -> '_4561.AGMAGleasonConicalGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4561.AGMAGleasonConicalGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1799.CylindricalGearMesh') -> '_4601.CylindricalGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4601.CylindricalGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh_load_case(self, design_entity_analysis: '_5923.CylindricalGearMeshLoadCase') -> '_4601.CylindricalGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4601.CylindricalGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh(self, design_entity: '_1805.HypoidGearMesh') -> '_4616.HypoidGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4616.HypoidGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_5962.HypoidGearMeshLoadCase') -> '_4616.HypoidGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4616.HypoidGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1808.KlingelnbergCycloPalloidConicalGearMesh') -> '_4621.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4621.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self, design_entity_analysis: '_5968.KlingelnbergCycloPalloidConicalGearMeshLoadCase') -> '_4621.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4621.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1809.KlingelnbergCycloPalloidHypoidGearMesh') -> '_4624.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4624.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_5971.KlingelnbergCycloPalloidHypoidGearMeshLoadCase') -> '_4624.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4624.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1810.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> '_4627.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4627.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_5974.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase') -> '_4627.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4627.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1813.SpiralBevelGearMesh') -> '_4655.SpiralBevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4655.SpiralBevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6003.SpiralBevelGearMeshLoadCase') -> '_4655.SpiralBevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4655.SpiralBevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1817.StraightBevelGearMesh') -> '_4664.StraightBevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4664.StraightBevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6013.StraightBevelGearMeshLoadCase') -> '_4664.StraightBevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4664.StraightBevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_mesh(self, design_entity: '_1819.WormGearMesh') -> '_4684.WormGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.WormGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4684.WormGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_mesh_load_case(self, design_entity_analysis: '_6033.WormGearMeshLoadCase') -> '_4684.WormGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.WormGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4684.WormGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1821.ZerolBevelGearMesh') -> '_4687.ZerolBevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4687.ZerolBevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6036.ZerolBevelGearMeshLoadCase') -> '_4687.ZerolBevelGearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4687.ZerolBevelGearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_gear_mesh(self, design_entity: '_1803.GearMesh') -> '_4612.GearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.GearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4612.GearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_gear_mesh_load_case(self, design_entity_analysis: '_5948.GearMeshLoadCase') -> '_4612.GearMeshModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.GearMeshModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4612.GearMeshModalAnalysis)(method_result) if method_result else None

    def results_for_abstract_assembly(self, design_entity: '_1907.AbstractAssembly') -> '_4559.AbstractAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AbstractAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4559.AbstractAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_abstract_assembly_load_case(self, design_entity_analysis: '_5876.AbstractAssemblyLoadCase') -> '_4559.AbstractAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AbstractAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4559.AbstractAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing(self, design_entity: '_1908.AbstractShaftOrHousing') -> '_4560.AbstractShaftOrHousingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftOrHousingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4560.AbstractShaftOrHousingModalAnalysis)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing_load_case(self, design_entity_analysis: '_5877.AbstractShaftOrHousingLoadCase') -> '_4560.AbstractShaftOrHousingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftOrHousingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4560.AbstractShaftOrHousingModalAnalysis)(method_result) if method_result else None

    def results_for_bearing(self, design_entity: '_1910.Bearing') -> '_4565.BearingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BearingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4565.BearingModalAnalysis)(method_result) if method_result else None

    def results_for_bearing_load_case(self, design_entity_analysis: '_5884.BearingLoadCase') -> '_4565.BearingModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BearingModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4565.BearingModalAnalysis)(method_result) if method_result else None

    def results_for_bolt(self, design_entity: '_1912.Bolt') -> '_4577.BoltModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BoltModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4577.BoltModalAnalysis)(method_result) if method_result else None

    def results_for_bolt_load_case(self, design_entity_analysis: '_5896.BoltLoadCase') -> '_4577.BoltModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BoltModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4577.BoltModalAnalysis)(method_result) if method_result else None

    def results_for_bolted_joint(self, design_entity: '_1913.BoltedJoint') -> '_4576.BoltedJointModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BoltedJointModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4576.BoltedJointModalAnalysis)(method_result) if method_result else None

    def results_for_bolted_joint_load_case(self, design_entity_analysis: '_5895.BoltedJointLoadCase') -> '_4576.BoltedJointModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BoltedJointModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4576.BoltedJointModalAnalysis)(method_result) if method_result else None

    def results_for_component(self, design_entity: '_1914.Component') -> '_4582.ComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4582.ComponentModalAnalysis)(method_result) if method_result else None

    def results_for_component_load_case(self, design_entity_analysis: '_5901.ComponentLoadCase') -> '_4582.ComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4582.ComponentModalAnalysis)(method_result) if method_result else None

    def results_for_connector(self, design_entity: '_1917.Connector') -> '_4593.ConnectorModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConnectorModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4593.ConnectorModalAnalysis)(method_result) if method_result else None

    def results_for_connector_load_case(self, design_entity_analysis: '_5914.ConnectorLoadCase') -> '_4593.ConnectorModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConnectorModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4593.ConnectorModalAnalysis)(method_result) if method_result else None

    def results_for_datum(self, design_entity: '_1918.Datum') -> '_4605.DatumModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.DatumModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4605.DatumModalAnalysis)(method_result) if method_result else None

    def results_for_datum_load_case(self, design_entity_analysis: '_5929.DatumLoadCase') -> '_4605.DatumModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.DatumModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4605.DatumModalAnalysis)(method_result) if method_result else None

    def results_for_external_cad_model(self, design_entity: '_1921.ExternalCADModel') -> '_4606.ExternalCADModelModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ExternalCADModelModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4606.ExternalCADModelModalAnalysis)(method_result) if method_result else None

    def results_for_external_cad_model_load_case(self, design_entity_analysis: '_5940.ExternalCADModelLoadCase') -> '_4606.ExternalCADModelModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ExternalCADModelModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4606.ExternalCADModelModalAnalysis)(method_result) if method_result else None

    def results_for_flexible_pin_assembly(self, design_entity: '_1922.FlexiblePinAssembly') -> '_4610.FlexiblePinAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.FlexiblePinAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4610.FlexiblePinAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_flexible_pin_assembly_load_case(self, design_entity_analysis: '_5944.FlexiblePinAssemblyLoadCase') -> '_4610.FlexiblePinAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.FlexiblePinAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4610.FlexiblePinAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_assembly(self, design_entity: '_1906.Assembly') -> '_4564.AssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4564.AssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_assembly_load_case(self, design_entity_analysis: '_5883.AssemblyLoadCase') -> '_4564.AssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4564.AssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_guide_dxf_model(self, design_entity: '_1923.GuideDxfModel') -> '_4615.GuideDxfModelModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.GuideDxfModelModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4615.GuideDxfModelModalAnalysis)(method_result) if method_result else None

    def results_for_guide_dxf_model_load_case(self, design_entity_analysis: '_5952.GuideDxfModelLoadCase') -> '_4615.GuideDxfModelModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.GuideDxfModelModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4615.GuideDxfModelModalAnalysis)(method_result) if method_result else None

    def results_for_imported_fe_component(self, design_entity: '_1926.ImportedFEComponent') -> '_4619.ImportedFEComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ImportedFEComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4619.ImportedFEComponentModalAnalysis)(method_result) if method_result else None

    def results_for_imported_fe_component_load_case(self, design_entity_analysis: '_5964.ImportedFEComponentLoadCase') -> '_4619.ImportedFEComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ImportedFEComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ImportedFEComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4619.ImportedFEComponentModalAnalysis)(method_result) if method_result else None

    def results_for_mass_disc(self, design_entity: '_1928.MassDisc') -> '_4630.MassDiscModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.MassDiscModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4630.MassDiscModalAnalysis)(method_result) if method_result else None

    def results_for_mass_disc_load_case(self, design_entity_analysis: '_5976.MassDiscLoadCase') -> '_4630.MassDiscModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.MassDiscModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4630.MassDiscModalAnalysis)(method_result) if method_result else None

    def results_for_measurement_component(self, design_entity: '_1929.MeasurementComponent') -> '_4631.MeasurementComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.MeasurementComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4631.MeasurementComponentModalAnalysis)(method_result) if method_result else None

    def results_for_measurement_component_load_case(self, design_entity_analysis: '_5977.MeasurementComponentLoadCase') -> '_4631.MeasurementComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.MeasurementComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4631.MeasurementComponentModalAnalysis)(method_result) if method_result else None

    def results_for_mountable_component(self, design_entity: '_1930.MountableComponent') -> '_4636.MountableComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.MountableComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4636.MountableComponentModalAnalysis)(method_result) if method_result else None

    def results_for_mountable_component_load_case(self, design_entity_analysis: '_5978.MountableComponentLoadCase') -> '_4636.MountableComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.MountableComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4636.MountableComponentModalAnalysis)(method_result) if method_result else None

    def results_for_oil_seal(self, design_entity: '_1931.OilSeal') -> '_4637.OilSealModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.OilSealModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4637.OilSealModalAnalysis)(method_result) if method_result else None

    def results_for_oil_seal_load_case(self, design_entity_analysis: '_5980.OilSealLoadCase') -> '_4637.OilSealModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.OilSealModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4637.OilSealModalAnalysis)(method_result) if method_result else None

    def results_for_part(self, design_entity: '_1933.Part') -> '_4639.PartModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PartModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4639.PartModalAnalysis)(method_result) if method_result else None

    def results_for_part_load_case(self, design_entity_analysis: '_5982.PartLoadCase') -> '_4639.PartModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PartModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4639.PartModalAnalysis)(method_result) if method_result else None

    def results_for_planet_carrier(self, design_entity: '_1934.PlanetCarrier') -> '_4642.PlanetCarrierModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PlanetCarrierModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4642.PlanetCarrierModalAnalysis)(method_result) if method_result else None

    def results_for_planet_carrier_load_case(self, design_entity_analysis: '_5986.PlanetCarrierLoadCase') -> '_4642.PlanetCarrierModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PlanetCarrierModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4642.PlanetCarrierModalAnalysis)(method_result) if method_result else None

    def results_for_point_load(self, design_entity: '_1936.PointLoad') -> '_4643.PointLoadModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PointLoadModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4643.PointLoadModalAnalysis)(method_result) if method_result else None

    def results_for_point_load_load_case(self, design_entity_analysis: '_5989.PointLoadLoadCase') -> '_4643.PointLoadModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PointLoadModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4643.PointLoadModalAnalysis)(method_result) if method_result else None

    def results_for_power_load(self, design_entity: '_1937.PowerLoad') -> '_4644.PowerLoadModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PowerLoadModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4644.PowerLoadModalAnalysis)(method_result) if method_result else None

    def results_for_power_load_load_case(self, design_entity_analysis: '_5990.PowerLoadLoadCase') -> '_4644.PowerLoadModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PowerLoadModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4644.PowerLoadModalAnalysis)(method_result) if method_result else None

    def results_for_root_assembly(self, design_entity: '_1938.RootAssembly') -> '_4649.RootAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.RootAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4649.RootAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_root_assembly_load_case(self, design_entity_analysis: '_5996.RootAssemblyLoadCase') -> '_4649.RootAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.RootAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4649.RootAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_specialised_assembly(self, design_entity: '_1940.SpecialisedAssembly') -> '_4654.SpecialisedAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpecialisedAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4654.SpecialisedAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_specialised_assembly_load_case(self, design_entity_analysis: '_6000.SpecialisedAssemblyLoadCase') -> '_4654.SpecialisedAssemblyModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpecialisedAssemblyModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4654.SpecialisedAssemblyModalAnalysis)(method_result) if method_result else None

    def results_for_unbalanced_mass(self, design_entity: '_1941.UnbalancedMass') -> '_4677.UnbalancedMassModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.UnbalancedMassModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4677.UnbalancedMassModalAnalysis)(method_result) if method_result else None

    def results_for_unbalanced_mass_load_case(self, design_entity_analysis: '_6030.UnbalancedMassLoadCase') -> '_4677.UnbalancedMassModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.UnbalancedMassModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4677.UnbalancedMassModalAnalysis)(method_result) if method_result else None

    def results_for_virtual_component(self, design_entity: '_1942.VirtualComponent') -> '_4678.VirtualComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.VirtualComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4678.VirtualComponentModalAnalysis)(method_result) if method_result else None

    def results_for_virtual_component_load_case(self, design_entity_analysis: '_6031.VirtualComponentLoadCase') -> '_4678.VirtualComponentModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.VirtualComponentModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4678.VirtualComponentModalAnalysis)(method_result) if method_result else None

    def results_for_shaft(self, design_entity: '_1945.Shaft') -> '_4651.ShaftModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ShaftModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4651.ShaftModalAnalysis)(method_result) if method_result else None

    def results_for_shaft_load_case(self, design_entity_analysis: '_5998.ShaftLoadCase') -> '_4651.ShaftModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ShaftModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4651.ShaftModalAnalysis)(method_result) if method_result else None

    def results_for_concept_gear(self, design_entity: '_1983.ConceptGear') -> '_4587.ConceptGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4587.ConceptGearModalAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_load_case(self, design_entity_analysis: '_5905.ConceptGearLoadCase') -> '_4587.ConceptGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4587.ConceptGearModalAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_set(self, design_entity: '_1984.ConceptGearSet') -> '_4588.ConceptGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4588.ConceptGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_concept_gear_set_load_case(self, design_entity_analysis: '_5907.ConceptGearSetLoadCase') -> '_4588.ConceptGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4588.ConceptGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_face_gear(self, design_entity: '_1990.FaceGear') -> '_4608.FaceGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.FaceGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4608.FaceGearModalAnalysis)(method_result) if method_result else None

    def results_for_face_gear_load_case(self, design_entity_analysis: '_5941.FaceGearLoadCase') -> '_4608.FaceGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.FaceGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4608.FaceGearModalAnalysis)(method_result) if method_result else None

    def results_for_face_gear_set(self, design_entity: '_1991.FaceGearSet') -> '_4609.FaceGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.FaceGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4609.FaceGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_face_gear_set_load_case(self, design_entity_analysis: '_5943.FaceGearSetLoadCase') -> '_4609.FaceGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.FaceGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4609.FaceGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear(self, design_entity: '_1975.AGMAGleasonConicalGear') -> '_4562.AGMAGleasonConicalGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4562.AGMAGleasonConicalGearModalAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_load_case(self, design_entity_analysis: '_5879.AGMAGleasonConicalGearLoadCase') -> '_4562.AGMAGleasonConicalGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4562.AGMAGleasonConicalGearModalAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_1976.AGMAGleasonConicalGearSet') -> '_4563.AGMAGleasonConicalGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4563.AGMAGleasonConicalGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set_load_case(self, design_entity_analysis: '_5881.AGMAGleasonConicalGearSetLoadCase') -> '_4563.AGMAGleasonConicalGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4563.AGMAGleasonConicalGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear(self, design_entity: '_1977.BevelDifferentialGear') -> '_4569.BevelDifferentialGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4569.BevelDifferentialGearModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_load_case(self, design_entity_analysis: '_5887.BevelDifferentialGearLoadCase') -> '_4569.BevelDifferentialGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4569.BevelDifferentialGearModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set(self, design_entity: '_1978.BevelDifferentialGearSet') -> '_4570.BevelDifferentialGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4570.BevelDifferentialGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set_load_case(self, design_entity_analysis: '_5889.BevelDifferentialGearSetLoadCase') -> '_4570.BevelDifferentialGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4570.BevelDifferentialGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear(self, design_entity: '_1979.BevelDifferentialPlanetGear') -> '_4571.BevelDifferentialPlanetGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialPlanetGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4571.BevelDifferentialPlanetGearModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear_load_case(self, design_entity_analysis: '_5890.BevelDifferentialPlanetGearLoadCase') -> '_4571.BevelDifferentialPlanetGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialPlanetGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4571.BevelDifferentialPlanetGearModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear(self, design_entity: '_1980.BevelDifferentialSunGear') -> '_4572.BevelDifferentialSunGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialSunGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4572.BevelDifferentialSunGearModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear_load_case(self, design_entity_analysis: '_5891.BevelDifferentialSunGearLoadCase') -> '_4572.BevelDifferentialSunGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialSunGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4572.BevelDifferentialSunGearModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear(self, design_entity: '_1981.BevelGear') -> '_4574.BevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4574.BevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_load_case(self, design_entity_analysis: '_5892.BevelGearLoadCase') -> '_4574.BevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4574.BevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_set(self, design_entity: '_1982.BevelGearSet') -> '_4575.BevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4575.BevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_bevel_gear_set_load_case(self, design_entity_analysis: '_5894.BevelGearSetLoadCase') -> '_4575.BevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.BevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4575.BevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_conical_gear(self, design_entity: '_1985.ConicalGear') -> '_4590.ConicalGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4590.ConicalGearModalAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_load_case(self, design_entity_analysis: '_5908.ConicalGearLoadCase') -> '_4590.ConicalGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4590.ConicalGearModalAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_set(self, design_entity: '_1986.ConicalGearSet') -> '_4591.ConicalGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4591.ConicalGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_conical_gear_set_load_case(self, design_entity_analysis: '_5912.ConicalGearSetLoadCase') -> '_4591.ConicalGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4591.ConicalGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear(self, design_entity: '_1987.CylindricalGear') -> '_4602.CylindricalGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4602.CylindricalGearModalAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_load_case(self, design_entity_analysis: '_5921.CylindricalGearLoadCase') -> '_4602.CylindricalGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4602.CylindricalGearModalAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_set(self, design_entity: '_1988.CylindricalGearSet') -> '_4603.CylindricalGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4603.CylindricalGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_gear_set_load_case(self, design_entity_analysis: '_5925.CylindricalGearSetLoadCase') -> '_4603.CylindricalGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4603.CylindricalGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear(self, design_entity: '_1989.CylindricalPlanetGear') -> '_4604.CylindricalPlanetGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CylindricalPlanetGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4604.CylindricalPlanetGearModalAnalysis)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear_load_case(self, design_entity_analysis: '_5926.CylindricalPlanetGearLoadCase') -> '_4604.CylindricalPlanetGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.CylindricalPlanetGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4604.CylindricalPlanetGearModalAnalysis)(method_result) if method_result else None

    def results_for_gear(self, design_entity: '_1992.Gear') -> '_4613.GearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.GearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4613.GearModalAnalysis)(method_result) if method_result else None

    def results_for_gear_load_case(self, design_entity_analysis: '_5946.GearLoadCase') -> '_4613.GearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.GearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4613.GearModalAnalysis)(method_result) if method_result else None

    def results_for_gear_set(self, design_entity: '_1994.GearSet') -> '_4614.GearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.GearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4614.GearSetModalAnalysis)(method_result) if method_result else None

    def results_for_gear_set_load_case(self, design_entity_analysis: '_5951.GearSetLoadCase') -> '_4614.GearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.GearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4614.GearSetModalAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear(self, design_entity: '_1996.HypoidGear') -> '_4617.HypoidGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4617.HypoidGearModalAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_load_case(self, design_entity_analysis: '_5961.HypoidGearLoadCase') -> '_4617.HypoidGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4617.HypoidGearModalAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_set(self, design_entity: '_1997.HypoidGearSet') -> '_4618.HypoidGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4618.HypoidGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_hypoid_gear_set_load_case(self, design_entity_analysis: '_5963.HypoidGearSetLoadCase') -> '_4618.HypoidGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4618.HypoidGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_1998.KlingelnbergCycloPalloidConicalGear') -> '_4622.KlingelnbergCycloPalloidConicalGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4622.KlingelnbergCycloPalloidConicalGearModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_load_case(self, design_entity_analysis: '_5967.KlingelnbergCycloPalloidConicalGearLoadCase') -> '_4622.KlingelnbergCycloPalloidConicalGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4622.KlingelnbergCycloPalloidConicalGearModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_1999.KlingelnbergCycloPalloidConicalGearSet') -> '_4623.KlingelnbergCycloPalloidConicalGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4623.KlingelnbergCycloPalloidConicalGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set_load_case(self, design_entity_analysis: '_5969.KlingelnbergCycloPalloidConicalGearSetLoadCase') -> '_4623.KlingelnbergCycloPalloidConicalGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4623.KlingelnbergCycloPalloidConicalGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2000.KlingelnbergCycloPalloidHypoidGear') -> '_4625.KlingelnbergCycloPalloidHypoidGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4625.KlingelnbergCycloPalloidHypoidGearModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_load_case(self, design_entity_analysis: '_5970.KlingelnbergCycloPalloidHypoidGearLoadCase') -> '_4625.KlingelnbergCycloPalloidHypoidGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4625.KlingelnbergCycloPalloidHypoidGearModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2001.KlingelnbergCycloPalloidHypoidGearSet') -> '_4626.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4626.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self, design_entity_analysis: '_5972.KlingelnbergCycloPalloidHypoidGearSetLoadCase') -> '_4626.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4626.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2002.KlingelnbergCycloPalloidSpiralBevelGear') -> '_4628.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4628.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self, design_entity_analysis: '_5973.KlingelnbergCycloPalloidSpiralBevelGearLoadCase') -> '_4628.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4628.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2003.KlingelnbergCycloPalloidSpiralBevelGearSet') -> '_4629.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4629.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_5975.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase') -> '_4629.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4629.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_planetary_gear_set(self, design_entity: '_2004.PlanetaryGearSet') -> '_4641.PlanetaryGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PlanetaryGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4641.PlanetaryGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_planetary_gear_set_load_case(self, design_entity_analysis: '_5984.PlanetaryGearSetLoadCase') -> '_4641.PlanetaryGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.PlanetaryGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4641.PlanetaryGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear(self, design_entity: '_2005.SpiralBevelGear') -> '_4656.SpiralBevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4656.SpiralBevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6002.SpiralBevelGearLoadCase') -> '_4656.SpiralBevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4656.SpiralBevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2006.SpiralBevelGearSet') -> '_4657.SpiralBevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4657.SpiralBevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6004.SpiralBevelGearSetLoadCase') -> '_4657.SpiralBevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4657.SpiralBevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2007.StraightBevelDiffGear') -> '_4662.StraightBevelDiffGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4662.StraightBevelDiffGearModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_load_case(self, design_entity_analysis: '_6009.StraightBevelDiffGearLoadCase') -> '_4662.StraightBevelDiffGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4662.StraightBevelDiffGearModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2008.StraightBevelDiffGearSet') -> '_4663.StraightBevelDiffGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4663.StraightBevelDiffGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set_load_case(self, design_entity_analysis: '_6011.StraightBevelDiffGearSetLoadCase') -> '_4663.StraightBevelDiffGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4663.StraightBevelDiffGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear(self, design_entity: '_2009.StraightBevelGear') -> '_4665.StraightBevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4665.StraightBevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_load_case(self, design_entity_analysis: '_6012.StraightBevelGearLoadCase') -> '_4665.StraightBevelGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4665.StraightBevelGearModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set(self, design_entity: '_2010.StraightBevelGearSet') -> '_4666.StraightBevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4666.StraightBevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set_load_case(self, design_entity_analysis: '_6014.StraightBevelGearSetLoadCase') -> '_4666.StraightBevelGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4666.StraightBevelGearSetModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2011.StraightBevelPlanetGear') -> '_4667.StraightBevelPlanetGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelPlanetGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4667.StraightBevelPlanetGearModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear_load_case(self, design_entity_analysis: '_6015.StraightBevelPlanetGearLoadCase') -> '_4667.StraightBevelPlanetGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelPlanetGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4667.StraightBevelPlanetGearModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2012.StraightBevelSunGear') -> '_4668.StraightBevelSunGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelSunGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4668.StraightBevelSunGearModalAnalysis)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear_load_case(self, design_entity_analysis: '_6016.StraightBevelSunGearLoadCase') -> '_4668.StraightBevelSunGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelSunGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4668.StraightBevelSunGearModalAnalysis)(method_result) if method_result else None

    def results_for_worm_gear(self, design_entity: '_2013.WormGear') -> '_4685.WormGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.WormGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4685.WormGearModalAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_load_case(self, design_entity_analysis: '_6032.WormGearLoadCase') -> '_4685.WormGearModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.WormGearModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new(_4685.WormGearModalAnalysis)(method_result) if method_result else None

    def results_for_worm_gear_set(self, design_entity: '_2014.WormGearSet') -> '_4686.WormGearSetModalAnalysis':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.modal_analyses.WormGearSetModalAnalysis
        '''

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_4686.WormGearSetModalAnalysis)(method_result) if method_result else None
