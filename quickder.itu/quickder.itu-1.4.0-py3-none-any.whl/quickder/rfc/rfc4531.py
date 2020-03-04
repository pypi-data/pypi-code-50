#
# asn2quickder output for RFC4351 -- automatically generated
#
# Read more about Quick `n' Easy DER on https://gitlab.com/arpa2/quick-der
#


#
# Import general definitions and package dependencies
#

from arpa2.quickder import api as _api

from rfc4511 import LDAPString


#
# Classes for ASN.1 type assignments
#

# TurnValue ::= SEQUENCE { mutual BOOLEAN DEFAULT FALSE, identifier LDAPString }
class TurnValue (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'mutual': ('_TYPTR', ['_api.ASN1Boolean'], 0),
        'identifier': ('_TYPTR', ['LDAPString'], 1) } )
    _context = globals ()
    _numcursori = 2

#
# Variables with ASN.1 value assignments
#


# asn2quickder output for RFC4351 ends here
