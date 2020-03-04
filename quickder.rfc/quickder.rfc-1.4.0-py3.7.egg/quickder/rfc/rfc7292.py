#
# asn2quickder output for RFC7292 -- automatically generated
#
# Read more about Quick `n' Easy DER on https://gitlab.com/arpa2/quick-der
#


#
# Import general definitions and package dependencies
#

from arpa2.quickder import api as _api

from rfc2315 import ContentInfo, DigestInfo
from rfc5208 import PrivateKeyInfo, EncryptedPrivateKeyInfo


#
# Classes for ASN.1 type assignments
#

# AuthenticatedSafe ::= SEQUENCE OF ContentInfo
class AuthenticatedSafe (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),2,
        ('_TYPTR', ['ContentInfo'], 0) )
    _context = globals ()
    _numcursori = 1

# CRLBag ::= SEQUENCE { crlId OBJECT IDENTIFIER, crltValue [0] EXPLICIT ANY }
class CRLBag (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'crlId': ('_TYPTR', ['_api.ASN1OID'], 0),
        'crltValue': ('_TYPTR', ['_api.ASN1Any'], 1) } )
    _context = globals ()
    _numcursori = 2

# CertBag ::= SEQUENCE { certId OBJECT IDENTIFIER, certValue [0] EXPLICIT ANY }
class CertBag (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'certId': ('_TYPTR', ['_api.ASN1OID'], 0),
        'certValue': ('_TYPTR', ['_api.ASN1Any'], 1) } )
    _context = globals ()
    _numcursori = 2

# KeyBag ::= PrivateKeyInfo
class KeyBag (PrivateKeyInfo):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['PrivateKeyInfo'], 0)
    _context = globals ()
    _numcursori = 5

# MacData ::= SEQUENCE { mac DigestInfo, macSalt OCTET STRING, iterations INTEGER DEFAULT 1 }
class MacData (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'mac': ('_TYPTR', ['DigestInfo'], 0),
        'macSalt': ('_TYPTR', ['_api.ASN1OctetString'], 3),
        'iterations': ('_TYPTR', ['_api.ASN1Integer'], 4) } )
    _context = globals ()
    _numcursori = 5

# PFX ::= SEQUENCE { version INTEGER, authSafe ContentInfo, macData MacData OPTIONAL }
class PFX (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'version': ('_TYPTR', ['_api.ASN1Integer'], 0),
        'authSafe': ('_TYPTR', ['ContentInfo'], 1),
        'macData': ('_TYPTR', ['MacData'], 3) } )
    _context = globals ()
    _numcursori = 8

# PKCS12Attribute ::= SEQUENCE { attrId OBJECT IDENTIFIER, attrValues SET OF ANY }
class PKCS12Attribute (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'attrId': ('_TYPTR', ['_api.ASN1OID'], 0),
        'attrValues': ('_SETOF', 1, (
            chr(_api.DER_PACK_ANY) +
            chr(_api.DER_PACK_END) ),1,
            ('_TYPTR', ['_api.ASN1Any'], 0) ) } )
    _context = globals ()
    _numcursori = 2

# PKCS8ShroudedKeyBag ::= EncryptedPrivateKeyInfo
class PKCS8ShroudedKeyBag (EncryptedPrivateKeyInfo):
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
    _recipe = ('_TYPTR', ['EncryptedPrivateKeyInfo'], 0)
    _context = globals ()
    _numcursori = 3

# SafeBag ::= SEQUENCE { bagId OBJECT IDENTIFIER, bagValue [0] EXPLICIT ANY, bagAttributes SET OF PKCS12Attribute OPTIONAL }
class SafeBag (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'bagId': ('_TYPTR', ['_api.ASN1OID'], 0),
        'bagValue': ('_TYPTR', ['_api.ASN1Any'], 1),
        'bagAttributes': ('_SETOF', 2, (
            chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
            chr(_api.DER_PACK_LEAVE) +
            chr(_api.DER_PACK_END) ),2,
            ('_TYPTR', ['PKCS12Attribute'], 0) ) } )
    _context = globals ()
    _numcursori = 3

# SafeContents ::= SEQUENCE OF SafeBag
class SafeContents (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),3,
        ('_TYPTR', ['SafeBag'], 0) )
    _context = globals ()
    _numcursori = 1

# SecretBag ::= SEQUENCE { secretTypeId OBJECT IDENTIFIER, secretValue [0] EXPLICIT ANY }
class SecretBag (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'secretTypeId': ('_TYPTR', ['_api.ASN1OID'], 0),
        'secretValue': ('_TYPTR', ['_api.ASN1Any'], 1) } )
    _context = globals ()
    _numcursori = 2

#
# Variables with ASN.1 value assignments
#

# rsadsi OBJECT IDENTIFIER ::= {iso(1) member-body(2) us(840) rsadsi(113549)}
rsadsi = _api.ASN1OID (bindata=[_api.der_format_OID ('1.2.840.113549')], context={})

# pkcs OBJECT IDENTIFIER ::= {rsadsi pkcs(1)}
pkcs = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (rsadsi.get()) + '.1')], context={})

# pkcs-12 OBJECT IDENTIFIER ::= {pkcs 12}
pkcs_12 = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs.get()) + '.12')], context={})

# bagtypes OBJECT IDENTIFIER ::= {pkcs-12 10 1}
bagtypes = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_12.get()) + '.10.1')], context={})

# pkcs-12PbeIds OBJECT IDENTIFIER ::= {pkcs-12 1}
pkcs_12PbeIds = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_12.get()) + '.1')], context={})

# pbeWithSHAAnd128BitRC2-CBC OBJECT IDENTIFIER ::= {pkcs-12PbeIds 5}
pbeWithSHAAnd128BitRC2_CBC = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_12PbeIds.get()) + '.5')], context={})

# pbeWithSHAAnd128BitRC4 OBJECT IDENTIFIER ::= {pkcs-12PbeIds 1}
pbeWithSHAAnd128BitRC4 = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_12PbeIds.get()) + '.1')], context={})

# pbeWithSHAAnd2-KeyTripleDES-CBC OBJECT IDENTIFIER ::= {pkcs-12PbeIds 4}
pbeWithSHAAnd2_KeyTripleDES_CBC = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_12PbeIds.get()) + '.4')], context={})

# pbeWithSHAAnd3-KeyTripleDES-CBC OBJECT IDENTIFIER ::= {pkcs-12PbeIds 3}
pbeWithSHAAnd3_KeyTripleDES_CBC = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_12PbeIds.get()) + '.3')], context={})

# pbeWithSHAAnd40BitRC4 OBJECT IDENTIFIER ::= {pkcs-12PbeIds 2}
pbeWithSHAAnd40BitRC4 = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_12PbeIds.get()) + '.2')], context={})

# pbewithSHAAnd40BitRC2-CBC OBJECT IDENTIFIER ::= {pkcs-12PbeIds 6}
pbewithSHAAnd40BitRC2_CBC = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_12PbeIds.get()) + '.6')], context={})


# asn2quickder output for RFC7292 ends here
