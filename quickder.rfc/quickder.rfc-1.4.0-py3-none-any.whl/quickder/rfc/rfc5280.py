#
# asn2quickder output for RFC5280 -- automatically generated
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

# OtherName ::= SEQUENCE { type-id OBJECT IDENTIFIER, value [0] EXPLICIT ANY }
class OtherName (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'type_id': ('_TYPTR', ['_api.ASN1OID'], 0),
        'value': ('_TYPTR', ['_api.ASN1Any'], 1) } )
    _context = globals ()
    _numcursori = 2

# DirectoryString ::= CHOICE { teletexString TeletexString SIZE(1..MAX), printableString PrintableString SIZE(1..MAX), universalString UniversalString SIZE(1..MAX), utf8String UTF8String SIZE(1..MAX), bmpString BMPString SIZE(1..MAX) }
class DirectoryString (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_TELETEXSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_PRINTABLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UNIVERSALSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'teletexString': ('_TYPTR', ['_api.ASN1TeletexString'], 0),
        'printableString': ('_TYPTR', ['_api.ASN1PrintableString'], 1),
        'universalString': ('_TYPTR', ['_api.ASN1UniversalString'], 2),
        'utf8String': ('_TYPTR', ['_api.ASN1UTF8String'], 3),
        'bmpString': 4 } )
    _context = globals ()
    _numcursori = 5

# EDIPartyName ::= SEQUENCE { nameAssigner [0] DirectoryString OPTIONAL, partyName [1] DirectoryString }
class EDIPartyName (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_TELETEXSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_PRINTABLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UNIVERSALSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_TELETEXSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_PRINTABLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UNIVERSALSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'nameAssigner': ('_TYPTR', ['DirectoryString'], 0),
        'partyName': ('_TYPTR', ['DirectoryString'], 5) } )
    _context = globals ()
    _numcursori = 10

# AttributeType ::= OBJECT IDENTIFIER
class AttributeType (_api.ASN1OID):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OID'], 0)
    _context = globals ()
    _numcursori = 1

# AttributeValue ::= ANY
class AttributeValue (_api.ASN1Any):
    _der_packer = (
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Any'], 0)
    _context = globals ()
    _numcursori = 1

# AttributeTypeAndValue ::= SEQUENCE { type AttributeType, value AttributeValue }
class AttributeTypeAndValue (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'type': ('_TYPTR', ['AttributeType'], 0),
        'value': ('_TYPTR', ['AttributeValue'], 1) } )
    _context = globals ()
    _numcursori = 2

# RelativeDistinguishedName ::= SET SIZE(1..MAX) OF AttributeTypeAndValue
class RelativeDistinguishedName (_api.ASN1SetOf):
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

# RDNSequence ::= SEQUENCE OF RelativeDistinguishedName
class RDNSequence (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_END) ),1,
        ('_TYPTR', ['RelativeDistinguishedName'], 0) )
    _context = globals ()
    _numcursori = 1

# Name ::= CHOICE { rdnSequence RDNSequence }
class Name (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'rdnSequence': ('_TYPTR', ['RDNSequence'], 0) } )
    _context = globals ()
    _numcursori = 1

# GeneralName ::= CHOICE { otherName [0] OtherName, rfc822Name [1] IA5String, dNSName [2] IA5String, directoryName [4] Name, ediPartyName [5] EDIPartyName, uniformResourceIdentifier [6] IA5String, iPAddress [7] OCTET STRING, registeredID [8] OBJECT IDENTIFIER }
class GeneralName (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(5)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_TELETEXSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_PRINTABLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UNIVERSALSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_TELETEXSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_PRINTABLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UNIVERSALSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(6)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(7)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(8)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'otherName': ('_TYPTR', ['OtherName'], 0),
        'rfc822Name': ('_TYPTR', ['_api.ASN1IA5String'], 2),
        'dNSName': ('_TYPTR', ['_api.ASN1IA5String'], 3),
        'directoryName': ('_TYPTR', ['Name'], 4),
        'ediPartyName': ('_TYPTR', ['EDIPartyName'], 5),
        'uniformResourceIdentifier': ('_TYPTR', ['_api.ASN1IA5String'], 15),
        'iPAddress': ('_TYPTR', ['_api.ASN1OctetString'], 16),
        'registeredID': ('_TYPTR', ['_api.ASN1OID'], 17) } )
    _context = globals ()
    _numcursori = 18

