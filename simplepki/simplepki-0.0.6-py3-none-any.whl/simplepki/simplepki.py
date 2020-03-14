import datetime
import os
import shutil

import click
import pkg_resources  # part of setuptools
import questionary
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID


def print_error(message):
    print('Error: {}'.format(message))
    quit(1)


def _base_pem_file_name(cn):
    cn = cn.replace('*', 'wildcard_').replace(' ', '_')
    return cn


def get_key_file_name(domain):
    return '{}.key.pem'.format(_base_pem_file_name(domain))


def get_certificate_request_file_name(domain):
    return '{}.csr.pem'.format(_base_pem_file_name(domain))


def get_certificate_file_name(domain):
    return '{}.cert.pem'.format(_base_pem_file_name(domain))


def get_passphrase_confirm():
    questions = [
        {
            'type': 'password',
            'name': 'passphrase',
            'message': 'Private key passphrase',
        },
        {
            'type': 'password',
            'name': 'passphrase_confirmation',
            'message': 'Confirm passphrase'
        }
    ]

    answers = questionary.prompt(questions)
    while not answers['passphrase'] == answers['passphrase_confirmation']:
        print('Passphrase does not match.')
        answers = questionary.prompt(questions)
    return answers['passphrase']


def get_passphrase():
    passphrase = questionary.password('Private key passphrase').ask()
    passphrase = bytes(passphrase.encode('utf-8'))
    return passphrase


def load_private_key(content):
    if not isinstance(content, bytes):
        raise TypeError('private key needs to be in bytes format')

    if 'ENCRYPTED' in content.decode():
        try:
            private_key = serialization.load_pem_private_key(content, get_passphrase(), default_backend())
        except ValueError as err:
            print_error(err)
    else:
        private_key = serialization.load_pem_private_key(content, None, default_backend())
    return private_key


def load_cert(content):
    if not isinstance(content, bytes):
        raise TypeError('content needs to be in bytes format')

    cert = x509.load_pem_x509_certificate(content, default_backend())
    return cert


VERSION = pkg_resources.get_distribution("simplepki").version
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=VERSION)
@click.option('--ca', help='ca to use. [default: root]')
@click.option('--root', help='root path')
@click.pass_context
def cli(ctx, ca, root):
    ctx.ensure_object(dict)
    ctx.obj['CA'] = ca if ca else os.getenv('SP_CA', 'root')
    if ca or os.getenv('SP_ROOT'):
        ctx.obj['ROOT'] = root if root else os.getenv('SP_ROOT')
    else:
        print_error('root path is required, use environment variables or --root')


@cli.group(help='create [command]')
@click.pass_context
def create(ctx):
    pass


@create.command(help='create certificate authority')
@click.option('--cn', help='certificate authority common name.')
@click.option('--organization', help='organization.')
@click.option('--organization-unit', help='organization unit.')
@click.option('--country', help='country.')
@click.option('--locality', help='locality.')
@click.option('--province', help='province.')
@click.option('--expire', help='certificate expire in days', default=7300, show_default=True, type=click.INT,
              required=True)
