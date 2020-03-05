'''_1969.py

ImportedFeLinkWithSelection
'''


from typing import Callable

from mastapy._internal import constructor
from mastapy.system_model.imported_fes import (
    _1837, _1966, _1967, _1968,
    _1970, _1971, _1972, _1973,
    _1974, _1975, _1976, _1988,
    _1999, _2000
)
from mastapy._internal.cast_exception import CastException
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_IMPORTED_FE_LINK_WITH_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.ImportedFEs', 'ImportedFeLinkWithSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('ImportedFeLinkWithSelection',)


class ImportedFeLinkWithSelection(_1.APIBase):
    '''ImportedFeLinkWithSelection

    This is a mastapy class.
    '''

    TYPE = _IMPORTED_FE_LINK_WITH_SELECTION
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ImportedFeLinkWithSelection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def add_selected_nodes(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'AddSelectedNodes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AddSelectedNodes

    @property
    def delete_all_nodes(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'DeleteAllNodes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DeleteAllNodes

    @property
    def select_component(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'SelectComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SelectComponent

    @property
    def link(self) -> '_1837.ImportedFELink':
        '''ImportedFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1837.ImportedFELink)(self.wrapped.Link) if self.wrapped.Link else None

    @property
    def link_of_type_imported_fe_electric_machine_stator_link(self) -> '_1966.ImportedFEElectricMachineStatorLink':
        '''ImportedFEElectricMachineStatorLink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1966.ImportedFEElectricMachineStatorLink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to ImportedFEElectricMachineStatorLink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new(_1966.ImportedFEElectricMachineStatorLink)(self.wrapped.Link) if self.wrapped.Link else None

    @property
    def link_of_type_imported_fe_gear_mesh_link(self) -> '_1967.ImportedFEGearMeshLink':
        '''ImportedFEGearMeshLink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1967.ImportedFEGearMeshLink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to ImportedFEGearMeshLink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new(_1967.ImportedFEGearMeshLink)(self.wrapped.Link) if self.wrapped.Link else None

    @property
    def link_of_type_imported_fe_gear_with_duplicated_meshes_link(self) -> '_1968.ImportedFEGearWithDuplicatedMeshesLink':
        '''ImportedFEGearWithDuplicatedMeshesLink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1968.ImportedFEGearWithDuplicatedMeshesLink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to ImportedFEGearWithDuplicatedMeshesLink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new(_1968.ImportedFEGearWithDuplicatedMeshesLink)(self.wrapped.Link) if self.wrapped.Link else None

    @property
    def link_of_type_imported_fe_multi_node_connector_link(self) -> '_1970.ImportedFEMultiNodeConnectorLink':
        '''ImportedFEMultiNodeConnectorLink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1970.ImportedFEMultiNodeConnectorLink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to ImportedFEMultiNodeConnectorLink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new(_1970.ImportedFEMultiNodeConnectorLink)(self.wrapped.Link) if self.wrapped.Link else None

    @property
    def link_of_type_imported_fe_multi_node_link(self) -> '_1971.ImportedFEMultiNodeLink':
        '''ImportedFEMultiNodeLink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1971.ImportedFEMultiNodeLink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to ImportedFEMultiNodeLink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new(_1971.ImportedFEMultiNodeLink)(self.wrapped.Link) if self.wrapped.Link else None

    @property
    def link_of_type_imported_fe_node_link(self) -> '_1972.ImportedFENodeLink':
        '''ImportedFENodeLink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1972.ImportedFENodeLink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to ImportedFENodeLink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new(_1972.ImportedFENodeLink)(self.wrapped.Link) if self.wrapped.Link else None

    @property
    def link_of_type_imported_fe_planetary_connector_multi_node_link(self) -> '_1973.ImportedFEPlanetaryConnectorMultiNodeLink':
        '''ImportedFEPlanetaryConnectorMultiNodeLink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1973.ImportedFEPlanetaryConnectorMultiNodeLink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to ImportedFEPlanetaryConnectorMultiNodeLink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new(_1973.ImportedFEPlanetaryConnectorMultiNodeLink)(self.wrapped.Link) if self.wrapped.Link else None

    @property
    def link_of_type_imported_fe_planet_based_link(self) -> '_1974.ImportedFEPlanetBasedLink':
        '''ImportedFEPlanetBasedLink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1974.ImportedFEPlanetBasedLink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to ImportedFEPlanetBasedLink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new(_1974.ImportedFEPlanetBasedLink)(self.wrapped.Link) if self.wrapped.Link else None

    @property
    def link_of_type_imported_fe_planet_carrier_link(self) -> '_1975.ImportedFEPlanetCarrierLink':
        '''ImportedFEPlanetCarrierLink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1975.ImportedFEPlanetCarrierLink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to ImportedFEPlanetCarrierLink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new(_1975.ImportedFEPlanetCarrierLink)(self.wrapped.Link) if self.wrapped.Link else None

    @property
    def link_of_type_imported_fe_point_load_link(self) -> '_1976.ImportedFEPointLoadLink':
        '''ImportedFEPointLoadLink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1976.ImportedFEPointLoadLink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to ImportedFEPointLoadLink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new(_1976.ImportedFEPointLoadLink)(self.wrapped.Link) if self.wrapped.Link else None

    @property
    def link_of_type_multi_angle_connection_link(self) -> '_1988.MultiAngleConnectionLink':
        '''MultiAngleConnectionLink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1988.MultiAngleConnectionLink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to MultiAngleConnectionLink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new(_1988.MultiAngleConnectionLink)(self.wrapped.Link) if self.wrapped.Link else None

    @property
    def link_of_type_rolling_ring_connection_link(self) -> '_1999.RollingRingConnectionLink':
        '''RollingRingConnectionLink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1999.RollingRingConnectionLink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to RollingRingConnectionLink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new(_1999.RollingRingConnectionLink)(self.wrapped.Link) if self.wrapped.Link else None

    @property
    def link_of_type_shaft_hub_connection_fe_link(self) -> '_2000.ShaftHubConnectionFELink':
        '''ShaftHubConnectionFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2000.ShaftHubConnectionFELink.TYPE not in self.wrapped.Link.__class__.__mro__:
            raise CastException('Failed to cast link to ShaftHubConnectionFELink. Expected: {}.'.format(self.wrapped.Link.__class__.__qualname__))

        return constructor.new(_2000.ShaftHubConnectionFELink)(self.wrapped.Link) if self.wrapped.Link else None
