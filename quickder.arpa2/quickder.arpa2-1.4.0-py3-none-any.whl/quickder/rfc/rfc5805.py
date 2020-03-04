#
# asn2quickder output for RFC5805 -- automatically generated
#
# Read more about Quick `n' Easy DER on https://gitlab.com/arpa2/quick-der
#


#
# Import general definitions and package dependencies
#

from arpa2.quickder import api as _api

from rfc4511 import MessageID, Controls


#
# Classes for ASN.1 type assignments
#

# TxnEndReq ::= SEQUENCE { commit BOOLEAN DEFAULT TRUE, identifier OCTET STRING }
class TxnEndReq (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'commit': ('_TYPTR', ['_api.ASN1Boolean'], 0),
        'identifier': ('_TYPTR', ['_api.ASN1OctetString'], 1) } )
    _context = globals ()
    _numcursori = 2

# TxnEndRes ::= SEQUENCE { messageID MessageID OPTIONAL, updatesControls SEQUENCE OF updateControls SEQUENCE { messageID MessageID, controls Controls } OPTIONAL }
class TxnEndRes (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'messageID': ('_TYPTR', ['MessageID'], 0),
        'updatesControls': ('_SEQOF', 1, (
            chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
            chr(_api.DER_PACK_LEAVE) +
            chr(_api.DER_PACK_END) ),2,
            ('_NAMED', {
                'messageID': ('_TYPTR', ['MessageID'], 0),
                'controls': ('_TYPTR', ['Controls'], 1) } ) ) } )
    _context = globals ()
    _numcursori = 2

#
# Variables with ASN.1 value assignments
#


# asn2quickder output for RFC5805 ends here
