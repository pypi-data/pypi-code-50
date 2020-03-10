from .base import Platform


class Local(Platform):
    platform_name = "local"

    def _do_get_preferred_common_name(self):
        return "LocalVerifier"

    def _do_process_certs(self, ca_cert, verification_cert):
        return {"platform_response": {}, "success": True}
