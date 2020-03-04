#
# asn2quickder output for RFC2898 -- automatically generated
#
# Read more about Quick `n' Easy DER on https://gitlab.com/arpa2/quick-der
#


#
# Import general definitions and package dependencies
#

from arpa2.quickder import api as _api

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

# PBEParameter ::= SEQUENCE { salt OCTET STRING SIZE(8), iterationCount INTEGER }
class PBEParameter (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'salt': ('_TYPTR', ['_api.ASN1OctetString'], 0),
        'iterationCount': ('_TYPTR', ['_api.ASN1Integer'], 1) } )
    _context = globals ()
    _numcursori = 2

# PBES2-params ::= SEQUENCE { keyDerivationFunc AlgorithmIdentifier, encryptionScheme AlgorithmIdentifier }
class PBES2_params (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'keyDerivationFunc': ('_TYPTR', ['AlgorithmIdentifier'], 0),
        'encryptionScheme': ('_TYPTR', ['AlgorithmIdentifier'], 2) } )
    _context = globals ()
    _numcursori = 4

# PBKDF2-params ::= SEQUENCE { salt CHOICE { specified OCTET STRING, otherSource AlgorithmIdentifier }, iterationCount INTEGER (1..MAX), keyLength INTEGER (1..MAX) OPTIONAL, prf AlgorithmIdentifier DEFAULT algid-hmacWithSHA1 }
class PBKDF2_params (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'salt': ('_NAMED', {
            'specified': ('_TYPTR', ['_api.ASN1OctetString'], 0),
            'otherSource': ('_TYPTR', ['AlgorithmIdentifier'], 1) } ),
        'iterationCount': ('_TYPTR', ['_api.ASN1Integer'], 3),
        'keyLength': ('_TYPTR', ['_api.ASN1Integer'], 4),
        'prf': ('_TYPTR', ['AlgorithmIdentifier'], 5) } )
    _context = globals ()
    _numcursori = 7

# PBKDF2Algorithms ::= ANY
class PBKDF2Algorithms (_api.ASN1Any):
    _der_packer = (
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Any'], 0)
    _context = globals ()
    _numcursori = 1

# PBMAC1-params ::= SEQUENCE { keyDerivationFunc AlgorithmIdentifier, messageAuthScheme AlgorithmIdentifier }
class PBMAC1_params (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'keyDerivationFunc': ('_TYPTR', ['AlgorithmIdentifier'], 0),
        'messageAuthScheme': ('_TYPTR', ['AlgorithmIdentifier'], 2) } )
    _context = globals ()
    _numcursori = 4

# RC2-CBC-Parameter ::= SEQUENCE { rc2ParameterVersion INTEGER OPTIONAL, iv OCTET STRING SIZE(8) }
class RC2_CBC_Parameter (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'rc2ParameterVersion': ('_TYPTR', ['_api.ASN1Integer'], 0),
        'iv': ('_TYPTR', ['_api.ASN1OctetString'], 1) } )
    _context = globals ()
    _numcursori = 2

# RC5-CBC-Parameters ::= SEQUENCE { version INTEGER, rounds INTEGER (8..127), blockSizeInBits INTEGER, iv OCTET STRING OPTIONAL }
class RC5_CBC_Parameters (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'version': ('_TYPTR', ['_api.ASN1Integer'], 0),
        'rounds': ('_TYPTR', ['_api.ASN1Integer'], 1),
        'blockSizeInBits': ('_TYPTR', ['_api.ASN1Integer'], 2),
        'iv': ('_TYPTR', ['_api.ASN1OctetString'], 3) } )
    _context = globals ()
    _numcursori = 4

#
# Variables with ASN.1 value assignments
#

# rsadsi OBJECT IDENTIFIER ::= {iso(1) member-body(2) us(840) 113549}
rsadsi = _api.ASN1OID (bindata=[_api.der_format_OID ('1.2.840.113549')], context={})

# encryptionAlgorithm OBJECT IDENTIFIER ::= {rsadsi 3}
encryptionAlgorithm = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (rsadsi.get()) + '.3')], context={})

# des-EDE3-CBC OBJECT IDENTIFIER ::= {encryptionAlgorithm 7}
des_EDE3_CBC = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (encryptionAlgorithm.get()) + '.7')], context={})

# desCBC OBJECT IDENTIFIER ::= {iso(1) identified-organization(3) oiw(14) secsig(3) algorithms(2) 7}
desCBC = _api.ASN1OID (bindata=[_api.der_format_OID ('1.3.14.3.2.7')], context={})

# digestAlgorithm OBJECT IDENTIFIER ::= {rsadsi 2}
digestAlgorithm = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (rsadsi.get()) + '.2')], context={})

# pkcs OBJECT IDENTIFIER ::= {rsadsi 1}
pkcs = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (rsadsi.get()) + '.1')], context={})

# pkcs-5 OBJECT IDENTIFIER ::= {pkcs 5}
pkcs_5 = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs.get()) + '.5')], context={})

# id-PBES2 OBJECT IDENTIFIER ::= {pkcs-5 13}
id_PBES2 = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_5.get()) + '.13')], context={})

# id-PBKDF2 OBJECT IDENTIFIER ::= {pkcs-5 12}
id_PBKDF2 = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_5.get()) + '.12')], context={})

# id-PBMAC1 OBJECT IDENTIFIER ::= {pkcs-5 14}
id_PBMAC1 = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_5.get()) + '.14')], context={})

# id-hmacWithSHA1 OBJECT IDENTIFIER ::= {digestAlgorithm 7}
id_hmacWithSHA1 = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (digestAlgorithm.get()) + '.7')], context={})

# pbeWithMD2AndDES-CBC OBJECT IDENTIFIER ::= {pkcs-5 1}
pbeWithMD2AndDES_CBC = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_5.get()) + '.1')], context={})

# pbeWithMD2AndRC2-CBC OBJECT IDENTIFIER ::= {pkcs-5 4}
pbeWithMD2AndRC2_CBC = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_5.get()) + '.4')], context={})

# pbeWithMD5AndDES-CBC OBJECT IDENTIFIER ::= {pkcs-5 3}
pbeWithMD5AndDES_CBC = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_5.get()) + '.3')], context={})

# pbeWithMD5AndRC2-CBC OBJECT IDENTIFIER ::= {pkcs-5 6}
pbeWithMD5AndRC2_CBC = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_5.get()) + '.6')], context={})

# pbeWithSHA1AndDES-CBC OBJECT IDENTIFIER ::= {pkcs-5 10}
pbeWithSHA1AndDES_CBC = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_5.get()) + '.10')], context={})

# pbeWithSHA1AndRC2-CBC OBJECT IDENTIFIER ::= {pkcs-5 11}
pbeWithSHA1AndRC2_CBC = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (pkcs_5.get()) + '.11')], context={})

# rc2CBC OBJECT IDENTIFIER ::= {encryptionAlgorithm 2}
rc2CBC = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (encryptionAlgorithm.get()) + '.2')], context={})

# rc5-CBC-PAD OBJECT IDENTIFIER ::= {encryptionAlgorithm 9}
rc5_CBC_PAD = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (encryptionAlgorithm.get()) + '.9')], context={})


# asn2quickder output for RFC2898 ends here
