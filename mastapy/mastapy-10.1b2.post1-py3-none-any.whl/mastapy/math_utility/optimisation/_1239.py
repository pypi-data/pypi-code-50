'''_1239.py

OptimizationVariable
'''


from typing import List

from mastapy.utility.units_and_measurements import _1071
from mastapy._internal import constructor, conversion
from mastapy.utility.units_and_measurements.measurements import (
    _1280, _1281, _1282, _1283,
    _1284, _1285, _1286, _1287,
    _1288, _1289, _1290, _1291,
    _1292, _1293, _1294, _1295,
    _1296, _1297, _1298, _1299,
    _1300, _1301, _1302, _1303,
    _1304, _1305, _1306, _1307,
    _1308, _1309, _1310, _1311,
    _1312, _1313, _1314, _1315,
    _1316, _1317, _1318, _1319,
    _1320, _1321, _1322, _1323,
    _1324, _1325, _1078, _1326,
    _1327, _1328, _1329, _1330,
    _1331, _1332, _1333, _1334,
    _1335, _1336, _1337, _1338,
    _1339, _1340, _1079, _1341,
    _1342, _1343, _1344, _1345,
    _1346, _1347, _1348, _1349,
    _1350, _1351, _1352, _1353,
    _1354, _1355, _1356, _1357,
    _1358, _1359, _1360, _1361,
    _1362, _1363, _1364, _1365,
    _1366, _1367, _1368, _1369,
    _1370, _1371, _1372, _1373,
    _1374, _1375, _1376, _1377,
    _1378, _1379, _1380
)
from mastapy._internal.cast_exception import CastException
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_OPTIMIZATION_VARIABLE = python_net_import('SMT.MastaAPI.MathUtility.Optimisation', 'OptimizationVariable')


__docformat__ = 'restructuredtext en'
__all__ = ('OptimizationVariable',)


