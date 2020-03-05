'''_2106.py

CompoundAdvancedSystemDeflectionAnalysis
'''


from typing import Iterable

from mastapy.system_model.part_model import (
    _1907, _1908, _1910, _1912,
    _1913, _1914, _1917, _1918,
    _1921, _1922, _1906, _1923,
    _1926, _1928, _1929, _1930,
    _1931, _1933, _1934, _1936,
    _1937, _1938, _1940, _1941,
    _1942
)
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _6180, _6181, _6186, _6197,
    _6198, _6203, _6214, _6225,
    _6226, _6230, _6185, _6234,
    _6238, _6249, _6250, _6251,
    _6252, _6253, _6256, _6257,
    _6258, _6263, _6267, _6290,
    _6291, _6264, _6207, _6209,
    _6227, _6229, _6182, _6184,
    _6189, _6191, _6192, _6193,
    _6194, _6196, _6210, _6212,
    _6221, _6223, _6224, _6231,
    _6233, _6235, _6237, _6240,
    _6242, _6243, _6245, _6246,
    _6248, _6255, _6268, _6270,
    _6274, _6276, _6277, _6279,
    _6280, _6281, _6292, _6294,
    _6295, _6297, _6188, _6199,
    _6201, _6204, _6206, _6215,
    _6217, _6219, _6220, _6259,
    _6265, _6261, _6260, _6271,
    _6273, _6282, _6283, _6284,
    _6285, _6286, _6288, _6289,
    _6218, _6187, _6202, _6213,
    _6239, _6254, _6262, _6266,
    _6200, _6205, _6216, _6272,
    _6287, _6190, _6208, _6228,
    _6275, _6195, _6211, _6183,
    _6222, _6236, _6241, _6244,
    _6247, _6269, _6278, _6293,
    _6296, _6232
)
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.shaft_model import _1945
from mastapy.system_model.part_model.gears import (
    _1983, _1984, _1990, _1991,
    _1975, _1976, _1977, _1978,
    _1979, _1980, _1981, _1982,
    _1985, _1986, _1987, _1988,
    _1989, _1992, _1994, _1996,
    _1997, _1998, _1999, _2000,
    _2001, _2002, _2003, _2004,
    _2005, _2006, _2007, _2008,
    _2009, _2010, _2011, _2012,
    _2013, _2014, _2015, _2016
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
from mastapy.system_model.analyses_and_results import _2073
from mastapy._internal.python_net import python_net_import

_COMPOUND_ADVANCED_SYSTEM_DEFLECTION_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundAdvancedSystemDeflectionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundAdvancedSystemDeflectionAnalysis',)


class CompoundAdvancedSystemDeflectionAnalysis(_2073.CompoundAnalysis):
    '''CompoundAdvancedSystemDeflectionAnalysis

    This is a mastapy class.
    '''

    TYPE = _COMPOUND_ADVANCED_SYSTEM_DEFLECTION_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CompoundAdvancedSystemDeflectionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    def results_for_abstract_assembly(self, design_entity: '_1907.AbstractAssembly') -> 'Iterable[_6180.AbstractAssemblyCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.AbstractAssemblyCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6180.AbstractAssemblyCompoundAdvancedSystemDeflection))

    def results_for_abstract_shaft_or_housing(self, design_entity: '_1908.AbstractShaftOrHousing') -> 'Iterable[_6181.AbstractShaftOrHousingCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.AbstractShaftOrHousingCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6181.AbstractShaftOrHousingCompoundAdvancedSystemDeflection))

    def results_for_bearing(self, design_entity: '_1910.Bearing') -> 'Iterable[_6186.BearingCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BearingCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6186.BearingCompoundAdvancedSystemDeflection))

    def results_for_bolt(self, design_entity: '_1912.Bolt') -> 'Iterable[_6197.BoltCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BoltCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6197.BoltCompoundAdvancedSystemDeflection))

    def results_for_bolted_joint(self, design_entity: '_1913.BoltedJoint') -> 'Iterable[_6198.BoltedJointCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BoltedJointCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6198.BoltedJointCompoundAdvancedSystemDeflection))

    def results_for_component(self, design_entity: '_1914.Component') -> 'Iterable[_6203.ComponentCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ComponentCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6203.ComponentCompoundAdvancedSystemDeflection))

    def results_for_connector(self, design_entity: '_1917.Connector') -> 'Iterable[_6214.ConnectorCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConnectorCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6214.ConnectorCompoundAdvancedSystemDeflection))

    def results_for_datum(self, design_entity: '_1918.Datum') -> 'Iterable[_6225.DatumCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.DatumCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6225.DatumCompoundAdvancedSystemDeflection))

    def results_for_external_cad_model(self, design_entity: '_1921.ExternalCADModel') -> 'Iterable[_6226.ExternalCADModelCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ExternalCADModelCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6226.ExternalCADModelCompoundAdvancedSystemDeflection))

    def results_for_flexible_pin_assembly(self, design_entity: '_1922.FlexiblePinAssembly') -> 'Iterable[_6230.FlexiblePinAssemblyCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.FlexiblePinAssemblyCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6230.FlexiblePinAssemblyCompoundAdvancedSystemDeflection))

    def results_for_assembly(self, design_entity: '_1906.Assembly') -> 'Iterable[_6185.AssemblyCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.AssemblyCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6185.AssemblyCompoundAdvancedSystemDeflection))

    def results_for_guide_dxf_model(self, design_entity: '_1923.GuideDxfModel') -> 'Iterable[_6234.GuideDxfModelCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.GuideDxfModelCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6234.GuideDxfModelCompoundAdvancedSystemDeflection))

    def results_for_imported_fe_component(self, design_entity: '_1926.ImportedFEComponent') -> 'Iterable[_6238.ImportedFEComponentCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ImportedFEComponentCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6238.ImportedFEComponentCompoundAdvancedSystemDeflection))

    def results_for_mass_disc(self, design_entity: '_1928.MassDisc') -> 'Iterable[_6249.MassDiscCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.MassDiscCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6249.MassDiscCompoundAdvancedSystemDeflection))

    def results_for_measurement_component(self, design_entity: '_1929.MeasurementComponent') -> 'Iterable[_6250.MeasurementComponentCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.MeasurementComponentCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6250.MeasurementComponentCompoundAdvancedSystemDeflection))

    def results_for_mountable_component(self, design_entity: '_1930.MountableComponent') -> 'Iterable[_6251.MountableComponentCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.MountableComponentCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6251.MountableComponentCompoundAdvancedSystemDeflection))

    def results_for_oil_seal(self, design_entity: '_1931.OilSeal') -> 'Iterable[_6252.OilSealCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.OilSealCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6252.OilSealCompoundAdvancedSystemDeflection))

    def results_for_part(self, design_entity: '_1933.Part') -> 'Iterable[_6253.PartCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.PartCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6253.PartCompoundAdvancedSystemDeflection))

    def results_for_planet_carrier(self, design_entity: '_1934.PlanetCarrier') -> 'Iterable[_6256.PlanetCarrierCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.PlanetCarrierCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6256.PlanetCarrierCompoundAdvancedSystemDeflection))

    def results_for_point_load(self, design_entity: '_1936.PointLoad') -> 'Iterable[_6257.PointLoadCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.PointLoadCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6257.PointLoadCompoundAdvancedSystemDeflection))

    def results_for_power_load(self, design_entity: '_1937.PowerLoad') -> 'Iterable[_6258.PowerLoadCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.PowerLoadCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6258.PowerLoadCompoundAdvancedSystemDeflection))

    def results_for_root_assembly(self, design_entity: '_1938.RootAssembly') -> 'Iterable[_6263.RootAssemblyCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.RootAssemblyCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6263.RootAssemblyCompoundAdvancedSystemDeflection))

    def results_for_specialised_assembly(self, design_entity: '_1940.SpecialisedAssembly') -> 'Iterable[_6267.SpecialisedAssemblyCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SpecialisedAssemblyCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6267.SpecialisedAssemblyCompoundAdvancedSystemDeflection))

    def results_for_unbalanced_mass(self, design_entity: '_1941.UnbalancedMass') -> 'Iterable[_6290.UnbalancedMassCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.UnbalancedMassCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6290.UnbalancedMassCompoundAdvancedSystemDeflection))

    def results_for_virtual_component(self, design_entity: '_1942.VirtualComponent') -> 'Iterable[_6291.VirtualComponentCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.VirtualComponentCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6291.VirtualComponentCompoundAdvancedSystemDeflection))

    def results_for_shaft(self, design_entity: '_1945.Shaft') -> 'Iterable[_6264.ShaftCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ShaftCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6264.ShaftCompoundAdvancedSystemDeflection))

    def results_for_concept_gear(self, design_entity: '_1983.ConceptGear') -> 'Iterable[_6207.ConceptGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConceptGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6207.ConceptGearCompoundAdvancedSystemDeflection))

    def results_for_concept_gear_set(self, design_entity: '_1984.ConceptGearSet') -> 'Iterable[_6209.ConceptGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConceptGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6209.ConceptGearSetCompoundAdvancedSystemDeflection))

    def results_for_face_gear(self, design_entity: '_1990.FaceGear') -> 'Iterable[_6227.FaceGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.FaceGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6227.FaceGearCompoundAdvancedSystemDeflection))

    def results_for_face_gear_set(self, design_entity: '_1991.FaceGearSet') -> 'Iterable[_6229.FaceGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.FaceGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6229.FaceGearSetCompoundAdvancedSystemDeflection))

    def results_for_agma_gleason_conical_gear(self, design_entity: '_1975.AGMAGleasonConicalGear') -> 'Iterable[_6182.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6182.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection))

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_1976.AGMAGleasonConicalGearSet') -> 'Iterable[_6184.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6184.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection))

    def results_for_bevel_differential_gear(self, design_entity: '_1977.BevelDifferentialGear') -> 'Iterable[_6189.BevelDifferentialGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BevelDifferentialGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6189.BevelDifferentialGearCompoundAdvancedSystemDeflection))

    def results_for_bevel_differential_gear_set(self, design_entity: '_1978.BevelDifferentialGearSet') -> 'Iterable[_6191.BevelDifferentialGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BevelDifferentialGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6191.BevelDifferentialGearSetCompoundAdvancedSystemDeflection))

    def results_for_bevel_differential_planet_gear(self, design_entity: '_1979.BevelDifferentialPlanetGear') -> 'Iterable[_6192.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6192.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection))

    def results_for_bevel_differential_sun_gear(self, design_entity: '_1980.BevelDifferentialSunGear') -> 'Iterable[_6193.BevelDifferentialSunGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BevelDifferentialSunGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6193.BevelDifferentialSunGearCompoundAdvancedSystemDeflection))

    def results_for_bevel_gear(self, design_entity: '_1981.BevelGear') -> 'Iterable[_6194.BevelGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BevelGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6194.BevelGearCompoundAdvancedSystemDeflection))

    def results_for_bevel_gear_set(self, design_entity: '_1982.BevelGearSet') -> 'Iterable[_6196.BevelGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BevelGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6196.BevelGearSetCompoundAdvancedSystemDeflection))

    def results_for_conical_gear(self, design_entity: '_1985.ConicalGear') -> 'Iterable[_6210.ConicalGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConicalGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6210.ConicalGearCompoundAdvancedSystemDeflection))

    def results_for_conical_gear_set(self, design_entity: '_1986.ConicalGearSet') -> 'Iterable[_6212.ConicalGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConicalGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6212.ConicalGearSetCompoundAdvancedSystemDeflection))

    def results_for_cylindrical_gear(self, design_entity: '_1987.CylindricalGear') -> 'Iterable[_6221.CylindricalGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CylindricalGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6221.CylindricalGearCompoundAdvancedSystemDeflection))

    def results_for_cylindrical_gear_set(self, design_entity: '_1988.CylindricalGearSet') -> 'Iterable[_6223.CylindricalGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CylindricalGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6223.CylindricalGearSetCompoundAdvancedSystemDeflection))

    def results_for_cylindrical_planet_gear(self, design_entity: '_1989.CylindricalPlanetGear') -> 'Iterable[_6224.CylindricalPlanetGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CylindricalPlanetGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6224.CylindricalPlanetGearCompoundAdvancedSystemDeflection))

    def results_for_gear(self, design_entity: '_1992.Gear') -> 'Iterable[_6231.GearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.GearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6231.GearCompoundAdvancedSystemDeflection))

    def results_for_gear_set(self, design_entity: '_1994.GearSet') -> 'Iterable[_6233.GearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.GearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6233.GearSetCompoundAdvancedSystemDeflection))

    def results_for_hypoid_gear(self, design_entity: '_1996.HypoidGear') -> 'Iterable[_6235.HypoidGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.HypoidGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6235.HypoidGearCompoundAdvancedSystemDeflection))

    def results_for_hypoid_gear_set(self, design_entity: '_1997.HypoidGearSet') -> 'Iterable[_6237.HypoidGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.HypoidGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6237.HypoidGearSetCompoundAdvancedSystemDeflection))

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_1998.KlingelnbergCycloPalloidConicalGear') -> 'Iterable[_6240.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6240.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_1999.KlingelnbergCycloPalloidConicalGearSet') -> 'Iterable[_6242.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6242.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2000.KlingelnbergCycloPalloidHypoidGear') -> 'Iterable[_6243.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6243.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2001.KlingelnbergCycloPalloidHypoidGearSet') -> 'Iterable[_6245.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6245.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2002.KlingelnbergCycloPalloidSpiralBevelGear') -> 'Iterable[_6246.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6246.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2003.KlingelnbergCycloPalloidSpiralBevelGearSet') -> 'Iterable[_6248.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6248.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection))

    def results_for_planetary_gear_set(self, design_entity: '_2004.PlanetaryGearSet') -> 'Iterable[_6255.PlanetaryGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.PlanetaryGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6255.PlanetaryGearSetCompoundAdvancedSystemDeflection))

    def results_for_spiral_bevel_gear(self, design_entity: '_2005.SpiralBevelGear') -> 'Iterable[_6268.SpiralBevelGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SpiralBevelGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6268.SpiralBevelGearCompoundAdvancedSystemDeflection))

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2006.SpiralBevelGearSet') -> 'Iterable[_6270.SpiralBevelGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SpiralBevelGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6270.SpiralBevelGearSetCompoundAdvancedSystemDeflection))

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2007.StraightBevelDiffGear') -> 'Iterable[_6274.StraightBevelDiffGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.StraightBevelDiffGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6274.StraightBevelDiffGearCompoundAdvancedSystemDeflection))

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2008.StraightBevelDiffGearSet') -> 'Iterable[_6276.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6276.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection))

    def results_for_straight_bevel_gear(self, design_entity: '_2009.StraightBevelGear') -> 'Iterable[_6277.StraightBevelGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.StraightBevelGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6277.StraightBevelGearCompoundAdvancedSystemDeflection))

    def results_for_straight_bevel_gear_set(self, design_entity: '_2010.StraightBevelGearSet') -> 'Iterable[_6279.StraightBevelGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.StraightBevelGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6279.StraightBevelGearSetCompoundAdvancedSystemDeflection))

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2011.StraightBevelPlanetGear') -> 'Iterable[_6280.StraightBevelPlanetGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.StraightBevelPlanetGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6280.StraightBevelPlanetGearCompoundAdvancedSystemDeflection))

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2012.StraightBevelSunGear') -> 'Iterable[_6281.StraightBevelSunGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.StraightBevelSunGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6281.StraightBevelSunGearCompoundAdvancedSystemDeflection))

    def results_for_worm_gear(self, design_entity: '_2013.WormGear') -> 'Iterable[_6292.WormGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.WormGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6292.WormGearCompoundAdvancedSystemDeflection))

    def results_for_worm_gear_set(self, design_entity: '_2014.WormGearSet') -> 'Iterable[_6294.WormGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.WormGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6294.WormGearSetCompoundAdvancedSystemDeflection))

    def results_for_zerol_bevel_gear(self, design_entity: '_2015.ZerolBevelGear') -> 'Iterable[_6295.ZerolBevelGearCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ZerolBevelGearCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6295.ZerolBevelGearCompoundAdvancedSystemDeflection))

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2016.ZerolBevelGearSet') -> 'Iterable[_6297.ZerolBevelGearSetCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ZerolBevelGearSetCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6297.ZerolBevelGearSetCompoundAdvancedSystemDeflection))

    def results_for_belt_drive(self, design_entity: '_2034.BeltDrive') -> 'Iterable[_6188.BeltDriveCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BeltDriveCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6188.BeltDriveCompoundAdvancedSystemDeflection))

    def results_for_clutch(self, design_entity: '_2036.Clutch') -> 'Iterable[_6199.ClutchCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ClutchCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6199.ClutchCompoundAdvancedSystemDeflection))

    def results_for_clutch_half(self, design_entity: '_2037.ClutchHalf') -> 'Iterable[_6201.ClutchHalfCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ClutchHalfCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6201.ClutchHalfCompoundAdvancedSystemDeflection))

    def results_for_concept_coupling(self, design_entity: '_2039.ConceptCoupling') -> 'Iterable[_6204.ConceptCouplingCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConceptCouplingCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6204.ConceptCouplingCompoundAdvancedSystemDeflection))

    def results_for_concept_coupling_half(self, design_entity: '_2040.ConceptCouplingHalf') -> 'Iterable[_6206.ConceptCouplingHalfCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConceptCouplingHalfCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6206.ConceptCouplingHalfCompoundAdvancedSystemDeflection))

    def results_for_coupling(self, design_entity: '_2041.Coupling') -> 'Iterable[_6215.CouplingCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CouplingCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6215.CouplingCompoundAdvancedSystemDeflection))

    def results_for_coupling_half(self, design_entity: '_2042.CouplingHalf') -> 'Iterable[_6217.CouplingHalfCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CouplingHalfCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6217.CouplingHalfCompoundAdvancedSystemDeflection))

    def results_for_cvt(self, design_entity: '_2043.CVT') -> 'Iterable[_6219.CVTCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CVTCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6219.CVTCompoundAdvancedSystemDeflection))

    def results_for_cvt_pulley(self, design_entity: '_2044.CVTPulley') -> 'Iterable[_6220.CVTPulleyCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CVTPulleyCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6220.CVTPulleyCompoundAdvancedSystemDeflection))

    def results_for_pulley(self, design_entity: '_2045.Pulley') -> 'Iterable[_6259.PulleyCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.PulleyCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6259.PulleyCompoundAdvancedSystemDeflection))

    def results_for_shaft_hub_connection(self, design_entity: '_2053.ShaftHubConnection') -> 'Iterable[_6265.ShaftHubConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ShaftHubConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6265.ShaftHubConnectionCompoundAdvancedSystemDeflection))

    def results_for_rolling_ring(self, design_entity: '_2051.RollingRing') -> 'Iterable[_6261.RollingRingCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.RollingRingCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6261.RollingRingCompoundAdvancedSystemDeflection))

    def results_for_rolling_ring_assembly(self, design_entity: '_2052.RollingRingAssembly') -> 'Iterable[_6260.RollingRingAssemblyCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.RollingRingAssemblyCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6260.RollingRingAssemblyCompoundAdvancedSystemDeflection))

    def results_for_spring_damper(self, design_entity: '_2054.SpringDamper') -> 'Iterable[_6271.SpringDamperCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SpringDamperCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6271.SpringDamperCompoundAdvancedSystemDeflection))

    def results_for_spring_damper_half(self, design_entity: '_2055.SpringDamperHalf') -> 'Iterable[_6273.SpringDamperHalfCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SpringDamperHalfCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6273.SpringDamperHalfCompoundAdvancedSystemDeflection))

    def results_for_synchroniser(self, design_entity: '_2056.Synchroniser') -> 'Iterable[_6282.SynchroniserCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SynchroniserCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6282.SynchroniserCompoundAdvancedSystemDeflection))

    def results_for_synchroniser_half(self, design_entity: '_2058.SynchroniserHalf') -> 'Iterable[_6283.SynchroniserHalfCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SynchroniserHalfCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6283.SynchroniserHalfCompoundAdvancedSystemDeflection))

    def results_for_synchroniser_part(self, design_entity: '_2059.SynchroniserPart') -> 'Iterable[_6284.SynchroniserPartCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SynchroniserPartCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6284.SynchroniserPartCompoundAdvancedSystemDeflection))

    def results_for_synchroniser_sleeve(self, design_entity: '_2060.SynchroniserSleeve') -> 'Iterable[_6285.SynchroniserSleeveCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SynchroniserSleeveCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6285.SynchroniserSleeveCompoundAdvancedSystemDeflection))

    def results_for_torque_converter(self, design_entity: '_2061.TorqueConverter') -> 'Iterable[_6286.TorqueConverterCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.TorqueConverterCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6286.TorqueConverterCompoundAdvancedSystemDeflection))

    def results_for_torque_converter_pump(self, design_entity: '_2062.TorqueConverterPump') -> 'Iterable[_6288.TorqueConverterPumpCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.TorqueConverterPumpCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6288.TorqueConverterPumpCompoundAdvancedSystemDeflection))

    def results_for_torque_converter_turbine(self, design_entity: '_2064.TorqueConverterTurbine') -> 'Iterable[_6289.TorqueConverterTurbineCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.TorqueConverterTurbineCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6289.TorqueConverterTurbineCompoundAdvancedSystemDeflection))

    def results_for_cvt_belt_connection(self, design_entity: '_1766.CVTBeltConnection') -> 'Iterable[_6218.CVTBeltConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CVTBeltConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6218.CVTBeltConnectionCompoundAdvancedSystemDeflection))

    def results_for_belt_connection(self, design_entity: '_1761.BeltConnection') -> 'Iterable[_6187.BeltConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BeltConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6187.BeltConnectionCompoundAdvancedSystemDeflection))

    def results_for_coaxial_connection(self, design_entity: '_1762.CoaxialConnection') -> 'Iterable[_6202.CoaxialConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CoaxialConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6202.CoaxialConnectionCompoundAdvancedSystemDeflection))

    def results_for_connection(self, design_entity: '_1765.Connection') -> 'Iterable[_6213.ConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6213.ConnectionCompoundAdvancedSystemDeflection))

    def results_for_inter_mountable_component_connection(self, design_entity: '_1774.InterMountableComponentConnection') -> 'Iterable[_6239.InterMountableComponentConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.InterMountableComponentConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6239.InterMountableComponentConnectionCompoundAdvancedSystemDeflection))

    def results_for_planetary_connection(self, design_entity: '_1777.PlanetaryConnection') -> 'Iterable[_6254.PlanetaryConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.PlanetaryConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6254.PlanetaryConnectionCompoundAdvancedSystemDeflection))

    def results_for_rolling_ring_connection(self, design_entity: '_1781.RollingRingConnection') -> 'Iterable[_6262.RollingRingConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.RollingRingConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6262.RollingRingConnectionCompoundAdvancedSystemDeflection))

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1785.ShaftToMountableComponentConnection') -> 'Iterable[_6266.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6266.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection))

    def results_for_clutch_connection(self, design_entity: '_1823.ClutchConnection') -> 'Iterable[_6200.ClutchConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ClutchConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6200.ClutchConnectionCompoundAdvancedSystemDeflection))

    def results_for_concept_coupling_connection(self, design_entity: '_1825.ConceptCouplingConnection') -> 'Iterable[_6205.ConceptCouplingConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConceptCouplingConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6205.ConceptCouplingConnectionCompoundAdvancedSystemDeflection))

    def results_for_coupling_connection(self, design_entity: '_1827.CouplingConnection') -> 'Iterable[_6216.CouplingConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CouplingConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6216.CouplingConnectionCompoundAdvancedSystemDeflection))

    def results_for_spring_damper_connection(self, design_entity: '_1829.SpringDamperConnection') -> 'Iterable[_6272.SpringDamperConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SpringDamperConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6272.SpringDamperConnectionCompoundAdvancedSystemDeflection))

    def results_for_torque_converter_connection(self, design_entity: '_1831.TorqueConverterConnection') -> 'Iterable[_6287.TorqueConverterConnectionCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.TorqueConverterConnectionCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6287.TorqueConverterConnectionCompoundAdvancedSystemDeflection))

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1791.BevelDifferentialGearMesh') -> 'Iterable[_6190.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6190.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection))

    def results_for_concept_gear_mesh(self, design_entity: '_1795.ConceptGearMesh') -> 'Iterable[_6208.ConceptGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConceptGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6208.ConceptGearMeshCompoundAdvancedSystemDeflection))

    def results_for_face_gear_mesh(self, design_entity: '_1801.FaceGearMesh') -> 'Iterable[_6228.FaceGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.FaceGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6228.FaceGearMeshCompoundAdvancedSystemDeflection))

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1815.StraightBevelDiffGearMesh') -> 'Iterable[_6275.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6275.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection))

    def results_for_bevel_gear_mesh(self, design_entity: '_1793.BevelGearMesh') -> 'Iterable[_6195.BevelGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BevelGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6195.BevelGearMeshCompoundAdvancedSystemDeflection))

    def results_for_conical_gear_mesh(self, design_entity: '_1797.ConicalGearMesh') -> 'Iterable[_6211.ConicalGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConicalGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6211.ConicalGearMeshCompoundAdvancedSystemDeflection))

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1789.AGMAGleasonConicalGearMesh') -> 'Iterable[_6183.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6183.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection))

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1799.CylindricalGearMesh') -> 'Iterable[_6222.CylindricalGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CylindricalGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6222.CylindricalGearMeshCompoundAdvancedSystemDeflection))

    def results_for_hypoid_gear_mesh(self, design_entity: '_1805.HypoidGearMesh') -> 'Iterable[_6236.HypoidGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.HypoidGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6236.HypoidGearMeshCompoundAdvancedSystemDeflection))

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1808.KlingelnbergCycloPalloidConicalGearMesh') -> 'Iterable[_6241.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6241.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection))

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1809.KlingelnbergCycloPalloidHypoidGearMesh') -> 'Iterable[_6244.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6244.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection))

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1810.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> 'Iterable[_6247.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6247.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection))

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1813.SpiralBevelGearMesh') -> 'Iterable[_6269.SpiralBevelGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.SpiralBevelGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6269.SpiralBevelGearMeshCompoundAdvancedSystemDeflection))

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1817.StraightBevelGearMesh') -> 'Iterable[_6278.StraightBevelGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.StraightBevelGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6278.StraightBevelGearMeshCompoundAdvancedSystemDeflection))

    def results_for_worm_gear_mesh(self, design_entity: '_1819.WormGearMesh') -> 'Iterable[_6293.WormGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.WormGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6293.WormGearMeshCompoundAdvancedSystemDeflection))

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1821.ZerolBevelGearMesh') -> 'Iterable[_6296.ZerolBevelGearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ZerolBevelGearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6296.ZerolBevelGearMeshCompoundAdvancedSystemDeflection))

    def results_for_gear_mesh(self, design_entity: '_1803.GearMesh') -> 'Iterable[_6232.GearMeshCompoundAdvancedSystemDeflection]':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            Iterable[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.GearMeshCompoundAdvancedSystemDeflection]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None), constructor.new(_6232.GearMeshCompoundAdvancedSystemDeflection))
