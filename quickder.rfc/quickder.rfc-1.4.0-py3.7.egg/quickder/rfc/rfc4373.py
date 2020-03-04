#
# asn2quickder output for RFC4373 -- automatically generated
#
# Read more about Quick `n' Easy DER on https://gitlab.com/arpa2/quick-der
#


#
# Import general definitions and package dependencies
#

from arpa2.quickder import api as _api

from rfc4511 import LDAPOID, LDAPResult, LDAPDN, LDAPString, Referral, Controls, AddRequest, ModifyRequest, DelRequest, ModifyDNRequest


#
# Classes for ASN.1 type assignments
#

# EndLBURPRequestValue ::= SEQUENCE { sequenceNumber INTEGER (1..maxInt) }
class EndLBURPRequestValue (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'sequenceNumber': ('_TYPTR', ['_api.ASN1Integer'], 0) } )
    _context = globals ()
    _numcursori = 1

# ExtendedRequest ::= [APPLICATION 23] SEQUENCE { requestName [0] LDAPOID, requestValue [1] OCTET STRING OPTIONAL }
class ExtendedRequest (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(23)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'requestName': ('_TYPTR', ['LDAPOID'], 0),
        'requestValue': ('_TYPTR', ['_api.ASN1OctetString'], 1) } )
    _context = globals ()
    _numcursori = 2

# ExtendedResponse ::= [APPLICATION 24] SEQUENCE { resultCode ENUMERATED { success (0), operationsError (1), protocolError (2), timeLimitExceeded (3), sizeLimitExceeded (4), compareFalse (5), compareTrue (6), authMethodNotSupported (7), strongerAuthRequired (8), referral (10), adminLimitExceeded (11), unavailableCriticalExtension (12), confidentialityRequired (13), saslBindInProgress (14), noSuchAttribute (16), undefinedAttributeType (17), inappropriateMatching (18), constraintViolation (19), attributeOrValueExists (20), invalidAttributeSyntax (21), noSuchObject (32), aliasProblem (33), invalidDNSyntax (34), aliasDereferencingProblem (36), inappropriateAuthentication (48), invalidCredentials (49), insufficientAccessRights (50), busy (51), unavailable (52), unwillingToPerform (53), loopDetect (54), namingViolation (64), objectClassViolation (65), notAllowedOnNonLeaf (66), notAllowedOnRDN (67), entryAlreadyExists (68), objectClassModsProhibited (69), affectsMultipleDSAs (71), other (80), ... }, matchedDN LDAPDN, diagnosticMessage LDAPString, referral [3] Referral OPTIONAL, responseName [10] LDAPOID OPTIONAL, response [11] OCTET STRING OPTIONAL }
class ExtendedResponse (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(24)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(10)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(11)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'resultCode': ('_TYPTR', ['_api.ASN1Enumerated'], 0),
        'matchedDN': ('_TYPTR', ['LDAPDN'], 1),
        'diagnosticMessage': ('_TYPTR', ['LDAPString'], 2),
        'referral': ('_TYPTR', ['Referral'], 3),
        'responseName': ('_TYPTR', ['LDAPOID'], 4),
        'response': ('_TYPTR', ['_api.ASN1OctetString'], 5) } )
    _context = globals ()
    _numcursori = 6

# UpdateOperationList ::= SEQUENCE OF SEQUENCE { updateOperation CHOICE { addRequest AddRequest, modifyRequest ModifyRequest, delRequest DelRequest, modDNRequest ModifyDNRequest }, controls [0] Controls OPTIONAL }
class UpdateOperationList (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(8)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(6)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(10)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(12)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),10,
        ('_NAMED', {
            'updateOperation': ('_NAMED', {
                'addRequest': ('_TYPTR', ['AddRequest'], 0),
                'modifyRequest': ('_TYPTR', ['ModifyRequest'], 2),
                'delRequest': ('_TYPTR', ['DelRequest'], 4),
                'modDNRequest': ('_TYPTR', ['ModifyDNRequest'], 5) } ),
            'controls': ('_TYPTR', ['Controls'], 9) } ) )
    _context = globals ()
    _numcursori = 1

# LBURPUpdateRequestValue ::= SEQUENCE { sequenceNumber INTEGER (1..maxInt), updateOperationList UpdateOperationList }
class LBURPUpdateRequestValue (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'sequenceNumber': ('_TYPTR', ['_api.ASN1Integer'], 0),
        'updateOperationList': ('_TYPTR', ['UpdateOperationList'], 1) } )
    _context = globals ()
    _numcursori = 2

# MaxOperations ::= INTEGER (0..maxInt)
class MaxOperations (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# OperationResult ::= SEQUENCE { operationNumber INTEGER, ldapResult LDAPResult }
class OperationResult (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'operationNumber': ('_TYPTR', ['_api.ASN1Integer'], 0),
        'ldapResult': ('_TYPTR', ['LDAPResult'], 1) } )
    _context = globals ()
    _numcursori = 5

# OperationResults ::= SEQUENCE OF OperationResult
class OperationResults (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),5,
        ('_TYPTR', ['OperationResult'], 0) )
    _context = globals ()
    _numcursori = 1

# StartLBURPRequestValue ::= SEQUENCE { updateStyleOID LDAPOID }
class StartLBURPRequestValue (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'updateStyleOID': ('_TYPTR', ['LDAPOID'], 0) } )
    _context = globals ()
    _numcursori = 1

# StartLBURPResponseValue ::= MaxOperations
class StartLBURPResponseValue (MaxOperations):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['MaxOperations'], 0)
    _context = globals ()
    _numcursori = 1

#
# Variables with ASN.1 value assignments
#

# maxInt INTEGER ::= 2147483647
maxInt = _api.ASN1Integer (bindata=[_api.der_format_INTEGER (2147483647)], context={})


# asn2quickder output for RFC4373 ends here
