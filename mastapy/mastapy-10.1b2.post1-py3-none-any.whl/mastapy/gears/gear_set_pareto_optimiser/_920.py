'''_920.py

ChartInfoBase
'''


from typing import (
    Callable, List, Generic, TypeVar
)

from mastapy.math_utility.optimisation import _1080
from mastapy._internal import constructor, conversion
from mastapy.utility.reporting_property_framework import _1081
from mastapy.scripting import _739
from mastapy.gears.gear_set_pareto_optimiser import (
    _922, _921, _924, _928,
    _929, _932, _935, _951,
    _952, _918, _930
)
from mastapy._internal.cast_exception import CastException
from mastapy import _1
from mastapy.gears.analysis import _390
from mastapy._internal.python_net import python_net_import

_CHART_INFO_BASE = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'ChartInfoBase')


__docformat__ = 'restructuredtext en'
__all__ = ('ChartInfoBase',)


TAnalysis = TypeVar('TAnalysis', bound='_390.AbstractGearSetAnalysis')
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
    def select_chart_type(self) -> '_1080.ParetoOptimisationStrategyChartInformation.ScatterOrBarChart':
        '''ParetoOptimisationStrategyChartInformation.ScatterOrBarChart: 'SelectChartType' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.SelectChartType)
        return constructor.new(_1080.ParetoOptimisationStrategyChartInformation.ScatterOrBarChart)(value) if value else None

    @select_chart_type.setter
    def select_chart_type(self, value: '_1080.ParetoOptimisationStrategyChartInformation.ScatterOrBarChart'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.SelectChartType = value

    @property
    def chart_type(self) -> '_1081.CustomChartType':
        '''CustomChartType: 'ChartType' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_enum(self.wrapped.ChartType)
        return constructor.new(_1081.CustomChartType)(value) if value else None

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
    def result_chart_scatter(self) -> '_739.SMTBitmap':
        '''SMTBitmap: 'ResultChartScatter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_739.SMTBitmap)(self.wrapped.ResultChartScatter) if self.wrapped.ResultChartScatter else None

    @property
    def result_chart_bar_and_line(self) -> '_739.SMTBitmap':
        '''SMTBitmap: 'ResultChartBarAndLine' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_739.SMTBitmap)(self.wrapped.ResultChartBarAndLine) if self.wrapped.ResultChartBarAndLine else None

    @property
    def chart_name(self) -> 'str':
        '''str: 'ChartName' is the original name of this property.'''

        return self.wrapped.ChartName

    @chart_name.setter
    def chart_name(self, value: 'str'):
        self.wrapped.ChartName = str(value) if value else None

    @property
    def optimiser(self) -> '_922.DesignSpaceSearchBase[TAnalysis, TCandidate]':
        '''DesignSpaceSearchBase[TAnalysis, TCandidate]: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_922.DesignSpaceSearchBase)[TAnalysis, TCandidate](self.wrapped.Optimiser) if self.wrapped.Optimiser else None

    @property
    def optimiser_of_type_cylindrical_gear_set_pareto_optimiser(self) -> '_921.CylindricalGearSetParetoOptimiser':
        '''CylindricalGearSetParetoOptimiser: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _921.CylindricalGearSetParetoOptimiser.TYPE not in self.wrapped.Optimiser.__class__.__mro__:
            raise CastException('Failed to cast optimiser to CylindricalGearSetParetoOptimiser. Expected: {}.'.format(self.wrapped.Optimiser.__class__.__qualname__))

        return constructor.new(_921.CylindricalGearSetParetoOptimiser)(self.wrapped.Optimiser) if self.wrapped.Optimiser else None

    @property
    def optimiser_of_type_face_gear_set_pareto_optimiser(self) -> '_924.FaceGearSetParetoOptimiser':
        '''FaceGearSetParetoOptimiser: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _924.FaceGearSetParetoOptimiser.TYPE not in self.wrapped.Optimiser.__class__.__mro__:
            raise CastException('Failed to cast optimiser to FaceGearSetParetoOptimiser. Expected: {}.'.format(self.wrapped.Optimiser.__class__.__qualname__))

        return constructor.new(_924.FaceGearSetParetoOptimiser)(self.wrapped.Optimiser) if self.wrapped.Optimiser else None

    @property
    def optimiser_of_type_gear_set_pareto_optimiser(self) -> '_928.GearSetParetoOptimiser':
        '''GearSetParetoOptimiser: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _928.GearSetParetoOptimiser.TYPE not in self.wrapped.Optimiser.__class__.__mro__:
            raise CastException('Failed to cast optimiser to GearSetParetoOptimiser. Expected: {}.'.format(self.wrapped.Optimiser.__class__.__qualname__))

        return constructor.new(_928.GearSetParetoOptimiser)(self.wrapped.Optimiser) if self.wrapped.Optimiser else None

    @property
    def optimiser_of_type_hypoid_gear_set_pareto_optimiser(self) -> '_929.HypoidGearSetParetoOptimiser':
        '''HypoidGearSetParetoOptimiser: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _929.HypoidGearSetParetoOptimiser.TYPE not in self.wrapped.Optimiser.__class__.__mro__:
            raise CastException('Failed to cast optimiser to HypoidGearSetParetoOptimiser. Expected: {}.'.format(self.wrapped.Optimiser.__class__.__qualname__))

        return constructor.new(_929.HypoidGearSetParetoOptimiser)(self.wrapped.Optimiser) if self.wrapped.Optimiser else None

    @property
    def optimiser_of_type_micro_geometry_design_space_search(self) -> '_932.MicroGeometryDesignSpaceSearch':
        '''MicroGeometryDesignSpaceSearch: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _932.MicroGeometryDesignSpaceSearch.TYPE not in self.wrapped.Optimiser.__class__.__mro__:
            raise CastException('Failed to cast optimiser to MicroGeometryDesignSpaceSearch. Expected: {}.'.format(self.wrapped.Optimiser.__class__.__qualname__))

        return constructor.new(_932.MicroGeometryDesignSpaceSearch)(self.wrapped.Optimiser) if self.wrapped.Optimiser else None

    @property
    def optimiser_of_type_micro_geometry_gear_set_design_space_search(self) -> '_935.MicroGeometryGearSetDesignSpaceSearch':
        '''MicroGeometryGearSetDesignSpaceSearch: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _935.MicroGeometryGearSetDesignSpaceSearch.TYPE not in self.wrapped.Optimiser.__class__.__mro__:
            raise CastException('Failed to cast optimiser to MicroGeometryGearSetDesignSpaceSearch. Expected: {}.'.format(self.wrapped.Optimiser.__class__.__qualname__))

        return constructor.new(_935.MicroGeometryGearSetDesignSpaceSearch)(self.wrapped.Optimiser) if self.wrapped.Optimiser else None

    @property
    def optimiser_of_type_spiral_bevel_gear_set_pareto_optimiser(self) -> '_951.SpiralBevelGearSetParetoOptimiser':
        '''SpiralBevelGearSetParetoOptimiser: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _951.SpiralBevelGearSetParetoOptimiser.TYPE not in self.wrapped.Optimiser.__class__.__mro__:
            raise CastException('Failed to cast optimiser to SpiralBevelGearSetParetoOptimiser. Expected: {}.'.format(self.wrapped.Optimiser.__class__.__qualname__))

        return constructor.new(_951.SpiralBevelGearSetParetoOptimiser)(self.wrapped.Optimiser) if self.wrapped.Optimiser else None

    @property
    def optimiser_of_type_straight_bevel_gear_set_pareto_optimiser(self) -> '_952.StraightBevelGearSetParetoOptimiser':
        '''StraightBevelGearSetParetoOptimiser: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _952.StraightBevelGearSetParetoOptimiser.TYPE not in self.wrapped.Optimiser.__class__.__mro__:
            raise CastException('Failed to cast optimiser to StraightBevelGearSetParetoOptimiser. Expected: {}.'.format(self.wrapped.Optimiser.__class__.__qualname__))

        return constructor.new(_952.StraightBevelGearSetParetoOptimiser)(self.wrapped.Optimiser) if self.wrapped.Optimiser else None

    @property
    def bars(self) -> 'List[_918.BarForPareto[TAnalysis, TCandidate]]':
        '''List[BarForPareto[TAnalysis, TCandidate]]: 'Bars' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bars, constructor.new(_918.BarForPareto)[TAnalysis, TCandidate])
        return value

    @property
    def input_sliders(self) -> 'List[_930.InputSliderForPareto[TAnalysis, TCandidate]]':
        '''List[InputSliderForPareto[TAnalysis, TCandidate]]: 'InputSliders' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.InputSliders, constructor.new(_930.InputSliderForPareto)[TAnalysis, TCandidate])
        return value