# AccessDescription ::= SEQUENCE { accessMethod OBJECT IDENTIFIER, accessLocation GeneralName }
class AccessDescription (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(5)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_TELETEXSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_PRINTABLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UNIVERSALSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_TELETEXSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_PRINTABLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UNIVERSALSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(6)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(7)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(8)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'accessMethod': ('_TYPTR', ['_api.ASN1OID'], 0),
        'accessLocation': ('_TYPTR', ['GeneralName'], 1) } )
    _context = globals ()
    _numcursori = 19

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

# Attribute ::= SEQUENCE { type AttributeType, values SET OF AttributeValue }
class Attribute (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'type': ('_TYPTR', ['AttributeType'], 0),
        'values': ('_SETOF', 1, (
            chr(_api.DER_PACK_ANY) +
            chr(_api.DER_PACK_END) ),1,
            ('_TYPTR', ['AttributeValue'], 0) ) } )
    _context = globals ()
    _numcursori = 2

# AuthorityInfoAccessSyntax ::= SEQUENCE SIZE(1..MAX) OF AccessDescription
class AuthorityInfoAccessSyntax (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(5)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_TELETEXSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_PRINTABLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UNIVERSALSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_TELETEXSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_PRINTABLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UNIVERSALSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(6)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(7)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(8)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),19,
        ('_TYPTR', ['AccessDescription'], 0) )
    _context = globals ()
    _numcursori = 1

# KeyIdentifier ::= OCTET STRING
class KeyIdentifier (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# GeneralNames ::= SEQUENCE SIZE(1..MAX) OF GeneralName
class GeneralNames (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(5)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_TELETEXSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_PRINTABLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UNIVERSALSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_TELETEXSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_PRINTABLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UNIVERSALSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(6)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(7)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(8)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_END) ),18,
        ('_TYPTR', ['GeneralName'], 0) )
    _context = globals ()
    _numcursori = 1

# CertificateSerialNumber ::= INTEGER
class CertificateSerialNumber (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# AuthorityKeyIdentifier ::= SEQUENCE { keyIdentifier [0] KeyIdentifier OPTIONAL, authorityCertIssuer [1] GeneralNames OPTIONAL, authorityCertSerialNumber [2] CertificateSerialNumber OPTIONAL }
class AuthorityKeyIdentifier (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'keyIdentifier': ('_TYPTR', ['KeyIdentifier'], 0),
        'authorityCertIssuer': ('_TYPTR', ['GeneralNames'], 1),
        'authorityCertSerialNumber': ('_TYPTR', ['CertificateSerialNumber'], 2) } )
    _context = globals ()
    _numcursori = 3

# CRLNumber ::= INTEGER (0..MAX)
class CRLNumber (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# BaseCRLNumber ::= CRLNumber
class BaseCRLNumber (CRLNumber):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['CRLNumber'], 0)
    _context = globals ()
    _numcursori = 1

# BaseDistance ::= INTEGER (0..MAX)
class BaseDistance (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# BasicConstraints ::= SEQUENCE { cA BOOLEAN DEFAULT FALSE, pathLenConstraint INTEGER (0..MAX) OPTIONAL }
class BasicConstraints (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'cA': ('_TYPTR', ['_api.ASN1Boolean'], 0),
        'pathLenConstraint': ('_TYPTR', ['_api.ASN1Integer'], 1) } )
    _context = globals ()
    _numcursori = 2

# CPSuri ::= IA5String
class CPSuri (_api.ASN1IA5String):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1IA5String'], 0)
    _context = globals ()
    _numcursori = 1

# ReasonFlags ::= BIT STRING { unused (0), keyCompromise (1), cACompromise (2), affiliationChanged (3), superseded (4), cessationOfOperation (5), certificateHold (6), privilegeWithdrawn (7), aACompromise (8) }
class ReasonFlags (_api.ASN1BitString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1BitString'], 0)
    _context = globals ()
    _numcursori = 1

# DistributionPointName ::= CHOICE { fullName [0] GeneralNames, nameRelativeToCRLIssuer [1] RelativeDistinguishedName }
class DistributionPointName (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'fullName': ('_TYPTR', ['GeneralNames'], 0),
        'nameRelativeToCRLIssuer': ('_TYPTR', ['RelativeDistinguishedName'], 1) } )
    _context = globals ()
    _numcursori = 2

