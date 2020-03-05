import pytest
import responses
import json
from pytmg import TMG
from pytmg import TMGResult
from .models import test_TMG_models


def test_tmg_init():
    tmg = TMG.TMG()
    assert tmg is not None


class TestPrivateSearchMethodSimple:
    @responses.activate
    def test_tmg_private_search_for_n9k_93180yc_ex(self):
        resp_json = test_TMG_models.N9K_C93180YC_EX_MODEL
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg._search(search_input=["N9K-C93180YC-EX"])
        assert res is not None
        assert (
            res["networkDevices"][0]["networkAndTransceiverCompatibility"][0][
                "productId"
            ]
            == "N9K-C93180YC-EX"
        )

    @responses.activate
    def test_tmg_private_search_for_n9k_9372px(self):
        resp_json = test_TMG_models.N9K_C9372PX_MODEL
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg._search(search_input=["N9K-C9372PX"])
        assert res is not None
        assert (
            res["networkDevices"][0]["networkAndTransceiverCompatibility"][0][
                "productId"
            ]
            == "N9K-C9372PX"
        )
        assert (
            res["networkDevices"][0]["networkAndTransceiverCompatibility"][1][
                "productId"
            ]
            == "N9K-C9372PX-E"
        )

    @responses.activate
    def test_tmg_private_search_for_ws_c3750_24ps(self):
        resp_json = test_TMG_models.WS_C3750_24PS_MODEL
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg._search(search_input=["WS-C3750-24PS"])
        assert res is not None
        assert (
            res["networkDevices"][0]["networkAndTransceiverCompatibility"][0][
                "productId"
            ]
            == "WS-C3750-24PS"
        )

    @responses.activate
    def test_tmg_private_search_for_all_3750s(self):
        resp_json = test_TMG_models.ALL_3750S_MODEL
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg._search(search_input=["WS-C3750"])
        assert res is not None
        product_list = [
            dev["productId"]
            for dev in res["networkDevices"][0]["networkAndTransceiverCompatibility"]
        ]
        product_list += [
            dev["productId"]
            for dev in res["networkDevices"][1]["networkAndTransceiverCompatibility"]
        ]
        assert "WS-C3750G-16TD" in product_list
        assert "WS-C3750-24PS" in product_list
        assert "WS-C3750-24TS" in product_list
        assert "WS-C3750-48PS" in product_list
        assert "WS-C3750-48TS" in product_list
        assert "WS-C3750G-12S" in product_list
        assert "WS-C3750G-24PS" in product_list
        assert "WS-C3750G-24TS" in product_list
        assert "WS-C3750G-24TS-E1U" in product_list
        assert "WS-C3750G-24TS-S1U" in product_list
        assert "WS-C3750G-48PS" in product_list
        assert "WS-C3750G-48TS" in product_list
        assert "WS-C3750-24FS-S" in product_list
        assert "WS-C3750V2-24PS" in product_list
        assert "WS-C3750V2-24TS" in product_list
        assert "WS-C3750V2-48PS" in product_list
        assert "WS-C3750V2-48TS" in product_list
        assert "WS-C3750V2-24FS-S" in product_list
        assert "WS-C3750E-24TD" in product_list
        assert "WS-C3750E-24PD" in product_list
        assert "WS-C3750E-48TD" in product_list
        assert "WS-C3750E-48PD" in product_list
        assert "WS-C3750E-48PDF" in product_list
        assert "WS-C3750X-12S" in product_list
        assert "WS-C3750X-24S" in product_list
        assert "WS-C3750-24WFS" in product_list
        assert "WS-C3750V2-24FS" in product_list
        assert "WS-C3750X-24T" in product_list
        assert "WS-C3750X-48T" in product_list
        assert "WS-C3750X-24P" in product_list
        assert "WS-C3750X-48P" in product_list
        assert "WS-C3750X-48PF" in product_list
        assert "WS-C3750X-12S" in product_list
        assert "WS-C3750X-24S" in product_list

    @responses.activate
    def test_tmg_private_search_for_xcvr_qsfp_40g_sr_bd(self):
        resp_json = test_TMG_models.XCVR_QSFP_40G_SR_BD
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg._search(search_input=["QSFP-40G-SR-BD"])
        assert res is not None
        assert res["totalCount"] == "33"
        assert res["networkDevices"] is not None
        assert len(res["networkDevices"]) == 1
        product_list = [
            dev["productId"]
            for dev in res["networkDevices"][0]["networkAndTransceiverCompatibility"]
        ]
        assert "C9400-SUP-1" in product_list
        assert "C9400-SUP-1XL" in product_list
        assert "C9400-SUP-1XL-Y" in product_list

        devices = res["networkDevices"][0]["networkAndTransceiverCompatibility"]
        for device in devices:
            for xcvr in device["transceivers"]:
                assert xcvr["productId"] == "QSFP-40G-SR-BD"


