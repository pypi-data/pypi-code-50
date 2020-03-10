import csv
import json
import os
from datetime import date
from pathlib import Path

from ..crypto.data_structures import CertPair, CSRAttrs


class Persistence:
    log_fields = ["date"] + sorted(CSRAttrs.attrs)

    def __init__(self, thing_type):
        self.thing_type = thing_type
        self.config_dir = self.__get_home_directory() / ".wintergreen"

        if not self.config_dir.exists():
            self.config_dir.mkdir()

        self.root_ca_directory = self.config_dir / thing_type
        self.audit_log = []
        self.encryption_algorithm = None
        self.log_path = self.root_ca_directory / "audit_log.csv"

    def save_audit_log(self):

        self.__maybe_create_audit_log_file()

        with open(self.log_path, "a") as f:
            today = date.today().isoformat()
            writer = csv.DictWriter(f, fieldnames=self.log_fields)
            for csr_attrs in self.audit_log:
                csr_attrs["date"] = today
                writer.writerow(csr_attrs)

    @property
    def loaded_audit_log(self):
        with open(self.log_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                yield row

    def describe_thing(self, common_name):
        for entry in self.loaded_audit_log:
            if entry["common_name"] == common_name:
                return json.dumps(entry)

    def describe_thing_type(self):
        things = [x["common_name"] for x in self.loaded_audit_log]
        with open(self.root_ca_directory / ".encryption_algorithm") as f:
            algo = f.read()

        description = f"encryption algorithm: {algo}\ntotal things: {len(things)}"
        for tn in things:
            description += f"\n{tn}"

        return description

    def describe(self):
        thing_types = [x.stem for x in self.config_dir.iterdir()]
        description = f"total thing types: {len(thing_types)}"
        for tt in thing_types:
            description += f"\n{tt}"

        return description

    def __maybe_create_audit_log_file(self):
        if not self.log_path.exists():
            with open(self.log_path, "w") as f:
                writer = csv.DictWriter(f, fieldnames=self.log_fields)
                writer.writeheader()

    @staticmethod
    def __get_home_directory():
        home = os.curdir

        if "HOME" in os.environ:
            home = os.environ["HOME"]
        elif os.name == "posix":
            home = os.path.expanduser("~/")
        elif os.name == "nt":
            if "HOMEPATH" in os.environ and "HOMEDRIVE" in os.environ:
                home = os.environ["HOMEDRIVE"] + os.environ["HOMEPATH"]
        else:
            home = os.environ["HOMEPATH"]

        return Path(home)

    def save_new_root_ca(self, root_ca_pair):
        serialized_pair = root_ca_pair.serialize()

        if self.root_ca_directory.is_dir():
            message = f"A root CA for this thing type is already present at {self.root_ca_directory}"  # noqa
            raise Exception(message)

        self.root_ca_directory.mkdir(parents=True)

        with open(self.root_ca_directory / "rootCA.crt", "w") as f:
            f.write(serialized_pair["cert"])

        with open(self.root_ca_directory / "rootCA.key", "w") as f:
            f.write(serialized_pair["key"])

        with open(self.root_ca_directory / ".encryption_algorithm", "w") as f:
            f.write(serialized_pair["encryption_algorithm"])

    def save_new_provisioned_certs(self, csr_attrs, provisioned_pair, root_ca_pair):
        serialized_provisioned_pair = provisioned_pair.serialize()
        serialized_root_ca_pair = root_ca_pair.serialize()

        provisioning_dir = self.root_ca_directory / csr_attrs["common_name"]

        provisioning_dir.mkdir()

        with open(provisioning_dir / "device_cert.crt", "w") as f:
            f.write(serialized_provisioned_pair["cert"])

        with open(provisioning_dir / "device_key.key", "w") as f:
            f.write(serialized_provisioned_pair["key"])

        with open(provisioning_dir / "device_cert_plus_ca_cert.crt", "w") as f:
            f.write(
                serialized_provisioned_pair["cert"] + serialized_root_ca_pair["cert"]
            )

        self.audit_log.append(csr_attrs)

    def load_ca_pair(self):
        paths = self.ca_paths
        ca_pair = CertPair.from_files(
            paths["cert"], paths["key"], paths["encryption_algorithm"]
        )
        return ca_pair

    @property
    def ca_paths(self):
        return {
            "cert": self.root_ca_directory / "rootCA.crt",
            "key": self.root_ca_directory / "rootCA.key",
            "encryption_algorithm": self.root_ca_directory / ".encryption_algorithm",
        }

    def provisioned_paths(self, common_name):
        return {
            "cert": self.root_ca_directory / common_name / "device_cert.crt",
            "key": self.root_ca_directory / common_name / "device_key.key",
            "cert_plus_ca_cert": self.root_ca_directory
            / common_name
            / "device_cert_plus_ca_cert.crt",
        }
