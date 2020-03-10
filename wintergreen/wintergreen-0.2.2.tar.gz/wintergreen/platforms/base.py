class Platform:
    platform_name = "base"

    def __init__(self, thing_type):
        self.thing_type = thing_type

    def _do_get_preferred_common_name():
        raise NotImplementedError

    def _do_process_certs():
        raise NotImplementedError

    def _do_verify_cert():
        raise NotImplementedError

    @staticmethod
    def __validate_common_name_response(cn):
        assert isinstance(cn, str)
        return cn

    @staticmethod
    def __validate_process_certs_response(response):
        assert set(response.keys()).issuperset({"platform_response", "success"})
        assert isinstance(response["platform_response"], dict)

        return response

    def get_preferred_common_name(self):
        cn = self._do_get_preferred_common_name()
        return self.__validate_common_name_response(cn)

    def process_certs(self, ca_cert, verification_cert):
        response = self._do_process_certs(ca_cert, verification_cert)
        response["platform"] = self.platform_name
        return self.__validate_process_certs_response(response)

    def verify_cert(self, key_path, cert_path, common_name):
        verified = self._do_verify_cert(key_path, cert_path, common_name)

        assert isinstance(verified, bool)
        return verified