# DistributionPoint ::= SEQUENCE { distributionPoint [0] DistributionPointName OPTIONAL, reasons [1] ReasonFlags OPTIONAL, cRLIssuer [2] GeneralNames OPTIONAL }
class DistributionPoint (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'distributionPoint': ('_TYPTR', ['DistributionPointName'], 0),
        'reasons': ('_TYPTR', ['ReasonFlags'], 2),
        'cRLIssuer': ('_TYPTR', ['GeneralNames'], 3) } )
    _context = globals ()
    _numcursori = 4

# CRLDistributionPoints ::= SEQUENCE SIZE(1..MAX) OF DistributionPoint
class CRLDistributionPoints (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),4,
        ('_TYPTR', ['DistributionPoint'], 0) )
    _context = globals ()
    _numcursori = 1

# CRLReason ::= ENUMERATED { unspecified (0), keyCompromise (1), cACompromise (2), affiliationChanged (3), superseded (4), cessationOfOperation (5), certificateHold (6), removeFromCRL (8), privilegeWithdrawn (9), aACompromise (10) }
class CRLReason (_api.ASN1Enumerated):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Enumerated'], 0)
    _context = globals ()
    _numcursori = 1

# CertPolicyId ::= OBJECT IDENTIFIER
class CertPolicyId (_api.ASN1OID):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OID'], 0)
    _context = globals ()
    _numcursori = 1

# Time ::= CHOICE { utcTime UTCTime, generalTime GeneralizedTime }
class Time (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'utcTime': ('_TYPTR', ['_api.ASN1UTCTime'], 0),
        'generalTime': ('_TYPTR', ['_api.ASN1GeneralizedTime'], 1) } )
    _context = globals ()
    _numcursori = 2

# Validity ::= SEQUENCE { notBefore Time, notAfter Time }
class Validity (_api.ASN1ConstructedType):
    _der_packer = (
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
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'notBefore': ('_TYPTR', ['Time'], 0),
        'notAfter': ('_TYPTR', ['Time'], 2) } )
    _context = globals ()
    _numcursori = 4

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

# Version ::= INTEGER { v1 (0), v2 (1), v3 (2) }
class Version (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# Extension ::= SEQUENCE { extnID OBJECT IDENTIFIER, critical BOOLEAN DEFAULT FALSE, extnValue OCTET STRING }
class Extension (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'extnID': ('_TYPTR', ['_api.ASN1OID'], 0),
        'critical': ('_TYPTR', ['_api.ASN1Boolean'], 1),
        'extnValue': ('_TYPTR', ['_api.ASN1OctetString'], 2) } )
    _context = globals ()
    _numcursori = 3

# Extensions ::= SEQUENCE SIZE(1..MAX) OF Extension
class Extensions (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),3,
        ('_TYPTR', ['Extension'], 0) )
    _context = globals ()
    _numcursori = 1

# UniqueIdentifier ::= BIT STRING
class UniqueIdentifier (_api.ASN1BitString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1BitString'], 0)
    _context = globals ()
    _numcursori = 1

# TBSCertificate ::= SEQUENCE { version [0] EXPLICIT Version DEFAULT v1, serialNumber CertificateSerialNumber, signature AlgorithmIdentifier, issuer Name, validity Validity, subject Name, subjectPublicKeyInfo SubjectPublicKeyInfo, issuerUniqueID [1] IMPLICIT UniqueIdentifier OPTIONAL, subjectUniqueID [2] IMPLICIT UniqueIdentifier OPTIONAL, extensions [3] EXPLICIT Extensions OPTIONAL }
class TBSCertificate (_api.ASN1ConstructedType):
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
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'version': ('_TYPTR', ['Version'], 0),
        'serialNumber': ('_TYPTR', ['CertificateSerialNumber'], 1),
        'signature': ('_TYPTR', ['AlgorithmIdentifier'], 2),
        'issuer': ('_TYPTR', ['Name'], 4),
        'validity': ('_TYPTR', ['Validity'], 5),
        'subject': ('_TYPTR', ['Name'], 9),
        'subjectPublicKeyInfo': ('_TYPTR', ['SubjectPublicKeyInfo'], 10),
        'issuerUniqueID': ('_TYPTR', ['UniqueIdentifier'], 13),
        'subjectUniqueID': ('_TYPTR', ['UniqueIdentifier'], 14),
        'extensions': ('_TYPTR', ['Extensions'], 15) } )
    _context = globals ()
    _numcursori = 16