class TestDeviceSearchingSimple:
    @responses.activate
    def test_tmg_search_for_n9k_93180yc_ex(self):
        resp_json = test_TMG_models.N9K_C93180YC_EX_MODEL
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg.search_device("N9K-C93180YC-EX")
        assert res is not None
        assert res.network_devices[0].product_id == "N9K-C93180YC-EX"

    @responses.activate
    def test_tmg_search_for_n9k_9372px(self):
        resp_json = test_TMG_models.N9K_C9372PX_MODEL
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg.search_device("N9K-C9372PX")
        assert res is not None
        assert res.network_devices[0].product_id == "N9K-C9372PX"

    @responses.activate
    def test_tmg_search_for_ws_c3750_24ps(self):
        resp_json = test_TMG_models.WS_C3750_24PS_MODEL
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg.search_device("WS-C3750-24PS")
        assert res is not None
        assert res.network_devices[0].product_id == "WS-C3750-24PS"

    @responses.activate
    def test_tmg_search_all_3750s(self):
        resp_json = test_TMG_models.ALL_3750S_MODEL
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg.search_device("WS-C3750")
        assert res is not None
        assert len(res.network_devices) > 1
        # Verify expected products are in returned list
        product_list = [dev.product_id for dev in res.network_devices]
        assert "WS-C3750G-16TD" in product_list
        assert "WS-C3750-24PS" in product_list
        assert "WS-C3750-24TS" in product_list
        assert "WS-C3750-48PS" in product_list
        assert "WS-C3750-48TS" in product_list
        assert "WS-C3750G-12S" in product_list
        assert "WS-C3750G-24PS" in product_list
        assert "WS-C3750G-24TS" in product_list
        assert "WS-C3750G-24TS-E1U" in product_list
        assert "WS-C3750G-24TS-S1U" in product_list
        assert "WS-C3750G-48PS" in product_list
        assert "WS-C3750G-48TS" in product_list
        assert "WS-C3750-24FS-S" in product_list
        assert "WS-C3750V2-24PS" in product_list
        assert "WS-C3750V2-24TS" in product_list
        assert "WS-C3750V2-48PS" in product_list
        assert "WS-C3750V2-48TS" in product_list
        assert "WS-C3750V2-24FS-S" in product_list
        assert "WS-C3750E-24TD" in product_list
        assert "WS-C3750E-24PD" in product_list
        assert "WS-C3750E-48TD" in product_list
        assert "WS-C3750E-48PD" in product_list
        assert "WS-C3750E-48PDF" in product_list
        assert "WS-C3750X-12S" in product_list
        assert "WS-C3750X-24S" in product_list
        assert "WS-C3750-24WFS" in product_list
        assert "WS-C3750V2-24FS" in product_list
        assert "WS-C3750X-24T" in product_list
        assert "WS-C3750X-48T" in product_list
        assert "WS-C3750X-24P" in product_list
        assert "WS-C3750X-48P" in product_list
        assert "WS-C3750X-48PF" in product_list
        assert "WS-C3750X-12S" in product_list
        assert "WS-C3750X-24S" in product_list

    @responses.activate
    def test_tmg_search_xcvr_qsfp_40g_sr_bd(self):
        resp_json = test_TMG_models.XCVR_QSFP_40G_SR_BD
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg.search_device("QSFP-40G-SR-BD")
        assert res is not None
        assert len(res.network_devices) == 3
        assert res.network_devices[0].product_id == "C9400-SUP-1"
        assert res.network_devices[1].product_id == "C9400-SUP-1XL"
        assert res.network_devices[2].product_id == "C9400-SUP-1XL-Y"
        for device in res.network_devices:
            for xcvr in device.transceivers:
                assert xcvr.product_id == "QSFP-40G-SR-BD"

    @responses.activate
    def test_tmg_search_multiple_devices(self):
        def tmg_callback(request):
            payload = json.loads(request.body)
            if payload["searchInput"][0] == "N9K-C93180YC-FX":
                resp_json = test_TMG_models.N9K_C93180YC_FX_MODEL
                return (
                    200,
                    {"content-type": "application/json"},
                    json.dumps(resp_json),
                )
            elif payload["searchInput"][0] == "C9300-48S":
                resp_json = test_TMG_models.C9300_48S_MODEL
                return (
                    200,
                    {"content-type": "application/json"},
                    json.dumps(resp_json),
                )
            elif payload["searchInput"][0] == "2951":
                resp_json = test_TMG_models.ISR2951_MODEL
                return (
                    200,
                    {"content-type": "application/json"},
                    json.dumps(resp_json),
                )
            else:
                return (503, {}, None)

        responses.add_callback(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            callback=tmg_callback,
            content_type="application/json",
        )

        device_list = [
            "N9K-C93180YC-FX",  # Nexus 93180YC-FX
            "C9300-48S",  # Catalyst 9300-48S
            "2951",  # ISR 2951
        ]
        tmg = TMG.TMG()
        res_list = tmg.search_devices(device_list)
        assert res_list is not None
        assert len(res_list) == 3
        for result in res_list:
            for result_device in result.network_devices:
                assert result_device.product_id in device_list


