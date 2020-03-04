#
# asn2quickder output for PKCS-7 -- automatically generated
#
# Read more about Quick `n' Easy DER on https://gitlab.com/arpa2/quick-der
#


#
# Import general definitions and package dependencies
#

from arpa2.quickder import api as _api

from rfc3280 import Certificate, CertificateSerialNumber, AlgorithmIdentifier, Name, AttributeTypeAndValue
from rfc1422 import CertificateRevocationList


#
# Classes for ASN.1 type assignments
#

# Attributes ::= SET OF AttributeTypeAndValue
class Attributes (_api.ASN1SetOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SETOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),2,
        ('_TYPTR', ['AttributeTypeAndValue'], 0) )
    _context = globals ()
    _numcursori = 1

# CertificateRevocationLists ::= SET OF CertificateRevocationList
class CertificateRevocationLists (_api.ASN1SetOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SETOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),6,
        ('_TYPTR', ['CertificateRevocationList'], 0) )
    _context = globals ()
    _numcursori = 1

# ContentEncryptionAlgorithmIdentifier ::= AlgorithmIdentifier
class ContentEncryptionAlgorithmIdentifier (AlgorithmIdentifier):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['AlgorithmIdentifier'], 0)
    _context = globals ()
    _numcursori = 2

# ContentType ::= OBJECT IDENTIFIER
class ContentType (_api.ASN1OID):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OID'], 0)
    _context = globals ()
    _numcursori = 1

# ContentInfo ::= SEQUENCE { contentType ContentType, content [0] EXPLICIT ANY OPTIONAL }
class ContentInfo (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'contentType': ('_TYPTR', ['ContentType'], 0),
        'content': ('_TYPTR', ['_api.ASN1Any'], 1) } )
    _context = globals ()
    _numcursori = 2

# Data ::= OCTET STRING
class Data (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# Digest ::= OCTET STRING
class Digest (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# Digest ::= OCTET STRING
class Digest (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# DigestAlgorithmIdentifier ::= AlgorithmIdentifier
class DigestAlgorithmIdentifier (AlgorithmIdentifier):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['AlgorithmIdentifier'], 0)
    _context = globals ()
    _numcursori = 2

# DigestAlgorithmIdentifiers ::= SET OF DigestAlgorithmIdentifier
class DigestAlgorithmIdentifiers (_api.ASN1SetOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SETOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),2,
        ('_TYPTR', ['DigestAlgorithmIdentifier'], 0) )
    _context = globals ()
    _numcursori = 1

# DigestEncryptionAlgorithmIdentifier ::= AlgorithmIdentifier
class DigestEncryptionAlgorithmIdentifier (AlgorithmIdentifier):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['AlgorithmIdentifier'], 0)
    _context = globals ()
    _numcursori = 2

# DigestInfo ::= SEQUENCE { digestAlgorithm DigestAlgorithmIdentifier, digest Digest }
class DigestInfo (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'digestAlgorithm': ('_TYPTR', ['DigestAlgorithmIdentifier'], 0),
        'digest': ('_TYPTR', ['Digest'], 2) } )
    _context = globals ()
    _numcursori = 3

# Version ::= INTEGER
class Version (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# DigestedData ::= SEQUENCE { version Version, digestAlgorithm DigestAlgorithmIdentifier, contentInfo ContentInfo, digest Digest }
class DigestedData (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'version': ('_TYPTR', ['Version'], 0),
        'digestAlgorithm': ('_TYPTR', ['DigestAlgorithmIdentifier'], 1),
        'contentInfo': ('_TYPTR', ['ContentInfo'], 3),
        'digest': ('_TYPTR', ['Digest'], 5) } )
    _context = globals ()
    _numcursori = 6

# EncryptedContent ::= OCTET STRING
class EncryptedContent (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# EncryptedContentInfo ::= SEQUENCE { contentType ContentType, contentEncryptionAlgorithm ContentEncryptionAlgorithmIdentifier, encryptedContent [0] IMPLICIT EncryptedContent OPTIONAL }
class EncryptedContentInfo (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'contentType': ('_TYPTR', ['ContentType'], 0),
        'contentEncryptionAlgorithm': ('_TYPTR', ['ContentEncryptionAlgorithmIdentifier'], 1),
        'encryptedContent': ('_TYPTR', ['EncryptedContent'], 3) } )
    _context = globals ()
    _numcursori = 4

