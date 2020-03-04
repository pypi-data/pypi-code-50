#
# asn2quickder output for RFC3909 -- automatically generated
#
# Read more about Quick `n' Easy DER on https://gitlab.com/arpa2/quick-der
#


#
# Import general definitions and package dependencies
#

from arpa2.quickder import api as _api

from rfc4511 import MessageID


#
# Classes for ASN.1 type assignments
#

# CancelRequestValue ::= SEQUENCE { cancelID MessageID }
class CancelRequestValue (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'cancelID': ('_TYPTR', ['MessageID'], 0) } )
    _context = globals ()
    _numcursori = 1

#
# Variables with ASN.1 value assignments
#


# asn2quickder output for RFC3909 ends here