# Certificate ::= SEQUENCE { tbsCertificate TBSCertificate, signatureAlgorithm AlgorithmIdentifier, signatureValue BIT STRING }
class Certificate (_api.ASN1ConstructedType):
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
    _recipe = ('_NAMED', {
        'tbsCertificate': ('_TYPTR', ['TBSCertificate'], 0),
        'signatureAlgorithm': ('_TYPTR', ['AlgorithmIdentifier'], 16),
        'signatureValue': ('_TYPTR', ['_api.ASN1BitString'], 18) } )
    _context = globals ()
    _numcursori = 19

# CertificateIssuer ::= GeneralNames
class CertificateIssuer (GeneralNames):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['GeneralNames'], 0)
    _context = globals ()
    _numcursori = 1

# TBSCertList ::= SEQUENCE { version Version OPTIONAL, signature AlgorithmIdentifier, issuer Name, thisUpdate Time, nextUpdate Time OPTIONAL, revokedCertificates SEQUENCE OF SEQUENCE { userCertificate CertificateSerialNumber, revocationDate Time, crlEntryExtensions Extensions OPTIONAL } OPTIONAL, crlExtensions [0] EXPLICIT Extensions OPTIONAL }
class TBSCertList (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'version': ('_TYPTR', ['Version'], 0),
        'signature': ('_TYPTR', ['AlgorithmIdentifier'], 1),
        'issuer': ('_TYPTR', ['Name'], 3),
        'thisUpdate': ('_TYPTR', ['Time'], 4),
        'nextUpdate': ('_TYPTR', ['Time'], 6),
        'revokedCertificates': ('_SEQOF', 8, (
            chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
            chr(_api.DER_PACK_CHOICE_BEGIN) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
            chr(_api.DER_PACK_CHOICE_END) +
            chr(_api.DER_PACK_OPTIONAL) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
            chr(_api.DER_PACK_LEAVE) +
            chr(_api.DER_PACK_END) ),4,
            ('_NAMED', {
                'userCertificate': ('_TYPTR', ['CertificateSerialNumber'], 0),
                'revocationDate': ('_TYPTR', ['Time'], 1),
                'crlEntryExtensions': ('_TYPTR', ['Extensions'], 3) } ) ),
        'crlExtensions': ('_TYPTR', ['Extensions'], 9) } )
    _context = globals ()
    _numcursori = 10

# CertificateList ::= SEQUENCE { tbsCertList TBSCertList, signatureAlgorithm AlgorithmIdentifier, signatureValue BIT STRING }
class CertificateList (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTCTIME) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
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
    _recipe = ('_NAMED', {
        'tbsCertList': ('_TYPTR', ['TBSCertList'], 0),
        'signatureAlgorithm': ('_TYPTR', ['AlgorithmIdentifier'], 10),
        'signatureValue': ('_TYPTR', ['_api.ASN1BitString'], 12) } )
    _context = globals ()
    _numcursori = 13

# PolicyQualifierId ::= OBJECT IDENTIFIER
class PolicyQualifierId (_api.ASN1OID):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OID'], 0)
    _context = globals ()
    _numcursori = 1

# PolicyQualifierInfo ::= SEQUENCE { policyQualifierId PolicyQualifierId, qualifier ANY }
class PolicyQualifierInfo (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'policyQualifierId': ('_TYPTR', ['PolicyQualifierId'], 0),
        'qualifier': ('_TYPTR', ['_api.ASN1Any'], 1) } )
    _context = globals ()
    _numcursori = 2

