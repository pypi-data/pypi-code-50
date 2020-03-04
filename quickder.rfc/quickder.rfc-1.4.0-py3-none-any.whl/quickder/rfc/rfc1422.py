#
# asn2quickder output for RFC1422 -- automatically generated
#
# Read more about Quick `n' Easy DER on https://gitlab.com/arpa2/quick-der
#


#
# Import general definitions and package dependencies
#

from arpa2.quickder import api as _api

from rfc3280 import Name


#
# Classes for ASN.1 type assignments
#

# AlgorithmIdentifier ::= SEQUENCE { algorithm OBJECT IDENTIFIER, parameters ANY OPTIONAL }
class AlgorithmIdentifier (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'algorithm': ('_TYPTR', ['_api.ASN1OID'], 0),
        'parameters': ('_TYPTR', ['_api.ASN1Any'], 1) } )
    _context = globals ()
    _numcursori = 2

# CertificateSerialNumber ::= INTEGER
class CertificateSerialNumber (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# CRLEntry ::= SEQUENCE { userCertificate CertificateSerialNumber, revocationDate UTCTime }
class CRLEntry (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'userCertificate': ('_TYPTR', ['CertificateSerialNumber'], 0),
        'revocationDate': ('_TYPTR', ['_api.ASN1UTCTime'], 1) } )
    _context = globals ()
    _numcursori = 2

# Validity ::= SEQUENCE { notBefore UTCTime, notAfter UTCTime }
class Validity (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'notBefore': ('_TYPTR', ['_api.ASN1UTCTime'], 0),
        'notAfter': ('_TYPTR', ['_api.ASN1UTCTime'], 1) } )
    _context = globals ()
    _numcursori = 2

# SubjectPublicKeyInfo ::= SEQUENCE { algorithm AlgorithmIdentifier, subjectPublicKey BIT STRING }
class SubjectPublicKeyInfo (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'algorithm': ('_TYPTR', ['AlgorithmIdentifier'], 0),
        'subjectPublicKey': ('_TYPTR', ['_api.ASN1BitString'], 2) } )
    _context = globals ()
    _numcursori = 3

# Version ::= INTEGER { v1988 (0) }
class Version (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# Certificate ::= SEQUENCE { version [0] Version DEFAULT v1988, serialNumber CertificateSerialNumber, signature AlgorithmIdentifier, issuer Name, validity Validity, subject Name, subjectPublicKeyInfo SubjectPublicKeyInfo }
class Certificate (_api.ASN1ConstructedType):
    _der_packer = (
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
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
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
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'version': ('_TYPTR', ['Version'], 0),
        'serialNumber': ('_TYPTR', ['CertificateSerialNumber'], 1),
        'signature': ('_TYPTR', ['AlgorithmIdentifier'], 2),
        'issuer': ('_TYPTR', ['Name'], 4),
        'validity': ('_TYPTR', ['Validity'], 5),
        'subject': ('_TYPTR', ['Name'], 7),
        'subjectPublicKeyInfo': ('_TYPTR', ['SubjectPublicKeyInfo'], 8) } )
    _context = globals ()
    _numcursori = 11

# CertificateRevocationList ::= SEQUENCE { signature AlgorithmIdentifier, issuer Name, lastUpdate UTCTime, nextUpdate UTCTime, revokedCertificates SEQUENCE OF CRLEntry OPTIONAL }
class CertificateRevocationList (_api.ASN1ConstructedType):
    _der_packer = (
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
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'signature': ('_TYPTR', ['AlgorithmIdentifier'], 0),
        'issuer': ('_TYPTR', ['Name'], 2),
        'lastUpdate': ('_TYPTR', ['_api.ASN1UTCTime'], 3),
        'nextUpdate': ('_TYPTR', ['_api.ASN1UTCTime'], 4),
        'revokedCertificates': ('_SEQOF', 5, (
            chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
            chr(_api.DER_PACK_LEAVE) +
            chr(_api.DER_PACK_END) ),2,
            ('_TYPTR', ['CRLEntry'], 0) ) } )
    _context = globals ()
    _numcursori = 6

#
# Variables with ASN.1 value assignments
#


# asn2quickder output for RFC1422 ends here
