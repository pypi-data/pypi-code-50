from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key


class CertPair(dict):
    @classmethod
    def from_files(cls, cert_path, key_path, encryption_algorithm_path):
        with open(cert_path, "rb") as f:
            cert = f.read()

        with open(key_path, "rb") as f:
            key = f.read()

        with open(encryption_algorithm_path, "r") as f:
            encryption_algorithm = f.read()

        return cls(
            {"cert": cert, "key": key, "encryption_algorithm": encryption_algorithm}
        ).deserialize()

    def deserialize(self):
        self["cert"] = x509.load_pem_x509_certificate(self["cert"], default_backend())
        self["key"] = load_pem_private_key(self["key"], None, default_backend())
        return self

    def serialize(self):
        return {
            "cert": self["cert"]
            .public_bytes(serialization.Encoding.PEM)
            .decode("utf-8"),
            "key": self["key"]
            .private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
            )
            .decode("utf-8"),
            "encryption_algorithm": self["encryption_algorithm"],
        }


class CSRAttrs(dict):

    attrs = {
        "common_name",
        "country",
        "fqdn",
        "locality",
        "organization",
        "state",
        "unit",
    }

    @classmethod
    def from_dict(cls, dictionary):
        keep_keys = cls.attrs.intersection(set(dictionary.keys()))
        return cls({k: dictionary[k] for k in keep_keys})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.attrs.issuperset(set(self.keys())):
            raise AttributeError("invalid keys for CSRAttrs")