# EncryptedData ::= SEQUENCE { version Version, encryptedContentInfo EncryptedContentInfo }
class EncryptedData (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'version': ('_TYPTR', ['Version'], 0),
        'encryptedContentInfo': ('_TYPTR', ['EncryptedContentInfo'], 1) } )
    _context = globals ()
    _numcursori = 5

# EncryptedDigest ::= OCTET STRING
class EncryptedDigest (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# EncryptedKey ::= OCTET STRING
class EncryptedKey (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# KeyEncryptionAlgorithmIdentifier ::= AlgorithmIdentifier
class KeyEncryptionAlgorithmIdentifier (AlgorithmIdentifier):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['AlgorithmIdentifier'], 0)
    _context = globals ()
    _numcursori = 2

# IssuerAndSerialNumber ::= SEQUENCE { issuer Name, serialNumber CertificateSerialNumber }
class IssuerAndSerialNumber (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'issuer': ('_TYPTR', ['Name'], 0),
        'serialNumber': ('_TYPTR', ['CertificateSerialNumber'], 1) } )
    _context = globals ()
    _numcursori = 2

# RecipientInfo ::= SEQUENCE { version Version, issuerAndSerialNumber IssuerAndSerialNumber, keyEncryptionAlgorithm KeyEncryptionAlgorithmIdentifier, encryptedKey EncryptedKey }
class RecipientInfo (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'version': ('_TYPTR', ['Version'], 0),
        'issuerAndSerialNumber': ('_TYPTR', ['IssuerAndSerialNumber'], 1),
        'keyEncryptionAlgorithm': ('_TYPTR', ['KeyEncryptionAlgorithmIdentifier'], 3),
        'encryptedKey': ('_TYPTR', ['EncryptedKey'], 5) } )
    _context = globals ()
    _numcursori = 6

# RecipientInfos ::= SET OF RecipientInfo
class RecipientInfos (_api.ASN1SetOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SETOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),6,
        ('_TYPTR', ['RecipientInfo'], 0) )
    _context = globals ()
    _numcursori = 1

# EnvelopedData ::= SEQUENCE { version Version, recipientInfos RecipientInfos, encryptedContentInfo EncryptedContentInfo }
class EnvelopedData (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'version': ('_TYPTR', ['Version'], 0),
        'recipientInfos': ('_TYPTR', ['RecipientInfos'], 1),
        'encryptedContentInfo': ('_TYPTR', ['EncryptedContentInfo'], 2) } )
    _context = globals ()
    _numcursori = 6

# ExtendedCertificate ::= Certificate
class ExtendedCertificate (Certificate):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['Certificate'], 0)
    _context = globals ()
    _numcursori = 19

# ExtendedCertificateOrCertificate ::= CHOICE { certificate Certificate, extendedCertificate [0] IMPLICIT ExtendedCertificate }
class ExtendedCertificateOrCertificate (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'certificate': ('_TYPTR', ['Certificate'], 0),
        'extendedCertificate': ('_TYPTR', ['ExtendedCertificate'], 19) } )
    _context = globals ()
    _numcursori = 38

# ExtendedCertificatesAndCertificates ::= SET OF ExtendedCertificateOrCertificate
class ExtendedCertificatesAndCertificates (_api.ASN1SetOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SETOF', 0, (
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_END) ),38,
        ('_TYPTR', ['ExtendedCertificateOrCertificate'], 0) )
    _context = globals ()
    _numcursori = 1

