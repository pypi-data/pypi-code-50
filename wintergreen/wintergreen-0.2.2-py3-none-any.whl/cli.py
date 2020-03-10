"""
Entrypoint for the Wintergreen CLI
"""
import json
import os
import sys

import click

from .crypto.cert_gen import CertGenerator
from .crypto.data_structures import CSRAttrs
from .initialize import init as init_impl
from .persistence import Persistence
from .platforms import AWSIoT, Local
from .provision import provision as provision_impl

basepath = os.path.dirname(os.path.abspath(__file__))

PLATFORM_DICT = {p_class.platform_name: p_class for p_class in [AWSIoT, Local]}
ENCRYPTION_ALGORITHMS = CertGenerator(1).encryption_algorithms


@click.group()
def cli():
    pass


@click.command()
@click.option("-t", "--thing-type", required=True, help="AWS IoT thing type")
@click.option(
    "-p",
    "--platform",
    required=True,
    help="Platform to upload root CA",
    default="aws",
    type=click.Choice(PLATFORM_DICT.keys()),
)
@click.option(
    "-a",
    "--algorithm",
    required=True,
    help="Encryption algorithms supported",
    default="rsa",
    type=click.Choice(ENCRYPTION_ALGORITHMS),
)
@click.option(
    "-c",
    "--country",
    required=True,
    type=str,
    help="Country code (2-letter) to use for provisioning certs i.e. US",
    default="US",
)
@click.option(
    "-f",
    "--fqdn",
    help="Domain of the organization to use in the CA e.g. verypossible.com",
)
@click.option("-o", "--organization", help="Organization name i.e. Very")
@click.option(
    "-s",
    "--state",
    type=str,
    help="State or Province code (2-letter) to use for provisioning certs i.e. TN",
)
@click.option(
    "-l",
    "--locality",
    type=str,
    help="Locality to use for provisioning certs i.e. Chattanooga",
)
@click.option(
    "-u",
    "--unit",
    type=str,
    help="Organizational unit to use for provisioning certs i.e. Engineering",
)
@click.option(
    "-d",
    "--days",
    type=int,
    show_default=True,
    default=365,
    help="Days until CA will expire",
)
@click.option("-k", "--key-size", type=int, show_default=True, default=2048)
def init(
    thing_type,
    platform,
    algorithm,
    country,
    fqdn,
    organization,
    state,
    locality,
    unit,
    days,
    key_size,
):
    csr_attrs = CSRAttrs(
        country=country,
        fqdn=fqdn,
        organization=organization,
        state=state,
        locality=locality,
        unit=unit,
    )

    platform_cls = PLATFORM_DICT[platform]

    output = init_impl(
        thing_type, platform_cls, algorithm, csr_attrs, days=days, key_size=key_size
    )

    click.echo(json.dumps(output, indent=4))


@click.command()
@click.option(
    "-t",
    "--thing-type",
    help="Same as the thing-type that was chosen in the `init` step.",
)
@click.option("-cn", "--common_name", default=None, help="Defaults to a UUIDv4")
@click.option("-c", "--country", required=True, default="US")
@click.option("-o", "--organization")
@click.option("-s", "--state")
@click.option("-l", "--locality")
@click.option("-u", "--unit")
@click.option(
    "-d",
    "--days",
    help="Days until certificate will expire",
    type=int,
    default=365,
    show_default=True,
)
@click.option("-k", "--key-size", type=int, show_default=True, default=2048)
@click.option(
    "-n",
    "--number",
    type=int,
    show_default=True,
    default=1,
    help="Number of certificates to provision",
)
@click.option("-v", "--verbosity", count=True, help="Verbosity, add v's for more.")
def provision(
    thing_type,
    common_name,
    country,
    organization,
    state,
    locality,
    unit,
    days,
    key_size,
    number,
    verbosity,
):
    csr_attrs = CSRAttrs(
        country=country,
        common_name=common_name,
        fqdn=None,
        organization=organization,
        state=state,
        locality=locality,
        unit=unit,
    )

    persister = Persistence(thing_type)

    for n in range(number):
        provisioned_attrs = provision_impl(
            persister, csr_attrs, days=days, key_size=key_size
        )

        if verbosity > 0:
            click.echo(f"{provisioned_attrs['common_name']}")

    if verbosity > 1:
        click.echo(f"Generated {number} certificate(s)")

    persister.save_audit_log()


@click.command()
@click.option(
    "-p",
    "--platform",
    required=True,
    help="Platform to upload root CA",
    default="aws",
    type=click.Choice(PLATFORM_DICT.keys()),
)
@click.option("-t", "--thing-type", required=True, help="AWS IoT thing type")
@click.option("-cn", "--common_name", required=True, help="Common name to verify")
def verify(platform, thing_type, common_name):
    platform_cls = PLATFORM_DICT[platform]
    plat = platform_cls(thing_type)
    persister = Persistence(thing_type)
    cert_path = persister.provisioned_paths(common_name)["cert_plus_ca_cert"]
    key_path = persister.provisioned_paths(common_name)["key"]

    if plat.verify_cert(key_path, cert_path, common_name):
        click.echo(f"Certificate verified on the {plat.platform_name} platform!")
    else:
        click.echo(
            f"Unable to verify certificate on the {plat.platform_name} platform..."
        )
        sys.exit(1)


@click.command()
@click.option("-t", "--thing-type", default="", help="Thing type to receive info about")
@click.option(
    "-cn", "--common_name", default="", help="Common name to receive info about"
)
def info(thing_type, common_name):
    persistor = Persistence(thing_type)
    if thing_type and common_name:
        description = persistor.describe_thing(common_name)
    elif thing_type:
        description = persistor.describe_thing_type()
    else:
        description = persistor.describe()

    click.echo(description)


cli.add_command(init)
cli.add_command(provision)
cli.add_command(verify)
cli.add_command(info)

if __name__ == "__main__":
    cli()
