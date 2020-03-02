import enum
from typing import List, Optional

from pydantic import Field

from kisters.network_store.model_library.base import BaseLink as _BaseLink
from kisters.network_store.model_library.base import Model as _Model


class _Link(_BaseLink):
    domain: str = Field("water", const=True)


class Delay(_Link):
    element_class: str = Field("Delay", const=True)
    transit_time: float = Field(
        0.0, description="Time delay in seconds between source and target nodes"
    )


class PipeFrictionModel(str, enum.Enum):
    DARCY_WEISBACH = "darcy-weisbach"
    HAZEN_WILLIAMS = "hazen-williams"


class Pipe(_Link):
    element_class: str = Field("Pipe", const=True)
    diameter: float = Field(..., ge=0.0, description="Measured internal diameter")
    length: float = Field(..., ge=0.0, description="Longitudinal length of the pipe")
    roughness: float = Field(..., ge=0.0, description="Friction coefficient")
    model: PipeFrictionModel = Field(
        ..., description="Friction loss approximation method"
    )
    check_valve: Optional[bool] = Field(False, description="Disallow reverse flow")


class ChannelRoughnessModel(str, enum.Enum):
    CHEZY = "chezy"
    MANNING = "manning"


class ChannelRoutingModel(str, enum.Enum):
    SAINT_VENANT = "saint-venant"
    INERTIAL_WAVE = "inertial-wave"
    DIFFUSIVE_WAVE = "diffusive-wave"


class _CrossSectionStation(_Model):
    lr: float = Field(
        ..., description="Station distance from left bank when looking downstream"
    )
    z: float = Field(..., description="Station elevation")


class _LongitudinalStation(_Model):
    distance: Optional[float] = Field(
        None, ge=0.0, description="Distance along channel from source node"
    )
    roughness: float = Field(..., gt=0.0, description="Friction coefficient")
    cross_section: List[_CrossSectionStation] = Field(
        ..., min_items=3, description="List of points defining the channel bottom",
    )


class Channel(_Link):
    element_class: str = Field("Channel", const=True)
    length: float = Field(..., gt=0.0, description="Longitudinal length of the channel")
    stations: List[_LongitudinalStation] = Field(
        ...,
        min_items=1,
        description="List of longitudinal stations defining channel geometry",
    )
    roughness_model: ChannelRoughnessModel = Field(
        ChannelRoughnessModel.CHEZY, description="Friction loss approximation method"
    )
    model: ChannelRoutingModel = Field(
        ..., description="Fluid dynamics approximation method"
    )


class FlowControlledStructure(_Link):
    element_class: str = Field("FlowControlledStructure", const=True)
    min_flow: Optional[float] = Field(
        None, description="Minimum volumetric flow rate in m^3/s"
    )
    max_flow: Optional[float] = Field(
        None, description="Maximum volumetric flow rate in m^3/s"
    )


class _PumpTurbineSpeedPoint(_Model):
    flow: float = Field(..., gt=0.0)
    head: float = Field(..., gt=0.0)
    speed: float = Field(1.0, gt=0.0)


class _PumpTurbineEfficiencyPoint(_Model):
    flow: float = Field(..., gt=0.0)
    head: float = Field(..., gt=0.0)
    efficiency: float = Field(..., gt=0.0, le=1.0)


class _PumpTurbineHeadTWCorrection(_Model):
    link_uid: str = Field(..., regex="^[a-zA-Z]\\w*$")
    power: int = Field(..., ge=0.0)
    value: float


class _PumpTurbineOtherConstraints(_Model):
    flow_power: int = Field(..., ge=0.0)
    head_power: int = Field(..., ge=0.0)
    value: float


class _PumpTurbine(_Link):
    speed: Optional[List[_PumpTurbineSpeedPoint]] = Field(
        None, min_items=1, description="Flow-head-speed curve of drive shaft"
    )
    efficiency: Optional[List[_PumpTurbineEfficiencyPoint]] = Field(
        None,
        min_items=1,
        description="Flow-head-efficiency energy conversion curve of assembly",
    )
    length: Optional[float] = Field(None, gt=0.0, description="Length of flow path")
    min_flow: Optional[float] = Field(
        None, ge=0.0, description="Minimum volumetric flow rate in m^3/s"
    )
    max_flow: Optional[float] = Field(
        None, description="Maximum volumetric flow rate in m^3/s"
    )
    min_head: Optional[float] = Field(None, ge=0.0, description="Minimum head in m")
    max_head: Optional[float] = Field(None, description="Maximum head in m")
    min_power: Optional[float] = Field(None, ge=0.0, description="Minimum power in W")
    max_power: Optional[float] = Field(None, description="Maximum power in W")
    min_speed: Optional[float] = Field(None, ge=0.0, description="Minimum speed")
    max_speed: Optional[float] = Field(None, description="Maximum speed")
    head_tailwater_correction: Optional[List[_PumpTurbineHeadTWCorrection]] = Field(
        None,
        description="This polynomial is added to the difference between"
        " up- and downstream levels",
    )
    other_constraints: Optional[List[_PumpTurbineOtherConstraints]] = Field(
        None, description="Every polynomial will be added a constraint <= 0"
    )


class Pump(_PumpTurbine):
    element_class: str = Field("Pump", const=True)


class Turbine(_PumpTurbine):
    element_class: str = Field("Turbine", const=True)


class ValveModel(str, enum.Enum):
    PRV = "prv"
    PSV = "psv"
    PBV = "pbv"
    FCV = "fcv"
    TCV = "tcv"
    GPV = "gpv"


class Valve(_Link):
    element_class: str = Field("Valve", const=True)
    model: ValveModel = Field(..., description="Specific type of valve")
    coefficient: float = Field(..., ge=0.0, description="Energy loss coefficient")
    diameter: float = Field(
        ..., ge=0.0, description="Measured characteristic internal diameter"
    )
    setting: float = Field(
        ..., description="Valve setting, meaning varies with valve model"
    )


class WeirModel(str, enum.Enum):
    FREE = "free"
    SUBMERGED = "submerged"
    DYNAMIC = "dynamic"


class Weir(_Link):
    element_class: str = Field("Weir", const=True)
    model: WeirModel = Field(..., description="Specific type of weir")
    coefficient: float = Field(..., ge=0.0, description="Energy loss coefficient")
    min_crest_level: float
    max_crest_level: float
    crest_width: float = Field(..., gt=0.0)


class OrificeModel(str, enum.Enum):
    FREE = "free"
    SUBMERGED = "submerged"
    DYNAMIC = "dynamic"


class Orifice(_Link):
    element_class: str = Field("Orifice", const=True)
    model: OrificeModel = Field(..., description="Specific type of orifice")
    coefficient: float = Field(..., ge=0.0, description="Energy loss coefficient")
    aperture: float = Field(..., ge=0.0, description="Characteristic width of opening")