class TestPrivateSearchMethodAdvanced:
    @responses.activate
    def test_tmg_private_search_advanced_ios_xe_fet_10g(self):
        resp_json = test_TMG_models.ADV_SEARCH_IOS_XE_FET_10G_MODEL
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg._search(
            cable_type=["Duplex Fiber"],
            data_rate=["10 Gbps"],
            form_factor=["SFP+"],
            reach=["100m"],
            os_type=["IOS XE"],
        )
        assert res is not None
        assert int(res["totalCount"]) >= 2
        devices = res["networkDevices"]

        # Verify product families
        assert devices[0]["productFamily"] == "C9300"
        assert devices[1]["productFamily"] == "C9300L"

        # Verify device PIDs
        dev_one = devices[0]["networkAndTransceiverCompatibility"][0]
        dev_two = devices[1]["networkAndTransceiverCompatibility"][0]
        dev_three = devices[1]["networkAndTransceiverCompatibility"][1]
        dev_four = devices[1]["networkAndTransceiverCompatibility"][2]
        dev_five = devices[1]["networkAndTransceiverCompatibility"][3]
        assert dev_one["productId"] == "C9300-NM-8X"
        assert dev_two["productId"] == "C9300L-24T-4X"
        assert dev_three["productId"] == "C9300L-48T-4X"
        assert dev_four["productId"] == "C9300L-24P-4X"
        assert dev_five["productId"] == "C9300L-48P-4X"

        # Verify each device's transceivers
        dev_one["transceivers"][0]["productId"] == "FET-10G"
        dev_two["transceivers"][0]["productId"] == "FET-10G"
        dev_three["transceivers"][0]["productId"] == "FET-10G"
        dev_four["transceivers"][0]["productId"] == "FET-10G"
        dev_five["transceivers"][0]["productId"] == "FET-10G"

    @responses.activate
    def test_tmg_private_search_advanced_ucs_xr_1gbps(self):
        resp_json = test_TMG_models.ADV_SEARCH_UCS_XR_1GBPS_MODEL
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg._search(
            cable_type=["Cat5e/6A"],
            data_rate=["10/100/1000 Mbps"],
            form_factor=["SFP"],
            reach=["100m"],
            os_type=["IOS XR", "UCS"],
        )
        assert res is not None
        assert int(res["totalCount"]) >= 5
        devices = res["networkDevices"]

        # Verify product families
        assert devices[0]["productFamily"] == "UCSB"
        assert devices[1]["productFamily"] == "NCS5000"
        assert devices[2]["productFamily"] == "NCS5500"
        assert devices[3]["productFamily"] == "ASR9000"
        assert devices[4]["productFamily"] == "NCS540"

        # Verify device PIDs
        expected_devices = [
            "UCS-FI-M-6324",
            "UCS-FI-6332-U",
            "UCS-FI-6332-16UP-U",
            "N10-S6100",
            "N10-S6200",
            "N10-E0440",
            "N10-E0600",
            "N20-I6584",
            "UCS-FI-6248UP",
            "UCS-FI-E16UP",
            "UCS-IOM-2208XP",
            "UCS-FI-6454",
            "NCS 5001",
            "NCS 5002",
            "NC55-24H12F-SE",
            "NCS-5501",
            "NCS-5501-SE",
            "NC55-MOD-A-S",
            "NCS-55A2-MOD-S",
            "NC55-MOD-A-SE-S",
            "NCS-55A2-MOD-HD-S",
            "NCS-55A2-MOD-SE-S",
            "NCS-55A2-MOD-HX-S",
            "NCS-55A2-MOD-SE-H-S",
            "A9K-40GE-B",
            "A9K-40GE-E",
            "A9K-2T20GE-B",
            "A9K-2T20GE-E",
            "A9K-2T20GE-L",
            "A9K-40GE-L",
            "A9K-MPA-20X1GE",
            "A9K-40GE-TR",
            "A9K-40GE-SE",
            "A9K-4T16GE-TR",
            "A9K-4T16GE-SE",
            "A9K-RSP440-TR",
            "A9K-RSP440-SE",
            "ASR-9000V-AC",
            "ASR-9000V-DC-A",
            "ASR-9000V-DC-E",
            "ASR-9000V-24-A",
            "A9KV-V2-AC",
            "A9KV-V2-DC-A",
            "A9KV-V2-DC-E",
            "A9K-24X10GE-1G-SE",
            "A9K-24X10GE-1G-TR",
            "A9K-48X10GE-1G-SE",
            "A9K-48X10GE-1G-TR",
            "A9K-RSP440-LT",
            "A99-48X10GE-1G-SE",
            "A99-48X10GE-1G-TR",
            "N540-24Z8Q2C-SYS",
            "N540-ACC-SYS",
            "N540X-ACC-SYS",
            "N540-24Z8Q2C-M",
        ]
        for pf in devices:
            for dev in pf["networkAndTransceiverCompatibility"]:
                assert dev["productId"] in expected_devices

        # Verify supported transceivers
        for pf in devices:
            for dev in pf["networkAndTransceiverCompatibility"]:
                for xcvr in dev["transceivers"]:
                    assert xcvr["cableType"] == "Cat5e/6A"
                    assert xcvr["dataRate"] == "10/100/1000 Mbps"
                    assert xcvr["reach"] == "100m"
                    assert xcvr["formFactor"] == "SFP"
                    assert xcvr["osType"] == "UCS" or xcvr["osType"] == "IOS XR"
                    assert (
                        xcvr["productId"] == "GLC-T"
                        or xcvr["productId"] == "GLC-TE"
                        or xcvr["productId"] == "SFP-GE-T"
                    )


