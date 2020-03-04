#
# asn2quickder output for RFC3062 -- automatically generated
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

# PasswdModifyRequestValue ::= SEQUENCE { userIdentity [0] OCTET STRING OPTIONAL, oldPasswd [1] OCTET STRING OPTIONAL, newPasswd [2] OCTET STRING OPTIONAL }
class PasswdModifyRequestValue (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'userIdentity': ('_TYPTR', ['_api.ASN1OctetString'], 0),
        'oldPasswd': ('_TYPTR', ['_api.ASN1OctetString'], 1),
        'newPasswd': ('_TYPTR', ['_api.ASN1OctetString'], 2) } )
    _context = globals ()
    _numcursori = 3

# PasswdModifyResponseValue ::= SEQUENCE { genPasswd [0] OCTET STRING OPTIONAL }
class PasswdModifyResponseValue (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'genPasswd': ('_TYPTR', ['_api.ASN1OctetString'], 0) } )
    _context = globals ()
    _numcursori = 1

#
# Variables with ASN.1 value assignments
#

# passwdModifyOID OBJECT IDENTIFIER ::= {1 3 6 1 4 1 4203 1 11 1}
passwdModifyOID = _api.ASN1OID (bindata=[_api.der_format_OID ('1.3.6.1.4.1.4203.1.11.1')], context={})


# asn2quickder output for RFC3062 ends here