# PolicyInformation ::= SEQUENCE { policyIdentifier CertPolicyId, policyQualifiers SEQUENCE SIZE(1..MAX) OF PolicyQualifierInfo OPTIONAL }
class PolicyInformation (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'policyIdentifier': ('_TYPTR', ['CertPolicyId'], 0),
        'policyQualifiers': ('_SEQOF', 1, (
            chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
            chr(_api.DER_PACK_ANY) +
            chr(_api.DER_PACK_LEAVE) +
            chr(_api.DER_PACK_END) ),2,
            ('_TYPTR', ['PolicyQualifierInfo'], 0) ) } )
    _context = globals ()
    _numcursori = 2

# CertificatePolicies ::= SEQUENCE SIZE(1..MAX) OF PolicyInformation
class CertificatePolicies (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),2,
        ('_TYPTR', ['PolicyInformation'], 0) )
    _context = globals ()
    _numcursori = 1

# DisplayText ::= CHOICE { ia5String IA5String SIZE(1..200), visibleString VisibleString SIZE(1..200), bmpString BMPString SIZE(1..200), utf8String UTF8String SIZE(1..200) }
class DisplayText (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_VISIBLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'ia5String': ('_TYPTR', ['_api.ASN1IA5String'], 0),
        'visibleString': ('_TYPTR', ['_api.ASN1VisibleString'], 1),
        'bmpString': 2,
        'utf8String': ('_TYPTR', ['_api.ASN1UTF8String'], 3) } )
    _context = globals ()
    _numcursori = 4

# KeyPurposeId ::= OBJECT IDENTIFIER
class KeyPurposeId (_api.ASN1OID):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OID'], 0)
    _context = globals ()
    _numcursori = 1

# ExtKeyUsageSyntax ::= SEQUENCE SIZE(1..MAX) OF KeyPurposeId
class ExtKeyUsageSyntax (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_END) ),1,
        ('_TYPTR', ['KeyPurposeId'], 0) )
    _context = globals ()
    _numcursori = 1

# FreshestCRL ::= CRLDistributionPoints
class FreshestCRL (CRLDistributionPoints):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['CRLDistributionPoints'], 0)
    _context = globals ()
    _numcursori = 1

# FreshestCRL ::= CRLDistributionPoints
class FreshestCRL (CRLDistributionPoints):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['CRLDistributionPoints'], 0)
    _context = globals ()
    _numcursori = 1

# GeneralSubtree ::= SEQUENCE { base GeneralName, minimum [0] BaseDistance DEFAULT 0, maximum [1] BaseDistance OPTIONAL }
class GeneralSubtree (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(5)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_TELETEXSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_PRINTABLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UNIVERSALSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_TELETEXSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_PRINTABLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UNIVERSALSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(6)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(7)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(8)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'base': ('_TYPTR', ['GeneralName'], 0),
        'minimum': ('_TYPTR', ['BaseDistance'], 18),
        'maximum': ('_TYPTR', ['BaseDistance'], 19) } )
    _context = globals ()
    _numcursori = 20

# GeneralSubtrees ::= SEQUENCE SIZE(1..MAX) OF GeneralSubtree
class GeneralSubtrees (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(5)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_TELETEXSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_PRINTABLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UNIVERSALSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_TELETEXSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_PRINTABLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UNIVERSALSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(6)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(7)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(8)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),20,
        ('_TYPTR', ['GeneralSubtree'], 0) )
    _context = globals ()
    _numcursori = 1

# SkipCerts ::= INTEGER (0..MAX)
class SkipCerts (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# InhibitAnyPolicy ::= SkipCerts
class InhibitAnyPolicy (SkipCerts):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['SkipCerts'], 0)
    _context = globals ()
    _numcursori = 1

# InvalidityDate ::= GeneralizedTime
class InvalidityDate (_api.ASN1GeneralizedTime):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1GeneralizedTime'], 0)
    _context = globals ()
    _numcursori = 1

# IssuerAltName ::= GeneralNames
class IssuerAltName (GeneralNames):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['GeneralNames'], 0)
    _context = globals ()
    _numcursori = 1