class TestDeviceSearchingAdvanced:
    @responses.activate
    def test_tmg_search_advanced_ios_xe_fet_10g(self):
        resp_json = test_TMG_models.ADV_SEARCH_IOS_XE_FET_10G_MODEL
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        params = {
            "cable_type": ["Duplex Fiber"],
            "data_rate": ["10 Gbps"],
            "form_factor": ["SFP+"],
            "reach": ["100m"],
            "os_type": ["IOS XE"],
        }
        res = tmg.search(**params)
        assert res is not None
        assert res.total_count >= 2

        # Verify product families
        assert res.network_devices[0].product_family == "C9300"
        assert res.network_devices[1].product_family == "C9300L"

        # Verify device PIDs
        assert res.network_devices[0].product_id == "C9300-NM-8X"
        assert res.network_devices[1].product_id == "C9300L-24T-4X"
        assert res.network_devices[2].product_id == "C9300L-48T-4X"
        assert res.network_devices[3].product_id == "C9300L-24P-4X"
        assert res.network_devices[4].product_id == "C9300L-48P-4X"

        # Verify each device's transceivers
        assert res.network_devices[0].transceivers[0].product_id == "FET-10G"
        assert res.network_devices[1].transceivers[0].product_id == "FET-10G"
        assert res.network_devices[2].transceivers[0].product_id == "FET-10G"
        assert res.network_devices[3].transceivers[0].product_id == "FET-10G"
        assert res.network_devices[4].transceivers[0].product_id == "FET-10G"
