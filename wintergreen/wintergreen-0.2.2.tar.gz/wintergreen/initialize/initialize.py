"""
Create a root CA, just-in-time provisioning role, and registration config on AWS IoT.
"""

from ..crypto import CertGenerator
from ..persistence import Persistence


def init(
    thing_type, platform_cls, encryption_algorithm, csr_attrs, days=365, key_size=2048
):
    """
    Creates a custom root CA and registers it with the cloud provider for
    automatic provisioning.
    """

    platform = platform_cls(thing_type)

    # Cloud providers may want to provide a common name
    common_name = platform.get_preferred_common_name()
    csr_attrs["common_name"] = common_name

    cg = CertGenerator(key_size, encryption_algorithm)

    root_pair = cg.generate_ca_cert(days)
    csr_pair = cg.generate_csr(csr_attrs)
    verification_pair = cg.generate_signed_cert(csr_pair, root_pair, days)

    serialized_ca_pair = root_pair.serialize()
    serialized_verification_pair = verification_pair.serialize()

    platform_output = platform.process_certs(
        serialized_ca_pair["cert"], serialized_verification_pair["cert"]
    )

    persist = Persistence(thing_type)
    persist.save_new_root_ca(root_pair)

    output = platform_output

    return output