# IssuingDistributionPoint ::= SEQUENCE { distributionPoint [0] DistributionPointName OPTIONAL, onlyContainsUserCerts [1] BOOLEAN DEFAULT FALSE, onlyContainsCACerts [2] BOOLEAN DEFAULT FALSE, onlySomeReasons [3] ReasonFlags OPTIONAL, indirectCRL [4] BOOLEAN DEFAULT FALSE, onlyContainsAttributeCerts [5] BOOLEAN DEFAULT FALSE }
class IssuingDistributionPoint (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(5)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'distributionPoint': ('_TYPTR', ['DistributionPointName'], 0),
        'onlyContainsUserCerts': ('_TYPTR', ['_api.ASN1Boolean'], 2),
        'onlyContainsCACerts': ('_TYPTR', ['_api.ASN1Boolean'], 3),
        'onlySomeReasons': ('_TYPTR', ['ReasonFlags'], 4),
        'indirectCRL': ('_TYPTR', ['_api.ASN1Boolean'], 5),
        'onlyContainsAttributeCerts': ('_TYPTR', ['_api.ASN1Boolean'], 6) } )
    _context = globals ()
    _numcursori = 7

# KeyUsage ::= BIT STRING { digitalSignature (0), nonRepudiation (1), keyEncipherment (2), dataEncipherment (3), keyAgreement (4), keyCertSign (5), cRLSign (6), encipherOnly (7), decipherOnly (8) }
class KeyUsage (_api.ASN1BitString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1BitString'], 0)
    _context = globals ()
    _numcursori = 1

# NameConstraints ::= SEQUENCE { permittedSubtrees [0] GeneralSubtrees OPTIONAL, excludedSubtrees [1] GeneralSubtrees OPTIONAL }
class NameConstraints (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'permittedSubtrees': ('_TYPTR', ['GeneralSubtrees'], 0),
        'excludedSubtrees': ('_TYPTR', ['GeneralSubtrees'], 1) } )
    _context = globals ()
    _numcursori = 2

# NoticeReference ::= SEQUENCE { organization DisplayText, noticeNumbers SEQUENCE OF INTEGER }
class NoticeReference (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_VISIBLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'organization': ('_TYPTR', ['DisplayText'], 0),
        'noticeNumbers': ('_SEQOF', 4, (
            chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
            chr(_api.DER_PACK_END) ),1,
            ('_TYPTR', ['_api.ASN1Integer'], 0) ) } )
    _context = globals ()
    _numcursori = 5

# PolicyConstraints ::= SEQUENCE { requireExplicitPolicy [0] SkipCerts OPTIONAL, inhibitPolicyMapping [1] SkipCerts OPTIONAL }
class PolicyConstraints (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'requireExplicitPolicy': ('_TYPTR', ['SkipCerts'], 0),
        'inhibitPolicyMapping': ('_TYPTR', ['SkipCerts'], 1) } )
    _context = globals ()
    _numcursori = 2

# PolicyMappings ::= SEQUENCE SIZE(1..MAX) OF SEQUENCE { issuerDomainPolicy CertPolicyId, subjectDomainPolicy CertPolicyId }
class PolicyMappings (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),2,
        ('_NAMED', {
            'issuerDomainPolicy': ('_TYPTR', ['CertPolicyId'], 0),
            'subjectDomainPolicy': ('_TYPTR', ['CertPolicyId'], 1) } ) )
    _context = globals ()
    _numcursori = 1

# UserNotice ::= SEQUENCE { noticeRef NoticeReference OPTIONAL, explicitText DisplayText OPTIONAL }
class UserNotice (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_VISIBLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_VISIBLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'noticeRef': ('_TYPTR', ['NoticeReference'], 0),
        'explicitText': ('_TYPTR', ['DisplayText'], 5) } )
    _context = globals ()
    _numcursori = 9

# Qualifier ::= CHOICE { cPSuri CPSuri, userNotice UserNotice }
class Qualifier (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_VISIBLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_VISIBLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'cPSuri': ('_TYPTR', ['CPSuri'], 0),
        'userNotice': ('_TYPTR', ['UserNotice'], 1) } )
    _context = globals ()
    _numcursori = 10