# SignerInfo ::= SEQUENCE { version Version, issuerAndSerialNumber IssuerAndSerialNumber, digestAlgorithm DigestAlgorithmIdentifier, authenticatedAttributes [0] IMPLICIT Attributes OPTIONAL, digestEncryptionAlgorithm DigestEncryptionAlgorithmIdentifier, encryptedDigest EncryptedDigest, unauthenticatedAttributes [1] IMPLICIT Attributes OPTIONAL }
class SignerInfo (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'version': ('_TYPTR', ['Version'], 0),
        'issuerAndSerialNumber': ('_TYPTR', ['IssuerAndSerialNumber'], 1),
        'digestAlgorithm': ('_TYPTR', ['DigestAlgorithmIdentifier'], 3),
        'authenticatedAttributes': ('_TYPTR', ['Attributes'], 5),
        'digestEncryptionAlgorithm': ('_TYPTR', ['DigestEncryptionAlgorithmIdentifier'], 6),
        'encryptedDigest': ('_TYPTR', ['EncryptedDigest'], 8),
        'unauthenticatedAttributes': ('_TYPTR', ['Attributes'], 9) } )
    _context = globals ()
    _numcursori = 10

# SignerInfos ::= SET OF SignerInfo
class SignerInfos (_api.ASN1SetOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SETOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),10,
        ('_TYPTR', ['SignerInfo'], 0) )
    _context = globals ()
    _numcursori = 1

# SignedAndEnvelopedData ::= SEQUENCE { version Version, recipientInfos RecipientInfos, digestAlgorithms DigestAlgorithmIdentifiers, encryptedContentInfo EncryptedContentInfo, certificates [0] IMPLICIT ExtendedCertificatesAndCertificates OPTIONAL, crls [1] IMPLICIT CertificateRevocationLists OPTIONAL, signerInfos SignerInfos }
class SignedAndEnvelopedData (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'version': ('_TYPTR', ['Version'], 0),
        'recipientInfos': ('_TYPTR', ['RecipientInfos'], 1),
        'digestAlgorithms': ('_TYPTR', ['DigestAlgorithmIdentifiers'], 2),
        'encryptedContentInfo': ('_TYPTR', ['EncryptedContentInfo'], 3),
        'certificates': ('_TYPTR', ['ExtendedCertificatesAndCertificates'], 7),
        'crls': ('_TYPTR', ['CertificateRevocationLists'], 8),
        'signerInfos': ('_TYPTR', ['SignerInfos'], 9) } )
    _context = globals ()
    _numcursori = 10

# SignedData ::= SEQUENCE { version Version, digestAlgorithms DigestAlgorithmIdentifiers, contentInfo ContentInfo, certificates [0] IMPLICIT ExtendedCertificatesAndCertificates OPTIONAL, crls [1] IMPLICIT CertificateRevocationLists OPTIONAL, signerInfos SignerInfos }
class SignedData (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'version': ('_TYPTR', ['Version'], 0),
        'digestAlgorithms': ('_TYPTR', ['DigestAlgorithmIdentifiers'], 1),
        'contentInfo': ('_TYPTR', ['ContentInfo'], 2),
        'certificates': ('_TYPTR', ['ExtendedCertificatesAndCertificates'], 4),
        'crls': ('_TYPTR', ['CertificateRevocationLists'], 5),
        'signerInfos': ('_TYPTR', ['SignerInfos'], 6) } )
    _context = globals ()
    _numcursori = 7

#
# Variables with ASN.1 value assignments
#

# pkcs-7 OBJECT IDENTIFIER ::= {iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) 7}
pkcs_7 = _api.ASN1OID (bindata=[_api.der_format_OID ('1.2.840.113549.1.7')], context={})

# data OBJECT IDENTIFIER ::= {pkcs-7 1}
data = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_7.get()) + '.1')], context={})

# digestedData OBJECT IDENTIFIER ::= {pkcs-7 5}
digestedData = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_7.get()) + '.5')], context={})

# encryptedData OBJECT IDENTIFIER ::= {pkcs-7 6}
encryptedData = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_7.get()) + '.6')], context={})

# envelopedData OBJECT IDENTIFIER ::= {pkcs-7 3}
envelopedData = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_7.get()) + '.3')], context={})

# signedAndEnvelopedData OBJECT IDENTIFIER ::= {pkcs-7 4}
signedAndEnvelopedData = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_7.get()) + '.4')], context={})

# signedData OBJECT IDENTIFIER ::= {pkcs-7 2}
signedData = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_7.get()) + '.2')], context={})


# asn2quickder output for PKCS-7 ends here
