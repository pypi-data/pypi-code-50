#
# asn2quickder output for SPNEGOASNOneSpec -- automatically generated
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

# ContextFlags ::= BIT STRING { delegFlag (0), mutualFlag (1), replayFlag (2), sequenceFlag (3), anonFlag (4), confFlag (5), integFlag (6) } SIZE(32)
class ContextFlags (_api.ASN1BitString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1BitString'], 0)
    _context = globals ()
    _numcursori = 1

# MechType ::= OBJECT IDENTIFIER
class MechType (_api.ASN1OID):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OID'], 0)
    _context = globals ()
    _numcursori = 1

# MechTypeList ::= SEQUENCE OF MechType
class MechTypeList (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_END) ),1,
        ('_TYPTR', ['MechType'], 0) )
    _context = globals ()
    _numcursori = 1

# NegTokenInit ::= SEQUENCE { mechTypes [0] MechTypeList, reqFlags [1] ContextFlags OPTIONAL, mechToken [2] OCTET STRING OPTIONAL, mechListMIC [3] OCTET STRING OPTIONAL, ... }
class NegTokenInit (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'mechTypes': ('_TYPTR', ['MechTypeList'], 0),
        'reqFlags': ('_TYPTR', ['ContextFlags'], 1),
        'mechToken': ('_TYPTR', ['_api.ASN1OctetString'], 2),
        'mechListMIC': ('_TYPTR', ['_api.ASN1OctetString'], 3) } )
    _context = globals ()
    _numcursori = 4

# NegTokenResp ::= SEQUENCE { negState [0] ENUMERATED { accept-completed (0), accept-incomplete (1), reject (2), request-mic (3) } OPTIONAL, supportedMech [1] MechType OPTIONAL, responseToken [2] OCTET STRING OPTIONAL, mechListMIC [3] OCTET STRING OPTIONAL, ... }
class NegTokenResp (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'negState': ('_TYPTR', ['_api.ASN1Enumerated'], 0),
        'supportedMech': ('_TYPTR', ['MechType'], 1),
        'responseToken': ('_TYPTR', ['_api.ASN1OctetString'], 2),
        'mechListMIC': ('_TYPTR', ['_api.ASN1OctetString'], 3) } )
    _context = globals ()
    _numcursori = 4

# NegotiationToken ::= CHOICE { negTokenInit [0] NegTokenInit, negTokenResp [1] NegTokenResp }
class NegotiationToken (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'negTokenInit': ('_TYPTR', ['NegTokenInit'], 0),
        'negTokenResp': ('_TYPTR', ['NegTokenResp'], 4) } )
    _context = globals ()
    _numcursori = 8

#
# Variables with ASN.1 value assignments
#


# asn2quickder output for SPNEGOASNOneSpec ends here
