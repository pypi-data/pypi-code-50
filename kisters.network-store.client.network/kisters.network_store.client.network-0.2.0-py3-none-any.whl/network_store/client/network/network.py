from datetime import datetime
from typing import List, Optional

from kisters.network_store.model_library.base import (
    BaseLink,
    BaseNode,
    LocationExtent,
    LocationSet,
)
from kisters.network_store.model_library.util import element_from_dict, element_to_dict
from kisters.water.rest_client import RESTClient


class Network:
    _resource = "rest", "networks"

    def __init__(self, name: str, client: RESTClient, drop_existing: bool = False):
        self._name = name
        self._client = client
        self._network_resource = (*self._resource, self.name)
        if drop_existing:
            self.drop()

    def initialize(
        self,
        nodes: Optional[List[BaseNode]] = None,
        links: Optional[List[BaseLink]] = None,
    ):
        """Clear a network, optionally setting new links and nodes

        Note that this does not purge the network history- older versions of
        networks can be revisited even after being initialised. Useful for
        defining a complete network in one call.

        :param nodes:
            Optional list of nodes
        :param links:
            Optional list pf links
        """
        network_data = {}
        if nodes:
            network_data["nodes"] = [element_to_dict(e) for e in nodes]
        if links:
            network_data["links"] = [element_to_dict(e) for e in links]
        self._client.post(self._network_resource, data=network_data)

    def get_extent(
        self,
        location_set: LocationSet = LocationSet.GEOGRAPHIC,
        *,
        dt: Optional[datetime] = None
    ) -> LocationExtent:
        """Gets the min and max values over all node locations

        Note that at the moment, only nodes are considered. Link vertices are
        ignored.

        :param location_set:
            The name of the location attribute, one of the LocationSet enum
        :param dt:
            Optional timestamp to access a historical version of the model
        """
        parameters = {"location_set": location_set}
        if dt:
            parameters["datetime"] = element_to_dict(dt)
        extents = self._client.get(
            (*self._network_resource, "extent"), parameters=parameters
        )
        return LocationExtent.parse_obj(extents)

    def get_links(
        self,
        uids: Optional[List[str]] = None,
        display_names: Optional[List[str]] = None,
        element_class: Optional[str] = None,
        adjacent_nodes: Optional[List[str]] = None,
        only_interior: Optional[bool] = True,
        dt: Optional[datetime] = None,
    ) -> List[BaseLink]:
        """Gets an iterable of links

        Gets the the links in the network. The links are filterable by optional
        kwargs.

        :param uids:
            Optional list of uid strings to match
        :param display_names:
            Optional list of display name strings to match
        :param element_class:
            Optional element class string to match
        :param adjacent_nodes:
            Optional list of node uids that the links are connected to
        :param only_interior:
            Don't to match links that are attached at only one end to an adjacent_node
        :param dt:
            Optional timestamp to access a historical version of the model
        """
        parameters = {}
        data = {}
        if uids:
            data["uids"] = uids
        if display_names:
            data["display_names"] = display_names
        if element_class:
            if isinstance(element_class, str):
                parameters["element_class"] = element_class
            elif hasattr(element_class, "__name__"):
                parameters["element_class"] = element_class.__name__
            else:
                raise ValueError(
                    "kwarg element_class {} should be string or element class".format(
                        element_class
                    )
                )
        if adjacent_nodes:
            data["adjacent_node_uids"] = [
                (node if isinstance(node, str) else node.uid) for node in adjacent_nodes
            ]
        if not only_interior:
            parameters["only_interior"] = "False"
        if dt:
            parameters["datetime"] = element_to_dict(dt)
        result = self._client.get(
            (*self._network_resource, "links"), parameters=parameters, data=data
        )
        return [element_from_dict(e) for e in result]

    def get_nodes(
        self,
        uids: Optional[List[str]] = None,
        display_names: Optional[List[str]] = None,
        element_class: Optional[List[str]] = None,
        extent: Optional[LocationExtent] = None,
        schematic_extent: Optional[LocationExtent] = None,
        dt: Optional[datetime] = None,
    ) -> List[BaseNode]:
        """Gets an iterable of nodes

        Gets the the nodes in the network. The nodes are filterable by optional
        kwargs.

        :param uids:
            Optional list of uid strings to match
        :param display_names:
            Optional list of display name strings to match
        :param element_class:
            Optional element type string to match
        :param extent:
            Optional mapping of extent dimensions to min and max extent of that
            dimension that returned nodes should be found within.
        :param schematic_extent:
            Optional mapping of schematic_extent dimensions to min and max extent
            of that dimension that returned nodes should be found within.
        :param dt:
            Optional timestamp to access a historical version of the model
        """
        parameters = {}
        data = {}
        if uids:
            data["uids"] = uids
        if display_names:
            data["display_names"] = display_names
        if element_class:
            if isinstance(element_class, str):
                parameters["element_class"] = element_class
            elif hasattr(element_class, "__name__"):
                parameters["element_class"] = element_class.__name__
            else:
                raise ValueError(
                    "kwarg element_class {} should be string or element class".format(
                        element_class
                    )
                )
        if extent:
            if isinstance(extent, dict):
                extent = LocationExtent.parse_obj(extent)
            data["extent"] = element_to_dict(extent)
        if schematic_extent:
            if isinstance(schematic_extent, dict):
                schematic_extent = LocationExtent.parse_obj(schematic_extent)
            data["schematic_extent"] = element_to_dict(schematic_extent)
        if dt:
            parameters["datetime"] = element_to_dict(dt)

        result = self._client.get(
            (*self._network_resource, "nodes"), parameters=parameters, data=data
        )
        return [element_from_dict(e) for e in result]

    def save_nodes(self, nodes: List[BaseNode]):
        """Save a list of nodes"""
        self._client.post(
            (*self._network_resource, "nodes"),
            data={"elements": [element_to_dict(e) for e in nodes]},
        )

    def save_links(self, links: List[BaseLink]):
        """Save a list of links"""
        self._client.post(
            (*self._network_resource, "links"),
            data={"elements": [element_to_dict(e) for e in links]},
        )

    def drop(self, purge: bool = False):
        """Removes the network"""
        self._client.delete(self._network_resource, parameters={"purge": purge})

    def drop_links(self, uids: Optional[List[str]] = None, purge: bool = False):
        """Deletes the links with the given uids"""
        self._client.delete(
            (*self._network_resource, "links"),
            data={"uids": uids} if uids else None,
            parameters={"purge": purge},
        )

    def drop_nodes(self, uids: Optional[List[str]] = None, purge: bool = False):
        """Deletes the nodes with the given uids"""
        self._client.delete(
            (*self._network_resource, "nodes"),
            data={"uids": uids} if uids else None,
            parameters={"purge": purge},
        )

    @property
    def name(self) -> str:
        """The name of the network"""
        return self._name
