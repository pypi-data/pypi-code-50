"""
Handles crypto functions, creates certs
"""
import datetime
from uuid import uuid4

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec, rsa
from cryptography.x509.oid import NameOID

from .data_structures import CertPair

ISSUER = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "wintergreen")])


class CertGenerator:
    def __init__(self, key_size, encryption_algorithm="rsa"):
        self.key_size = key_size
        self.encryption_algorithm = encryption_algorithm

    @property
    def encryption_algorithms(self):
        return self.__key_generators.keys()

    @property
    def __key_generators(self):
        return {
            "rsa": lambda: rsa.generate_private_key(
                backend=default_backend(), public_exponent=65537, key_size=self.key_size
            ),
            "ec": lambda: ec.generate_private_key(ec.SECP256R1(), default_backend()),
        }

    def __new_private_key(self):
        """
        Equivalent to openssl genrsa -out rootCA.key key_size
        """
        return self.__key_generators[self.encryption_algorithm]()

    def generate_ca_cert(self, root_ca_days):
        """
        Equivalent to
        openssl req -x509 -new -nodes -key rootCA.key -sha256 -days root_ca_days -out rootCA.pem
        """  # noqa
        key = self.__new_private_key()
        valid_until = datetime.datetime.utcnow() + datetime.timedelta(days=root_ca_days)
        cert = (
            x509.CertificateBuilder()
            .subject_name(ISSUER)
            .issuer_name(ISSUER)
            .public_key(key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(datetime.datetime.utcnow())
            .not_valid_after(valid_until)
            .add_extension(x509.BasicConstraints(ca=True, path_length=0), critical=True)
            .add_extension(
                x509.KeyUsage(
                    digital_signature=True,
                    key_encipherment=False,
                    content_commitment=False,
                    data_encipherment=False,
                    key_agreement=False,
                    key_cert_sign=True,
                    crl_sign=True,
                    encipher_only=False,
                    decipher_only=False,
                ),
                critical=True,
            )
            .add_extension(
                x509.AuthorityKeyIdentifier.from_issuer_public_key(key.public_key()),
                critical=False,
            )
            .add_extension(
                x509.SubjectKeyIdentifier.from_public_key(key.public_key()),
                critical=False,
            )
            .sign(key, hashes.SHA256(), default_backend())
        )

        return CertPair(
            {
                "cert": cert,
                "key": key,
                "encryption_algorithm": self.encryption_algorithm,
            }
        )

    def generate_csr(self, csr_attrs):
        """
        Equivalent to
        openssl req -new -key verificationCert.key -out verificationCert.csr -config provisioning.cnf
        """  # noqa
        key = self.__new_private_key()
        csr = (
            x509.CertificateSigningRequestBuilder()
            .subject_name(
                x509.Name(
                    [
                        x509.NameAttribute(
                            NameOID.COMMON_NAME, f"{csr_attrs.get('common_name')}"
                        ),
                        x509.NameAttribute(
                            NameOID.ORGANIZATION_NAME,
                            f"{csr_attrs.get('organization')}",
                        ),
                        x509.NameAttribute(
                            NameOID.COUNTRY_NAME, f"{csr_attrs.get('country')}"
                        ),
                        x509.NameAttribute(
                            NameOID.STATE_OR_PROVINCE_NAME, f"{csr_attrs.get('state')}"
                        ),
                        x509.NameAttribute(
                            NameOID.LOCALITY_NAME, f"{csr_attrs.get('locality')}"
                        ),
                        x509.NameAttribute(
                            NameOID.ORGANIZATIONAL_UNIT_NAME, f"{csr_attrs.get('unit')}"
                        ),
                    ]
                )
            )
            .add_extension(
                x509.SubjectAlternativeName([x509.DNSName(f"{csr_attrs.get('fqdn')}")]),
                critical=False,
            )
            .sign(key, hashes.SHA256(), default_backend())
        )
        return {"csr": csr, "key": key}

    def generate_signed_cert(self, csr_pair, ca_pair, days):
        cert = (
            x509.CertificateBuilder()
            .subject_name(csr_pair["csr"].subject)
            .issuer_name(ca_pair["cert"].subject)
            .public_key(csr_pair["csr"].public_key())
            .serial_number(uuid4().int)  # pylint: disable=no-member
            .not_valid_before(datetime.datetime.utcnow())
            .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=days))
            .add_extension(
                extension=x509.KeyUsage(
                    digital_signature=True,
                    key_encipherment=True,
                    content_commitment=True,
                    data_encipherment=False,
                    key_agreement=False,
                    encipher_only=False,
                    decipher_only=False,
                    key_cert_sign=False,
                    crl_sign=False,
                ),
                critical=True,
            )
            .add_extension(
                extension=x509.BasicConstraints(ca=False, path_length=None),
                critical=True,
            )
            .add_extension(
                extension=x509.AuthorityKeyIdentifier.from_issuer_public_key(
                    ca_pair["key"].public_key()
                ),
                critical=False,
            )
            .sign(
                private_key=ca_pair["key"],
                algorithm=hashes.SHA256(),
                backend=default_backend(),
            )
        )
        return CertPair(
            {
                "cert": cert,
                "key": csr_pair["key"],
                "encryption_algorithm": self.encryption_algorithm,
            }
        )