@click.option('--pass', 'pass_', help='Password protect key file', is_flag=True)
@click.pass_context
def root(ctx, cn, organization, organization_unit, country, locality, province, expire, pass_):
    root_path = ctx.obj['ROOT']
    ca = ctx.obj['CA']
    root_ca_path = os.path.join(root_path, ca)
    cn = cn if cn else os.getenv('SP_CN')
    organization = organization if organization else os.getenv('SP_ORGANIZATION')
    organization_unit = organization_unit if organization_unit else os.getenv('SP_ORGANIZATION_UNIT')
    country = country if country else os.getenv('SP_COUNTRY')
    locality = locality if locality else os.getenv('SP_LOCALITY')
    province = province if province else os.getenv('SP_PROVINCE')

    if not organization:
        print_error('Organization is required')
    if os.path.exists(root_ca_path):
        print_error('Root CA already created in {}, if you would like to re-create it please delete this folder'
                    .format(root_ca_path))

    try:
        # Make our key
        key = rsa.generate_private_key(public_exponent=65537, key_size=4096, backend=default_backend())

        # Create self-signed cert
        # Add the information provided
        information = []
        if cn:
            information.append(x509.NameAttribute(NameOID.COMMON_NAME, cn))
        if organization:
            information.append(x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization))
        if organization_unit:
            information.append(x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, organization_unit))
        if country:
            information.append(x509.NameAttribute(NameOID.COUNTRY_NAME, country))
        if locality:
            information.append(x509.NameAttribute(NameOID.LOCALITY_NAME, locality))
        if province:
            information.append(x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, province))

        issuer = x509.Name(information)
        cert = x509.CertificateBuilder()
        cert = cert.subject_name(issuer).issuer_name(issuer)

        # Add the public key from our private key
        cert = cert.public_key(key.public_key())
        # Make a random serial number
        cert = cert.serial_number(x509.random_serial_number())

        # Make valid for the set expire
        cert = cert.not_valid_before(datetime.datetime.utcnow())
        cert = cert.not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=expire))

        # Add extensions
        cert = cert.add_extension(
            x509.KeyUsage(True, False, False, False, False, True, True, False, False), True)

        # Basic constraints
        cert = cert.add_extension(x509.BasicConstraints(True, None), True)

        # Add Subject key identifier from public key
        cert = cert.add_extension(x509.SubjectKeyIdentifier.from_public_key(key.public_key()), False)

        # Add authority key identifier
        cert = cert.add_extension(x509.AuthorityKeyIdentifier.from_issuer_public_key(key.public_key()), False)

        cert = cert.sign(key, hashes.SHA256(), default_backend())

        # Create the paths
        os.mkdir(root_ca_path)
        os.mkdir(os.path.join(root_ca_path, 'certs'))
        os.mkdir(os.path.join(root_ca_path, 'private'), 0o700)

        # Write our key to disk for safe keeping
        with open(os.path.join(root_ca_path, 'private/root.key.pem'), "wb") as f:
            if pass_:
                print('You will now be asked for the passphrase to protect the root CA key')
                passphrase = get_passphrase_confirm().encode('utf-8')

                to_be_written = key.private_bytes(encoding=serialization.Encoding.PEM,
                                                  format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                  encryption_algorithm=serialization.BestAvailableEncryption(
                                                      bytes(passphrase)))
            else:
                to_be_written = key.private_bytes(encoding=serialization.Encoding.PEM,
                                                  format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                  encryption_algorithm=serialization.NoEncryption())
            f.write(to_be_written)
        os.chmod(os.path.join(root_ca_path, 'private/root.key.pem'), 0o400)

        # Write our certificate out to disk.
        with open(os.path.join(root_ca_path, 'certs/root.cert.pem'), "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))
        os.chmod(os.path.join(root_ca_path, 'certs/root.cert.pem'), 0o644)

        print('Finished making your Root CA.')
        quit()
    except Exception as err:
        shutil.rmtree(ca)
        print_error(err)


@create.command(help='create intermediate certificate authority')
@click.option('--intermediate', help='intermediate ca folder.', default='intermediate', show_default=True)
@click.option('--cn', help='certificate authority common name.')
@click.option('--organization', help='organization.')
@click.option('--organization-unit', help='organization unit.')
@click.option('--country', help='country.')
@click.option('--locality', help='locality.')
@click.option('--province', help='province.')
@click.option('--expire', help='certificate expire in days', default=1095, show_default=True, type=click.INT,
              required=True)
@click.option('--pass', 'pass_', help='Password protect key file', is_flag=True)
@click.pass_context
def intermediate(ctx, intermediate, cn, organization, organization_unit, country, locality, province, expire, pass_):
    root_path = ctx.obj['ROOT']
    ca = ctx.obj['CA']
    root_ca_path = os.path.join(root_path, ca)
    intermediate = intermediate if intermediate else os.getenv('SP_INTERMEDIATE')
    intermediate_ca_path = os.path.join(root_path, intermediate)
    cn = cn if cn else os.getenv('SP_CN')
    organization = organization if organization else os.getenv('SP_ORGANIZATION')
    organization_unit = organization_unit if organization_unit else os.getenv('SP_ORGANIZATION_UNIT')
    country = country if country else os.getenv('SP_COUNTRY')
    locality = locality if locality else os.getenv('SP_LOCALITY')
    province = province if province else os.getenv('SP_PROVINCE')

    if not organization:
        print_error('Organization is required')
    if os.path.exists(intermediate_ca_path):
        print_error('Intermediate CA already created in {}, if you would like to re-create it please delete this folder'
                    .format(intermediate_ca_path))

    try:
        # Make our key
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

        # Create cert
        # Add the information provided
        information = []
        if cn:
            information.append(x509.NameAttribute(NameOID.COMMON_NAME, cn))
        if organization:
            information.append(x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization))
        if organization_unit:
            information.append(x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, organization_unit))
        if country:
            information.append(x509.NameAttribute(NameOID.COUNTRY_NAME, country))
        if locality:
            information.append(x509.NameAttribute(NameOID.LOCALITY_NAME, locality))
        if province:
            information.append(x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, province))

        subject = x509.Name(information)

        # Now we need to get the issuer information from the root CA
        with open(os.path.join(root_ca_path, 'certs/root.cert.pem'), 'rb') as f:
            root_ca_cert = load_cert(f.read())

        issuer = root_ca_cert.subject

        with open(os.path.join(root_ca_path, 'private/root.key.pem'), 'rb') as f:
            print('You may now be asked for the passphrase for the root CA key if it\'s protected')
            root_ca_key = load_private_key(f.read())

        cert = x509.CertificateBuilder()
        cert = cert.subject_name(subject).issuer_name(issuer)

        # Add the public key from our private key
        cert = cert.public_key(key.public_key())
        # Make a random serial number
        cert = cert.serial_number(x509.random_serial_number())

        # Make valid for the set expire
        cert = cert.not_valid_before(datetime.datetime.utcnow())
        cert = cert.not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=expire))

        # Add extensions
        cert = cert.add_extension(
            x509.KeyUsage(True, False, False, False, False, True, True, False, False), True)

        # Basic constraints
        cert = cert.add_extension(x509.BasicConstraints(True, None), True)

        # Add Subject key identifier from public key
        cert = cert.add_extension(x509.SubjectKeyIdentifier.from_public_key(key.public_key()), False)

        # Add authority key identifier
        cert = cert.add_extension(x509.AuthorityKeyIdentifier.from_issuer_public_key(root_ca_key.public_key()), False)

        cert = cert.sign(root_ca_key, hashes.SHA256(), default_backend())

        # Create the paths
        os.mkdir(intermediate_ca_path)
        os.mkdir(os.path.join(intermediate_ca_path, 'certs'))
        os.mkdir(os.path.join(intermediate_ca_path, 'private'), 0o700)

        # Write our key to disk for safe keeping
        with open(os.path.join(intermediate_ca_path, 'private/root.key.pem'), "wb") as f:
            if pass_:
                print('You will now be asked for the passphrase to protect the intermediate CA key')
                passphrase = get_passphrase_confirm().encode('utf-8')

                to_be_written = key.private_bytes(encoding=serialization.Encoding.PEM,
                                                  format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                  encryption_algorithm=serialization.BestAvailableEncryption(
                                                      bytes(passphrase)))
            else:
                to_be_written = key.private_bytes(encoding=serialization.Encoding.PEM,
                                                  format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                  encryption_algorithm=serialization.NoEncryption())
            f.write(to_be_written)
        os.chmod(os.path.join(intermediate_ca_path, 'private/root.key.pem'), 0o400)

        # Write our certificate out to disk.
        with open(os.path.join(intermediate_ca_path, 'certs/root.cert.pem'), "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))
        os.chmod(os.path.join(intermediate_ca_path, 'certs/root.cert.pem'), 0o644)

        print('Finished making your Intermediate CA.')
        quit()
    except Exception as err:
        shutil.rmtree(intermediate_ca_path)
        print_error(err)


@create.command(help='create certificate')
@click.argument('cn')
@click.option('--dns', help='DNS domain, subdomain or (*.)wildcard.', multiple=True)
@click.option('--organization', help='organization.')
@click.option('--organization-unit', help='organization unit.')
@click.option('--country', help='country.')
@click.option('--locality', help='locality.')
@click.option('--province', help='province.')
@click.option('--expire', help='certificate expire in days', default=365, show_default=True, type=click.INT,
              required=True)
@click.option('--pass', 'pass_', help='Password protect key file', is_flag=True)
@click.pass_context
def cert(ctx, cn, dns, organization, organization_unit, country, locality, province, expire, pass_):
    root_path = ctx.obj['ROOT']
    ca = ctx.obj['CA']
    root_ca_path = os.path.join(root_path, ca)
    organization = organization if organization else os.getenv('SP_ORGANIZATION')
    organization_unit = organization_unit if organization_unit else os.getenv('SP_ORGANIZATION_UNIT')
    country = country if country else os.getenv('SP_COUNTRY')
    locality = locality if locality else os.getenv('SP_LOCALITY')
    province = province if province else os.getenv('SP_PROVINCE')

    if not organization:
        print_error('Organization is required')
    if not os.path.exists(root_ca_path):
        print_error('Could not find CA in {}.'.format(root_ca_path))

    try:
        # Make our key
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

        # Create cert
        # Add the information provided
        information = []
        if cn:
            information.append(x509.NameAttribute(NameOID.COMMON_NAME, cn))
        if organization:
            information.append(x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization))
        if organization_unit:
            information.append(x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, organization_unit))
        if country:
            information.append(x509.NameAttribute(NameOID.COUNTRY_NAME, country))
        if locality:
            information.append(x509.NameAttribute(NameOID.LOCALITY_NAME, locality))
        if province:
            information.append(x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, province))

        subject = x509.Name(information)

        # Now we need to get the issuer information from the CA
        with open(os.path.join(root_ca_path, 'certs/root.cert.pem'), 'rb') as f:
            ca_cert = load_cert(f.read())

        issuer = ca_cert.subject

        with open(os.path.join(root_ca_path, 'private/root.key.pem'), 'rb') as f:
            print('You may now be asked for the passphrase for the selected CA if it\'s protected')
            ca_key = load_private_key(f.read())

        cert = x509.CertificateBuilder()
        cert = cert.subject_name(subject).issuer_name(issuer)

        # Add the public key from our private key
        cert = cert.public_key(key.public_key())
        # Make a random serial number
        cert = cert.serial_number(x509.random_serial_number())

        # Make valid for the set expire
        cert = cert.not_valid_before(datetime.datetime.utcnow())
        cert = cert.not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=expire))

        # Add extensions
        cert = cert.add_extension(
            x509.KeyUsage(True, False, True, False, False, False, False, False, False), True)
        cert = cert.add_extension(x509.ExtendedKeyUsage([x509.oid.ExtendedKeyUsageOID.SERVER_AUTH,
                                                         x509.oid.ExtendedKeyUsageOID.CLIENT_AUTH]), False)

        # Basic constraints
        cert = cert.add_extension(x509.BasicConstraints(False, None), True)

        # Add Subject key identifier from public key
        cert = cert.add_extension(x509.SubjectKeyIdentifier.from_public_key(key.public_key()), False)

        # Add authority key identifier
        cert = cert.add_extension(x509.AuthorityKeyIdentifier.from_issuer_public_key(ca_key.public_key()), False)

        cert = cert.add_extension(x509.SubjectAlternativeName([x509.DNSName(d) for d in dns]), False)

        cert = cert.sign(ca_key, hashes.SHA256(), default_backend())

        # Write our key to disk for safe keeping
        with open(os.path.join(root_ca_path, 'private/{}'.format(get_key_file_name(cn))), "wb") as f:
            if pass_:
                print('You will now be asked for the passphrase to protect the cert key')
                passphrase = get_passphrase_confirm().encode('utf-8')

                to_be_written = key.private_bytes(encoding=serialization.Encoding.PEM,
                                                  format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                  encryption_algorithm=serialization.BestAvailableEncryption(
                                                      bytes(passphrase)))
            else:
                to_be_written = key.private_bytes(encoding=serialization.Encoding.PEM,
                                                  format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                  encryption_algorithm=serialization.NoEncryption())
            f.write(to_be_written)
        os.chmod(os.path.join(root_ca_path, 'private/{}'.format(get_key_file_name(cn))), 0o400)

        # Write our certificate out to disk.
        with open(os.path.join(root_ca_path, 'certs/{}'.format(get_certificate_file_name(cn))), "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))
        os.chmod(os.path.join(root_ca_path, 'certs/{}'.format(get_certificate_file_name(cn))), 0o644)

        print('Finished making your certificate.')
        quit()
    except Exception as err:
        print_error(err)

# TODO
# @cli.command(help='revoke path/to/ca-name/certs/cert path/to/ca-name/certs/cert2')
# @click.argument('certs', nargs=-1, type=click.File('r'))
# @click.pass_context
# def revoke(ctx, certs):
#     pass
#
#
# @cli.command(help='generate certificate revocation list')
# @click.option('--expire', type=click.INT, help='expiration limit in days', default=7, show_default=True)
# @click.option('--ca-name', type=click.STRING, help='specify name to use', default='ca', show_default=True)
# @click.pass_context
# def crl(ctx, expire, ca_name):
#     pass