# SkipCerts ::= INTEGER (0..MAX)
class SkipCerts (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# SubjectAltName ::= GeneralNames
class SubjectAltName (GeneralNames):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['GeneralNames'], 0)
    _context = globals ()
    _numcursori = 1

# SubjectDirectoryAttributes ::= SEQUENCE SIZE(1..MAX) OF Attribute
class SubjectDirectoryAttributes (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),2,
        ('_TYPTR', ['Attribute'], 0) )
    _context = globals ()
    _numcursori = 1

# SubjectInfoAccessSyntax ::= SEQUENCE SIZE(1..MAX) OF AccessDescription
class SubjectInfoAccessSyntax (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(5)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_TELETEXSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_PRINTABLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UNIVERSALSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_TELETEXSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_PRINTABLESTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UNIVERSALSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BMPSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(6)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(7)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(8)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),19,
        ('_TYPTR', ['AccessDescription'], 0) )
    _context = globals ()
    _numcursori = 1

# SubjectKeyIdentifier ::= KeyIdentifier
class SubjectKeyIdentifier (KeyIdentifier):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['KeyIdentifier'], 0)
    _context = globals ()
    _numcursori = 1

#
# Variables with ASN.1 value assignments
#

# id-ce OBJECT IDENTIFIER ::= {joint-iso-ccitt(2) ds(5) 29}
id_ce = _api.ASN1OID (bindata=[_api.der_format_OID ('2.5.29')], context={})

# id-ce-extKeyUsage OBJECT IDENTIFIER ::= {id-ce 37}
id_ce_extKeyUsage = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.37')], context={})

# anyExtendedKeyUsage OBJECT IDENTIFIER ::= {id-ce-extKeyUsage 0}
anyExtendedKeyUsage = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce_extKeyUsage.get()) + '.0')], context={})

# id-ce-certificatePolicies OBJECT IDENTIFIER ::= {id-ce 32}
id_ce_certificatePolicies = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.32')], context={})

# anyPolicy OBJECT IDENTIFIER ::= {id-ce-certificatePolicies 0}
anyPolicy = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce_certificatePolicies.get()) + '.0')], context={})

# id-pkix OBJECT IDENTIFIER ::= {iso(1) identified-organization(3) dod(6) internet(1) security(5) mechanisms(5) pkix(7)}
id_pkix = _api.ASN1OID (bindata=[_api.der_format_OID ('1.3.6.1.5.5.7')], context={})

# id-ad OBJECT IDENTIFIER ::= {id-pkix 48}
id_ad = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_pkix.get()) + '.48')], context={})

# id-ad-caIssuers OBJECT IDENTIFIER ::= {id-ad 2}
id_ad_caIssuers = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ad.get()) + '.2')], context={})

# id-ad-caRepository OBJECT IDENTIFIER ::= {id-ad 5}
id_ad_caRepository = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ad.get()) + '.5')], context={})

# id-ad-ocsp OBJECT IDENTIFIER ::= {id-ad 1}
id_ad_ocsp = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ad.get()) + '.1')], context={})

# id-ad-timeStamping OBJECT IDENTIFIER ::= {id-ad 3}
id_ad_timeStamping = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ad.get()) + '.3')], context={})

# id-ce-authorityKeyIdentifier OBJECT IDENTIFIER ::= {id-ce 35}
id_ce_authorityKeyIdentifier = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.35')], context={})

# id-ce-basicConstraints OBJECT IDENTIFIER ::= {id-ce 19}
id_ce_basicConstraints = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.19')], context={})

# id-ce-cRLDistributionPoints OBJECT IDENTIFIER ::= {id-ce 31}
id_ce_cRLDistributionPoints = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.31')], context={})

# id-ce-cRLNumber OBJECT IDENTIFIER ::= {id-ce 20}
id_ce_cRLNumber = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.20')], context={})

# id-ce-cRLReasons OBJECT IDENTIFIER ::= {id-ce 21}
id_ce_cRLReasons = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.21')], context={})

# id-ce-certificateIssuer OBJECT IDENTIFIER ::= {id-ce 29}
id_ce_certificateIssuer = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.29')], context={})

# id-ce-deltaCRLIndicator OBJECT IDENTIFIER ::= {id-ce 27}
id_ce_deltaCRLIndicator = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.27')], context={})

