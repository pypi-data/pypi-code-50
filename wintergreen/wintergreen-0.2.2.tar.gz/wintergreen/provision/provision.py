"""
Create a cert and private key for a new device that will connect to AWS IoT.
"""

from uuid import uuid4

from ..crypto.cert_gen import CertGenerator


def provision(persister, csr_attrs, days=365, key_size=2048, **kwargs):
    """
    Creates a new device key and certificate that is signed by a custom root CA.
    """

    csr_attrs = {
        **csr_attrs,
        **{"common_name": csr_attrs.get("common_name", str(uuid4()))},
    }

    ca_pair = persister.load_ca_pair()

    cg = CertGenerator(key_size, ca_pair["encryption_algorithm"])
    csr_pair = cg.generate_csr(csr_attrs)

    cert_pair = cg.generate_signed_cert(csr_pair, ca_pair, days)

    persister.save_new_provisioned_certs(csr_attrs, cert_pair, ca_pair)

    return csr_attrs
