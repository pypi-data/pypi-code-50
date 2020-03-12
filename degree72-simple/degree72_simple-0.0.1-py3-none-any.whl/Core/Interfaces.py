class JobTools:
    """
        Such as the title
    """

    def __init__(self):
        """
            [log]: log
            [dao]: For db
            [ap]: For json auto build
            [proxy_instance]: For proxy's setting as quick as possbile
        """
        self.log = None
        self.dao = None
        self._ap = None
        self._proxy_instance = None

    @property
    def proxy(self):
        return self._proxy_instance.proxy_point_pool

    @proxy.setter
    def proxy(self, p):
        self._proxy_instance.set_proxies_pool(p)

    """
        Proxy local
    """

    @property
    def NONE_PROXY(self):
        return self._proxy_instance.NONE_PROXY

    @property
    def LOCALHOST(self):
        return self._proxy_instance.LOCALHOST

    @property
    def LOCAL_PROXY_P1(self):
        return self._proxy_instance.LOCAL_PROXY_P1

    @property
    def LOCAL_PROXY_P2(self):
        return self._proxy_instance.LOCAL_PROXY_P2

    # @property
    # def LOCAL_PROXY_P3(self):
    #     return self._proxy_instance.LOCAL_PROXY_P3

    @property
    def LOCAL_PROXY_P4(self):
        return self._proxy_instance.LOCAL_PROXY_P4

    @property
    def LOCAL_PROXY_P5(self):
        return self._proxy_instance.LOCAL_PROXY_P5

    # @property
    # def LOCAL_PROXY_P6(self):
    #     return self._proxy_instance.LOCAL_PROXY_P6

    # @property
    # def LOCAL_PROXY_D1(self):
    #     return self._proxy_instance.LOCAL_PROXY_D1

    @property
    def PROXY_P6(self):
        return self._proxy_instance.PROXY_P6

    """
        Proxy server
    """

    @property
    def PROXY_NODE_N0(self):
        return self._proxy_instance.PROXY_NODE_N0

    @property
    def PROXY_NODE_N25(self):
        return self._proxy_instance.PROXY_NODE_N25

    @property
    def PROXY_NODE_ST0(self):
        return self._proxy_instance.PROXY_NODE_ST0

    @property
    def PROXY_NODE_ST25(self):
        return self._proxy_instance.PROXY_NODE_ST25

    @property
    def PROXY_U1_NS_ALL(self):
        return self._proxy_instance.PROXY_U1_NS_ALL

    @property
    def PROXY_U1_NS_25(self):
        return self._proxy_instance.PROXY_U1_NS_25

    # @property
    # def PROXY_NODE_P1(self):
    #     return self._proxy_instance.PROXY_NODE_P1

    # @property
    # def PROXY_NODE_P2(self):
    #     return self._proxy_instance.PROXY_NODE_P2

    # @property
    # def PROXY_NODE_P5(self):
    #     return self._proxy_instance.PROXY_NODE_P5

    # @property
    # def PROXY_NODE_D1(self):
    #     return self._proxy_instance.PROXY_NODE_D1

    @property
    def PROXY_SQUID_LUMI(self):
        return self._proxy_instance.PROXY_SQUID_LUMI

    @property
    def PROXY_SQUID_LUMI2(self):
        return self._proxy_instance.PROXY_SQUID_LUMI2

    """
        The proxy for different country
    """

    @property
    def PROXY_SQUID_US_0(self):
        return self._proxy_instance.PROXY_SQUID_US_0

    @property
    def PROXY_SQUID_IN_0(self):
        return self._proxy_instance.PROXY_SQUID_IN_0

    @property
    def PROXY_SQUID_ID_0(self):
        return self._proxy_instance.PROXY_SQUID_ID_0

    @property
    def PROXY_SQUID_JP_0(self):
        return self._proxy_instance.PROXY_SQUID_JP_0

    @property
    def PROXY_SQUID_MY_0(self):
        return self._proxy_instance.PROXY_SQUID_MY_0

    @property
    def PROXY_SQUID_PH_0(self):
        return self._proxy_instance.PROXY_SQUID_PH_0

    @property
    def PROXY_SQUID_SG_0(self):
        return self._proxy_instance.PROXY_SQUID_SG_0

    @property
    def PROXY_SQUID_TW_0(self):
        return self._proxy_instance.PROXY_SQUID_TW_0

    @property
    def PROXY_SQUID_TH_0(self):
        return self._proxy_instance.PROXY_SQUID_TH_0

    @property
    def PROXY_SQUID_VN_0(self):
        return self._proxy_instance.PROXY_SQUID_VN_0

    @property
    def PROXY_SQUID_AU_0(self):
        return self._proxy_instance.PROXY_SQUID_AU_0

    @property
    def PROXY_SQUID_NZ_0(self):
        return self._proxy_instance.PROXY_SQUID_NZ_0

    @property
    def PROXY_SQUID_PL_0(self):
        return self._proxy_instance.PROXY_SQUID_PL_0

    @property
    def PROXY_SQUID_RU_0(self):
        return self._proxy_instance.PROXY_SQUID_RU_0

    @property
    def PROXY_SQUID_NO_0(self):
        return self._proxy_instance.PROXY_SQUID_NO_0

    @property
    def PROXY_SQUID_BR_0(self):
        return self._proxy_instance.PROXY_SQUID_BR_0

    @property
    def PROXY_SQUID_MX_0(self):
        return self._proxy_instance.PROXY_SQUID_MX_0

    @property
    def PROXY_SQUID_ZA_0(self):
        return self._proxy_instance.PROXY_SQUID_ZA_0

    @property
    def PROXY_SQUID_CA_0(self):
        return self._proxy_instance.PROXY_SQUID_CA_0

    @property
    def PROXY_SQUID_AT_0(self):
        return self._proxy_instance.PROXY_SQUID_AT_0

    @property
    def PROXY_SQUID_BE_0(self):
        return self._proxy_instance.PROXY_SQUID_BE_0

    @property
    def PROXY_SQUID_DK_0(self):
        return self._proxy_instance.PROXY_SQUID_DK_0

    @property
    def PROXY_SQUID_FR_0(self):
        return self._proxy_instance.PROXY_SQUID_FR_0

    @property
    def PROXY_SQUID_DE_0(self):
        return self._proxy_instance.PROXY_SQUID_DE_0

    @property
    def PROXY_SQUID_IT_0(self):
        return self._proxy_instance.PROXY_SQUID_IT_0

    @property
    def PROXY_SQUID_PT_0(self):
        return self._proxy_instance.PROXY_SQUID_PT_0

    @property
    def PROXY_SQUID_ES_0(self):
        return self._proxy_instance.PROXY_SQUID_ES_0

    @property
    def PROXY_SQUID_SE_0(self):
        return self._proxy_instance.PROXY_SQUID_SE_0

    @property
    def PROXY_SQUID_TR_0(self):
        return self._proxy_instance.PROXY_SQUID_TR_0

    @property
    def PROXY_SQUID_GB_0(self):
        return self._proxy_instance.PROXY_SQUID_GB_0

    @property
    def PROXY_SQUID_AR_0(self):
        return self._proxy_instance.PROXY_SQUID_AR_0

    @property
    def PROXY_SQUID_KR_0(self):
        return self._proxy_instance.PROXY_SQUID_KR_0

    @property
    def PROXY_SQUID_IE_0(self):
        return self._proxy_instance.PROXY_SQUID_IE_0

    """
        The squid server on the lum3
    """
    @property
    def PROXY_SQUID_US_3(self):
        return self._proxy_instance.PROXY_SQUID_US_3

    @property
    def PROXY_SQUID_IN_3(self):
        return self._proxy_instance.PROXY_SQUID_IN_3

    @property
    def PROXY_SQUID_ID_3(self):
        return self._proxy_instance.PROXY_SQUID_ID_3

    @property
    def PROXY_SQUID_JP_3(self):
        return self._proxy_instance.PROXY_SQUID_JP_3

    @property
    def PROXY_SQUID_MY_3(self):
        return self._proxy_instance.PROXY_SQUID_MY_3

    @property
    def PROXY_SQUID_PH_3(self):
        return self._proxy_instance.PROXY_SQUID_PH_3

    @property
    def PROXY_SQUID_SG_3(self):
        return self._proxy_instance.PROXY_SQUID_SG_3

    @property
    def PROXY_SQUID_TW_3(self):
        return self._proxy_instance.PROXY_SQUID_TW_3

    @property
    def PROXY_SQUID_TH_3(self):
        return self._proxy_instance.PROXY_SQUID_TH_3

    @property
    def PROXY_SQUID_VN_3(self):
        return self._proxy_instance.PROXY_SQUID_VN_3

    @property
    def PROXY_SQUID_AU_3(self):
        return self._proxy_instance.PROXY_SQUID_AU_3

    @property
    def PROXY_SQUID_NZ_3(self):
        return self._proxy_instance.PROXY_SQUID_NZ_3

    @property
    def PROXY_SQUID_PL_3(self):
        return self._proxy_instance.PROXY_SQUID_PL_3

    @property
    def PROXY_SQUID_RU_3(self):
        return self._proxy_instance.PROXY_SQUID_RU_3

    @property
    def PROXY_SQUID_NO_3(self):
        return self._proxy_instance.PROXY_SQUID_NO_3

    @property
    def PROXY_SQUID_BR_3(self):
        return self._proxy_instance.PROXY_SQUID_BR_3

    @property
    def PROXY_SQUID_MX_3(self):
        return self._proxy_instance.PROXY_SQUID_MX_3

    @property
    def PROXY_SQUID_ZA_3(self):
        return self._proxy_instance.PROXY_SQUID_ZA_3

    @property
    def PROXY_SQUID_CA_3(self):
        return self._proxy_instance.PROXY_SQUID_CA_3

    @property
    def PROXY_SQUID_AT_3(self):
        return self._proxy_instance.PROXY_SQUID_AT_3

    @property
    def PROXY_SQUID_BE_3(self):
        return self._proxy_instance.PROXY_SQUID_BE_3

    @property
    def PROXY_SQUID_DK_3(self):
        return self._proxy_instance.PROXY_SQUID_DK_3

    @property
    def PROXY_SQUID_FR_3(self):
        return self._proxy_instance.PROXY_SQUID_FR_3

    @property
    def PROXY_SQUID_DE_3(self):
        return self._proxy_instance.PROXY_SQUID_DE_3

    @property
    def PROXY_SQUID_IT_3(self):
        return self._proxy_instance.PROXY_SQUID_IT_3

    @property
    def PROXY_SQUID_PT_3(self):
        return self._proxy_instance.PROXY_SQUID_PT_3

    @property
    def PROXY_SQUID_ES_3(self):
        return self._proxy_instance.PROXY_SQUID_ES_3

    @property
    def PROXY_SQUID_SE_3(self):
        return self._proxy_instance.PROXY_SQUID_SE_3

    @property
    def PROXY_SQUID_TR_3(self):
        return self._proxy_instance.PROXY_SQUID_TR_3

    @property
    def PROXY_SQUID_GB_3(self):
        return self._proxy_instance.PROXY_SQUID_GB_3

    @property
    def PROXY_SQUID_AR_3(self):
        return self._proxy_instance.PROXY_SQUID_AR_3

    @property
    def PROXY_SQUID_KR_3(self):
        return self._proxy_instance.PROXY_SQUID_KR_3

    @property
    def PROXY_SQUID_IE_3(self):
        return self._proxy_instance.PROXY_SQUID_IE_3

    @property
    def PROXY_SQUID_US_4(self):
        return self._proxy_instance.PROXY_SQUID_US_4