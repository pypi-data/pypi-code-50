'''_3227.py

ConnectionPowerFlow
'''


from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import (
    _1815, _1811, _1812, _1816,
    _1824, _1827, _1831, _1835
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.connections_and_sockets.gears import (
    _1839, _1841, _1843, _1845,
    _1847, _1849, _1851, _1853,
    _1855, _1858, _1859, _1860,
    _1863, _1865, _1867, _1869,
    _1871
)
from mastapy.system_model.connections_and_sockets.couplings import (
    _1873, _1875, _1877, _1879,
    _1881, _1883
)
from mastapy.system_model.analyses_and_results.power_flows import _3276
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2220, _2187, _2192, _2194,
    _2199, _2204, _2207, _2210,
    _2213, _2217, _2222, _2225,
    _2228, _2229, _2230, _2241,
    _2245, _2249, _2253, _2254,
    _2257, _2260, _2271, _2274,
    _2280, _2287, _2289, _2292,
    _2295, _2298, _2310, _2318,
    _2321
)
from mastapy.system_model.analyses_and_results.analysis_cases import _6465
from mastapy._internal.python_net import python_net_import

_CONNECTION_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'ConnectionPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionPowerFlow',)


class ConnectionPowerFlow(_6465.ConnectionStaticLoadAnalysisCase):
    '''ConnectionPowerFlow

    This is a mastapy class.
    '''

    TYPE = _CONNECTION_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConnectionPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def is_loaded(self) -> 'bool':
        '''bool: 'IsLoaded' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.IsLoaded

    @property
    def component_design(self) -> '_1815.Connection':
        '''Connection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1815.Connection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_belt_connection(self) -> '_1811.BeltConnection':
        '''BeltConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1811.BeltConnection.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BeltConnection. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1811.BeltConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_coaxial_connection(self) -> '_1812.CoaxialConnection':
        '''CoaxialConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1812.CoaxialConnection.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CoaxialConnection. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1812.CoaxialConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_cvt_belt_connection(self) -> '_1816.CVTBeltConnection':
        '''CVTBeltConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1816.CVTBeltConnection.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CVTBeltConnection. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1816.CVTBeltConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_inter_mountable_component_connection(self) -> '_1824.InterMountableComponentConnection':
        '''InterMountableComponentConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1824.InterMountableComponentConnection.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to InterMountableComponentConnection. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1824.InterMountableComponentConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_planetary_connection(self) -> '_1827.PlanetaryConnection':
        '''PlanetaryConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1827.PlanetaryConnection.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PlanetaryConnection. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1827.PlanetaryConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_rolling_ring_connection(self) -> '_1831.RollingRingConnection':
        '''RollingRingConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1831.RollingRingConnection.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to RollingRingConnection. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1831.RollingRingConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_shaft_to_mountable_component_connection(self) -> '_1835.ShaftToMountableComponentConnection':
        '''ShaftToMountableComponentConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1835.ShaftToMountableComponentConnection.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ShaftToMountableComponentConnection. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1835.ShaftToMountableComponentConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_agma_gleason_conical_gear_mesh(self) -> '_1839.AGMAGleasonConicalGearMesh':
        '''AGMAGleasonConicalGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1839.AGMAGleasonConicalGearMesh.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to AGMAGleasonConicalGearMesh. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1839.AGMAGleasonConicalGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_bevel_differential_gear_mesh(self) -> '_1841.BevelDifferentialGearMesh':
        '''BevelDifferentialGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1841.BevelDifferentialGearMesh.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialGearMesh. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1841.BevelDifferentialGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_bevel_gear_mesh(self) -> '_1843.BevelGearMesh':
        '''BevelGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1843.BevelGearMesh.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelGearMesh. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1843.BevelGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_concept_gear_mesh(self) -> '_1845.ConceptGearMesh':
        '''ConceptGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1845.ConceptGearMesh.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptGearMesh. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1845.ConceptGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_conical_gear_mesh(self) -> '_1847.ConicalGearMesh':
        '''ConicalGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1847.ConicalGearMesh.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConicalGearMesh. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1847.ConicalGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_cylindrical_gear_mesh(self) -> '_1849.CylindricalGearMesh':
        '''CylindricalGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1849.CylindricalGearMesh.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGearMesh. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1849.CylindricalGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_face_gear_mesh(self) -> '_1851.FaceGearMesh':
        '''FaceGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1851.FaceGearMesh.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to FaceGearMesh. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1851.FaceGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_gear_mesh(self) -> '_1853.GearMesh':
        '''GearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1853.GearMesh.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to GearMesh. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1853.GearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_hypoid_gear_mesh(self) -> '_1855.HypoidGearMesh':
        '''HypoidGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1855.HypoidGearMesh.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to HypoidGearMesh. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1855.HypoidGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh(self) -> '_1858.KlingelnbergCycloPalloidConicalGearMesh':
        '''KlingelnbergCycloPalloidConicalGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1858.KlingelnbergCycloPalloidConicalGearMesh.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidConicalGearMesh. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1858.KlingelnbergCycloPalloidConicalGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self) -> '_1859.KlingelnbergCycloPalloidHypoidGearMesh':
        '''KlingelnbergCycloPalloidHypoidGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1859.KlingelnbergCycloPalloidHypoidGearMesh.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidHypoidGearMesh. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1859.KlingelnbergCycloPalloidHypoidGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self) -> '_1860.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        '''KlingelnbergCycloPalloidSpiralBevelGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1860.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidSpiralBevelGearMesh. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1860.KlingelnbergCycloPalloidSpiralBevelGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_spiral_bevel_gear_mesh(self) -> '_1863.SpiralBevelGearMesh':
        '''SpiralBevelGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1863.SpiralBevelGearMesh.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpiralBevelGearMesh. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1863.SpiralBevelGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_straight_bevel_diff_gear_mesh(self) -> '_1865.StraightBevelDiffGearMesh':
        '''StraightBevelDiffGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1865.StraightBevelDiffGearMesh.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelDiffGearMesh. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1865.StraightBevelDiffGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_straight_bevel_gear_mesh(self) -> '_1867.StraightBevelGearMesh':
        '''StraightBevelGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1867.StraightBevelGearMesh.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelGearMesh. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1867.StraightBevelGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_worm_gear_mesh(self) -> '_1869.WormGearMesh':
        '''WormGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1869.WormGearMesh.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to WormGearMesh. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1869.WormGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_zerol_bevel_gear_mesh(self) -> '_1871.ZerolBevelGearMesh':
        '''ZerolBevelGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1871.ZerolBevelGearMesh.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ZerolBevelGearMesh. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1871.ZerolBevelGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_clutch_connection(self) -> '_1873.ClutchConnection':
        '''ClutchConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1873.ClutchConnection.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ClutchConnection. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1873.ClutchConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_concept_coupling_connection(self) -> '_1875.ConceptCouplingConnection':
        '''ConceptCouplingConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1875.ConceptCouplingConnection.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptCouplingConnection. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1875.ConceptCouplingConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_coupling_connection(self) -> '_1877.CouplingConnection':
        '''CouplingConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1877.CouplingConnection.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CouplingConnection. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1877.CouplingConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_part_to_part_shear_coupling_connection(self) -> '_1879.PartToPartShearCouplingConnection':
        '''PartToPartShearCouplingConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1879.PartToPartShearCouplingConnection.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PartToPartShearCouplingConnection. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1879.PartToPartShearCouplingConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_spring_damper_connection(self) -> '_1881.SpringDamperConnection':
        '''SpringDamperConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1881.SpringDamperConnection.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpringDamperConnection. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1881.SpringDamperConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_design_of_type_torque_converter_connection(self) -> '_1883.TorqueConverterConnection':
        '''TorqueConverterConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1883.TorqueConverterConnection.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to TorqueConverterConnection. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new(_1883.TorqueConverterConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def connection_design(self) -> '_1815.Connection':
        '''Connection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1815.Connection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_belt_connection(self) -> '_1811.BeltConnection':
        '''BeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1811.BeltConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to BeltConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1811.BeltConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_coaxial_connection(self) -> '_1812.CoaxialConnection':
        '''CoaxialConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1812.CoaxialConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to CoaxialConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1812.CoaxialConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_cvt_belt_connection(self) -> '_1816.CVTBeltConnection':
        '''CVTBeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1816.CVTBeltConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to CVTBeltConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1816.CVTBeltConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_inter_mountable_component_connection(self) -> '_1824.InterMountableComponentConnection':
        '''InterMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1824.InterMountableComponentConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to InterMountableComponentConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1824.InterMountableComponentConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_planetary_connection(self) -> '_1827.PlanetaryConnection':
        '''PlanetaryConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1827.PlanetaryConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to PlanetaryConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1827.PlanetaryConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_rolling_ring_connection(self) -> '_1831.RollingRingConnection':
        '''RollingRingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1831.RollingRingConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to RollingRingConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1831.RollingRingConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_shaft_to_mountable_component_connection(self) -> '_1835.ShaftToMountableComponentConnection':
        '''ShaftToMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1835.ShaftToMountableComponentConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ShaftToMountableComponentConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1835.ShaftToMountableComponentConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_agma_gleason_conical_gear_mesh(self) -> '_1839.AGMAGleasonConicalGearMesh':
        '''AGMAGleasonConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1839.AGMAGleasonConicalGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to AGMAGleasonConicalGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1839.AGMAGleasonConicalGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_bevel_differential_gear_mesh(self) -> '_1841.BevelDifferentialGearMesh':
        '''BevelDifferentialGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1841.BevelDifferentialGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to BevelDifferentialGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1841.BevelDifferentialGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_bevel_gear_mesh(self) -> '_1843.BevelGearMesh':
        '''BevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1843.BevelGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to BevelGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1843.BevelGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_concept_gear_mesh(self) -> '_1845.ConceptGearMesh':
        '''ConceptGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1845.ConceptGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ConceptGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1845.ConceptGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_conical_gear_mesh(self) -> '_1847.ConicalGearMesh':
        '''ConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1847.ConicalGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ConicalGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1847.ConicalGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_cylindrical_gear_mesh(self) -> '_1849.CylindricalGearMesh':
        '''CylindricalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1849.CylindricalGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to CylindricalGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1849.CylindricalGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_face_gear_mesh(self) -> '_1851.FaceGearMesh':
        '''FaceGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1851.FaceGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to FaceGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1851.FaceGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_gear_mesh(self) -> '_1853.GearMesh':
        '''GearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1853.GearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to GearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1853.GearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_hypoid_gear_mesh(self) -> '_1855.HypoidGearMesh':
        '''HypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1855.HypoidGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to HypoidGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1855.HypoidGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh(self) -> '_1858.KlingelnbergCycloPalloidConicalGearMesh':
        '''KlingelnbergCycloPalloidConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1858.KlingelnbergCycloPalloidConicalGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to KlingelnbergCycloPalloidConicalGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1858.KlingelnbergCycloPalloidConicalGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self) -> '_1859.KlingelnbergCycloPalloidHypoidGearMesh':
        '''KlingelnbergCycloPalloidHypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1859.KlingelnbergCycloPalloidHypoidGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to KlingelnbergCycloPalloidHypoidGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1859.KlingelnbergCycloPalloidHypoidGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self) -> '_1860.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        '''KlingelnbergCycloPalloidSpiralBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1860.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to KlingelnbergCycloPalloidSpiralBevelGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1860.KlingelnbergCycloPalloidSpiralBevelGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_spiral_bevel_gear_mesh(self) -> '_1863.SpiralBevelGearMesh':
        '''SpiralBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1863.SpiralBevelGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to SpiralBevelGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1863.SpiralBevelGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_straight_bevel_diff_gear_mesh(self) -> '_1865.StraightBevelDiffGearMesh':
        '''StraightBevelDiffGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1865.StraightBevelDiffGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to StraightBevelDiffGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1865.StraightBevelDiffGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_straight_bevel_gear_mesh(self) -> '_1867.StraightBevelGearMesh':
        '''StraightBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1867.StraightBevelGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to StraightBevelGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1867.StraightBevelGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_worm_gear_mesh(self) -> '_1869.WormGearMesh':
        '''WormGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1869.WormGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to WormGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1869.WormGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_zerol_bevel_gear_mesh(self) -> '_1871.ZerolBevelGearMesh':
        '''ZerolBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1871.ZerolBevelGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ZerolBevelGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1871.ZerolBevelGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_clutch_connection(self) -> '_1873.ClutchConnection':
        '''ClutchConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1873.ClutchConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ClutchConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1873.ClutchConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_concept_coupling_connection(self) -> '_1875.ConceptCouplingConnection':
        '''ConceptCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1875.ConceptCouplingConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ConceptCouplingConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1875.ConceptCouplingConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_coupling_connection(self) -> '_1877.CouplingConnection':
        '''CouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1877.CouplingConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to CouplingConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1877.CouplingConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_part_to_part_shear_coupling_connection(self) -> '_1879.PartToPartShearCouplingConnection':
        '''PartToPartShearCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1879.PartToPartShearCouplingConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to PartToPartShearCouplingConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1879.PartToPartShearCouplingConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_spring_damper_connection(self) -> '_1881.SpringDamperConnection':
        '''SpringDamperConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1881.SpringDamperConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to SpringDamperConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1881.SpringDamperConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_torque_converter_connection(self) -> '_1883.TorqueConverterConnection':
        '''TorqueConverterConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1883.TorqueConverterConnection.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to TorqueConverterConnection. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1883.TorqueConverterConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def power_flow(self) -> '_3276.PowerFlow':
        '''PowerFlow: 'PowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3276.PowerFlow)(self.wrapped.PowerFlow) if self.wrapped.PowerFlow else None

    @property
    def torsional_system_deflection_analysis(self) -> '_2220.ConnectionSystemDeflection':
        '''ConnectionSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2220.ConnectionSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_agma_gleason_conical_gear_mesh_system_deflection(self) -> '_2187.AGMAGleasonConicalGearMeshSystemDeflection':
        '''AGMAGleasonConicalGearMeshSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2187.AGMAGleasonConicalGearMeshSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to AGMAGleasonConicalGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2187.AGMAGleasonConicalGearMeshSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_belt_connection_system_deflection(self) -> '_2192.BeltConnectionSystemDeflection':
        '''BeltConnectionSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2192.BeltConnectionSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to BeltConnectionSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2192.BeltConnectionSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_bevel_differential_gear_mesh_system_deflection(self) -> '_2194.BevelDifferentialGearMeshSystemDeflection':
        '''BevelDifferentialGearMeshSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2194.BevelDifferentialGearMeshSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to BevelDifferentialGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2194.BevelDifferentialGearMeshSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_bevel_gear_mesh_system_deflection(self) -> '_2199.BevelGearMeshSystemDeflection':
        '''BevelGearMeshSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2199.BevelGearMeshSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to BevelGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2199.BevelGearMeshSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_clutch_connection_system_deflection(self) -> '_2204.ClutchConnectionSystemDeflection':
        '''ClutchConnectionSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2204.ClutchConnectionSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to ClutchConnectionSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2204.ClutchConnectionSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_coaxial_connection_system_deflection(self) -> '_2207.CoaxialConnectionSystemDeflection':
        '''CoaxialConnectionSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2207.CoaxialConnectionSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to CoaxialConnectionSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2207.CoaxialConnectionSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_concept_coupling_connection_system_deflection(self) -> '_2210.ConceptCouplingConnectionSystemDeflection':
        '''ConceptCouplingConnectionSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2210.ConceptCouplingConnectionSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to ConceptCouplingConnectionSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2210.ConceptCouplingConnectionSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_concept_gear_mesh_system_deflection(self) -> '_2213.ConceptGearMeshSystemDeflection':
        '''ConceptGearMeshSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2213.ConceptGearMeshSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to ConceptGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2213.ConceptGearMeshSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_conical_gear_mesh_system_deflection(self) -> '_2217.ConicalGearMeshSystemDeflection':
        '''ConicalGearMeshSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2217.ConicalGearMeshSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to ConicalGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2217.ConicalGearMeshSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_coupling_connection_system_deflection(self) -> '_2222.CouplingConnectionSystemDeflection':
        '''CouplingConnectionSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2222.CouplingConnectionSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to CouplingConnectionSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2222.CouplingConnectionSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_cvt_belt_connection_system_deflection(self) -> '_2225.CVTBeltConnectionSystemDeflection':
        '''CVTBeltConnectionSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2225.CVTBeltConnectionSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to CVTBeltConnectionSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2225.CVTBeltConnectionSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_cylindrical_gear_mesh_system_deflection(self) -> '_2228.CylindricalGearMeshSystemDeflection':
        '''CylindricalGearMeshSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2228.CylindricalGearMeshSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to CylindricalGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2228.CylindricalGearMeshSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_cylindrical_gear_mesh_system_deflection_timestep(self) -> '_2229.CylindricalGearMeshSystemDeflectionTimestep':
        '''CylindricalGearMeshSystemDeflectionTimestep: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2229.CylindricalGearMeshSystemDeflectionTimestep.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to CylindricalGearMeshSystemDeflectionTimestep. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2229.CylindricalGearMeshSystemDeflectionTimestep)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_cylindrical_gear_mesh_system_deflection_with_ltca_results(self) -> '_2230.CylindricalGearMeshSystemDeflectionWithLTCAResults':
        '''CylindricalGearMeshSystemDeflectionWithLTCAResults: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2230.CylindricalGearMeshSystemDeflectionWithLTCAResults.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to CylindricalGearMeshSystemDeflectionWithLTCAResults. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2230.CylindricalGearMeshSystemDeflectionWithLTCAResults)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_face_gear_mesh_system_deflection(self) -> '_2241.FaceGearMeshSystemDeflection':
        '''FaceGearMeshSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2241.FaceGearMeshSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to FaceGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2241.FaceGearMeshSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_gear_mesh_system_deflection(self) -> '_2245.GearMeshSystemDeflection':
        '''GearMeshSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2245.GearMeshSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to GearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2245.GearMeshSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_hypoid_gear_mesh_system_deflection(self) -> '_2249.HypoidGearMeshSystemDeflection':
        '''HypoidGearMeshSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2249.HypoidGearMeshSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to HypoidGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2249.HypoidGearMeshSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_inter_mountable_component_connection_system_deflection(self) -> '_2253.InterMountableComponentConnectionSystemDeflection':
        '''InterMountableComponentConnectionSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2253.InterMountableComponentConnectionSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to InterMountableComponentConnectionSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2253.InterMountableComponentConnectionSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(self) -> '_2254.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection':
        '''KlingelnbergCycloPalloidConicalGearMeshSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2254.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to KlingelnbergCycloPalloidConicalGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2254.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(self) -> '_2257.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection':
        '''KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2257.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2257.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(self) -> '_2260.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection':
        '''KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2260.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2260.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_part_to_part_shear_coupling_connection_system_deflection(self) -> '_2271.PartToPartShearCouplingConnectionSystemDeflection':
        '''PartToPartShearCouplingConnectionSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2271.PartToPartShearCouplingConnectionSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to PartToPartShearCouplingConnectionSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2271.PartToPartShearCouplingConnectionSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_planetary_connection_system_deflection(self) -> '_2274.PlanetaryConnectionSystemDeflection':
        '''PlanetaryConnectionSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2274.PlanetaryConnectionSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to PlanetaryConnectionSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2274.PlanetaryConnectionSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_rolling_ring_connection_system_deflection(self) -> '_2280.RollingRingConnectionSystemDeflection':
        '''RollingRingConnectionSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2280.RollingRingConnectionSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to RollingRingConnectionSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2280.RollingRingConnectionSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_shaft_to_mountable_component_connection_system_deflection(self) -> '_2287.ShaftToMountableComponentConnectionSystemDeflection':
        '''ShaftToMountableComponentConnectionSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2287.ShaftToMountableComponentConnectionSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to ShaftToMountableComponentConnectionSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2287.ShaftToMountableComponentConnectionSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_spiral_bevel_gear_mesh_system_deflection(self) -> '_2289.SpiralBevelGearMeshSystemDeflection':
        '''SpiralBevelGearMeshSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2289.SpiralBevelGearMeshSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to SpiralBevelGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2289.SpiralBevelGearMeshSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_spring_damper_connection_system_deflection(self) -> '_2292.SpringDamperConnectionSystemDeflection':
        '''SpringDamperConnectionSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2292.SpringDamperConnectionSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to SpringDamperConnectionSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2292.SpringDamperConnectionSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_straight_bevel_diff_gear_mesh_system_deflection(self) -> '_2295.StraightBevelDiffGearMeshSystemDeflection':
        '''StraightBevelDiffGearMeshSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2295.StraightBevelDiffGearMeshSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to StraightBevelDiffGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2295.StraightBevelDiffGearMeshSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_straight_bevel_gear_mesh_system_deflection(self) -> '_2298.StraightBevelGearMeshSystemDeflection':
        '''StraightBevelGearMeshSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2298.StraightBevelGearMeshSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to StraightBevelGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2298.StraightBevelGearMeshSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_torque_converter_connection_system_deflection(self) -> '_2310.TorqueConverterConnectionSystemDeflection':
        '''TorqueConverterConnectionSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2310.TorqueConverterConnectionSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to TorqueConverterConnectionSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2310.TorqueConverterConnectionSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_worm_gear_mesh_system_deflection(self) -> '_2318.WormGearMeshSystemDeflection':
        '''WormGearMeshSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2318.WormGearMeshSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to WormGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2318.WormGearMeshSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None

    @property
    def torsional_system_deflection_analysis_of_type_zerol_bevel_gear_mesh_system_deflection(self) -> '_2321.ZerolBevelGearMeshSystemDeflection':
        '''ZerolBevelGearMeshSystemDeflection: 'TorsionalSystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2321.ZerolBevelGearMeshSystemDeflection.TYPE not in self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__mro__:
            raise CastException('Failed to cast torsional_system_deflection_analysis to ZerolBevelGearMeshSystemDeflection. Expected: {}.'.format(self.wrapped.TorsionalSystemDeflectionAnalysis.__class__.__qualname__))

        return constructor.new(_2321.ZerolBevelGearMeshSystemDeflection)(self.wrapped.TorsionalSystemDeflectionAnalysis) if self.wrapped.TorsionalSystemDeflectionAnalysis else None
