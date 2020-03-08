"""
Class representing a Cisco network device based upon results of Cisco TMG API
"""
from pytmg.TMGTransceiver import TMGTransceiver


class TMGNetworkDevice:
    """
    An object that represents a Cisco network device within the context of
    Cisco's TMG API.

    
    """

    def __init__(self, input, product_family, network_family_data_sheet):
        """
        Instantiates TMGNetworkDevice object and parses relevant results of Cisco's
        TMG API.

        The results of Cisco's TMG API are hierarchically organized so that each
        network device is directly associated with a list of supported
        transceivers. When searching in Cisco's TMG API, only transceivers and/or
        network devices that match the user-defined search parameters are returned
        as results.

        pyTMG's TMGNetworkDevice class mimics this hierarchy. The raw output of the
        relevant Cisco TMG API elements is accessible via the "result" attribute.
        The product family for the network device is accessible via the
        "product_family" attribute, and the relevant Cisco data sheet documentation
        is accessible via the "network_family_data_sheet" attribute.

        A list of supported transceivers that match the user-defined search
        parameters are accessible via a list in the "transceivers" attribute.
        Each object in this list is of the TMGTransceiver class.

        :param dict input: A dictionary containing the results of a TMG object 
            search against Cisco TMG's API relevant to a specific network
            device
        """
        self.result = input
        self.product_id = self.result["productId"]
        self.product_family = product_family
        self.network_family_data_sheet = network_family_data_sheet
        self.transceivers = []
        for transceiver in self.result["transceivers"]:
            self.transceivers.append(TMGTransceiver(transceiver))
