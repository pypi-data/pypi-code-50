import pytest
from pytmg import TMGNetworkDevice


def test_tmg_network_device_init():
    test_product_family = "N9300"
    test_datasheet = "https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/datasheet-c78-741560.html"
    test_network_device_input = {
        "productId": "N9K-C93180YC-EX",
        "transceivers": [
            {
                "tmgId": 24739,
                "productFamilyId": 5,
                "productFamily": "QSFP100",
                "productModelId": 1,
                "productId": "QSFP-100G-SR4-S",
                "version": " ",
                "versionId": None,
                "description": None,
                "formFactor": "QSFP28",
                "reach": "100m (OM4)",
                "temperatureRange": "0 to 70C",
                "digitalDiagnostic": "Y",
                "cableType": "Ribbon Fiber",
                "media": "MMF",
                "connectorType": "MPO-12",
                "transmissionStandard": " ",
                "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/datasheet-c78-736282.html",
                "endOfSale": " ",
                "dataRate": "100 Gbps",
                "transceiverNotes": None,
                "noteCount": 0,
                "state": None,
                "stateMessage": None,
                "updatedOn": None,
                "updatedBy": None,
                "transceiverBusinessUnit": "TMG",
                "networkModelId": 43,
                "breakoutMode": " ",
                "osType": "ACI",
                "domSupport": "ACI",
                "softReleaseMinVer": "ACI-N9KDK9-11.3(2)",
                "networkDeviceNotes": None,
                "releaseId": 1061,
                "softReleaseDOM": "ACI-N9KDK9-11.3(2)",
                "type": "Optic",
            },
            {
                "tmgId": 24740,
                "productFamilyId": 5,
                "productFamily": "QSFP100",
                "productModelId": 1,
                "productId": "QSFP-100G-SR4-S",
                "version": " ",
                "versionId": None,
                "description": None,
                "formFactor": "QSFP28",
                "reach": "100m (OM4)",
                "temperatureRange": "0 to 70C",
                "digitalDiagnostic": "Y",
                "cableType": "Ribbon Fiber",
                "media": "MMF",
                "connectorType": "MPO-12",
                "transmissionStandard": " ",
                "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/datasheet-c78-736282.html",
                "endOfSale": " ",
                "dataRate": "100 Gbps",
                "transceiverNotes": None,
                "noteCount": 0,
                "state": None,
                "stateMessage": None,
                "updatedOn": None,
                "updatedBy": None,
                "transceiverBusinessUnit": "TMG",
                "networkModelId": 43,
                "breakoutMode": " ",
                "osType": "NX-OS",
                "domSupport": "NX-OS",
                "softReleaseMinVer": "NX-OS 7.03I4.2",
                "networkDeviceNotes": None,
                "releaseId": 552,
                "softReleaseDOM": "NX-OS 7.03I4.2",
                "type": "Optic",
            },
        ],
    }
    tmg_net_dev = TMGNetworkDevice.TMGNetworkDevice(
        test_network_device_input, test_product_family, test_datasheet
    )
    assert tmg_net_dev is not None
    assert tmg_net_dev.result == test_network_device_input
    assert tmg_net_dev.product_family == test_product_family
    assert tmg_net_dev.network_family_data_sheet == test_datasheet
    assert len(tmg_net_dev.transceivers) == 2
    first_xcvr = tmg_net_dev.transceivers[0]
    second_xcvr = tmg_net_dev.transceivers[1]
    assert first_xcvr.product_id == "QSFP-100G-SR4-S"
    assert second_xcvr.product_id == "QSFP-100G-SR4-S"
