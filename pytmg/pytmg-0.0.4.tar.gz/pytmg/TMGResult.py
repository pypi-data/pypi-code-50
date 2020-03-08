"""
Class for results of calls to pyTMG TMG object
"""
from pytmg.TMGNetworkDevice import TMGNetworkDevice


class TMGResult:
    """
    The TMGResult object is the primary "exit point" for the pyTMG library.


    """

    def __init__(self, input_results):
        """
        Instantiates TMGResult object and parses results of Cisco's TMG API.

        The results of Cisco's TMG API are hierarchically organized so that
        network devices are at the "top" of the tree, while the transceivers
        supported on those network devices are attached to each network
        device at the bottom of the tree. For example, consider a search
        for the below devices:
        
        * N9K-C93180YC-EX
        * N9K-C9372PX
        * N9K-C9336C-FX2

        A QSFP-40G-SR4 transceiver is supported for the NX-OS operating
        system on all three of these network devices. Cisco's TMG API
        would return results structured as follows:

        Results
        +-- Network Devices
            +-- N9K-C93180YC-EX
                +-- QSFP-40G-SR
            +-- N9K-C9372PX
                +-- QSFP-40G-SR
            +-- N9K-C9336C-FX2
                +-- QSFP-40G-SR
        
        pyTMG's TMGResult class mimics this hierarchy. The full output of
        Cisco's TMG API is accessible via the "result" attribute. The
        total number of network devices contained in the results is accessible
        via the "total_count" attribute. The "network_devices" attribute
        contains a list of network devices that match the search parameters.

        Each network device in the "network_devices" list attribute is an
        object of TMGNetworkDevice. The hierarchy of transceivers that
        match the search parameters are organized under each TMGNetworkDevice
        object.

        :param dict input_results: A dictionary containing the results of a TMG
            object's search against Cisco's TMG API.
        """
        self.result = input_results
        self.total_count = int(self.result["totalCount"])
        self.network_devices = []
        for product_family in self.result["networkDevices"]:
            for network_device in product_family["networkAndTransceiverCompatibility"]:
                self.network_devices.append(
                    TMGNetworkDevice(
                        network_device,
                        product_family["productFamily"],
                        product_family["networkFamilyDataSheet"],
                    )
                )
