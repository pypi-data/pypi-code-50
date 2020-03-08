import pytest
import json
from pytmg.TMGTransceiver import TMGTransceiver


def test_tmg_transceiver_init_valid_data():
    input_data = """{
        "tmgId": 24739,
        "productFamilyId": 5,
        "productFamily": "QSFP100",
        "productModelId": 1,
        "productId": "QSFP-100G-SR4-S",
        "version": " ",
        "versionId": null,
        "description": null,
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
        "transceiverNotes": null,
        "noteCount": 0,
        "state": null,
        "stateMessage": null,
        "updatedOn": null,
        "updatedBy": null,
        "transceiverBusinessUnit": "TMG",
        "networkModelId": 43,
        "breakoutMode": " ",
        "osType": "ACI",
        "domSupport": "ACI",
        "softReleaseMinVer": "ACI-N9KDK9-11.3(2)",
        "networkDeviceNotes": null,
        "releaseId": 1061,
        "softReleaseDOM": "ACI-N9KDK9-11.3(2)",
        "type": "Optic"
    }"""
    xcvr = TMGTransceiver(json.loads(input_data))
    assert xcvr is not None
    assert xcvr.tmg_id == 24739
    assert xcvr.product_family_id == 5
    assert xcvr.product_family == "QSFP100"
    assert xcvr.product_model_id == 1
    assert xcvr.product_id == "QSFP-100G-SR4-S"
    assert xcvr.version == " "
    assert xcvr.version_id is None
    assert xcvr.description is None
    assert xcvr.form_factor == "QSFP28"
    assert xcvr.reach == "100m (OM4)"
    assert xcvr.temperature_range == "0 to 70C"
    assert xcvr.digital_diagnostic == "Y"
    assert xcvr.cable_type == "Ribbon Fiber"
    assert xcvr.media == "MMF"
    assert xcvr.connector_type == "MPO-12"
    assert xcvr.transmission_standard == " "
    assert (
        xcvr.transceiver_model_data_sheet
        == "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/datasheet-c78-736282.html"
    )
    assert xcvr.end_of_sale == " "
    assert xcvr.data_rate == "100 Gbps"
    assert xcvr.transceiver_notes is None
    assert xcvr.note_count == 0
    assert xcvr.state is None
    assert xcvr.state_message is None
    assert xcvr.updated_on is None
    assert xcvr.updated_by is None
    assert xcvr.transceiver_business_unit == "TMG"
    assert xcvr.network_model_id == 43
    assert xcvr.breakout_mode == " "
    assert xcvr.os_type == "ACI"
    assert xcvr.dom_support == "ACI"
    assert xcvr.soft_release_min_ver == "ACI-N9KDK9-11.3(2)"
    assert xcvr.network_device_notes is None
    assert xcvr.release_id == 1061
    assert xcvr.soft_release_dom == "ACI-N9KDK9-11.3(2)"
    assert xcvr.type == "Optic"


def test_tmg_transceiver_clean_aci_11_sw_release():
    input_data = """{
        "tmgId": 24739,
        "productFamilyId": 5,
        "productFamily": "QSFP100",
        "productModelId": 1,
        "productId": "QSFP-100G-SR4-S",
        "version": " ",
        "versionId": null,
        "description": null,
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
        "transceiverNotes": null,
        "noteCount": 0,
        "state": null,
        "stateMessage": null,
        "updatedOn": null,
        "updatedBy": null,
        "transceiverBusinessUnit": "TMG",
        "networkModelId": 43,
        "breakoutMode": " ",
        "osType": "ACI",
        "domSupport": "ACI",
        "softReleaseMinVer": "ACI-N9KDK9-11.3(2)",
        "networkDeviceNotes": null,
        "releaseId": 1061,
        "softReleaseDOM": "ACI-N9KDK9-11.3(2)",
        "type": "Optic"
    }"""
    xcvr = TMGTransceiver(json.loads(input_data))
    assert xcvr is not None
    assert xcvr.clean_soft_release_min_ver == "11.3(2)"


def test_tmg_transceiver_clean_aci_14_sw_release():
    input_data = """{
        "tmgId": 24739,
        "productFamilyId": 5,
        "productFamily": "QSFP100",
        "productModelId": 1,
        "productId": "QSFP-100G-SR4-S",
        "version": " ",
        "versionId": null,
        "description": null,
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
        "transceiverNotes": null,
        "noteCount": 0,
        "state": null,
        "stateMessage": null,
        "updatedOn": null,
        "updatedBy": null,
        "transceiverBusinessUnit": "TMG",
        "networkModelId": 43,
        "breakoutMode": " ",
        "osType": "ACI",
        "domSupport": "ACI",
        "softReleaseMinVer": "ACI-N9KDK9-14.1(1)",
        "networkDeviceNotes": null,
        "releaseId": 1061,
        "softReleaseDOM": "ACI-N9KDK9-14.1(1)",
        "type": "Optic"
    }"""
    xcvr = TMGTransceiver(json.loads(input_data))
    assert xcvr is not None
    assert xcvr.clean_soft_release_min_ver == "14.1(1)"


def test_tmg_transceiver_clean_nxos_7_sw_release():
    input_data = """{
        "tmgId": 24740,
        "productFamilyId": 5,
        "productFamily": "QSFP100",
        "productModelId": 1,
        "productId": "QSFP-100G-SR4-S",
        "version": " ",
        "versionId": null,
        "description": null,
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
        "transceiverNotes": null,
        "noteCount": 0,
        "state": null,
        "stateMessage": null,
        "updatedOn": null,
        "updatedBy": null,
        "transceiverBusinessUnit": "TMG",
        "networkModelId": 43,
        "breakoutMode": " ",
        "osType": "NX-OS",
        "domSupport": "NX-OS",
        "softReleaseMinVer": "NX-OS 7.03I4.2",
        "networkDeviceNotes": null,
        "releaseId": 552,
        "softReleaseDOM": "NX-OS 7.03I4.2",
        "type": "Optic"
    }"""
    xcvr = TMGTransceiver(json.loads(input_data))
    assert xcvr is not None
    assert xcvr.clean_soft_release_min_ver == "7.0(3)I4(2)"


def test_tmg_transceiver_clean_nxos_9_sw_release():
    input_data = """{
        "tmgId": 24740,
        "productFamilyId": 5,
        "productFamily": "QSFP100",
        "productModelId": 1,
        "productId": "QSFP-100G-SR4-S",
        "version": " ",
        "versionId": null,
        "description": null,
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
        "transceiverNotes": null,
        "noteCount": 0,
        "state": null,
        "stateMessage": null,
        "updatedOn": null,
        "updatedBy": null,
        "transceiverBusinessUnit": "TMG",
        "networkModelId": 43,
        "breakoutMode": " ",
        "osType": "NX-OS",
        "domSupport": "NX-OS",
        "softReleaseMinVer": "NX-OS 9.2.1",
        "networkDeviceNotes": null,
        "releaseId": 552,
        "softReleaseDOM": "NX-OS 9.2.1",
        "type": "Optic"
    }"""
    xcvr = TMGTransceiver(json.loads(input_data))
    assert xcvr is not None
    assert xcvr.clean_soft_release_min_ver == "9.2(1)"
