'''_1086.py

OptimizationVariable
'''


from typing import List

from mastapy.utility.units_and_measurements import _1138
from mastapy._internal import constructor, conversion
from mastapy.utility.units_and_measurements.measurements import (
    _1145, _1146, _1147, _1148,
    _1149, _1150, _1151, _1152,
    _1153, _1154, _1155, _1156,
    _1157, _1158, _1159, _1160,
    _1161, _1162, _1163, _1164,
    _1165, _1166, _1167, _1168,
    _1169, _1170, _1171, _1172,
    _1173, _1174, _1175, _1176,
    _1177, _1178, _1179, _1180,
    _1181, _1182, _1183, _1184,
    _1185, _1186, _1187, _1188,
    _1189, _1190, _1191, _1192,
    _1193, _1194, _1195, _1196,
    _1197, _1198, _1199, _1200,
    _1201, _1202, _1203, _1204,
    _1205, _1206, _1207, _1208,
    _1209, _1210, _1211, _1212,
    _1213, _1214, _1215, _1216,
    _1217, _1218, _1219, _1220,
    _1221, _1222, _1223, _1224,
    _1225, _1226, _1227, _1228,
    _1229, _1230, _1231, _1232,
    _1233, _1234, _1235, _1236,
    _1237, _1238, _1239, _1240,
    _1241, _1242, _1243, _1244,
    _1245, _1246, _1247, _1248,
    _1249, _1250
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
    def measurement(self) -> '_1138.MeasurementBase':
        '''MeasurementBase: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1138.MeasurementBase)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_acceleration(self) -> '_1145.Acceleration':
        '''Acceleration: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1145.Acceleration.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Acceleration. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1145.Acceleration)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_angle(self) -> '_1146.Angle':
        '''Angle: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1146.Angle.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Angle. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1146.Angle)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_angle_per_unit_temperature(self) -> '_1147.AnglePerUnitTemperature':
        '''AnglePerUnitTemperature: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1147.AnglePerUnitTemperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AnglePerUnitTemperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1147.AnglePerUnitTemperature)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_angle_small(self) -> '_1148.AngleSmall':
        '''AngleSmall: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1148.AngleSmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngleSmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1148.AngleSmall)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_angle_very_small(self) -> '_1149.AngleVerySmall':
        '''AngleVerySmall: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1149.AngleVerySmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngleVerySmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1149.AngleVerySmall)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_angular_acceleration(self) -> '_1150.AngularAcceleration':
        '''AngularAcceleration: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1150.AngularAcceleration.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularAcceleration. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1150.AngularAcceleration)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_angular_compliance(self) -> '_1151.AngularCompliance':
        '''AngularCompliance: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1151.AngularCompliance.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularCompliance. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1151.AngularCompliance)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_angular_jerk(self) -> '_1152.AngularJerk':
        '''AngularJerk: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1152.AngularJerk.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularJerk. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1152.AngularJerk)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_angular_stiffness(self) -> '_1153.AngularStiffness':
        '''AngularStiffness: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1153.AngularStiffness.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularStiffness. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1153.AngularStiffness)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_angular_velocity(self) -> '_1154.AngularVelocity':
        '''AngularVelocity: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1154.AngularVelocity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularVelocity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1154.AngularVelocity)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_area(self) -> '_1155.Area':
        '''Area: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1155.Area.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Area. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1155.Area)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_area_small(self) -> '_1156.AreaSmall':
        '''AreaSmall: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1156.AreaSmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AreaSmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1156.AreaSmall)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_cycles(self) -> '_1157.Cycles':
        '''Cycles: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1157.Cycles.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Cycles. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1157.Cycles)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_damage(self) -> '_1158.Damage':
        '''Damage: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1158.Damage.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Damage. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1158.Damage)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_damage_rate(self) -> '_1159.DamageRate':
        '''DamageRate: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1159.DamageRate.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to DamageRate. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1159.DamageRate)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_decibel(self) -> '_1160.Decibel':
        '''Decibel: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1160.Decibel.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Decibel. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1160.Decibel)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_density(self) -> '_1161.Density':
        '''Density: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1161.Density.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Density. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1161.Density)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_energy(self) -> '_1162.Energy':
        '''Energy: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1162.Energy.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Energy. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1162.Energy)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_energy_per_unit_area(self) -> '_1163.EnergyPerUnitArea':
        '''EnergyPerUnitArea: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1163.EnergyPerUnitArea.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to EnergyPerUnitArea. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1163.EnergyPerUnitArea)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_energy_per_unit_area_small(self) -> '_1164.EnergyPerUnitAreaSmall':
        '''EnergyPerUnitAreaSmall: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1164.EnergyPerUnitAreaSmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to EnergyPerUnitAreaSmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1164.EnergyPerUnitAreaSmall)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_energy_small(self) -> '_1165.EnergySmall':
        '''EnergySmall: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1165.EnergySmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to EnergySmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1165.EnergySmall)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_enum(self) -> '_1166.Enum':
        '''Enum: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1166.Enum.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Enum. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1166.Enum)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_flow_rate(self) -> '_1167.FlowRate':
        '''FlowRate: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1167.FlowRate.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to FlowRate. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1167.FlowRate)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_force(self) -> '_1168.Force':
        '''Force: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1168.Force.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Force. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1168.Force)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_force_per_unit_length(self) -> '_1169.ForcePerUnitLength':
        '''ForcePerUnitLength: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1169.ForcePerUnitLength.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ForcePerUnitLength. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1169.ForcePerUnitLength)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_force_per_unit_pressure(self) -> '_1170.ForcePerUnitPressure':
        '''ForcePerUnitPressure: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1170.ForcePerUnitPressure.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ForcePerUnitPressure. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1170.ForcePerUnitPressure)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_force_per_unit_temperature(self) -> '_1171.ForcePerUnitTemperature':
        '''ForcePerUnitTemperature: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1171.ForcePerUnitTemperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ForcePerUnitTemperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1171.ForcePerUnitTemperature)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_fraction_measurement_base(self) -> '_1172.FractionMeasurementBase':
        '''FractionMeasurementBase: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1172.FractionMeasurementBase.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to FractionMeasurementBase. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1172.FractionMeasurementBase)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_frequency(self) -> '_1173.Frequency':
        '''Frequency: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1173.Frequency.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Frequency. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1173.Frequency)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_fuel_consumption_engine(self) -> '_1174.FuelConsumptionEngine':
        '''FuelConsumptionEngine: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1174.FuelConsumptionEngine.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to FuelConsumptionEngine. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1174.FuelConsumptionEngine)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_fuel_efficiency_vehicle(self) -> '_1175.FuelEfficiencyVehicle':
        '''FuelEfficiencyVehicle: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1175.FuelEfficiencyVehicle.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to FuelEfficiencyVehicle. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1175.FuelEfficiencyVehicle)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_gradient(self) -> '_1176.Gradient':
        '''Gradient: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1176.Gradient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Gradient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1176.Gradient)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_heat_conductivity(self) -> '_1177.HeatConductivity':
        '''HeatConductivity: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1177.HeatConductivity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatConductivity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1177.HeatConductivity)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_heat_transfer(self) -> '_1178.HeatTransfer':
        '''HeatTransfer: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1178.HeatTransfer.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatTransfer. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1178.HeatTransfer)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_heat_transfer_coefficient_for_plastic_gear_tooth(self) -> '_1179.HeatTransferCoefficientForPlasticGearTooth':
        '''HeatTransferCoefficientForPlasticGearTooth: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1179.HeatTransferCoefficientForPlasticGearTooth.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatTransferCoefficientForPlasticGearTooth. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1179.HeatTransferCoefficientForPlasticGearTooth)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_heat_transfer_resistance(self) -> '_1180.HeatTransferResistance':
        '''HeatTransferResistance: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1180.HeatTransferResistance.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatTransferResistance. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1180.HeatTransferResistance)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_impulse(self) -> '_1181.Impulse':
        '''Impulse: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1181.Impulse.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Impulse. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1181.Impulse)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_index(self) -> '_1182.Index':
        '''Index: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1182.Index.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Index. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1182.Index)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_integer(self) -> '_1183.Integer':
        '''Integer: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1183.Integer.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Integer. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1183.Integer)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_inverse_short_length(self) -> '_1184.InverseShortLength':
        '''InverseShortLength: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1184.InverseShortLength.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to InverseShortLength. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1184.InverseShortLength)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_inverse_short_time(self) -> '_1185.InverseShortTime':
        '''InverseShortTime: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1185.InverseShortTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to InverseShortTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1185.InverseShortTime)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_jerk(self) -> '_1186.Jerk':
        '''Jerk: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1186.Jerk.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Jerk. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1186.Jerk)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_kinematic_viscosity(self) -> '_1187.KinematicViscosity':
        '''KinematicViscosity: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1187.KinematicViscosity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to KinematicViscosity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1187.KinematicViscosity)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_length_long(self) -> '_1188.LengthLong':
        '''LengthLong: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1188.LengthLong.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthLong. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1188.LengthLong)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_length_medium(self) -> '_1189.LengthMedium':
        '''LengthMedium: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1189.LengthMedium.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthMedium. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1189.LengthMedium)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_length_per_unit_temperature(self) -> '_1190.LengthPerUnitTemperature':
        '''LengthPerUnitTemperature: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1190.LengthPerUnitTemperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthPerUnitTemperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1190.LengthPerUnitTemperature)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_length_short(self) -> '_1191.LengthShort':
        '''LengthShort: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1191.LengthShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1191.LengthShort)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_length_to_the_fourth(self) -> '_1192.LengthToTheFourth':
        '''LengthToTheFourth: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1192.LengthToTheFourth.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthToTheFourth. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1192.LengthToTheFourth)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_length_very_long(self) -> '_1193.LengthVeryLong':
        '''LengthVeryLong: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1193.LengthVeryLong.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthVeryLong. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1193.LengthVeryLong)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_length_very_short(self) -> '_1194.LengthVeryShort':
        '''LengthVeryShort: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1194.LengthVeryShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthVeryShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1194.LengthVeryShort)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_length_very_short_per_length_short(self) -> '_1195.LengthVeryShortPerLengthShort':
        '''LengthVeryShortPerLengthShort: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1195.LengthVeryShortPerLengthShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthVeryShortPerLengthShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1195.LengthVeryShortPerLengthShort)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_linear_angular_damping(self) -> '_1196.LinearAngularDamping':
        '''LinearAngularDamping: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1196.LinearAngularDamping.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearAngularDamping. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1196.LinearAngularDamping)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_linear_angular_stiffness_cross_term(self) -> '_1197.LinearAngularStiffnessCrossTerm':
        '''LinearAngularStiffnessCrossTerm: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1197.LinearAngularStiffnessCrossTerm.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearAngularStiffnessCrossTerm. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1197.LinearAngularStiffnessCrossTerm)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_linear_damping(self) -> '_1198.LinearDamping':
        '''LinearDamping: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1198.LinearDamping.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearDamping. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1198.LinearDamping)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_linear_flexibility(self) -> '_1199.LinearFlexibility':
        '''LinearFlexibility: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1199.LinearFlexibility.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearFlexibility. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1199.LinearFlexibility)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_linear_stiffness(self) -> '_1200.LinearStiffness':
        '''LinearStiffness: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1200.LinearStiffness.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearStiffness. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1200.LinearStiffness)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_mass(self) -> '_1201.Mass':
        '''Mass: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1201.Mass.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Mass. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1201.Mass)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_mass_per_unit_length(self) -> '_1202.MassPerUnitLength':
        '''MassPerUnitLength: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1202.MassPerUnitLength.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MassPerUnitLength. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1202.MassPerUnitLength)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_mass_per_unit_time(self) -> '_1203.MassPerUnitTime':
        '''MassPerUnitTime: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1203.MassPerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MassPerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1203.MassPerUnitTime)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_moment_of_inertia(self) -> '_1204.MomentOfInertia':
        '''MomentOfInertia: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1204.MomentOfInertia.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MomentOfInertia. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1204.MomentOfInertia)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_moment_of_inertia_per_unit_length(self) -> '_1205.MomentOfInertiaPerUnitLength':
        '''MomentOfInertiaPerUnitLength: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1205.MomentOfInertiaPerUnitLength.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MomentOfInertiaPerUnitLength. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1205.MomentOfInertiaPerUnitLength)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_moment_per_unit_pressure(self) -> '_1206.MomentPerUnitPressure':
        '''MomentPerUnitPressure: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1206.MomentPerUnitPressure.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MomentPerUnitPressure. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1206.MomentPerUnitPressure)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_number(self) -> '_1207.Number':
        '''Number: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1207.Number.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Number. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1207.Number)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_percentage(self) -> '_1208.Percentage':
        '''Percentage: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1208.Percentage.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Percentage. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1208.Percentage)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_power(self) -> '_1209.Power':
        '''Power: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1209.Power.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Power. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1209.Power)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_power_per_small_area(self) -> '_1210.PowerPerSmallArea':
        '''PowerPerSmallArea: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1210.PowerPerSmallArea.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerPerSmallArea. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1210.PowerPerSmallArea)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_power_small(self) -> '_1211.PowerSmall':
        '''PowerSmall: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1211.PowerSmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1211.PowerSmall)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_power_small_per_area(self) -> '_1212.PowerSmallPerArea':
        '''PowerSmallPerArea: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1212.PowerSmallPerArea.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmallPerArea. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1212.PowerSmallPerArea)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_power_small_per_unit_area_per_unit_time(self) -> '_1213.PowerSmallPerUnitAreaPerUnitTime':
        '''PowerSmallPerUnitAreaPerUnitTime: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1213.PowerSmallPerUnitAreaPerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmallPerUnitAreaPerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1213.PowerSmallPerUnitAreaPerUnitTime)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_power_small_per_unit_time(self) -> '_1214.PowerSmallPerUnitTime':
        '''PowerSmallPerUnitTime: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1214.PowerSmallPerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmallPerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1214.PowerSmallPerUnitTime)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_pressure(self) -> '_1215.Pressure':
        '''Pressure: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1215.Pressure.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Pressure. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1215.Pressure)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_pressure_per_unit_time(self) -> '_1216.PressurePerUnitTime':
        '''PressurePerUnitTime: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1216.PressurePerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PressurePerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1216.PressurePerUnitTime)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_pressure_velocity_product(self) -> '_1217.PressureVelocityProduct':
        '''PressureVelocityProduct: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1217.PressureVelocityProduct.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PressureVelocityProduct. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1217.PressureVelocityProduct)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_pressure_viscosity_coefficient(self) -> '_1218.PressureViscosityCoefficient':
        '''PressureViscosityCoefficient: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1218.PressureViscosityCoefficient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PressureViscosityCoefficient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1218.PressureViscosityCoefficient)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_price(self) -> '_1219.Price':
        '''Price: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1219.Price.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Price. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1219.Price)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_quadratic_angular_damping(self) -> '_1220.QuadraticAngularDamping':
        '''QuadraticAngularDamping: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1220.QuadraticAngularDamping.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to QuadraticAngularDamping. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1220.QuadraticAngularDamping)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_quadratic_drag(self) -> '_1221.QuadraticDrag':
        '''QuadraticDrag: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1221.QuadraticDrag.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to QuadraticDrag. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1221.QuadraticDrag)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_rescaled_measurement(self) -> '_1222.RescaledMeasurement':
        '''RescaledMeasurement: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1222.RescaledMeasurement.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to RescaledMeasurement. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1222.RescaledMeasurement)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_rotatum(self) -> '_1223.Rotatum':
        '''Rotatum: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1223.Rotatum.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Rotatum. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1223.Rotatum)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_safety_factor(self) -> '_1224.SafetyFactor':
        '''SafetyFactor: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1224.SafetyFactor.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to SafetyFactor. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1224.SafetyFactor)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_specific_acoustic_impedance(self) -> '_1225.SpecificAcousticImpedance':
        '''SpecificAcousticImpedance: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1225.SpecificAcousticImpedance.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to SpecificAcousticImpedance. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1225.SpecificAcousticImpedance)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_specific_heat(self) -> '_1226.SpecificHeat':
        '''SpecificHeat: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1226.SpecificHeat.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to SpecificHeat. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1226.SpecificHeat)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_square_root_of_unit_force_per_unit_area(self) -> '_1227.SquareRootOfUnitForcePerUnitArea':
        '''SquareRootOfUnitForcePerUnitArea: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1227.SquareRootOfUnitForcePerUnitArea.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to SquareRootOfUnitForcePerUnitArea. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1227.SquareRootOfUnitForcePerUnitArea)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_stiffness_per_unit_face_width(self) -> '_1228.StiffnessPerUnitFaceWidth':
        '''StiffnessPerUnitFaceWidth: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1228.StiffnessPerUnitFaceWidth.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to StiffnessPerUnitFaceWidth. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1228.StiffnessPerUnitFaceWidth)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_stress(self) -> '_1229.Stress':
        '''Stress: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1229.Stress.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Stress. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1229.Stress)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_temperature(self) -> '_1230.Temperature':
        '''Temperature: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1230.Temperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Temperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1230.Temperature)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_temperature_difference(self) -> '_1231.TemperatureDifference':
        '''TemperatureDifference: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1231.TemperatureDifference.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TemperatureDifference. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1231.TemperatureDifference)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_temperature_per_unit_time(self) -> '_1232.TemperaturePerUnitTime':
        '''TemperaturePerUnitTime: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1232.TemperaturePerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TemperaturePerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1232.TemperaturePerUnitTime)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_text(self) -> '_1233.Text':
        '''Text: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1233.Text.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Text. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1233.Text)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_thermal_contact_coefficient(self) -> '_1234.ThermalContactCoefficient':
        '''ThermalContactCoefficient: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1234.ThermalContactCoefficient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ThermalContactCoefficient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1234.ThermalContactCoefficient)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_thermal_expansion_coefficient(self) -> '_1235.ThermalExpansionCoefficient':
        '''ThermalExpansionCoefficient: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1235.ThermalExpansionCoefficient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ThermalExpansionCoefficient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1235.ThermalExpansionCoefficient)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_thermo_elastic_factor(self) -> '_1236.ThermoElasticFactor':
        '''ThermoElasticFactor: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1236.ThermoElasticFactor.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ThermoElasticFactor. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1236.ThermoElasticFactor)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_time(self) -> '_1237.Time':
        '''Time: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1237.Time.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Time. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1237.Time)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_time_short(self) -> '_1238.TimeShort':
        '''TimeShort: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1238.TimeShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TimeShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1238.TimeShort)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_time_very_short(self) -> '_1239.TimeVeryShort':
        '''TimeVeryShort: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1239.TimeVeryShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TimeVeryShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1239.TimeVeryShort)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_torque(self) -> '_1240.Torque':
        '''Torque: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1240.Torque.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Torque. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1240.Torque)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_torque_converter_inverse_k(self) -> '_1241.TorqueConverterInverseK':
        '''TorqueConverterInverseK: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1241.TorqueConverterInverseK.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TorqueConverterInverseK. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1241.TorqueConverterInverseK)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_torque_converter_k(self) -> '_1242.TorqueConverterK':
        '''TorqueConverterK: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1242.TorqueConverterK.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TorqueConverterK. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1242.TorqueConverterK)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_torque_per_unit_temperature(self) -> '_1243.TorquePerUnitTemperature':
        '''TorquePerUnitTemperature: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1243.TorquePerUnitTemperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TorquePerUnitTemperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1243.TorquePerUnitTemperature)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_velocity(self) -> '_1244.Velocity':
        '''Velocity: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1244.Velocity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Velocity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1244.Velocity)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_velocity_small(self) -> '_1245.VelocitySmall':
        '''VelocitySmall: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1245.VelocitySmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to VelocitySmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1245.VelocitySmall)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_viscosity(self) -> '_1246.Viscosity':
        '''Viscosity: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1246.Viscosity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Viscosity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1246.Viscosity)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_voltage(self) -> '_1247.Voltage':
        '''Voltage: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1247.Voltage.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Voltage. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1247.Voltage)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_volume(self) -> '_1248.Volume':
        '''Volume: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1248.Volume.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Volume. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1248.Volume)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_wear_coefficient(self) -> '_1249.WearCoefficient':
        '''WearCoefficient: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1249.WearCoefficient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to WearCoefficient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1249.WearCoefficient)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def measurement_of_type_yank(self) -> '_1250.Yank':
        '''Yank: 'Measurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1250.Yank.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Yank. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new(_1250.Yank)(self.wrapped.Measurement) if self.wrapped.Measurement else None

    @property
    def results(self) -> 'List[float]':
        '''List[float]: 'Results' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Results, float)
        return value
