'''_792.py

ChartInfoBase
'''


from typing import (
    Callable, List, Generic, TypeVar
)

from mastapy.math_utility.optimisation import _1213
from mastapy._internal import constructor, conversion
from mastapy.utility.reporting_property_framework import _1371
from mastapy.scripting import _6321
from mastapy.gears.gear_set_pareto_optimiser import (
    _794, _793, _796, _800,
    _801, _804, _807, _823,
    _824, _790, _802
)
from mastapy._internal.cast_exception import CastException
from mastapy import _1
from mastapy.gears.analysis import _1060
from mastapy._internal.python_net import python_net_import

_CHART_INFO_BASE = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'ChartInfoBase')


__docformat__ = 'restructuredtext en'
__all__ = ('ChartInfoBase',)


TAnalysis = TypeVar('TAnalysis', bound='_1060.AbstractGearSetAnalysis')
TCandidate = TypeVar('TCandidate', bound='')


class ChartInfoBase(_1.APIBase, Generic[TAnalysis, TCandidate]):
    '''ChartInfoBase

    This is a mastapy class.

    Generic Types:
        TAnalysis
        TCandidate
    '''

    TYPE = _CHART_INFO_BASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ChartInfoBase.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def select_chart_type(self) -> '_1213.ParetoOptimisationStrategyChartInformation.ScatterOrBarChart':
        '''ParetoOptimisationStrategyChartInformation.ScatterOrBarChart: 'SelectChartType' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.SelectChartType)
        return constructor.new(_1213.ParetoOptimisationStrategyChartInformation.ScatterOrBarChart)(value) if value else None

    @select_chart_type.setter
    def select_chart_type(self, value: '_1213.ParetoOptimisationStrategyChartInformation.ScatterOrBarChart'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.SelectChartType = value

    @property
    def chart_type(self) -> '_1371.CustomChartType':
        '''CustomChartType: 'ChartType' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_enum(self.wrapped.ChartType)
        return constructor.new(_1371.CustomChartType)(value) if value else None

    @property
    def remove_chart(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'RemoveChart' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RemoveChart

    @property
    def add_bar(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'AddBar' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AddBar

    @property
    def selected_candidate_design(self) -> 'int':
        '''int: 'SelectedCandidateDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SelectedCandidateDesign

    @property
    def add_selected_design(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'AddSelectedDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AddSelectedDesign

    @property
    def add_selected_designs(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'AddSelectedDesigns' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AddSelectedDesigns

    @property
    def result_chart_scatter(self) -> '_6321.SMTBitmap':
        '''SMTBitmap: 'ResultChartScatter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6321.SMTBitmap)(self.wrapped.ResultChartScatter) if self.wrapped.ResultChartScatter else None

    @property
    def result_chart_bar_and_line(self) -> '_6321.SMTBitmap':
        '''SMTBitmap: 'ResultChartBarAndLine' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6321.SMTBitmap)(self.wrapped.ResultChartBarAndLine) if self.wrapped.ResultChartBarAndLine else None

    @property
    def chart_name(self) -> 'str':
        '''str: 'ChartName' is the original name of this property.'''

        return self.wrapped.ChartName

    @chart_name.setter
    def chart_name(self, value: 'str'):
        self.wrapped.ChartName = str(value) if value else None

    @property
    def optimiser(self) -> '_794.DesignSpaceSearchBase[TAnalysis, TCandidate]':
        '''DesignSpaceSearchBase[TAnalysis, TCandidate]: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_794.DesignSpaceSearchBase)[TAnalysis, TCandidate](self.wrapped.Optimiser) if self.wrapped.Optimiser else None

    @property
    def optimiser_of_type_cylindrical_gear_set_pareto_optimiser(self) -> '_793.CylindricalGearSetParetoOptimiser':
        '''CylindricalGearSetParetoOptimiser: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _793.CylindricalGearSetParetoOptimiser.TYPE not in self.wrapped.Optimiser.__class__.__mro__:
            raise CastException('Failed to cast optimiser to CylindricalGearSetParetoOptimiser. Expected: {}.'.format(self.wrapped.Optimiser.__class__.__qualname__))

        return constructor.new(_793.CylindricalGearSetParetoOptimiser)(self.wrapped.Optimiser) if self.wrapped.Optimiser else None

    @property
    def optimiser_of_type_face_gear_set_pareto_optimiser(self) -> '_796.FaceGearSetParetoOptimiser':
        '''FaceGearSetParetoOptimiser: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _796.FaceGearSetParetoOptimiser.TYPE not in self.wrapped.Optimiser.__class__.__mro__:
            raise CastException('Failed to cast optimiser to FaceGearSetParetoOptimiser. Expected: {}.'.format(self.wrapped.Optimiser.__class__.__qualname__))

        return constructor.new(_796.FaceGearSetParetoOptimiser)(self.wrapped.Optimiser) if self.wrapped.Optimiser else None

    @property
    def optimiser_of_type_gear_set_pareto_optimiser(self) -> '_800.GearSetParetoOptimiser':
        '''GearSetParetoOptimiser: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _800.GearSetParetoOptimiser.TYPE not in self.wrapped.Optimiser.__class__.__mro__:
            raise CastException('Failed to cast optimiser to GearSetParetoOptimiser. Expected: {}.'.format(self.wrapped.Optimiser.__class__.__qualname__))

        return constructor.new(_800.GearSetParetoOptimiser)(self.wrapped.Optimiser) if self.wrapped.Optimiser else None

    @property
    def optimiser_of_type_hypoid_gear_set_pareto_optimiser(self) -> '_801.HypoidGearSetParetoOptimiser':
        '''HypoidGearSetParetoOptimiser: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _801.HypoidGearSetParetoOptimiser.TYPE not in self.wrapped.Optimiser.__class__.__mro__:
            raise CastException('Failed to cast optimiser to HypoidGearSetParetoOptimiser. Expected: {}.'.format(self.wrapped.Optimiser.__class__.__qualname__))

        return constructor.new(_801.HypoidGearSetParetoOptimiser)(self.wrapped.Optimiser) if self.wrapped.Optimiser else None

    @property
    def optimiser_of_type_micro_geometry_design_space_search(self) -> '_804.MicroGeometryDesignSpaceSearch':
        '''MicroGeometryDesignSpaceSearch: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _804.MicroGeometryDesignSpaceSearch.TYPE not in self.wrapped.Optimiser.__class__.__mro__:
            raise CastException('Failed to cast optimiser to MicroGeometryDesignSpaceSearch. Expected: {}.'.format(self.wrapped.Optimiser.__class__.__qualname__))

        return constructor.new(_804.MicroGeometryDesignSpaceSearch)(self.wrapped.Optimiser) if self.wrapped.Optimiser else None

    @property
    def optimiser_of_type_micro_geometry_gear_set_design_space_search(self) -> '_807.MicroGeometryGearSetDesignSpaceSearch':
        '''MicroGeometryGearSetDesignSpaceSearch: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _807.MicroGeometryGearSetDesignSpaceSearch.TYPE not in self.wrapped.Optimiser.__class__.__mro__:
            raise CastException('Failed to cast optimiser to MicroGeometryGearSetDesignSpaceSearch. Expected: {}.'.format(self.wrapped.Optimiser.__class__.__qualname__))

        return constructor.new(_807.MicroGeometryGearSetDesignSpaceSearch)(self.wrapped.Optimiser) if self.wrapped.Optimiser else None

    @property
    def optimiser_of_type_spiral_bevel_gear_set_pareto_optimiser(self) -> '_823.SpiralBevelGearSetParetoOptimiser':
        '''SpiralBevelGearSetParetoOptimiser: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _823.SpiralBevelGearSetParetoOptimiser.TYPE not in self.wrapped.Optimiser.__class__.__mro__:
            raise CastException('Failed to cast optimiser to SpiralBevelGearSetParetoOptimiser. Expected: {}.'.format(self.wrapped.Optimiser.__class__.__qualname__))

        return constructor.new(_823.SpiralBevelGearSetParetoOptimiser)(self.wrapped.Optimiser) if self.wrapped.Optimiser else None

    @property
    def optimiser_of_type_straight_bevel_gear_set_pareto_optimiser(self) -> '_824.StraightBevelGearSetParetoOptimiser':
        '''StraightBevelGearSetParetoOptimiser: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _824.StraightBevelGearSetParetoOptimiser.TYPE not in self.wrapped.Optimiser.__class__.__mro__:
            raise CastException('Failed to cast optimiser to StraightBevelGearSetParetoOptimiser. Expected: {}.'.format(self.wrapped.Optimiser.__class__.__qualname__))

        return constructor.new(_824.StraightBevelGearSetParetoOptimiser)(self.wrapped.Optimiser) if self.wrapped.Optimiser else None

    @property
    def bars(self) -> 'List[_790.BarForPareto[TAnalysis, TCandidate]]':
        '''List[BarForPareto[TAnalysis, TCandidate]]: 'Bars' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bars, constructor.new(_790.BarForPareto)[TAnalysis, TCandidate])
        return value

    @property
    def input_sliders(self) -> 'List[_802.InputSliderForPareto[TAnalysis, TCandidate]]':
        '''List[InputSliderForPareto[TAnalysis, TCandidate]]: 'InputSliders' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.InputSliders, constructor.new(_802.InputSliderForPareto)[TAnalysis, TCandidate])
        return value
