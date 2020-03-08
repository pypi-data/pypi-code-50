"""
Class representing a Cisco-branded transceiver based upon results of Cisco TMG
API
"""
import re


class TMGTransceiver:
    """
    An object that represents a Cisco-branded transceiver within the context of
    Cisco's TMG API.

    """

    def __init__(self, input):
        """
        Instantiates TMGTransceiver object and parses relevant results of 
        Cisco's TMG API.

        Cisco's TMG API links specific PIDs/models of transceivers to network
        devices to indicate support. Furthermore, information about how a
        transceiver is supported (such as operating system version,
        environmental factors such as temperature range, etc.) is included.

        :param dict input: A dictionary containing the results of a TMG object 
            search against Cisco TMG's API relevant to a specific
            transceiver
        """
        self.result = input
        self.tmg_id = self.result["tmgId"]
        self.product_family_id = self.result["productFamilyId"]
        self.product_family = self.result["productFamily"]
        self.product_model_id = self.result["productModelId"]
        self.product_id = self.result["productId"]
        self.version = self.result["version"]
        self.version_id = self.result["versionId"]
        self.description = self.result["description"]
        self.form_factor = self.result["formFactor"]
        self.reach = self.result["reach"]
        self.temperature_range = self.result["temperatureRange"]
        self.digital_diagnostic = self.result["digitalDiagnostic"]
        self.cable_type = self.result["cableType"]
        self.media = self.result["media"]
        self.connector_type = self.result["connectorType"]
        self.transmission_standard = self.result["transmissionStandard"]
        self.transceiver_model_data_sheet = self.result["transceiverModelDataSheet"]
        self.end_of_sale = self.result["endOfSale"]
        self.data_rate = self.result["dataRate"]
        self.transceiver_notes = self.result["transceiverNotes"]
        self.note_count = self.result["noteCount"]
        self.state = self.result["state"]
        self.state_message = self.result["stateMessage"]
        self.updated_on = self.result["updatedOn"]
        self.updated_by = self.result["updatedBy"]
        self.transceiver_business_unit = self.result["transceiverBusinessUnit"]
        self.network_model_id = self.result["networkModelId"]
        self.breakout_mode = self.result["breakoutMode"]
        self.os_type = self.result["osType"]
        self.dom_support = self.result["domSupport"]
        self.soft_release_min_ver = self.result["softReleaseMinVer"]
        self.network_device_notes = self.result["networkDeviceNotes"]
        self.release_id = self.result["releaseId"]
        self.soft_release_dom = self.result["softReleaseDOM"]
        self.type = self.result["type"]
        self.clean_soft_release_min_ver = self._clean_soft_release()

    def _clean_soft_release(self):
        """
        Normalize network device software release provided by Cisco's TMG API.

        Cisco's TMG API sometimes presents network device software releases
        in a format that is inconsistent with the "official" format. The
        purpose of this method is to attempt to normalize the software
        release format presented by Cisco's TMG API to allow better
        interoperability.

        Currently, the below operating systems are supported:

        * Full Support:

        * Partial Support:
          - ACI
          - NX-OS
        """
        if self.os_type == "ACI":
            return self._clean_aci_soft_release()
        elif self.os_type == "NX-OS":
            return self._clean_nxos_soft_release()
        else:
            # Return "dirty" software release, which is better than nothing
            return self.soft_release_min_ver

    def _clean_aci_soft_release(self):
        """
        Normalize Cisco ACI network device software releases provided by
        Cisco's TMG API.

        Most Cisco-branded transceivers supported by ACI software return
        with a softReleaseMinVer format as follows:

            ACI-N9KDK9-11.3(2)

        The desired format is as follows:

            11.3(2)

        This method converts the first format into the second format.
        This is done by simply replacing the "ACI-N9KDK9-" substring in 
        the softReleaseMinVer value.
        """
        if "ACI-N9KDK9-" in self.soft_release_min_ver:
            return self.soft_release_min_ver.replace("ACI-N9KDK9-", "")

    def _clean_nxos_soft_release(self):
        """
        Normalize Cisco NX-OS network device software releases provided by
        Cisco's TMG API.

        Most Cisco-branded transceivers supported by NX-OS software return
        with a softReleaseMinVer format as follows:

            NX-OS 7.03I4.2

        The desired format is as follows:

            7.0(3)I4(2)

        This method converts the first format into the second format with 
        a regex string identifying:
        1. The major release (7.0(3)) (not part of a capture group)
        2. The minor release (I4) (capture group 1)
        3. The maintenance release (2) (capture group 2)

        Supported transceivers introduced in 9.x NX-OS software releases have
        a softReleaseMinVer format as follows:

            NX-OS 9.2.1

        The desired format is as follows:

            9.2(1)
        
        This method converts the first format into the second format with a
        regex string identifying:
        1. The minor release (2) (capture group 1)
        2. The maintenance release (1) (capture group 2)
        """
        if "NX-OS" in self.soft_release_min_ver:
            nxos_7_dirty_re = r"NX-OS 7.03I(\d+)\.(\d+)"
            nxos_7_res = re.search(nxos_7_dirty_re, self.soft_release_min_ver)
            if nxos_7_res:
                mnr_rel = nxos_7_res.group(1)
                mnt_rel = nxos_7_res.group(2)
                clean_sw_rel = "7.0(3)I{}({})".format(mnr_rel, mnt_rel)
                return clean_sw_rel
            nxos_9_dirty_re = r"NX-OS 9.(\d+)\.(\d+)"
            nxos_9_res = re.search(nxos_9_dirty_re, self.soft_release_min_ver)
            if nxos_9_res:
                mnr_rel = nxos_9_res.group(1)
                mnt_rel = nxos_9_res.group(2)
                clean_sw_rel = "9.{}({})".format(mnr_rel, mnt_rel)
                return clean_sw_rel
