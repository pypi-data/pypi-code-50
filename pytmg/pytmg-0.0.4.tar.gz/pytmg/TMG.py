"""
Base class for the pyTMG library.
"""
import json
import requests
from pytmg.TMGResult import TMGResult


class TMG:
    """
    The TMG object is the primary point of entry for pyTMG.

    A TMG object instantiates basic access information for Cisco's TMG
    (Transceiver Module Group) Compatibility Matrix, as well as provides
    methods for common tasks performed through the TMG web application.
    """

    def __init__(self):
        """
        Instantiates an object of class TMG.
        """
        self.search_url = "https://tmgmatrix.cisco.com/public/api/networkdevice/search"
        self.suggest_url = (
            "https://tmgmatrix.cisco.com/public/api/networkdevice/autosuggest"
        )

    def _search(
        self,
        cable_type=[],
        data_rate=[],
        form_factor=[],
        reach=[],
        search_input=[],
        os_type=[],
        transceiver_product_family=[],
        transceiver_product_id=[],
        network_device_product_family=[],
        network_device_product_id=[],
    ):
        # TODO: Add support for advanced search functionality - right now,
        #       only "search_input" is really supported.
        body = {
            "cableType": cable_type,
            "dataRate": data_rate,
            "formFactor": form_factor,
            "reach": reach,
            "searchInput": search_input,
            "osType": os_type,
            "transceiverProductFamily": transceiver_product_family,
            "transceiverProductID": transceiver_product_id,
            "networkDeviceProductFamily": network_device_product_family,
            "networkDeviceProductID": network_device_product_id,
        }
        headers = {"content-type": "application/json"}

        res = requests.post(self.search_url, json=body, headers=headers)
        res.raise_for_status()
        return res.json()

    def search(self, **kwargs):
        """
        Performs a search query against Cisco's TMG (Transceiver Module Group)
        Compatibility Matrix.

        :param dict kwargs: A dictionary containing specific parameters of the
            search query.
        
        :Examples:

        >>> from pytmg import TMG
        >>> tmg = TMG.TMG()
        >>> params = {
        ...     "search_input": ["N9K-C93180YC-EX"],
        ... }
        >>> tmg_res = tmg.search(**params)
        """
        results = self._search(
            cable_type=kwargs.get("cable_type", []),
            data_rate=kwargs.get("data_rate", []),
            form_factor=kwargs.get("form_factor", []),
            reach=kwargs.get("reach", []),
            search_input=kwargs.get("search_input", []),
            os_type=kwargs.get("os_type", []),
            transceiver_product_family=kwargs.get("transceiver_product_family", []),
            transceiver_product_id=kwargs.get("transceiver_product_id", []),
            network_device_product_family=kwargs.get(
                "network_device_product_family", []
            ),
            network_device_product_id=kwargs.get("network_device_product_id", []),
        )
        return TMGResult(results)

    def search_device(self, search_device):
        """
        Performs a search for a network device.

        This method performs a simple search for all transceivers supported by
        a specific network device. This is akin to using the "search bar"
        functionality on Cisco's official web application.

        :param str search_device: The PID/model number of the Cisco network
            device that you would like to search for.

        :Examples:

        >>> from pytmg import TMG
        >>> tmg = TMG.TMG()
        >>> tmg_res = tmg.search_device("N9K-C93180YC-EX")

        >>> from pytmg import TMG
        >>> tmg = TMG.TMG()
        >>> tmg_res = tmg.search_device("WS-C2960")
        """
        search_terms = {"search_input": [search_device]}
        res = self.search(**search_terms)
        return res

    def search_devices(self, search_devices):
        """
        Performs a search for multiple network devices.

        This method performs a simple search for all transceivers supported by
        a list of specific network devices. This is akin to adding multiple
        network devices to the "search bar" on Cisco's official web
        application.

        :param list search_devices: A list of PIDs/model numbers of Cisco
            network devices that you would like to search for.
        
        :Examples:

        >>> from pytmg import TMG
        >>> tmg = TMG.TMG()
        >>> device_list = [
        ...     "N9K-C93180YC-EX",
        ...     "WS-C2960",
        ...     "WS-C3750",
        ... ]
        >>> tmg_res_list = tmg.search_devices(device_list)
        >>> len(tmg_res_list)
        3
        """
        tmg_results = []
        for device in search_devices:
            res = self.search_device(device)
            tmg_results.append(res)
        return tmg_results
