#
# asn2quickder output for PKCS-8 -- automatically generated
#
# Read more about Quick `n' Easy DER on https://gitlab.com/arpa2/quick-der
#


#
# Import general definitions and package dependencies
#

from arpa2.quickder import api as _api

from rfc2898 import AlgorithmIdentifier


#
# Classes for ASN.1 type assignments
#

# Context ::= SEQUENCE { contextType OBJECT IDENTIFIER, contextValues SET SIZE(1..MAX) OF ANY, fallback BOOLEAN DEFAULT FALSE }
class Context (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'contextType': ('_TYPTR', ['_api.ASN1OID'], 0),
        'contextValues': ('_SETOF', 1, (
            chr(_api.DER_PACK_ANY) +
            chr(_api.DER_PACK_END) ),1,
            ('_TYPTR', ['_api.ASN1Any'], 0) ),
        'fallback': ('_TYPTR', ['_api.ASN1Boolean'], 2) } )
    _context = globals ()
    _numcursori = 3

# Attribute ::= SEQUENCE { type OBJECT IDENTIFIER, values SET SIZE(0..MAX) OF ANY, valuesWithContext SET SIZE(1..MAX) OF SEQUENCE { value ANY, contextList SET SIZE(1..MAX) OF Context } OPTIONAL }
class Attribute (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'type': ('_TYPTR', ['_api.ASN1OID'], 0),
        'values': ('_SETOF', 1, (
            chr(_api.DER_PACK_ANY) +
            chr(_api.DER_PACK_END) ),1,
            ('_TYPTR', ['_api.ASN1Any'], 0) ),
        'valuesWithContext': ('_SETOF', 2, (
            chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
            chr(_api.DER_PACK_ANY) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
            chr(_api.DER_PACK_LEAVE) +
            chr(_api.DER_PACK_END) ),2,
            ('_NAMED', {
                'value': ('_TYPTR', ['_api.ASN1Any'], 0),
                'contextList': ('_SETOF', 1, (
                    chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
                    chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
                    chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
                    chr(_api.DER_PACK_OPTIONAL) +
                    chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
                    chr(_api.DER_PACK_LEAVE) +
                    chr(_api.DER_PACK_END) ),3,
                    ('_TYPTR', ['Context'], 0) ) } ) ) } )
    _context = globals ()
    _numcursori = 3

# Attributes ::= SET OF Attribute
class Attributes (_api.ASN1SetOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SETOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),3,
        ('_TYPTR', ['Attribute'], 0) )
    _context = globals ()
    _numcursori = 1

# EncryptedData ::= OCTET STRING
class EncryptedData (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# EncryptedPrivateKeyInfo ::= SEQUENCE { encryptionAlgorithm AlgorithmIdentifier, encryptedData EncryptedData }
class EncryptedPrivateKeyInfo (_api.ASN1ConstructedType):
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
        'encryptionAlgorithm': ('_TYPTR', ['AlgorithmIdentifier'], 0),
        'encryptedData': ('_TYPTR', ['EncryptedData'], 2) } )
    _context = globals ()
    _numcursori = 3

# KeyEncryptionAlgorithms ::= ANY
class KeyEncryptionAlgorithms (_api.ASN1Any):
    _der_packer = (
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Any'], 0)
    _context = globals ()
    _numcursori = 1

# PrivateKey ::= OCTET STRING
class PrivateKey (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# PrivateKeyAlgorithms ::= ANY
class PrivateKeyAlgorithms (_api.ASN1Any):
    _der_packer = (
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Any'], 0)
    _context = globals ()
    _numcursori = 1

# Version ::= INTEGER
class Version (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# PrivateKeyInfo ::= SEQUENCE { version Version, privateKeyAlgorithm AlgorithmIdentifier, privateKey PrivateKey, attributes [0] Attributes OPTIONAL }
class PrivateKeyInfo (_api.ASN1ConstructedType):
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
    _recipe = ('_NAMED', {
        'version': ('_TYPTR', ['Version'], 0),
        'privateKeyAlgorithm': ('_TYPTR', ['AlgorithmIdentifier'], 1),
        'privateKey': ('_TYPTR', ['PrivateKey'], 3),
        'attributes': ('_TYPTR', ['Attributes'], 4) } )
    _context = globals ()
    _numcursori = 5

#
# Variables with ASN.1 value assignments
#


# asn2quickder output for PKCS-8 ends here