# id-ce-freshestCRL OBJECT IDENTIFIER ::= {id-ce 46}
id_ce_freshestCRL = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.46')], context={})

# id-ce-freshestCRL OBJECT IDENTIFIER ::= {id-ce 46}
id_ce_freshestCRL = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.46')], context={})

# id-ce-inhibitAnyPolicy OBJECT IDENTIFIER ::= {id-ce 54}
id_ce_inhibitAnyPolicy = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.54')], context={})

# id-ce-invalidityDate OBJECT IDENTIFIER ::= {id-ce 24}
id_ce_invalidityDate = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.24')], context={})

# id-ce-issuerAltName OBJECT IDENTIFIER ::= {id-ce 18}
id_ce_issuerAltName = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.18')], context={})

# id-ce-issuingDistributionPoint OBJECT IDENTIFIER ::= {id-ce 28}
id_ce_issuingDistributionPoint = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.28')], context={})

# id-ce-keyUsage OBJECT IDENTIFIER ::= {id-ce 15}
id_ce_keyUsage = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.15')], context={})

# id-ce-nameConstraints OBJECT IDENTIFIER ::= {id-ce 30}
id_ce_nameConstraints = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.30')], context={})

# id-ce-policyConstraints OBJECT IDENTIFIER ::= {id-ce 36}
id_ce_policyConstraints = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.36')], context={})

# id-ce-policyMappings OBJECT IDENTIFIER ::= {id-ce 33}
id_ce_policyMappings = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.33')], context={})

# id-ce-subjectAltName OBJECT IDENTIFIER ::= {id-ce 17}
id_ce_subjectAltName = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.17')], context={})

# id-ce-subjectDirectoryAttributes OBJECT IDENTIFIER ::= {id-ce 9}
id_ce_subjectDirectoryAttributes = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.9')], context={})

# id-ce-subjectKeyIdentifier OBJECT IDENTIFIER ::= {id-ce 14}
id_ce_subjectKeyIdentifier = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_ce.get()) + '.14')], context={})

# id-kp OBJECT IDENTIFIER ::= {id-pkix 3}
id_kp = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_pkix.get()) + '.3')], context={})

# id-kp-OCSPSigning OBJECT IDENTIFIER ::= {id-kp 9}
id_kp_OCSPSigning = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_kp.get()) + '.9')], context={})

# id-kp-clientAuth OBJECT IDENTIFIER ::= {id-kp 2}
id_kp_clientAuth = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_kp.get()) + '.2')], context={})

# id-kp-codeSigning OBJECT IDENTIFIER ::= {id-kp 3}
id_kp_codeSigning = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_kp.get()) + '.3')], context={})

# id-kp-emailProtection OBJECT IDENTIFIER ::= {id-kp 4}
id_kp_emailProtection = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_kp.get()) + '.4')], context={})

# id-kp-serverAuth OBJECT IDENTIFIER ::= {id-kp 1}
id_kp_serverAuth = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_kp.get()) + '.1')], context={})

# id-kp-timeStamping OBJECT IDENTIFIER ::= {id-kp 8}
id_kp_timeStamping = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_kp.get()) + '.8')], context={})

# id-pe OBJECT IDENTIFIER ::= {id-pkix 1}
id_pe = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_pkix.get()) + '.1')], context={})

# id-pe-authorityInfoAccess OBJECT IDENTIFIER ::= {id-pe 1}
id_pe_authorityInfoAccess = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_pe.get()) + '.1')], context={})

# id-pe-subjectInfoAccess OBJECT IDENTIFIER ::= {id-pe 11}
id_pe_subjectInfoAccess = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_pe.get()) + '.11')], context={})

# id-qt OBJECT IDENTIFIER ::= {id-pkix 2}
id_qt = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_pkix.get()) + '.2')], context={})

# id-qt-cps OBJECT IDENTIFIER ::= {id-qt 1}
id_qt_cps = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_qt.get()) + '.1')], context={})

# id-qt-unotice OBJECT IDENTIFIER ::= {id-qt 2}
id_qt_unotice = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_qt.get()) + '.2')], context={})


# asn2quickder output for RFC5280 ends here
