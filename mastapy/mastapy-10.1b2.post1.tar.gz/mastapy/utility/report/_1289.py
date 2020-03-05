'''_1289.py

DynamicCustomReportItem
'''


from mastapy._internal import constructor
from mastapy.utility.report import (
    _1271, _1254, _1259, _1260,
    _1261, _1262, _1263, _1264,
    _1266, _1267, _1268, _1269,
    _1270, _1272, _1274, _1275,
    _1277, _1278, _1279, _1281,
    _1282, _1283, _1284, _1286,
    _1287
)
from mastapy.shafts import _21
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.cylindrical import _782
from mastapy.utility_gui.charts import _1481, _1482
from mastapy.bearings.bearing_results import _1548, _1551, _1559
from mastapy.system_model.analyses_and_results.system_deflections.reporting import _2331
from mastapy.system_model.analyses_and_results.parametric_study_tools import _3524
from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4812, _4816
from mastapy._internal.python_net import python_net_import

_DYNAMIC_CUSTOM_REPORT_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'DynamicCustomReportItem')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicCustomReportItem',)


class DynamicCustomReportItem(_1278.CustomReportNameableItem):
    '''DynamicCustomReportItem

    This is a mastapy class.
    '''

    TYPE = _DYNAMIC_CUSTOM_REPORT_ITEM

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DynamicCustomReportItem.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def is_main_report_item(self) -> 'bool':
        '''bool: 'IsMainReportItem' is the original name of this property.'''

        return self.wrapped.IsMainReportItem

    @is_main_report_item.setter
    def is_main_report_item(self, value: 'bool'):
        self.wrapped.IsMainReportItem = bool(value) if value else False

    @property
    def inner_item(self) -> '_1271.CustomReportItem':
        '''CustomReportItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1271.CustomReportItem)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_shaft_damage_results_table_and_chart(self) -> '_21.ShaftDamageResultsTableAndChart':
        '''ShaftDamageResultsTableAndChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _21.ShaftDamageResultsTableAndChart.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to ShaftDamageResultsTableAndChart. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_21.ShaftDamageResultsTableAndChart)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_cylindrical_gear_table_with_mg_charts(self) -> '_782.CylindricalGearTableWithMGCharts':
        '''CylindricalGearTableWithMGCharts: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _782.CylindricalGearTableWithMGCharts.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CylindricalGearTableWithMGCharts. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_782.CylindricalGearTableWithMGCharts)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_ad_hoc_custom_table(self) -> '_1254.AdHocCustomTable':
        '''AdHocCustomTable: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1254.AdHocCustomTable.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to AdHocCustomTable. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1254.AdHocCustomTable)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_chart(self) -> '_1259.CustomChart':
        '''CustomChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1259.CustomChart.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomChart. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1259.CustomChart)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_graphic(self) -> '_1260.CustomGraphic':
        '''CustomGraphic: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1260.CustomGraphic.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomGraphic. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1260.CustomGraphic)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_image(self) -> '_1261.CustomImage':
        '''CustomImage: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1261.CustomImage.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomImage. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1261.CustomImage)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report(self) -> '_1262.CustomReport':
        '''CustomReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1262.CustomReport.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReport. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1262.CustomReport)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_cad_drawing(self) -> '_1263.CustomReportCadDrawing':
        '''CustomReportCadDrawing: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1263.CustomReportCadDrawing.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportCadDrawing. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1263.CustomReportCadDrawing)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_chart(self) -> '_1264.CustomReportChart':
        '''CustomReportChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1264.CustomReportChart.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportChart. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1264.CustomReportChart)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_column(self) -> '_1266.CustomReportColumn':
        '''CustomReportColumn: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1266.CustomReportColumn.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportColumn. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1266.CustomReportColumn)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_columns(self) -> '_1267.CustomReportColumns':
        '''CustomReportColumns: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1267.CustomReportColumns.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportColumns. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1267.CustomReportColumns)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_definition_item(self) -> '_1268.CustomReportDefinitionItem':
        '''CustomReportDefinitionItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1268.CustomReportDefinitionItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportDefinitionItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1268.CustomReportDefinitionItem)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_horizontal_line(self) -> '_1269.CustomReportHorizontalLine':
        '''CustomReportHorizontalLine: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1269.CustomReportHorizontalLine.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportHorizontalLine. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1269.CustomReportHorizontalLine)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_html_item(self) -> '_1270.CustomReportHtmlItem':
        '''CustomReportHtmlItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1270.CustomReportHtmlItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportHtmlItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1270.CustomReportHtmlItem)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_item_container(self) -> '_1272.CustomReportItemContainer':
        '''CustomReportItemContainer: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1272.CustomReportItemContainer.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportItemContainer. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1272.CustomReportItemContainer)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_item_container_collection_base(self) -> '_1274.CustomReportItemContainerCollectionBase':
        '''CustomReportItemContainerCollectionBase: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1274.CustomReportItemContainerCollectionBase.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportItemContainerCollectionBase. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1274.CustomReportItemContainerCollectionBase)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_item_container_collection_item(self) -> '_1275.CustomReportItemContainerCollectionItem':
        '''CustomReportItemContainerCollectionItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1275.CustomReportItemContainerCollectionItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportItemContainerCollectionItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1275.CustomReportItemContainerCollectionItem)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_multi_property_item_base(self) -> '_1277.CustomReportMultiPropertyItemBase':
        '''CustomReportMultiPropertyItemBase: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1277.CustomReportMultiPropertyItemBase.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportMultiPropertyItemBase. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1277.CustomReportMultiPropertyItemBase)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_nameable_item(self) -> '_1278.CustomReportNameableItem':
        '''CustomReportNameableItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1278.CustomReportNameableItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportNameableItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1278.CustomReportNameableItem)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_named_item(self) -> '_1279.CustomReportNamedItem':
        '''CustomReportNamedItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1279.CustomReportNamedItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportNamedItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1279.CustomReportNamedItem)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_status_item(self) -> '_1281.CustomReportStatusItem':
        '''CustomReportStatusItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1281.CustomReportStatusItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportStatusItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1281.CustomReportStatusItem)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_tab(self) -> '_1282.CustomReportTab':
        '''CustomReportTab: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1282.CustomReportTab.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportTab. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1282.CustomReportTab)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_tabs(self) -> '_1283.CustomReportTabs':
        '''CustomReportTabs: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1283.CustomReportTabs.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportTabs. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1283.CustomReportTabs)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_text(self) -> '_1284.CustomReportText':
        '''CustomReportText: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1284.CustomReportText.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportText. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1284.CustomReportText)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_sub_report(self) -> '_1286.CustomSubReport':
        '''CustomSubReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1286.CustomSubReport.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomSubReport. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1286.CustomSubReport)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_table(self) -> '_1287.CustomTable':
        '''CustomTable: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1287.CustomTable.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomTable. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1287.CustomTable)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_dynamic_custom_report_item(self) -> 'DynamicCustomReportItem':
        '''DynamicCustomReportItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if DynamicCustomReportItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to DynamicCustomReportItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(DynamicCustomReportItem)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_line_chart(self) -> '_1481.CustomLineChart':
        '''CustomLineChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1481.CustomLineChart.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomLineChart. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1481.CustomLineChart)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_table_and_chart(self) -> '_1482.CustomTableAndChart':
        '''CustomTableAndChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1482.CustomTableAndChart.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomTableAndChart. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1482.CustomTableAndChart)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_loaded_bearing_chart_reporter(self) -> '_1548.LoadedBearingChartReporter':
        '''LoadedBearingChartReporter: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1548.LoadedBearingChartReporter.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to LoadedBearingChartReporter. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1548.LoadedBearingChartReporter)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_loaded_bearing_temperature_chart(self) -> '_1551.LoadedBearingTemperatureChart':
        '''LoadedBearingTemperatureChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1551.LoadedBearingTemperatureChart.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to LoadedBearingTemperatureChart. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1551.LoadedBearingTemperatureChart)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_loaded_roller_element_chart_reporter(self) -> '_1559.LoadedRollerElementChartReporter':
        '''LoadedRollerElementChartReporter: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1559.LoadedRollerElementChartReporter.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to LoadedRollerElementChartReporter. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1559.LoadedRollerElementChartReporter)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_shaft_system_deflection_sections_report(self) -> '_2331.ShaftSystemDeflectionSectionsReport':
        '''ShaftSystemDeflectionSectionsReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2331.ShaftSystemDeflectionSectionsReport.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to ShaftSystemDeflectionSectionsReport. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_2331.ShaftSystemDeflectionSectionsReport)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_parametric_study_histogram(self) -> '_3524.ParametricStudyHistogram':
        '''ParametricStudyHistogram: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _3524.ParametricStudyHistogram.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to ParametricStudyHistogram. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_3524.ParametricStudyHistogram)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_campbell_diagram_report(self) -> '_4812.CampbellDiagramReport':
        '''CampbellDiagramReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4812.CampbellDiagramReport.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CampbellDiagramReport. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_4812.CampbellDiagramReport)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_per_mode_results_report(self) -> '_4816.PerModeResultsReport':
        '''PerModeResultsReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4816.PerModeResultsReport.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to PerModeResultsReport. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_4816.PerModeResultsReport)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None