class OptimizationVariable(_1.APIBase):
    '''OptimizationVariable

    This is a mastapy class.
    '''

    TYPE = _OPTIMIZATION_VARIABLE
    __hash__ = None

    def __init__(self, instance_to_wrap: 'OptimizationVariable.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def measurement(self) -> '_1071.MeasurementBase':
        '''MeasurementBase: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1071.MeasurementBase)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_acceleration(self) -> '_1280.Acceleration':
        '''Acceleration: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1280.Acceleration.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Acceleration. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1280.Acceleration)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_angle(self) -> '_1281.Angle':
        '''Angle: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1281.Angle.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Angle. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1281.Angle)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_angle_per_unit_temperature(self) -> '_1282.AnglePerUnitTemperature':
        '''AnglePerUnitTemperature: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1282.AnglePerUnitTemperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AnglePerUnitTemperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1282.AnglePerUnitTemperature)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_angle_small(self) -> '_1283.AngleSmall':
        '''AngleSmall: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1283.AngleSmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngleSmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1283.AngleSmall)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_angle_very_small(self) -> '_1284.AngleVerySmall':
        '''AngleVerySmall: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1284.AngleVerySmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngleVerySmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1284.AngleVerySmall)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_angular_acceleration(self) -> '_1285.AngularAcceleration':
        '''AngularAcceleration: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1285.AngularAcceleration.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularAcceleration. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1285.AngularAcceleration)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_angular_compliance(self) -> '_1286.AngularCompliance':
        '''AngularCompliance: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1286.AngularCompliance.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularCompliance. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1286.AngularCompliance)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_angular_jerk(self) -> '_1287.AngularJerk':
        '''AngularJerk: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1287.AngularJerk.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularJerk. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1287.AngularJerk)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_angular_stiffness(self) -> '_1288.AngularStiffness':
        '''AngularStiffness: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1288.AngularStiffness.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularStiffness. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1288.AngularStiffness)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_angular_velocity(self) -> '_1289.AngularVelocity':
        '''AngularVelocity: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1289.AngularVelocity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularVelocity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1289.AngularVelocity)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_area(self) -> '_1290.Area':
        '''Area: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1290.Area.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Area. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1290.Area)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_area_small(self) -> '_1291.AreaSmall':
        '''AreaSmall: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1291.AreaSmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AreaSmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1291.AreaSmall)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_cycles(self) -> '_1292.Cycles':
        '''Cycles: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1292.Cycles.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Cycles. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1292.Cycles)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_damage(self) -> '_1293.Damage':
        '''Damage: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1293.Damage.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Damage. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1293.Damage)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_damage_rate(self) -> '_1294.DamageRate':
        '''DamageRate: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1294.DamageRate.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to DamageRate. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1294.DamageRate)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_decibel(self) -> '_1295.Decibel':
        '''Decibel: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1295.Decibel.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Decibel. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1295.Decibel)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_density(self) -> '_1296.Density':
        '''Density: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1296.Density.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Density. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1296.Density)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_energy(self) -> '_1297.Energy':
        '''Energy: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1297.Energy.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Energy. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1297.Energy)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_energy_per_unit_area(self) -> '_1298.EnergyPerUnitArea':
        '''EnergyPerUnitArea: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1298.EnergyPerUnitArea.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to EnergyPerUnitArea. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1298.EnergyPerUnitArea)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_energy_per_unit_area_small(self) -> '_1299.EnergyPerUnitAreaSmall':
        '''EnergyPerUnitAreaSmall: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1299.EnergyPerUnitAreaSmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to EnergyPerUnitAreaSmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1299.EnergyPerUnitAreaSmall)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_energy_small(self) -> '_1300.EnergySmall':
        '''EnergySmall: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1300.EnergySmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to EnergySmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1300.EnergySmall)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_enum(self) -> '_1301.Enum':
        '''Enum: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1301.Enum.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Enum. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1301.Enum)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_flow_rate(self) -> '_1302.FlowRate':
        '''FlowRate: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1302.FlowRate.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to FlowRate. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1302.FlowRate)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_force(self) -> '_1303.Force':
        '''Force: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1303.Force.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Force. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1303.Force)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_force_per_unit_length(self) -> '_1304.ForcePerUnitLength':
        '''ForcePerUnitLength: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1304.ForcePerUnitLength.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ForcePerUnitLength. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1304.ForcePerUnitLength)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_force_per_unit_pressure(self) -> '_1305.ForcePerUnitPressure':
        '''ForcePerUnitPressure: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1305.ForcePerUnitPressure.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ForcePerUnitPressure. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1305.ForcePerUnitPressure)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_force_per_unit_temperature(self) -> '_1306.ForcePerUnitTemperature':
        '''ForcePerUnitTemperature: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1306.ForcePerUnitTemperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ForcePerUnitTemperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1306.ForcePerUnitTemperature)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_fraction_measurement_base(self) -> '_1307.FractionMeasurementBase':
        '''FractionMeasurementBase: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1307.FractionMeasurementBase.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to FractionMeasurementBase. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1307.FractionMeasurementBase)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_frequency(self) -> '_1308.Frequency':
        '''Frequency: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1308.Frequency.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Frequency. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1308.Frequency)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_fuel_consumption_engine(self) -> '_1309.FuelConsumptionEngine':
        '''FuelConsumptionEngine: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1309.FuelConsumptionEngine.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to FuelConsumptionEngine. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1309.FuelConsumptionEngine)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_fuel_efficiency_vehicle(self) -> '_1310.FuelEfficiencyVehicle':
        '''FuelEfficiencyVehicle: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1310.FuelEfficiencyVehicle.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to FuelEfficiencyVehicle. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1310.FuelEfficiencyVehicle)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_gradient(self) -> '_1311.Gradient':
        '''Gradient: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1311.Gradient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Gradient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1311.Gradient)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_heat_conductivity(self) -> '_1312.HeatConductivity':
        '''HeatConductivity: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1312.HeatConductivity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatConductivity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1312.HeatConductivity)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_heat_transfer(self) -> '_1313.HeatTransfer':
        '''HeatTransfer: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1313.HeatTransfer.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatTransfer. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1313.HeatTransfer)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_heat_transfer_coefficient_for_plastic_gear_tooth(self) -> '_1314.HeatTransferCoefficientForPlasticGearTooth':
        '''HeatTransferCoefficientForPlasticGearTooth: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1314.HeatTransferCoefficientForPlasticGearTooth.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatTransferCoefficientForPlasticGearTooth. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1314.HeatTransferCoefficientForPlasticGearTooth)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_heat_transfer_resistance(self) -> '_1315.HeatTransferResistance':
        '''HeatTransferResistance: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1315.HeatTransferResistance.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatTransferResistance. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1315.HeatTransferResistance)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_impulse(self) -> '_1316.Impulse':
        '''Impulse: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1316.Impulse.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Impulse. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1316.Impulse)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_index(self) -> '_1317.Index':
        '''Index: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1317.Index.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Index. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1317.Index)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_integer(self) -> '_1318.Integer':
        '''Integer: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1318.Integer.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Integer. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1318.Integer)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_inverse_short_length(self) -> '_1319.InverseShortLength':
        '''InverseShortLength: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1319.InverseShortLength.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to InverseShortLength. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1319.InverseShortLength)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_inverse_short_time(self) -> '_1320.InverseShortTime':
        '''InverseShortTime: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1320.InverseShortTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to InverseShortTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1320.InverseShortTime)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_jerk(self) -> '_1321.Jerk':
        '''Jerk: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1321.Jerk.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Jerk. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1321.Jerk)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_kinematic_viscosity(self) -> '_1322.KinematicViscosity':
        '''KinematicViscosity: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1322.KinematicViscosity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to KinematicViscosity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1322.KinematicViscosity)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_length_long(self) -> '_1323.LengthLong':
        '''LengthLong: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1323.LengthLong.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthLong. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1323.LengthLong)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_length_medium(self) -> '_1324.LengthMedium':
        '''LengthMedium: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1324.LengthMedium.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthMedium. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1324.LengthMedium)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_length_per_unit_temperature(self) -> '_1325.LengthPerUnitTemperature':
        '''LengthPerUnitTemperature: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1325.LengthPerUnitTemperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthPerUnitTemperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1325.LengthPerUnitTemperature)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_length_short(self) -> '_1078.LengthShort':
        '''LengthShort: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1078.LengthShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1078.LengthShort)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_length_to_the_fourth(self) -> '_1326.LengthToTheFourth':
        '''LengthToTheFourth: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1326.LengthToTheFourth.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthToTheFourth. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1326.LengthToTheFourth)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_length_very_long(self) -> '_1327.LengthVeryLong':
        '''LengthVeryLong: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1327.LengthVeryLong.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthVeryLong. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1327.LengthVeryLong)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_length_very_short(self) -> '_1328.LengthVeryShort':
        '''LengthVeryShort: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1328.LengthVeryShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthVeryShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1328.LengthVeryShort)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_length_very_short_per_length_short(self) -> '_1329.LengthVeryShortPerLengthShort':
        '''LengthVeryShortPerLengthShort: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1329.LengthVeryShortPerLengthShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthVeryShortPerLengthShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1329.LengthVeryShortPerLengthShort)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_linear_angular_damping(self) -> '_1330.LinearAngularDamping':
        '''LinearAngularDamping: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1330.LinearAngularDamping.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearAngularDamping. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1330.LinearAngularDamping)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_linear_angular_stiffness_cross_term(self) -> '_1331.LinearAngularStiffnessCrossTerm':
        '''LinearAngularStiffnessCrossTerm: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1331.LinearAngularStiffnessCrossTerm.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearAngularStiffnessCrossTerm. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1331.LinearAngularStiffnessCrossTerm)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_linear_damping(self) -> '_1332.LinearDamping':
        '''LinearDamping: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1332.LinearDamping.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearDamping. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1332.LinearDamping)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_linear_flexibility(self) -> '_1333.LinearFlexibility':
        '''LinearFlexibility: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1333.LinearFlexibility.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearFlexibility. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1333.LinearFlexibility)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_linear_stiffness(self) -> '_1334.LinearStiffness':
        '''LinearStiffness: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1334.LinearStiffness.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearStiffness. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1334.LinearStiffness)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_mass(self) -> '_1335.Mass':
        '''Mass: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1335.Mass.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Mass. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1335.Mass)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_mass_per_unit_length(self) -> '_1336.MassPerUnitLength':
        '''MassPerUnitLength: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1336.MassPerUnitLength.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MassPerUnitLength. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1336.MassPerUnitLength)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_mass_per_unit_time(self) -> '_1337.MassPerUnitTime':
        '''MassPerUnitTime: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1337.MassPerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MassPerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1337.MassPerUnitTime)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_moment_of_inertia(self) -> '_1338.MomentOfInertia':
        '''MomentOfInertia: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1338.MomentOfInertia.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MomentOfInertia. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1338.MomentOfInertia)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_moment_of_inertia_per_unit_length(self) -> '_1339.MomentOfInertiaPerUnitLength':
        '''MomentOfInertiaPerUnitLength: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1339.MomentOfInertiaPerUnitLength.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MomentOfInertiaPerUnitLength. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1339.MomentOfInertiaPerUnitLength)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_moment_per_unit_pressure(self) -> '_1340.MomentPerUnitPressure':
        '''MomentPerUnitPressure: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1340.MomentPerUnitPressure.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MomentPerUnitPressure. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1340.MomentPerUnitPressure)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_number(self) -> '_1079.Number':
        '''Number: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1079.Number.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Number. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1079.Number)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_percentage(self) -> '_1341.Percentage':
        '''Percentage: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1341.Percentage.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Percentage. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1341.Percentage)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_power(self) -> '_1342.Power':
        '''Power: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1342.Power.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Power. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1342.Power)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_power_per_small_area(self) -> '_1343.PowerPerSmallArea':
        '''PowerPerSmallArea: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1343.PowerPerSmallArea.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerPerSmallArea. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1343.PowerPerSmallArea)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_power_small(self) -> '_1344.PowerSmall':
        '''PowerSmall: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1344.PowerSmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1344.PowerSmall)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_power_small_per_unit_time(self) -> '_1345.PowerSmallPerUnitTime':
        '''PowerSmallPerUnitTime: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1345.PowerSmallPerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmallPerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1345.PowerSmallPerUnitTime)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_pressure(self) -> '_1346.Pressure':
        '''Pressure: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1346.Pressure.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Pressure. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1346.Pressure)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_pressure_velocity_product(self) -> '_1347.PressureVelocityProduct':
        '''PressureVelocityProduct: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1347.PressureVelocityProduct.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PressureVelocityProduct. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1347.PressureVelocityProduct)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_pressure_viscosity_coefficient(self) -> '_1348.PressureViscosityCoefficient':
        '''PressureViscosityCoefficient: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1348.PressureViscosityCoefficient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PressureViscosityCoefficient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1348.PressureViscosityCoefficient)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_price(self) -> '_1349.Price':
        '''Price: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1349.Price.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Price. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1349.Price)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_quadratic_angular_damping(self) -> '_1350.QuadraticAngularDamping':
        '''QuadraticAngularDamping: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1350.QuadraticAngularDamping.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to QuadraticAngularDamping. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1350.QuadraticAngularDamping)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_quadratic_drag(self) -> '_1351.QuadraticDrag':
        '''QuadraticDrag: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1351.QuadraticDrag.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to QuadraticDrag. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1351.QuadraticDrag)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_rescaled_measurement(self) -> '_1352.RescaledMeasurement':
        '''RescaledMeasurement: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1352.RescaledMeasurement.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to RescaledMeasurement. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1352.RescaledMeasurement)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_rotatum(self) -> '_1353.Rotatum':
        '''Rotatum: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1353.Rotatum.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Rotatum. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1353.Rotatum)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_safety_factor(self) -> '_1354.SafetyFactor':
        '''SafetyFactor: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1354.SafetyFactor.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to SafetyFactor. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1354.SafetyFactor)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_specific_acoustic_impedance(self) -> '_1355.SpecificAcousticImpedance':
        '''SpecificAcousticImpedance: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1355.SpecificAcousticImpedance.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to SpecificAcousticImpedance. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1355.SpecificAcousticImpedance)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_specific_heat(self) -> '_1356.SpecificHeat':
        '''SpecificHeat: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1356.SpecificHeat.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to SpecificHeat. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1356.SpecificHeat)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_square_root_of_unit_force_per_unit_area(self) -> '_1357.SquareRootOfUnitForcePerUnitArea':
        '''SquareRootOfUnitForcePerUnitArea: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1357.SquareRootOfUnitForcePerUnitArea.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to SquareRootOfUnitForcePerUnitArea. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1357.SquareRootOfUnitForcePerUnitArea)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_stiffness_per_unit_face_width(self) -> '_1358.StiffnessPerUnitFaceWidth':
        '''StiffnessPerUnitFaceWidth: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1358.StiffnessPerUnitFaceWidth.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to StiffnessPerUnitFaceWidth. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1358.StiffnessPerUnitFaceWidth)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_stress(self) -> '_1359.Stress':
        '''Stress: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1359.Stress.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Stress. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1359.Stress)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_temperature(self) -> '_1360.Temperature':
        '''Temperature: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1360.Temperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Temperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1360.Temperature)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_temperature_difference(self) -> '_1361.TemperatureDifference':
        '''TemperatureDifference: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1361.TemperatureDifference.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TemperatureDifference. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1361.TemperatureDifference)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_temperature_per_unit_time(self) -> '_1362.TemperaturePerUnitTime':
        '''TemperaturePerUnitTime: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1362.TemperaturePerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TemperaturePerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1362.TemperaturePerUnitTime)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_text(self) -> '_1363.Text':
        '''Text: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1363.Text.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Text. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1363.Text)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_thermal_contact_coefficient(self) -> '_1364.ThermalContactCoefficient':
        '''ThermalContactCoefficient: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1364.ThermalContactCoefficient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ThermalContactCoefficient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1364.ThermalContactCoefficient)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_thermal_expansion_coefficient(self) -> '_1365.ThermalExpansionCoefficient':
        '''ThermalExpansionCoefficient: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1365.ThermalExpansionCoefficient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ThermalExpansionCoefficient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1365.ThermalExpansionCoefficient)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_thermo_elastic_factor(self) -> '_1366.ThermoElasticFactor':
        '''ThermoElasticFactor: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1366.ThermoElasticFactor.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ThermoElasticFactor. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1366.ThermoElasticFactor)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_time(self) -> '_1367.Time':
        '''Time: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1367.Time.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Time. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1367.Time)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_time_short(self) -> '_1368.TimeShort':
        '''TimeShort: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1368.TimeShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TimeShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1368.TimeShort)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_time_very_short(self) -> '_1369.TimeVeryShort':
        '''TimeVeryShort: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1369.TimeVeryShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TimeVeryShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1369.TimeVeryShort)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_torque(self) -> '_1370.Torque':
        '''Torque: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1370.Torque.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Torque. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1370.Torque)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_torque_converter_inverse_k(self) -> '_1371.TorqueConverterInverseK':
        '''TorqueConverterInverseK: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1371.TorqueConverterInverseK.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TorqueConverterInverseK. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1371.TorqueConverterInverseK)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_torque_converter_k(self) -> '_1372.TorqueConverterK':
        '''TorqueConverterK: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1372.TorqueConverterK.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TorqueConverterK. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1372.TorqueConverterK)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_torque_per_unit_temperature(self) -> '_1373.TorquePerUnitTemperature':
        '''TorquePerUnitTemperature: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1373.TorquePerUnitTemperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TorquePerUnitTemperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1373.TorquePerUnitTemperature)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_velocity(self) -> '_1374.Velocity':
        '''Velocity: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1374.Velocity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Velocity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1374.Velocity)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_velocity_small(self) -> '_1375.VelocitySmall':
        '''VelocitySmall: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1375.VelocitySmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to VelocitySmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1375.VelocitySmall)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_viscosity(self) -> '_1376.Viscosity':
        '''Viscosity: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1376.Viscosity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Viscosity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1376.Viscosity)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_voltage(self) -> '_1377.Voltage':
        '''Voltage: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1377.Voltage.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Voltage. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1377.Voltage)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_volume(self) -> '_1378.Volume':
        '''Volume: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1378.Volume.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Volume. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1378.Volume)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_wear_coefficient(self) -> '_1379.WearCoefficient':
        '''WearCoefficient: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1379.WearCoefficient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to WearCoefficient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1379.WearCoefficient)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_yank(self) -> '_1380.Yank':
        '''Yank: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1380.Yank.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Yank. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1380.Yank)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def results(self) -> 'List[float]':
        '''List[float]: 'Results' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Results, float)
        return value
