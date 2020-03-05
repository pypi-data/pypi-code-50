'''_2175.py

CompoundModalAnalysisAnalysis
'''


from typing import Iterable

from mastapy.system_model.part_model import (
    _1959, _1960, _1963, _1965,
    _1966, _1967, _1970, _1971,
    _1974, _1975, _1958, _1976,
    _1979, _1982, _1983, _1984,
    _1986, _1987, _1988, _1990,
    _1991, _1993, _1995, _1996,
    _1997
)
from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
    _4823, _4824, _4829, _4840,
    _4841, _4846, _4857, _4868,
    _4869, _4873, _4828, _4877,
    _4881, _4892, _4893, _4894,
    _4895, _4896, _4902, _4903,
    _4904, _4909, _4913, _4936,
    _4937, _4910, _4850, _4852,
    _4870, _4872, _4825, _4827,
    _4832, _4834, _4835, _4836,
    _4837, _4839, _4853, _4855,
    _4864, _4866, _4867, _4874,
    _4876, _4878, _4880, _4883,
    _4885, _4886, _4888, _4889,
    _4891, _4901, _4914, _4916,
    _4920, _4922, _4923, _4925,
    _4926, _4927, _4938, _4940,
    _4941, _4943, _4897, _4899,
    _4831, _4842, _4844, _4847,
    _4849, _4858, _4860, _4862,
    _4863, _4905, _4911, _4907,
    _4906, _4917, _4919, _4928,
    _4929, _4930, _4931, _4932,
    _4934, _4935, _4861, _4830,
    _4845, _4856, _4882, _4900,
    _4908, _4912, _4833, _4851,
    _4871, _4921, _4838, _4854,
    _4826, _4865, _4879, _4884,
    _4887, _4890, _4915, _4924,
    _4939, _4942, _4875, _4898,
    _4843, _4848, _4859, _4918,
    _4933
)
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.shaft_model import _2000
from mastapy.system_model.part_model.gears import (
    _2038, _2039, _2045, _2046,
    _2030, _2031, _2032, _2033,
    _2034, _2035, _2036, _2037,
    _2040, _2041, _2042, _2043,
    _2044, _2047, _2049, _2051,
    _2052, _2053, _2054, _2055,
    _2056, _2057, _2058, _2059,
    _2060, _2061, _2062, _2063,
    _2064, _2065, _2066, _2067,
    _2068, _2069, _2070, _2071
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
from mastapy.system_model.analyses_and_results import _2130
from mastapy._internal.python_net import python_net_import

_COMPOUND_MODAL_ANALYSIS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundModalAnalysisAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundModalAnalysisAnalysis',)


class CompoundModalAnalysisAnalysis(_2130.CompoundAnalysis):
    '''CompoundModalAnalysisAnalysis

    This is a mastapy class.
    '''

    TYPE = _COMPOUND_MODAL_ANALYSIS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CompoundModalAnalysisAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    def results_for_abstract_assembly(self, design_entity: '_1959.AbstractAssembly') -> 'Iterable[_4823.AbstractAssemblyCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.AbstractAssemblyCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4823.AbstractAssemblyCompoundModalAnalysis))

    def results_for_abstract_shaft_or_housing(self, design_entity: '_1960.AbstractShaftOrHousing') -> 'Iterable[_4824.AbstractShaftOrHousingCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.AbstractShaftOrHousingCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4824.AbstractShaftOrHousingCompoundModalAnalysis))

    def results_for_bearing(self, design_entity: '_1963.Bearing') -> 'Iterable[_4829.BearingCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BearingCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4829.BearingCompoundModalAnalysis))

    def results_for_bolt(self, design_entity: '_1965.Bolt') -> 'Iterable[_4840.BoltCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BoltCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4840.BoltCompoundModalAnalysis))

    def results_for_bolted_joint(self, design_entity: '_1966.BoltedJoint') -> 'Iterable[_4841.BoltedJointCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BoltedJointCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4841.BoltedJointCompoundModalAnalysis))

    def results_for_component(self, design_entity: '_1967.Component') -> 'Iterable[_4846.ComponentCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ComponentCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4846.ComponentCompoundModalAnalysis))

    def results_for_connector(self, design_entity: '_1970.Connector') -> 'Iterable[_4857.ConnectorCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConnectorCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4857.ConnectorCompoundModalAnalysis))

    def results_for_datum(self, design_entity: '_1971.Datum') -> 'Iterable[_4868.DatumCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.DatumCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4868.DatumCompoundModalAnalysis))

    def results_for_external_cad_model(self, design_entity: '_1974.ExternalCADModel') -> 'Iterable[_4869.ExternalCADModelCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ExternalCADModelCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4869.ExternalCADModelCompoundModalAnalysis))

    def results_for_flexible_pin_assembly(self, design_entity: '_1975.FlexiblePinAssembly') -> 'Iterable[_4873.FlexiblePinAssemblyCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.FlexiblePinAssemblyCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4873.FlexiblePinAssemblyCompoundModalAnalysis))

    def results_for_assembly(self, design_entity: '_1958.Assembly') -> 'Iterable[_4828.AssemblyCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.AssemblyCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4828.AssemblyCompoundModalAnalysis))

    def results_for_guide_dxf_model(self, design_entity: '_1976.GuideDxfModel') -> 'Iterable[_4877.GuideDxfModelCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.GuideDxfModelCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4877.GuideDxfModelCompoundModalAnalysis))

    def results_for_imported_fe_component(self, design_entity: '_1979.ImportedFEComponent') -> 'Iterable[_4881.ImportedFEComponentCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ImportedFEComponentCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4881.ImportedFEComponentCompoundModalAnalysis))

    def results_for_mass_disc(self, design_entity: '_1982.MassDisc') -> 'Iterable[_4892.MassDiscCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.MassDiscCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4892.MassDiscCompoundModalAnalysis))

    def results_for_measurement_component(self, design_entity: '_1983.MeasurementComponent') -> 'Iterable[_4893.MeasurementComponentCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.MeasurementComponentCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4893.MeasurementComponentCompoundModalAnalysis))

    def results_for_mountable_component(self, design_entity: '_1984.MountableComponent') -> 'Iterable[_4894.MountableComponentCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.MountableComponentCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4894.MountableComponentCompoundModalAnalysis))

    def results_for_oil_seal(self, design_entity: '_1986.OilSeal') -> 'Iterable[_4895.OilSealCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.OilSealCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4895.OilSealCompoundModalAnalysis))

    def results_for_part(self, design_entity: '_1987.Part') -> 'Iterable[_4896.PartCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PartCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4896.PartCompoundModalAnalysis))

    def results_for_planet_carrier(self, design_entity: '_1988.PlanetCarrier') -> 'Iterable[_4902.PlanetCarrierCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PlanetCarrierCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4902.PlanetCarrierCompoundModalAnalysis))

    def results_for_point_load(self, design_entity: '_1990.PointLoad') -> 'Iterable[_4903.PointLoadCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PointLoadCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4903.PointLoadCompoundModalAnalysis))

    def results_for_power_load(self, design_entity: '_1991.PowerLoad') -> 'Iterable[_4904.PowerLoadCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PowerLoadCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4904.PowerLoadCompoundModalAnalysis))

    def results_for_root_assembly(self, design_entity: '_1993.RootAssembly') -> 'Iterable[_4909.RootAssemblyCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.RootAssemblyCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4909.RootAssemblyCompoundModalAnalysis))

    def results_for_specialised_assembly(self, design_entity: '_1995.SpecialisedAssembly') -> 'Iterable[_4913.SpecialisedAssemblyCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SpecialisedAssemblyCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4913.SpecialisedAssemblyCompoundModalAnalysis))

    def results_for_unbalanced_mass(self, design_entity: '_1996.UnbalancedMass') -> 'Iterable[_4936.UnbalancedMassCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.UnbalancedMassCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4936.UnbalancedMassCompoundModalAnalysis))

    def results_for_virtual_component(self, design_entity: '_1997.VirtualComponent') -> 'Iterable[_4937.VirtualComponentCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.VirtualComponentCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4937.VirtualComponentCompoundModalAnalysis))

    def results_for_shaft(self, design_entity: '_2000.Shaft') -> 'Iterable[_4910.ShaftCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ShaftCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4910.ShaftCompoundModalAnalysis))

    def results_for_concept_gear(self, design_entity: '_2038.ConceptGear') -> 'Iterable[_4850.ConceptGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConceptGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4850.ConceptGearCompoundModalAnalysis))

    def results_for_concept_gear_set(self, design_entity: '_2039.ConceptGearSet') -> 'Iterable[_4852.ConceptGearSetCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConceptGearSetCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4852.ConceptGearSetCompoundModalAnalysis))

    def results_for_face_gear(self, design_entity: '_2045.FaceGear') -> 'Iterable[_4870.FaceGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.FaceGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4870.FaceGearCompoundModalAnalysis))

    def results_for_face_gear_set(self, design_entity: '_2046.FaceGearSet') -> 'Iterable[_4872.FaceGearSetCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.FaceGearSetCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4872.FaceGearSetCompoundModalAnalysis))

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2030.AGMAGleasonConicalGear') -> 'Iterable[_4825.AGMAGleasonConicalGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.AGMAGleasonConicalGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4825.AGMAGleasonConicalGearCompoundModalAnalysis))

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2031.AGMAGleasonConicalGearSet') -> 'Iterable[_4827.AGMAGleasonConicalGearSetCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.AGMAGleasonConicalGearSetCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4827.AGMAGleasonConicalGearSetCompoundModalAnalysis))

    def results_for_bevel_differential_gear(self, design_entity: '_2032.BevelDifferentialGear') -> 'Iterable[_4832.BevelDifferentialGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BevelDifferentialGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4832.BevelDifferentialGearCompoundModalAnalysis))

    def results_for_bevel_differential_gear_set(self, design_entity: '_2033.BevelDifferentialGearSet') -> 'Iterable[_4834.BevelDifferentialGearSetCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BevelDifferentialGearSetCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4834.BevelDifferentialGearSetCompoundModalAnalysis))

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2034.BevelDifferentialPlanetGear') -> 'Iterable[_4835.BevelDifferentialPlanetGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BevelDifferentialPlanetGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4835.BevelDifferentialPlanetGearCompoundModalAnalysis))

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2035.BevelDifferentialSunGear') -> 'Iterable[_4836.BevelDifferentialSunGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BevelDifferentialSunGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4836.BevelDifferentialSunGearCompoundModalAnalysis))

    def results_for_bevel_gear(self, design_entity: '_2036.BevelGear') -> 'Iterable[_4837.BevelGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BevelGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4837.BevelGearCompoundModalAnalysis))

    def results_for_bevel_gear_set(self, design_entity: '_2037.BevelGearSet') -> 'Iterable[_4839.BevelGearSetCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BevelGearSetCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4839.BevelGearSetCompoundModalAnalysis))

    def results_for_conical_gear(self, design_entity: '_2040.ConicalGear') -> 'Iterable[_4853.ConicalGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConicalGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4853.ConicalGearCompoundModalAnalysis))

    def results_for_conical_gear_set(self, design_entity: '_2041.ConicalGearSet') -> 'Iterable[_4855.ConicalGearSetCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConicalGearSetCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4855.ConicalGearSetCompoundModalAnalysis))

    def results_for_cylindrical_gear(self, design_entity: '_2042.CylindricalGear') -> 'Iterable[_4864.CylindricalGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CylindricalGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4864.CylindricalGearCompoundModalAnalysis))

    def results_for_cylindrical_gear_set(self, design_entity: '_2043.CylindricalGearSet') -> 'Iterable[_4866.CylindricalGearSetCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CylindricalGearSetCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4866.CylindricalGearSetCompoundModalAnalysis))

    def results_for_cylindrical_planet_gear(self, design_entity: '_2044.CylindricalPlanetGear') -> 'Iterable[_4867.CylindricalPlanetGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CylindricalPlanetGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4867.CylindricalPlanetGearCompoundModalAnalysis))

    def results_for_gear(self, design_entity: '_2047.Gear') -> 'Iterable[_4874.GearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.GearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4874.GearCompoundModalAnalysis))

    def results_for_gear_set(self, design_entity: '_2049.GearSet') -> 'Iterable[_4876.GearSetCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.GearSetCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4876.GearSetCompoundModalAnalysis))

    def results_for_hypoid_gear(self, design_entity: '_2051.HypoidGear') -> 'Iterable[_4878.HypoidGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.HypoidGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4878.HypoidGearCompoundModalAnalysis))

    def results_for_hypoid_gear_set(self, design_entity: '_2052.HypoidGearSet') -> 'Iterable[_4880.HypoidGearSetCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.HypoidGearSetCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4880.HypoidGearSetCompoundModalAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2053.KlingelnbergCycloPalloidConicalGear') -> 'Iterable[_4883.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4883.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2054.KlingelnbergCycloPalloidConicalGearSet') -> 'Iterable[_4885.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4885.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2055.KlingelnbergCycloPalloidHypoidGear') -> 'Iterable[_4886.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4886.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2056.KlingelnbergCycloPalloidHypoidGearSet') -> 'Iterable[_4888.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4888.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2057.KlingelnbergCycloPalloidSpiralBevelGear') -> 'Iterable[_4889.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4889.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2058.KlingelnbergCycloPalloidSpiralBevelGearSet') -> 'Iterable[_4891.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4891.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis))

    def results_for_planetary_gear_set(self, design_entity: '_2059.PlanetaryGearSet') -> 'Iterable[_4901.PlanetaryGearSetCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PlanetaryGearSetCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4901.PlanetaryGearSetCompoundModalAnalysis))

    def results_for_spiral_bevel_gear(self, design_entity: '_2060.SpiralBevelGear') -> 'Iterable[_4914.SpiralBevelGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SpiralBevelGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4914.SpiralBevelGearCompoundModalAnalysis))

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2061.SpiralBevelGearSet') -> 'Iterable[_4916.SpiralBevelGearSetCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SpiralBevelGearSetCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4916.SpiralBevelGearSetCompoundModalAnalysis))

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2062.StraightBevelDiffGear') -> 'Iterable[_4920.StraightBevelDiffGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.StraightBevelDiffGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4920.StraightBevelDiffGearCompoundModalAnalysis))

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2063.StraightBevelDiffGearSet') -> 'Iterable[_4922.StraightBevelDiffGearSetCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.StraightBevelDiffGearSetCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4922.StraightBevelDiffGearSetCompoundModalAnalysis))

    def results_for_straight_bevel_gear(self, design_entity: '_2064.StraightBevelGear') -> 'Iterable[_4923.StraightBevelGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.StraightBevelGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4923.StraightBevelGearCompoundModalAnalysis))

    def results_for_straight_bevel_gear_set(self, design_entity: '_2065.StraightBevelGearSet') -> 'Iterable[_4925.StraightBevelGearSetCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.StraightBevelGearSetCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4925.StraightBevelGearSetCompoundModalAnalysis))

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2066.StraightBevelPlanetGear') -> 'Iterable[_4926.StraightBevelPlanetGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.StraightBevelPlanetGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4926.StraightBevelPlanetGearCompoundModalAnalysis))

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2067.StraightBevelSunGear') -> 'Iterable[_4927.StraightBevelSunGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.StraightBevelSunGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4927.StraightBevelSunGearCompoundModalAnalysis))

    def results_for_worm_gear(self, design_entity: '_2068.WormGear') -> 'Iterable[_4938.WormGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.WormGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4938.WormGearCompoundModalAnalysis))

    def results_for_worm_gear_set(self, design_entity: '_2069.WormGearSet') -> 'Iterable[_4940.WormGearSetCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.WormGearSetCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4940.WormGearSetCompoundModalAnalysis))

    def results_for_zerol_bevel_gear(self, design_entity: '_2070.ZerolBevelGear') -> 'Iterable[_4941.ZerolBevelGearCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ZerolBevelGearCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4941.ZerolBevelGearCompoundModalAnalysis))

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2071.ZerolBevelGearSet') -> 'Iterable[_4943.ZerolBevelGearSetCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ZerolBevelGearSetCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4943.ZerolBevelGearSetCompoundModalAnalysis))

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2100.PartToPartShearCoupling') -> 'Iterable[_4897.PartToPartShearCouplingCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PartToPartShearCouplingCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4897.PartToPartShearCouplingCompoundModalAnalysis))

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2101.PartToPartShearCouplingHalf') -> 'Iterable[_4899.PartToPartShearCouplingHalfCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PartToPartShearCouplingHalfCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4899.PartToPartShearCouplingHalfCompoundModalAnalysis))

    def results_for_belt_drive(self, design_entity: '_2089.BeltDrive') -> 'Iterable[_4831.BeltDriveCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BeltDriveCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4831.BeltDriveCompoundModalAnalysis))

    def results_for_clutch(self, design_entity: '_2091.Clutch') -> 'Iterable[_4842.ClutchCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ClutchCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4842.ClutchCompoundModalAnalysis))

    def results_for_clutch_half(self, design_entity: '_2092.ClutchHalf') -> 'Iterable[_4844.ClutchHalfCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ClutchHalfCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4844.ClutchHalfCompoundModalAnalysis))

    def results_for_concept_coupling(self, design_entity: '_2094.ConceptCoupling') -> 'Iterable[_4847.ConceptCouplingCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConceptCouplingCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4847.ConceptCouplingCompoundModalAnalysis))

    def results_for_concept_coupling_half(self, design_entity: '_2095.ConceptCouplingHalf') -> 'Iterable[_4849.ConceptCouplingHalfCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConceptCouplingHalfCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4849.ConceptCouplingHalfCompoundModalAnalysis))

    def results_for_coupling(self, design_entity: '_2096.Coupling') -> 'Iterable[_4858.CouplingCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CouplingCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4858.CouplingCompoundModalAnalysis))

    def results_for_coupling_half(self, design_entity: '_2097.CouplingHalf') -> 'Iterable[_4860.CouplingHalfCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CouplingHalfCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4860.CouplingHalfCompoundModalAnalysis))

    def results_for_cvt(self, design_entity: '_2098.CVT') -> 'Iterable[_4862.CVTCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CVTCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4862.CVTCompoundModalAnalysis))

    def results_for_cvt_pulley(self, design_entity: '_2099.CVTPulley') -> 'Iterable[_4863.CVTPulleyCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CVTPulleyCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4863.CVTPulleyCompoundModalAnalysis))

    def results_for_pulley(self, design_entity: '_2102.Pulley') -> 'Iterable[_4905.PulleyCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PulleyCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4905.PulleyCompoundModalAnalysis))

    def results_for_shaft_hub_connection(self, design_entity: '_2110.ShaftHubConnection') -> 'Iterable[_4911.ShaftHubConnectionCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ShaftHubConnectionCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4911.ShaftHubConnectionCompoundModalAnalysis))

    def results_for_rolling_ring(self, design_entity: '_2108.RollingRing') -> 'Iterable[_4907.RollingRingCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.RollingRingCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4907.RollingRingCompoundModalAnalysis))

    def results_for_rolling_ring_assembly(self, design_entity: '_2109.RollingRingAssembly') -> 'Iterable[_4906.RollingRingAssemblyCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.RollingRingAssemblyCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4906.RollingRingAssemblyCompoundModalAnalysis))

    def results_for_spring_damper(self, design_entity: '_2111.SpringDamper') -> 'Iterable[_4917.SpringDamperCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SpringDamperCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4917.SpringDamperCompoundModalAnalysis))

    def results_for_spring_damper_half(self, design_entity: '_2112.SpringDamperHalf') -> 'Iterable[_4919.SpringDamperHalfCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SpringDamperHalfCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4919.SpringDamperHalfCompoundModalAnalysis))

    def results_for_synchroniser(self, design_entity: '_2113.Synchroniser') -> 'Iterable[_4928.SynchroniserCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SynchroniserCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4928.SynchroniserCompoundModalAnalysis))

    def results_for_synchroniser_half(self, design_entity: '_2115.SynchroniserHalf') -> 'Iterable[_4929.SynchroniserHalfCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SynchroniserHalfCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4929.SynchroniserHalfCompoundModalAnalysis))

    def results_for_synchroniser_part(self, design_entity: '_2116.SynchroniserPart') -> 'Iterable[_4930.SynchroniserPartCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SynchroniserPartCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4930.SynchroniserPartCompoundModalAnalysis))

    def results_for_synchroniser_sleeve(self, design_entity: '_2117.SynchroniserSleeve') -> 'Iterable[_4931.SynchroniserSleeveCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SynchroniserSleeveCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4931.SynchroniserSleeveCompoundModalAnalysis))

    def results_for_torque_converter(self, design_entity: '_2118.TorqueConverter') -> 'Iterable[_4932.TorqueConverterCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.TorqueConverterCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4932.TorqueConverterCompoundModalAnalysis))

    def results_for_torque_converter_pump(self, design_entity: '_2119.TorqueConverterPump') -> 'Iterable[_4934.TorqueConverterPumpCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.TorqueConverterPumpCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4934.TorqueConverterPumpCompoundModalAnalysis))

    def results_for_torque_converter_turbine(self, design_entity: '_2121.TorqueConverterTurbine') -> 'Iterable[_4935.TorqueConverterTurbineCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.TorqueConverterTurbineCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4935.TorqueConverterTurbineCompoundModalAnalysis))

    def results_for_cvt_belt_connection(self, design_entity: '_1816.CVTBeltConnection') -> 'Iterable[_4861.CVTBeltConnectionCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CVTBeltConnectionCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4861.CVTBeltConnectionCompoundModalAnalysis))

    def results_for_belt_connection(self, design_entity: '_1811.BeltConnection') -> 'Iterable[_4830.BeltConnectionCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BeltConnectionCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4830.BeltConnectionCompoundModalAnalysis))

    def results_for_coaxial_connection(self, design_entity: '_1812.CoaxialConnection') -> 'Iterable[_4845.CoaxialConnectionCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CoaxialConnectionCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4845.CoaxialConnectionCompoundModalAnalysis))

    def results_for_connection(self, design_entity: '_1815.Connection') -> 'Iterable[_4856.ConnectionCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConnectionCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4856.ConnectionCompoundModalAnalysis))

    def results_for_inter_mountable_component_connection(self, design_entity: '_1824.InterMountableComponentConnection') -> 'Iterable[_4882.InterMountableComponentConnectionCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.InterMountableComponentConnectionCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4882.InterMountableComponentConnectionCompoundModalAnalysis))

    def results_for_planetary_connection(self, design_entity: '_1827.PlanetaryConnection') -> 'Iterable[_4900.PlanetaryConnectionCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PlanetaryConnectionCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4900.PlanetaryConnectionCompoundModalAnalysis))

    def results_for_rolling_ring_connection(self, design_entity: '_1831.RollingRingConnection') -> 'Iterable[_4908.RollingRingConnectionCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.RollingRingConnectionCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4908.RollingRingConnectionCompoundModalAnalysis))

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1835.ShaftToMountableComponentConnection') -> 'Iterable[_4912.ShaftToMountableComponentConnectionCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ShaftToMountableComponentConnectionCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4912.ShaftToMountableComponentConnectionCompoundModalAnalysis))

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1841.BevelDifferentialGearMesh') -> 'Iterable[_4833.BevelDifferentialGearMeshCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BevelDifferentialGearMeshCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4833.BevelDifferentialGearMeshCompoundModalAnalysis))

    def results_for_concept_gear_mesh(self, design_entity: '_1845.ConceptGearMesh') -> 'Iterable[_4851.ConceptGearMeshCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConceptGearMeshCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4851.ConceptGearMeshCompoundModalAnalysis))

    def results_for_face_gear_mesh(self, design_entity: '_1851.FaceGearMesh') -> 'Iterable[_4871.FaceGearMeshCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.FaceGearMeshCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4871.FaceGearMeshCompoundModalAnalysis))

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1865.StraightBevelDiffGearMesh') -> 'Iterable[_4921.StraightBevelDiffGearMeshCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.StraightBevelDiffGearMeshCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4921.StraightBevelDiffGearMeshCompoundModalAnalysis))

    def results_for_bevel_gear_mesh(self, design_entity: '_1843.BevelGearMesh') -> 'Iterable[_4838.BevelGearMeshCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.BevelGearMeshCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4838.BevelGearMeshCompoundModalAnalysis))

    def results_for_conical_gear_mesh(self, design_entity: '_1847.ConicalGearMesh') -> 'Iterable[_4854.ConicalGearMeshCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConicalGearMeshCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4854.ConicalGearMeshCompoundModalAnalysis))

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1839.AGMAGleasonConicalGearMesh') -> 'Iterable[_4826.AGMAGleasonConicalGearMeshCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.AGMAGleasonConicalGearMeshCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4826.AGMAGleasonConicalGearMeshCompoundModalAnalysis))

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1849.CylindricalGearMesh') -> 'Iterable[_4865.CylindricalGearMeshCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CylindricalGearMeshCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4865.CylindricalGearMeshCompoundModalAnalysis))

    def results_for_hypoid_gear_mesh(self, design_entity: '_1855.HypoidGearMesh') -> 'Iterable[_4879.HypoidGearMeshCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.HypoidGearMeshCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4879.HypoidGearMeshCompoundModalAnalysis))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1858.KlingelnbergCycloPalloidConicalGearMesh') -> 'Iterable[_4884.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4884.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1859.KlingelnbergCycloPalloidHypoidGearMesh') -> 'Iterable[_4887.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4887.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1860.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> 'Iterable[_4890.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4890.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis))

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1863.SpiralBevelGearMesh') -> 'Iterable[_4915.SpiralBevelGearMeshCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SpiralBevelGearMeshCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4915.SpiralBevelGearMeshCompoundModalAnalysis))

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1867.StraightBevelGearMesh') -> 'Iterable[_4924.StraightBevelGearMeshCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.StraightBevelGearMeshCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4924.StraightBevelGearMeshCompoundModalAnalysis))

    def results_for_worm_gear_mesh(self, design_entity: '_1869.WormGearMesh') -> 'Iterable[_4939.WormGearMeshCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.WormGearMeshCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4939.WormGearMeshCompoundModalAnalysis))

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1871.ZerolBevelGearMesh') -> 'Iterable[_4942.ZerolBevelGearMeshCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ZerolBevelGearMeshCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4942.ZerolBevelGearMeshCompoundModalAnalysis))

    def results_for_gear_mesh(self, design_entity: '_1853.GearMesh') -> 'Iterable[_4875.GearMeshCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.GearMeshCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4875.GearMeshCompoundModalAnalysis))

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_1879.PartToPartShearCouplingConnection') -> 'Iterable[_4898.PartToPartShearCouplingConnectionCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.PartToPartShearCouplingConnectionCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4898.PartToPartShearCouplingConnectionCompoundModalAnalysis))

    def results_for_clutch_connection(self, design_entity: '_1873.ClutchConnection') -> 'Iterable[_4843.ClutchConnectionCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ClutchConnectionCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4843.ClutchConnectionCompoundModalAnalysis))

    def results_for_concept_coupling_connection(self, design_entity: '_1875.ConceptCouplingConnection') -> 'Iterable[_4848.ConceptCouplingConnectionCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.ConceptCouplingConnectionCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4848.ConceptCouplingConnectionCompoundModalAnalysis))

    def results_for_coupling_connection(self, design_entity: '_1877.CouplingConnection') -> 'Iterable[_4859.CouplingConnectionCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.CouplingConnectionCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4859.CouplingConnectionCompoundModalAnalysis))

    def results_for_spring_damper_connection(self, design_entity: '_1881.SpringDamperConnection') -> 'Iterable[_4918.SpringDamperConnectionCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.SpringDamperConnectionCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4918.SpringDamperConnectionCompoundModalAnalysis))

    def results_for_torque_converter_connection(self, design_entity: '_1883.TorqueConverterConnection') -> 'Iterable[_4933.TorqueConverterConnectionCompoundModalAnalysis]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.modal_analyses.compound.TorqueConverterConnectionCompoundModalAnalysis]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_4933.TorqueConverterConnectionCompoundModalAnalysis))
