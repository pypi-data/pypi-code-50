'''_1969.py

ConnectedSockets
'''


from mastapy.system_model.connections_and_sockets import (
    _1836, _1817, _1819, _1821,
    _1822, _1823, _1825, _1826,
    _1828, _1829, _1832, _1833,
    _1834, _1815, _1811, _1812,
    _1816, _1824, _1827, _1831,
    _1835
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.connections_and_sockets.gears import (
    _1840, _1842, _1844, _1846,
    _1848, _1850, _1852, _1854,
    _1856, _1857, _1861, _1862,
    _1864, _1866, _1868, _1870,
    _1872, _1839, _1841, _1843,
    _1845, _1847, _1849, _1851,
    _1853, _1855, _1858, _1859,
    _1860, _1863, _1865, _1867,
    _1869, _1871
)
from mastapy.system_model.connections_and_sockets.couplings import (
    _1874, _1876, _1878, _1880,
    _1882, _1884, _1885, _1873,
    _1875, _1877, _1879, _1881,
    _1883
)
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_CONNECTED_SOCKETS = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'ConnectedSockets')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectedSockets',)


class ConnectedSockets(_1.APIBase):
    '''ConnectedSockets

    This is a mastapy class.
    '''

    TYPE = _CONNECTED_SOCKETS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConnectedSockets.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def socket_a(self) -> '_1836.Socket':
        '''Socket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1836.Socket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_cvt_pulley_socket(self) -> '_1817.CVTPulleySocket':
        '''CVTPulleySocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1817.CVTPulleySocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CVTPulleySocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1817.CVTPulleySocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_cylindrical_socket(self) -> '_1819.CylindricalSocket':
        '''CylindricalSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1819.CylindricalSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CylindricalSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1819.CylindricalSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_electric_machine_stator_socket(self) -> '_1821.ElectricMachineStatorSocket':
        '''ElectricMachineStatorSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1821.ElectricMachineStatorSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ElectricMachineStatorSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1821.ElectricMachineStatorSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_inner_shaft_connecting_socket(self) -> '_1822.InnerShaftConnectingSocket':
        '''InnerShaftConnectingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1822.InnerShaftConnectingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to InnerShaftConnectingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1822.InnerShaftConnectingSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_inner_shaft_socket(self) -> '_1823.InnerShaftSocket':
        '''InnerShaftSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1823.InnerShaftSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to InnerShaftSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1823.InnerShaftSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_outer_shaft_connecting_socket(self) -> '_1825.OuterShaftConnectingSocket':
        '''OuterShaftConnectingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1825.OuterShaftConnectingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to OuterShaftConnectingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1825.OuterShaftConnectingSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_outer_shaft_socket(self) -> '_1826.OuterShaftSocket':
        '''OuterShaftSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1826.OuterShaftSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to OuterShaftSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1826.OuterShaftSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_planetary_socket(self) -> '_1828.PlanetarySocket':
        '''PlanetarySocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1828.PlanetarySocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to PlanetarySocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1828.PlanetarySocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_pulley_socket(self) -> '_1829.PulleySocket':
        '''PulleySocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1829.PulleySocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to PulleySocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1829.PulleySocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_rolling_ring_socket(self) -> '_1832.RollingRingSocket':
        '''RollingRingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1832.RollingRingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to RollingRingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1832.RollingRingSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_shaft_connecting_socket(self) -> '_1833.ShaftConnectingSocket':
        '''ShaftConnectingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1833.ShaftConnectingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ShaftConnectingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1833.ShaftConnectingSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_shaft_socket(self) -> '_1834.ShaftSocket':
        '''ShaftSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1834.ShaftSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ShaftSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1834.ShaftSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_agma_gleason_conical_gear_teeth_socket(self) -> '_1840.AGMAGleasonConicalGearTeethSocket':
        '''AGMAGleasonConicalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1840.AGMAGleasonConicalGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to AGMAGleasonConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1840.AGMAGleasonConicalGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_bevel_differential_gear_teeth_socket(self) -> '_1842.BevelDifferentialGearTeethSocket':
        '''BevelDifferentialGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1842.BevelDifferentialGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to BevelDifferentialGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1842.BevelDifferentialGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_bevel_gear_teeth_socket(self) -> '_1844.BevelGearTeethSocket':
        '''BevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1844.BevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to BevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1844.BevelGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_concept_gear_teeth_socket(self) -> '_1846.ConceptGearTeethSocket':
        '''ConceptGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1846.ConceptGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ConceptGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1846.ConceptGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_conical_gear_teeth_socket(self) -> '_1848.ConicalGearTeethSocket':
        '''ConicalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1848.ConicalGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1848.ConicalGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_cylindrical_gear_teeth_socket(self) -> '_1850.CylindricalGearTeethSocket':
        '''CylindricalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1850.CylindricalGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CylindricalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1850.CylindricalGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_face_gear_teeth_socket(self) -> '_1852.FaceGearTeethSocket':
        '''FaceGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1852.FaceGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to FaceGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1852.FaceGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_gear_teeth_socket(self) -> '_1854.GearTeethSocket':
        '''GearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1854.GearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to GearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1854.GearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_hypoid_gear_teeth_socket(self) -> '_1856.HypoidGearTeethSocket':
        '''HypoidGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1856.HypoidGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to HypoidGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1856.HypoidGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_klingelnberg_conical_gear_teeth_socket(self) -> '_1857.KlingelnbergConicalGearTeethSocket':
        '''KlingelnbergConicalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1857.KlingelnbergConicalGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to KlingelnbergConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1857.KlingelnbergConicalGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_klingelnberg_hypoid_gear_teeth_socket(self) -> '_1861.KlingelnbergHypoidGearTeethSocket':
        '''KlingelnbergHypoidGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1861.KlingelnbergHypoidGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to KlingelnbergHypoidGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1861.KlingelnbergHypoidGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_klingelnberg_spiral_bevel_gear_teeth_socket(self) -> '_1862.KlingelnbergSpiralBevelGearTeethSocket':
        '''KlingelnbergSpiralBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1862.KlingelnbergSpiralBevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to KlingelnbergSpiralBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1862.KlingelnbergSpiralBevelGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_spiral_bevel_gear_teeth_socket(self) -> '_1864.SpiralBevelGearTeethSocket':
        '''SpiralBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1864.SpiralBevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to SpiralBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1864.SpiralBevelGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_straight_bevel_diff_gear_teeth_socket(self) -> '_1866.StraightBevelDiffGearTeethSocket':
        '''StraightBevelDiffGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1866.StraightBevelDiffGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to StraightBevelDiffGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1866.StraightBevelDiffGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_straight_bevel_gear_teeth_socket(self) -> '_1868.StraightBevelGearTeethSocket':
        '''StraightBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1868.StraightBevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to StraightBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1868.StraightBevelGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_worm_gear_teeth_socket(self) -> '_1870.WormGearTeethSocket':
        '''WormGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1870.WormGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to WormGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1870.WormGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_zerol_bevel_gear_teeth_socket(self) -> '_1872.ZerolBevelGearTeethSocket':
        '''ZerolBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1872.ZerolBevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ZerolBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1872.ZerolBevelGearTeethSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_clutch_socket(self) -> '_1874.ClutchSocket':
        '''ClutchSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1874.ClutchSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ClutchSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1874.ClutchSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_concept_coupling_socket(self) -> '_1876.ConceptCouplingSocket':
        '''ConceptCouplingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1876.ConceptCouplingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ConceptCouplingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1876.ConceptCouplingSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_coupling_socket(self) -> '_1878.CouplingSocket':
        '''CouplingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1878.CouplingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CouplingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1878.CouplingSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_part_to_part_shear_coupling_socket(self) -> '_1880.PartToPartShearCouplingSocket':
        '''PartToPartShearCouplingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1880.PartToPartShearCouplingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to PartToPartShearCouplingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1880.PartToPartShearCouplingSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_spring_damper_socket(self) -> '_1882.SpringDamperSocket':
        '''SpringDamperSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1882.SpringDamperSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to SpringDamperSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1882.SpringDamperSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_torque_converter_pump_socket(self) -> '_1884.TorqueConverterPumpSocket':
        '''TorqueConverterPumpSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1884.TorqueConverterPumpSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to TorqueConverterPumpSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1884.TorqueConverterPumpSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_torque_converter_turbine_socket(self) -> '_1885.TorqueConverterTurbineSocket':
        '''TorqueConverterTurbineSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1885.TorqueConverterTurbineSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to TorqueConverterTurbineSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new(_1885.TorqueConverterTurbineSocket)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_b(self) -> '_1836.Socket':
        '''Socket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1836.Socket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_cvt_pulley_socket(self) -> '_1817.CVTPulleySocket':
        '''CVTPulleySocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1817.CVTPulleySocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CVTPulleySocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1817.CVTPulleySocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_cylindrical_socket(self) -> '_1819.CylindricalSocket':
        '''CylindricalSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1819.CylindricalSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CylindricalSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1819.CylindricalSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_electric_machine_stator_socket(self) -> '_1821.ElectricMachineStatorSocket':
        '''ElectricMachineStatorSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1821.ElectricMachineStatorSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ElectricMachineStatorSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1821.ElectricMachineStatorSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_inner_shaft_connecting_socket(self) -> '_1822.InnerShaftConnectingSocket':
        '''InnerShaftConnectingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1822.InnerShaftConnectingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to InnerShaftConnectingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1822.InnerShaftConnectingSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_inner_shaft_socket(self) -> '_1823.InnerShaftSocket':
        '''InnerShaftSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1823.InnerShaftSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to InnerShaftSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1823.InnerShaftSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_outer_shaft_connecting_socket(self) -> '_1825.OuterShaftConnectingSocket':
        '''OuterShaftConnectingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1825.OuterShaftConnectingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to OuterShaftConnectingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1825.OuterShaftConnectingSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_outer_shaft_socket(self) -> '_1826.OuterShaftSocket':
        '''OuterShaftSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1826.OuterShaftSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to OuterShaftSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1826.OuterShaftSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_planetary_socket(self) -> '_1828.PlanetarySocket':
        '''PlanetarySocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1828.PlanetarySocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to PlanetarySocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1828.PlanetarySocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_pulley_socket(self) -> '_1829.PulleySocket':
        '''PulleySocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1829.PulleySocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to PulleySocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1829.PulleySocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_rolling_ring_socket(self) -> '_1832.RollingRingSocket':
        '''RollingRingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1832.RollingRingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to RollingRingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1832.RollingRingSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_shaft_connecting_socket(self) -> '_1833.ShaftConnectingSocket':
        '''ShaftConnectingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1833.ShaftConnectingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ShaftConnectingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1833.ShaftConnectingSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_shaft_socket(self) -> '_1834.ShaftSocket':
        '''ShaftSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1834.ShaftSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ShaftSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1834.ShaftSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_agma_gleason_conical_gear_teeth_socket(self) -> '_1840.AGMAGleasonConicalGearTeethSocket':
        '''AGMAGleasonConicalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1840.AGMAGleasonConicalGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to AGMAGleasonConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1840.AGMAGleasonConicalGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_bevel_differential_gear_teeth_socket(self) -> '_1842.BevelDifferentialGearTeethSocket':
        '''BevelDifferentialGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1842.BevelDifferentialGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to BevelDifferentialGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1842.BevelDifferentialGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_bevel_gear_teeth_socket(self) -> '_1844.BevelGearTeethSocket':
        '''BevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1844.BevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to BevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1844.BevelGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_concept_gear_teeth_socket(self) -> '_1846.ConceptGearTeethSocket':
        '''ConceptGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1846.ConceptGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ConceptGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1846.ConceptGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_conical_gear_teeth_socket(self) -> '_1848.ConicalGearTeethSocket':
        '''ConicalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1848.ConicalGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1848.ConicalGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_cylindrical_gear_teeth_socket(self) -> '_1850.CylindricalGearTeethSocket':
        '''CylindricalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1850.CylindricalGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CylindricalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1850.CylindricalGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_face_gear_teeth_socket(self) -> '_1852.FaceGearTeethSocket':
        '''FaceGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1852.FaceGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to FaceGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1852.FaceGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_gear_teeth_socket(self) -> '_1854.GearTeethSocket':
        '''GearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1854.GearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to GearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1854.GearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_hypoid_gear_teeth_socket(self) -> '_1856.HypoidGearTeethSocket':
        '''HypoidGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1856.HypoidGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to HypoidGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1856.HypoidGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_klingelnberg_conical_gear_teeth_socket(self) -> '_1857.KlingelnbergConicalGearTeethSocket':
        '''KlingelnbergConicalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1857.KlingelnbergConicalGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to KlingelnbergConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1857.KlingelnbergConicalGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_klingelnberg_hypoid_gear_teeth_socket(self) -> '_1861.KlingelnbergHypoidGearTeethSocket':
        '''KlingelnbergHypoidGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1861.KlingelnbergHypoidGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to KlingelnbergHypoidGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1861.KlingelnbergHypoidGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_klingelnberg_spiral_bevel_gear_teeth_socket(self) -> '_1862.KlingelnbergSpiralBevelGearTeethSocket':
        '''KlingelnbergSpiralBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1862.KlingelnbergSpiralBevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to KlingelnbergSpiralBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1862.KlingelnbergSpiralBevelGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_spiral_bevel_gear_teeth_socket(self) -> '_1864.SpiralBevelGearTeethSocket':
        '''SpiralBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1864.SpiralBevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to SpiralBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1864.SpiralBevelGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_straight_bevel_diff_gear_teeth_socket(self) -> '_1866.StraightBevelDiffGearTeethSocket':
        '''StraightBevelDiffGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1866.StraightBevelDiffGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to StraightBevelDiffGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1866.StraightBevelDiffGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_straight_bevel_gear_teeth_socket(self) -> '_1868.StraightBevelGearTeethSocket':
        '''StraightBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1868.StraightBevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to StraightBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1868.StraightBevelGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_worm_gear_teeth_socket(self) -> '_1870.WormGearTeethSocket':
        '''WormGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1870.WormGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to WormGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1870.WormGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_zerol_bevel_gear_teeth_socket(self) -> '_1872.ZerolBevelGearTeethSocket':
        '''ZerolBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1872.ZerolBevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ZerolBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1872.ZerolBevelGearTeethSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_clutch_socket(self) -> '_1874.ClutchSocket':
        '''ClutchSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1874.ClutchSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ClutchSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1874.ClutchSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_concept_coupling_socket(self) -> '_1876.ConceptCouplingSocket':
        '''ConceptCouplingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1876.ConceptCouplingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ConceptCouplingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1876.ConceptCouplingSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_coupling_socket(self) -> '_1878.CouplingSocket':
        '''CouplingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1878.CouplingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CouplingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1878.CouplingSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_part_to_part_shear_coupling_socket(self) -> '_1880.PartToPartShearCouplingSocket':
        '''PartToPartShearCouplingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1880.PartToPartShearCouplingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to PartToPartShearCouplingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1880.PartToPartShearCouplingSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_spring_damper_socket(self) -> '_1882.SpringDamperSocket':
        '''SpringDamperSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1882.SpringDamperSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to SpringDamperSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1882.SpringDamperSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_torque_converter_pump_socket(self) -> '_1884.TorqueConverterPumpSocket':
        '''TorqueConverterPumpSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1884.TorqueConverterPumpSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to TorqueConverterPumpSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1884.TorqueConverterPumpSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_torque_converter_turbine_socket(self) -> '_1885.TorqueConverterTurbineSocket':
        '''TorqueConverterTurbineSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1885.TorqueConverterTurbineSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to TorqueConverterTurbineSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new(_1885.TorqueConverterTurbineSocket)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def connection(self) -> '_1815.Connection':
        '''Connection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1815.Connection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_belt_connection(self) -> '_1811.BeltConnection':
        '''BeltConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1811.BeltConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to BeltConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1811.BeltConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_coaxial_connection(self) -> '_1812.CoaxialConnection':
        '''CoaxialConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1812.CoaxialConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CoaxialConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1812.CoaxialConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_cvt_belt_connection(self) -> '_1816.CVTBeltConnection':
        '''CVTBeltConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1816.CVTBeltConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CVTBeltConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1816.CVTBeltConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_inter_mountable_component_connection(self) -> '_1824.InterMountableComponentConnection':
        '''InterMountableComponentConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1824.InterMountableComponentConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to InterMountableComponentConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1824.InterMountableComponentConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_planetary_connection(self) -> '_1827.PlanetaryConnection':
        '''PlanetaryConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1827.PlanetaryConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to PlanetaryConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1827.PlanetaryConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_rolling_ring_connection(self) -> '_1831.RollingRingConnection':
        '''RollingRingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1831.RollingRingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to RollingRingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1831.RollingRingConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_shaft_to_mountable_component_connection(self) -> '_1835.ShaftToMountableComponentConnection':
        '''ShaftToMountableComponentConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1835.ShaftToMountableComponentConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ShaftToMountableComponentConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1835.ShaftToMountableComponentConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_agma_gleason_conical_gear_mesh(self) -> '_1839.AGMAGleasonConicalGearMesh':
        '''AGMAGleasonConicalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1839.AGMAGleasonConicalGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to AGMAGleasonConicalGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1839.AGMAGleasonConicalGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_bevel_differential_gear_mesh(self) -> '_1841.BevelDifferentialGearMesh':
        '''BevelDifferentialGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1841.BevelDifferentialGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to BevelDifferentialGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1841.BevelDifferentialGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_bevel_gear_mesh(self) -> '_1843.BevelGearMesh':
        '''BevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1843.BevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to BevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1843.BevelGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_concept_gear_mesh(self) -> '_1845.ConceptGearMesh':
        '''ConceptGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1845.ConceptGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ConceptGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1845.ConceptGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_conical_gear_mesh(self) -> '_1847.ConicalGearMesh':
        '''ConicalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1847.ConicalGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ConicalGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1847.ConicalGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_cylindrical_gear_mesh(self) -> '_1849.CylindricalGearMesh':
        '''CylindricalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1849.CylindricalGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CylindricalGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1849.CylindricalGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_face_gear_mesh(self) -> '_1851.FaceGearMesh':
        '''FaceGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1851.FaceGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to FaceGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1851.FaceGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_gear_mesh(self) -> '_1853.GearMesh':
        '''GearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1853.GearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to GearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1853.GearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_hypoid_gear_mesh(self) -> '_1855.HypoidGearMesh':
        '''HypoidGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1855.HypoidGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to HypoidGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1855.HypoidGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh(self) -> '_1858.KlingelnbergCycloPalloidConicalGearMesh':
        '''KlingelnbergCycloPalloidConicalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1858.KlingelnbergCycloPalloidConicalGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to KlingelnbergCycloPalloidConicalGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1858.KlingelnbergCycloPalloidConicalGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self) -> '_1859.KlingelnbergCycloPalloidHypoidGearMesh':
        '''KlingelnbergCycloPalloidHypoidGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1859.KlingelnbergCycloPalloidHypoidGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to KlingelnbergCycloPalloidHypoidGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1859.KlingelnbergCycloPalloidHypoidGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self) -> '_1860.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        '''KlingelnbergCycloPalloidSpiralBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1860.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to KlingelnbergCycloPalloidSpiralBevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1860.KlingelnbergCycloPalloidSpiralBevelGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_spiral_bevel_gear_mesh(self) -> '_1863.SpiralBevelGearMesh':
        '''SpiralBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1863.SpiralBevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to SpiralBevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1863.SpiralBevelGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_straight_bevel_diff_gear_mesh(self) -> '_1865.StraightBevelDiffGearMesh':
        '''StraightBevelDiffGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1865.StraightBevelDiffGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to StraightBevelDiffGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1865.StraightBevelDiffGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_straight_bevel_gear_mesh(self) -> '_1867.StraightBevelGearMesh':
        '''StraightBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1867.StraightBevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to StraightBevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1867.StraightBevelGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_worm_gear_mesh(self) -> '_1869.WormGearMesh':
        '''WormGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1869.WormGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to WormGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1869.WormGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_zerol_bevel_gear_mesh(self) -> '_1871.ZerolBevelGearMesh':
        '''ZerolBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1871.ZerolBevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ZerolBevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1871.ZerolBevelGearMesh)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_clutch_connection(self) -> '_1873.ClutchConnection':
        '''ClutchConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1873.ClutchConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ClutchConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1873.ClutchConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_concept_coupling_connection(self) -> '_1875.ConceptCouplingConnection':
        '''ConceptCouplingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1875.ConceptCouplingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ConceptCouplingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1875.ConceptCouplingConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_coupling_connection(self) -> '_1877.CouplingConnection':
        '''CouplingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1877.CouplingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CouplingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1877.CouplingConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_part_to_part_shear_coupling_connection(self) -> '_1879.PartToPartShearCouplingConnection':
        '''PartToPartShearCouplingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1879.PartToPartShearCouplingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to PartToPartShearCouplingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1879.PartToPartShearCouplingConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_spring_damper_connection(self) -> '_1881.SpringDamperConnection':
        '''SpringDamperConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1881.SpringDamperConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to SpringDamperConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1881.SpringDamperConnection)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_torque_converter_connection(self) -> '_1883.TorqueConverterConnection':
        '''TorqueConverterConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1883.TorqueConverterConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to TorqueConverterConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new(_1883.TorqueConverterConnection)(self.wrapped.Connection) if self.wrapped.Connection else None
